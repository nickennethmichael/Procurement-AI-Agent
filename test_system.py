"""
Test script for Procurement Optimization AI Agent
Verifies that all components work correctly
"""

import sys
import traceback
from datetime import datetime

import pandas as pd

def test_imports():
    """Test that all modules can be imported"""
    print("Testing imports...")
    
    try:
        from agent.procurement_agent import ProcurementAgent
        print("✅ ProcurementAgent imported successfully")
    except Exception as e:
        print(f"❌ Error importing ProcurementAgent: {e}")
        return False
    
    try:
        from agent.llm_interface import LLMInterface, get_available_models
        print("✅ LLMInterface imported successfully")
    except Exception as e:
        print(f"❌ Error importing LLMInterface: {e}")
        return False
    
    try:
        from data.sample_data import SampleDataGenerator
        print("✅ SampleDataGenerator imported successfully")
    except Exception as e:
        print(f"❌ Error importing SampleDataGenerator: {e}")
        return False
    
    try:
        from models.demand_forecaster import DemandForecaster
        print("✅ DemandForecaster imported successfully")
    except Exception as e:
        print(f"❌ Error importing DemandForecaster: {e}")
        return False
    
    try:
        from models.cost_optimizer import CostOptimizer
        print("✅ CostOptimizer imported successfully")
    except Exception as e:
        print(f"❌ Error importing CostOptimizer: {e}")
        return False
    
    return True

def test_sample_data_generation():
    """Test sample data generation"""
    print("\nTesting sample data generation...")
    
    try:
        from data.sample_data import SampleDataGenerator
        
        generator = SampleDataGenerator()
        data = generator.generate_complete_dataset(50)  # Generate 50 orders for testing
        repeatable_data = SampleDataGenerator(seed=42).generate_complete_dataset(50)
        repeated_seed_data = SampleDataGenerator(seed=42).generate_complete_dataset(50)

        pd.testing.assert_frame_equal(
            repeatable_data['purchase_orders'],
            repeated_seed_data['purchase_orders']
        )
        if data['purchase_orders'].equals(repeatable_data['purchase_orders']):
            print("❌ Default sample data should vary between generations")
            return False
        
        # Check data structure
        required_keys = ['purchase_orders', 'vendors', 'items', 'historical_data']
        for key in required_keys:
            if key not in data:
                print(f"❌ Missing key in sample data: {key}")
                return False
        
        # Check data content
        if len(data['purchase_orders']) == 0:
            print("❌ No purchase orders generated")
            return False
        
        if len(data['vendors']) == 0:
            print("❌ No vendors generated")
            return False
        
        if len(data['items']) == 0:
            print("❌ No items generated")
            return False

        orders = data['purchase_orders']
        if orders['item_id'].nunique() != len(data['items']):
            print("❌ Purchase orders do not cover the full item catalog")
            return False
        if orders['unit_price'].min() >= 1 or orders['unit_price'].max() < 1000:
            print("❌ Purchase orders do not cover low and high price ranges")
            return False
        if not (orders['total_amount'].round(2) == (orders['quantity'] * orders['unit_price']).round(2)).all():
            print("❌ Purchase order totals do not match item quantities and prices")
            return False
        
        print(f"✅ Sample data generated successfully:")
        print(f"   - Purchase Orders: {len(data['purchase_orders'])}")
        print(f"   - Vendors: {len(data['vendors'])}")
        print(f"   - Items: {len(data['items'])}")
        print(f"   - Historical Data Points: {len(data['historical_data'])}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error generating sample data: {e}")
        traceback.print_exc()
        return False

def test_llm_interface():
    """Test LLM interface"""
    print("\nTesting LLM interface...")
    
    try:
        from agent.llm_interface import LLMInterface, get_available_models
        
        # Test available models
        models = get_available_models()
        if not models or not isinstance(models, dict):
            print("❌ get_available_models() failed")
            return False
        
        print(f"✅ Available models: {list(models.keys())}")
        
        # Test LLM interface initialization (with mock)
        llm = LLMInterface("ollama", "mistral:7b")
        
        # Test response generation
        test_prompt = "Hello, this is a test prompt."
        response = llm.generate_response(test_prompt)
        
        if not response or len(response) == 0:
            print("❌ LLM response generation failed")
            return False
        
        print(f"✅ LLM response generated: {len(response)} characters")
        
        return True
        
    except Exception as e:
        print(f"❌ Error testing LLM interface: {e}")
        traceback.print_exc()
        return False

def test_demand_forecasting():
    """Test demand forecasting"""
    print("\nTesting demand forecasting...")
    
    try:
        from models.demand_forecaster import DemandForecaster
        from data.sample_data import SampleDataGenerator
        
        # Generate sample data
        generator = SampleDataGenerator()
        data = generator.generate_complete_dataset(100)
        
        # Test demand forecaster
        forecaster = DemandForecaster()
        
        # Test model training
        training_results = forecaster.train_models(data['purchase_orders'])
        
        if 'error' in training_results:
            print(f"❌ Model training failed: {training_results['error']}")
            return False
        
        print("✅ Model training completed")
        
        # Test forecasting
        forecast_results = forecaster.forecast_demand(data['purchase_orders'], 30)
        
        if 'error' in forecast_results:
            print(f"❌ Forecasting failed: {forecast_results['error']}")
            return False
        
        print(f"✅ Forecasting completed:")
        print(f"   - Model used: {forecast_results.get('model_used', 'Unknown')}")
        print(f"   - Forecast period: {forecast_results.get('forecast_period', 'Unknown')}")
        print(f"   - Total predicted spend: ${forecast_results.get('total_predicted_spend', 0):,.2f}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error testing demand forecasting: {e}")
        traceback.print_exc()
        return False

def test_cost_optimization():
    """Test cost optimization"""
    print("\nTesting cost optimization...")
    
    try:
        from models.cost_optimizer import CostOptimizer
        from data.sample_data import SampleDataGenerator
        
        # Generate sample data
        generator = SampleDataGenerator()
        data = generator.generate_complete_dataset(100)
        
        # Test cost optimizer
        optimizer = CostOptimizer()
        
        # Test optimization analysis
        opportunities = optimizer.analyze_cost_opportunities(
            data['purchase_orders'],
            data['vendors'],
            data['items']
        )
        
        if not opportunities:
            print("❌ Cost optimization analysis failed")
            return False
        
        total_savings = opportunities.get('total_potential_savings', 0)
        print(f"✅ Cost optimization completed:")
        print(f"   - Total potential savings: ${total_savings:,.2f}")
        
        strategy_names = [
            'bulk_purchasing',
            'vendor_consolidation',
            'price_negotiation',
            'inventory_optimization',
            'contract_optimization'
        ]
        missing_opportunities = [
            strategy for strategy in strategy_names
            if 'error' in opportunities.get(strategy, {})
            or not opportunities.get(strategy, {}).get('opportunities')
        ]
        if missing_opportunities:
            print(f"❌ Strategies returned no opportunities: {', '.join(missing_opportunities)}")
            return False

        # Count successful strategies
        successful_strategies = 0
        for strategy, result in opportunities.items():
            if strategy != 'total_potential_savings' and isinstance(result, dict) and 'error' not in result:
                successful_strategies += 1
        
        print(f"   - Successful strategies: {successful_strategies}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error testing cost optimization: {e}")
        traceback.print_exc()
        return False

def test_procurement_agent():
    """Test the main procurement agent"""
    print("\nTesting procurement agent...")
    
    try:
        from agent.procurement_agent import ProcurementAgent
        from data.sample_data import SampleDataGenerator
        
        # Generate sample data
        generator = SampleDataGenerator()
        data = generator.generate_complete_dataset(50)
        
        # Test agent initialization
        agent = ProcurementAgent("ollama", "mistral:7b")
        print("✅ Agent initialized successfully")
        
        # Test analysis
        results = agent.analyze_procurement_data(
            data['purchase_orders'],
            data['vendors'],
            data['historical_data']
        )
        
        if not results:
            print("❌ Agent analysis failed")
            return False
        
        print("✅ Agent analysis completed successfully")
        print(f"   - Model used: {results.get('model_info', {}).get('name', 'Unknown')}")
        print(f"   - Timestamp: {results.get('timestamp', 'Unknown')}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error testing procurement agent: {e}")
        traceback.print_exc()
        return False

def main():
    """Run all tests"""
    print("🏥 Procurement Optimization AI Agent - System Test")
    print("=" * 60)
    print(f"Test started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    tests = [
        ("Import Test", test_imports),
        ("Sample Data Generation", test_sample_data_generation),
        ("LLM Interface", test_llm_interface),
        ("Demand Forecasting", test_demand_forecasting),
        ("Cost Optimization", test_cost_optimization),
        ("Procurement Agent", test_procurement_agent)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"Running {test_name}...")
        try:
            if test_func():
                passed += 1
                print(f"✅ {test_name} PASSED")
            else:
                print(f"❌ {test_name} FAILED")
        except Exception as e:
            print(f"❌ {test_name} FAILED with exception: {e}")
            traceback.print_exc()
        
        print("-" * 60)
    
    print(f"\nTest Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! The system is ready to use.")
        print("\nTo run the Streamlit application:")
        print("streamlit run app.py")
    else:
        print("⚠️  Some tests failed. Please check the errors above.")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
