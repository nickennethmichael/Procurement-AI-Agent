# Quick Start Guide - Procurement Optimization AI Agent

## 🚀 Get Started in 5 Minutes

### 1. Install Dependencies

Use **Python 3.11** with the pinned dependencies. Python 3.14 is not supported by this dependency set; pip may otherwise try to build NumPy and pandas from source.

On Windows PowerShell, create a virtual environment and use its Python executable directly. This avoids PowerShell's script execution policy; activation is not required:

```bash
py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

### 2. Install Ollama (Optional - for local LLM)

Download from [https://ollama.ai/](https://ollama.ai/) and install.

Then pull a model:
```bash
ollama pull mistral:7b
```

### 3. Run the System Test

```bash
.\.venv\Scripts\python.exe test_system.py
```

This will verify all components are working correctly.

### 4. Launch the Application

```bash
.\.venv\Scripts\python.exe -m streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`

## 🎯 Quick Demo

1. **Initialize AI Agent**: Click "🚀 Initialize AI Agent" in the sidebar
2. **Load Sample Data**: Click "📁 Load Sample Data" to generate test data
3. **Explore Dashboard**: View key metrics and visualizations
4. **Run AI Analysis**: Go to "🤖 AI Analysis" tab and click "🔍 Run AI Analysis"
5. **Generate Forecasts**: Visit "📈 Demand Forecasting" tab
6. **Optimize Costs**: Check "💰 Cost Optimization" tab
7. **Download Reports**: Use "📋 Reports" tab to generate comprehensive reports

## 🔧 Configuration

### Environment Variables

Create a `.env` file (optional):

```env
# LLM Configuration
LLM_TYPE=ollama
LLM_MODEL=mistral:7b
LLM_TEMPERATURE=0.1

# Database Configuration
DATABASE_URL=sqlite:///procurement.db

# Analysis Configuration
FORECAST_DAYS=30
CONFIDENCE_LEVEL=0.95
```

### Available Models

**Ollama Models:**
- `mistral:7b` (recommended)
- `llama2:7b`
- `llama2:13b`
- `codellama:7b`
- `neural-chat:7b`

**Hugging Face Models:**
- `microsoft/DialoGPT-medium`
- `gpt2`
- `microsoft/DialoGPT-small`
- `EleutherAI/gpt-neo-125M`

## 📊 Features Overview

### 🤖 AI-Powered Analysis
- **LangChain + LangGraph** workflow for multi-step reasoning
- **Local LLM** support (no API costs)
- **Autonomous analysis** of procurement data
- **Intelligent recommendations** for optimization

### 📈 Demand Forecasting
- **Scikit-learn + XGBoost** models
- **Time series analysis** with seasonal patterns
- **Confidence intervals** for predictions
- **Feature importance** analysis

### 💰 Cost Optimization
- **Bulk purchasing** opportunities
- **Vendor consolidation** strategies
- **Price negotiation** insights
- **Inventory optimization** recommendations
- **Contract optimization** suggestions

### 📊 Interactive Dashboard
- **Real-time metrics** and KPIs
- **Interactive visualizations** with Plotly
- **Vendor performance** analysis
- **Spending trends** and patterns

### 📋 Comprehensive Reports
- **Executive summaries**
- **Detailed analysis** reports
- **Cost optimization** recommendations
- **Vendor performance** evaluations
- **Demand forecast** reports

## 🏥 Sample Data

The system includes realistic hospital procurement data:

- **Purchase Orders**: 100+ sample orders with realistic amounts and dates
- **Vendors**: 5+ vendors across different categories (Medical Supplies, Equipment, Pharmaceuticals)
- **Items**: 20+ medical items (PPE, Medical Supplies, Equipment, Pharmaceuticals, Laboratory)
- **Historical Data**: 12 months of daily procurement data with seasonal patterns

## 🔍 Troubleshooting

### Common Issues

1. **Import Errors**: Make sure all dependencies are installed
   ```bash
   pip install -r requirements.txt
   ```

2. **LLM Not Found**: If using Ollama, ensure it's running
   ```bash
   ollama serve
   ```

3. **Database Errors**: The system will create a SQLite database automatically

4. **Memory Issues**: For large datasets, consider using a smaller model or reducing data size

### Getting Help

1. Run the test script: `python test_system.py`
2. Check the console output for error messages
3. Verify all dependencies are installed correctly
4. Ensure you have sufficient system resources

## 🎯 Next Steps

1. **Customize Data**: Replace sample data with your actual procurement data
2. **Configure Models**: Adjust LLM parameters for your specific needs
3. **Extend Analysis**: Add custom optimization strategies
4. **Deploy**: Deploy to production with proper security and scaling

## 📚 Documentation

- **README.md**: Complete project documentation
- **Code Comments**: Detailed inline documentation
- **Type Hints**: Full type annotations for all functions
- **Error Handling**: Comprehensive error handling and logging

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

MIT License - see LICENSE file for details.

---

**Ready to optimize your procurement? Start with `streamlit run app.py`! 🚀**
