"""
Sample Data Generator for Hospital Procurement System
Generates realistic sample data for testing and demonstration
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
from typing import Dict, List, Optional, Tuple


class SampleDataGenerator:
    """Generate realistic sample data for hospital procurement"""
    
    def __init__(self, seed: Optional[int] = None):
        """Initialize the sample data generator"""
        self.random = random.Random(seed)
        self.vendors = self._create_vendor_list()
        self.items = self._create_item_catalog()
        self.categories = self._get_categories()
    
    def _create_vendor_list(self) -> List[Dict]:
        """Create a list of sample vendors"""
        return [
            {
                "name": "Medical Supplies Co.",
                "contact_person": "John Smith",
                "email": "john@medsupplies.com",
                "phone": "555-0101",
                "category": "Medical Supplies",
                "rating": 4.5,
                "quality_score": 4.2,
                "reliability_score": 4.8,
                "delivery_lead_time": 7
            },
            {
                "name": "Hospital Equipment Inc.",
                "contact_person": "Sarah Johnson",
                "email": "sarah@hospitequip.com",
                "phone": "555-0102",
                "category": "Equipment",
                "rating": 4.2,
                "quality_score": 4.0,
                "reliability_score": 4.5,
                "delivery_lead_time": 14
            },
            {
                "name": "Pharmaceutical Solutions",
                "contact_person": "Mike Brown",
                "email": "mike@pharmsol.com",
                "phone": "555-0103",
                "category": "Pharmaceuticals",
                "rating": 4.8,
                "quality_score": 4.7,
                "reliability_score": 4.9,
                "delivery_lead_time": 5
            },
            {
                "name": "Surgical Instruments Ltd.",
                "contact_person": "Dr. Emily Chen",
                "email": "emily@surgicalinst.com",
                "phone": "555-0104",
                "category": "Surgical Equipment",
                "rating": 4.6,
                "quality_score": 4.8,
                "reliability_score": 4.7,
                "delivery_lead_time": 10
            },
            {
                "name": "Laboratory Supplies Corp.",
                "contact_person": "David Wilson",
                "email": "david@labsupplies.com",
                "phone": "555-0105",
                "category": "Laboratory",
                "rating": 3.8,
                "quality_score": 3.9,
                "reliability_score": 4.0,
                "delivery_lead_time": 8
            }
        ]
    
    def _create_item_catalog(self) -> List[Dict]:
        """Create a catalog of medical items"""
        return [
            # PPE Items
            {"name": "Surgical Masks", "category": "PPE", "subcategory": "Face Protection", "unit": "box", "unit_price": 25.0, "is_critical": True},
            {"name": "N95 Respirators", "category": "PPE", "subcategory": "Face Protection", "unit": "box", "unit_price": 45.0, "is_critical": True},
            {"name": "Disposable Gloves", "category": "PPE", "subcategory": "Hand Protection", "unit": "box", "unit_price": 15.0, "is_critical": True},
            {"name": "Protective Gowns", "category": "PPE", "subcategory": "Body Protection", "unit": "piece", "unit_price": 8.0, "is_critical": True},
            
            # Medical Supplies
            {"name": "Syringes 10ml", "category": "Medical Supplies", "subcategory": "Injection", "unit": "piece", "unit_price": 0.50, "is_critical": True},
            {"name": "Syringes 5ml", "category": "Medical Supplies", "subcategory": "Injection", "unit": "piece", "unit_price": 0.40, "is_critical": True},
            {"name": "IV Catheters", "category": "Medical Supplies", "subcategory": "IV Therapy", "unit": "piece", "unit_price": 2.50, "is_critical": True},
            {"name": "Bandages", "category": "Medical Supplies", "subcategory": "Wound Care", "unit": "box", "unit_price": 12.0, "is_critical": False},
            {"name": "Gauze Pads", "category": "Medical Supplies", "subcategory": "Wound Care", "unit": "box", "unit_price": 8.0, "is_critical": False},
            
            # Equipment
            {"name": "Hospital Beds", "category": "Equipment", "subcategory": "Furniture", "unit": "piece", "unit_price": 2500.0, "is_critical": False},
            {"name": "Patient Monitors", "category": "Equipment", "subcategory": "Monitoring", "unit": "piece", "unit_price": 3500.0, "is_critical": True},
            {"name": "Defibrillators", "category": "Equipment", "subcategory": "Emergency", "unit": "piece", "unit_price": 8000.0, "is_critical": True},
            {"name": "Wheelchairs", "category": "Equipment", "subcategory": "Mobility", "unit": "piece", "unit_price": 450.0, "is_critical": False},
            
            # Pharmaceuticals
            {"name": "Paracetamol 500mg", "category": "Pharmaceuticals", "subcategory": "Pain Relief", "unit": "bottle", "unit_price": 15.0, "is_critical": True},
            {"name": "Ibuprofen 400mg", "category": "Pharmaceuticals", "subcategory": "Pain Relief", "unit": "bottle", "unit_price": 18.0, "is_critical": True},
            {"name": "Antibiotics", "category": "Pharmaceuticals", "subcategory": "Antimicrobial", "unit": "bottle", "unit_price": 45.0, "is_critical": True},
            
            # Laboratory
            {"name": "Test Tubes", "category": "Laboratory", "subcategory": "Glassware", "unit": "box", "unit_price": 35.0, "is_critical": False},
            {"name": "Microscope Slides", "category": "Laboratory", "subcategory": "Glassware", "unit": "box", "unit_price": 22.0, "is_critical": False},
            {"name": "Reagent Kits", "category": "Laboratory", "subcategory": "Reagents", "unit": "kit", "unit_price": 120.0, "is_critical": True}
        ]
    
    def _get_categories(self) -> Dict[str, List[str]]:
        """Get categories and their subcategories"""
        return {
            "PPE": ["Face Protection", "Hand Protection", "Body Protection"],
            "Medical Supplies": ["Injection", "IV Therapy", "Wound Care", "Surgical"],
            "Equipment": ["Furniture", "Monitoring", "Emergency", "Mobility"],
            "Pharmaceuticals": ["Pain Relief", "Antimicrobial", "Cardiovascular"],
            "Laboratory": ["Glassware", "Reagents", "Equipment"],
            "Surgical Equipment": ["Instruments", "Implants", "Consumables"]
        }
    
    def generate_purchase_orders(self, num_orders: int = 500, start_date: str = "2023-01-01", end_date: str = "2024-01-31") -> pd.DataFrame:
        """Generate sample purchase orders"""
        
        orders = []
        start_dt = datetime.strptime(start_date, "%Y-%m-%d")
        end_dt = datetime.strptime(end_date, "%Y-%m-%d")
        
        vendor_candidates = {
            "PPE": [1, 4],
            "Medical Supplies": [1, 4],
            "Equipment": [2, 4],
            "Pharmaceuticals": [1, 3],
            "Laboratory": [1, 5]
        }
        vendor_price_factors = {1: 0.90, 2: 0.88, 3: 1.15, 4: 1.18, 5: 1.12}
        frequent_items = {0, 1, 2, 4, 6, 7, 8, 13, 14, 15}
        item_order_counts = {}

        for i in range(num_orders):
            # Random order date
            order_date = start_dt + timedelta(days=self.random.randint(0, (end_dt - start_dt).days))

            # Cycle through every price tier while repeatedly replenishing common supplies.
            item_index = i % len(self.items)
            item = self.items[item_index]
            candidates = vendor_candidates[item["category"]]
            item_order_count = item_order_counts.get(item_index, 0)
            vendor_id = (
                candidates[1]
                if item["category"] == "Laboratory" or item_order_count % 4 == 3
                else candidates[0]
            )
            item_order_counts[item_index] = item_order_count + 1
            vendor = self.vendors[vendor_id - 1]
            if item["category"] == "Laboratory":
                quantity = self.random.randint(1, 3)
            elif item["unit_price"] >= 450:
                quantity = self.random.randint(1, 5)
            elif item_index in frequent_items and item_order_count > 0:
                quantity = (
                    self.random.randint(1, 10)
                    if vendor_id == candidates[0]
                    else self.random.randint(30, 100)
                )
            else:
                quantity = self.random.randint(10, 100)
            unit_price = round(item["unit_price"] * vendor_price_factors[vendor_id], 2)
            
            # Random status with weighted probability
            status_weights = {"pending": 0.2, "approved": 0.3, "delivered": 0.4, "cancelled": 0.1}
            status = self.random.choices(list(status_weights.keys()), weights=list(status_weights.values()))[0]
            total_amount = round(quantity * unit_price, 2)
            
            # Expected delivery date
            expected_delivery = order_date + timedelta(days=vendor["delivery_lead_time"])
            
            # Actual delivery date (if delivered)
            actual_delivery = None
            if status == "delivered":
                actual_delivery = expected_delivery + timedelta(days=self.random.randint(-2, 5))
            
            order = {
                "order_id": i + 1,
                "order_number": f"PO-2024-{i+1:03d}",
                "vendor_id": vendor_id,
                "vendor_name": vendor["name"],
                "item_id": self.items.index(item) + 1,
                "quantity": quantity,
                "unit_price": unit_price,
                "order_date": order_date,
                "expected_delivery_date": expected_delivery,
                "actual_delivery_date": actual_delivery,
                "status": status,
                "total_amount": round(total_amount, 2),
                "currency": "USD",
                "created_by": "procurement@hospital.com",
                "category": vendor["category"]
            }
            
            orders.append(order)
        
        return pd.DataFrame(orders)
    
    def generate_vendor_data(self) -> pd.DataFrame:
        """Generate vendor data"""
        vendors_data = []
        
        for i, vendor in enumerate(self.vendors):
            vendor_data = {
                "vendor_id": i + 1,
                "name": vendor["name"],
                "contact_person": vendor["contact_person"],
                "email": vendor["email"],
                "phone": vendor["phone"],
                "category": vendor["category"],
                "rating": vendor["rating"],
                "status": "active",
                "quality_score": vendor["quality_score"],
                "reliability_score": vendor["reliability_score"],
                "delivery_lead_time": vendor["delivery_lead_time"],
                "contract_start_date": datetime(2023, 1, 1),
                "contract_end_date": datetime(2025, 12, 31),
                "payment_terms": "Net 30"
            }
            vendors_data.append(vendor_data)
        
        return pd.DataFrame(vendors_data)
    
    def generate_item_data(self) -> pd.DataFrame:
        """Generate item catalog data"""
        items_data = []
        primary_vendors = {
            "PPE": 1,
            "Medical Supplies": 1,
            "Equipment": 2,
            "Pharmaceuticals": 3,
            "Laboratory": 5
        }
        
        for i, item in enumerate(self.items):
            vendor_id = primary_vendors[item["category"]]
            
            item_data = {
                "item_id": i + 1,
                "name": item["name"],
                "description": f"High-quality {item['name'].lower()} for hospital use",
                "category": item["category"],
                "subcategory": item["subcategory"],
                "unit": item["unit"],
                "vendor_id": vendor_id,
                "unit_price": item["unit_price"],
                "min_order_quantity": 1 if item["unit_price"] >= 450 else 10,
                "lead_time": self.random.randint(3, 21),
                "is_critical": item["is_critical"],
                "is_active": True
            }
            items_data.append(item_data)
        
        return pd.DataFrame(items_data)
    
    def generate_historical_data(self, months: int = 12) -> pd.DataFrame:
        """Generate historical procurement data for trend analysis"""
        
        historical_data = []
        start_date = datetime.now() - timedelta(days=months * 30)
        
        for i in range(months * 30):  # Daily data for the specified months
            date = start_date + timedelta(days=i)
            
            # Add some seasonality and trends
            base_amount = 5000  # Base daily spend
            seasonal_factor = 1 + 0.3 * np.sin(2 * np.pi * i / 365)  # Seasonal variation
            trend_factor = 1 + 0.001 * i  # Slight upward trend
            random_factor = self.random.uniform(0.8, 1.2)  # Random variation
            
            daily_spend = base_amount * seasonal_factor * trend_factor * random_factor
            
            # Add some category distribution
            categories = list(self.categories.keys())
            category = self.random.choice(categories)
            
            historical_data.append({
                "date": date,
                "amount": round(daily_spend, 2),
                "category": category,
                "vendor_count": self.random.randint(3, 8),
                "order_count": self.random.randint(10, 30)
            })
        
        return pd.DataFrame(historical_data)
    
    def generate_complete_dataset(self, num_orders: int = 500) -> Dict[str, pd.DataFrame]:
        """Generate complete dataset for testing"""
        
        return {
            "purchase_orders": self.generate_purchase_orders(num_orders),
            "vendors": self.generate_vendor_data(),
            "items": self.generate_item_data(),
            "historical_data": self.generate_historical_data()
        }
    
    def save_sample_data(self, output_dir: str = "sample_data"):
        """Save sample data to CSV files"""
        import os
        
        # Create output directory
        os.makedirs(output_dir, exist_ok=True)
        
        # Generate data
        data = self.generate_complete_dataset()
        
        # Save to CSV files
        for name, df in data.items():
            filename = f"{output_dir}/{name}.csv"
            df.to_csv(filename, index=False)
            print(f"Saved {filename} with {len(df)} records")
        
        print(f"Sample data saved to {output_dir}/ directory")


def create_sample_data():
    """Convenience function to create and save sample data"""
    generator = SampleDataGenerator()
    generator.save_sample_data()
    return generator.generate_complete_dataset()


if __name__ == "__main__":
    # Generate and save sample data
    create_sample_data()
