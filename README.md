# Procurement Optimization AI Agent

An intelligent AI agent that autonomously analyzes hospital purchase orders and vendor pricing to predict optimal procurement strategies for cost and availability optimization.

## Features

- **Autonomous Analysis**: AI agent analyzes purchase orders and vendor data
- **Cost Optimization**: Predicts optimal procurement strategies for cost reduction
- **Availability Forecasting**: Forecasts demand and availability patterns
- **Vendor Analysis**: Evaluates vendor performance and pricing
- **Interactive Dashboard**: Streamlit-based user interface
- **Open Source**: Uses local LLMs (Ollama/Mistral-7B) without paid APIs

## Tech Stack

- **Agentic AI**: LangChain + LangGraph
- **LLM**: Ollama (Mistral-7B/LLaMA-3) or Hugging Face Transformers
- **Data Handling**: Pandas + SQLAlchemy
- **Analytics**: Scikit-learn + XGBoost
- **UI**: Streamlit
- **Visualization**: Plotly + Matplotlib

## Installation

Use **Python 3.11** for the pinned dependencies in `requirements.txt`. In particular, these versions do not provide compatible wheels for Python 3.14, so pip may try to build NumPy and pandas from source.

1. Clone the repository:
```bash
git clone <repository-url>
cd procurement-optimization-ai
```

2. Create a virtual environment and install dependencies (Windows PowerShell). Activation is optional; using its Python executable directly avoids PowerShell's script execution policy:
```bash
py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

If `py -3.11` is not found, install Python 3.11 and ensure the Python launcher is available.

3. Install Ollama (for local LLM):
```bash
# Download from https://ollama.ai/
# Then run:
ollama pull mistral:7b
```

4. Run the application:
```bash
.\.venv\Scripts\python.exe -m streamlit run app.py
```

## Project Structure

```
├── app.py                          # Main Streamlit application
├── agent/
│   ├── __init__.py
│   ├── procurement_agent.py        # Main AI agent logic
│   ├── llm_interface.py           # LLM interface (Ollama/HuggingFace)
│   └── graph_workflow.py          # LangGraph workflow
├── data/
│   ├── __init__.py
│   ├── database.py                # SQLAlchemy database models
│   ├── sample_data.py             # Sample hospital data generator
│   └── data_processor.py          # Data processing utilities
├── models/
│   ├── __init__.py
│   ├── demand_forecaster.py       # Demand forecasting models
│   ├── cost_optimizer.py          # Cost optimization algorithms
│   └── vendor_analyzer.py         # Vendor analysis models
├── utils/
│   ├── __init__.py
│   ├── visualization.py           # Plotting utilities
│   └── config.py                  # Configuration settings
└── requirements.txt
```

## How the App Works

This application is designed as a simple end-to-end procurement analysis workflow for a healthcare organization:

1. **Initialize the AI agent**
   - Open the app in Streamlit.
   - In the left sidebar, choose the LLM type (`ollama` or `huggingface`).
   - Select a model and click **Initialize AI Agent**.
   - The agent prepares the reasoning workflow that will analyze purchase orders and vendor pricing.

2. **Load procurement data**
   - Click **Load Sample Data** to generate realistic hospital purchase-order and vendor data.
   - The **Sample purchase orders** slider controls how many orders are generated in the sample dataset. It ranges from 100 to 1000 orders, in steps of 100.
   - A higher value creates a larger, richer dataset for broader price variation and more realistic optimization insights; a lower value gives a smaller, faster test dataset.
   - Clicking **Load Sample Data** again does not reuse the exact same data; each run creates a fresh sample dataset with slightly different values, which is useful for testing how the app responds to new purchasing patterns.
   - You can also use the database setup option to initialize example records in the local app database.
   - The data includes purchase order amounts, categories, vendor info, dates, and spending patterns.

3. **Explore the dashboard**
   - The **Dashboard** tab summarizes spending, active vendors, average order value, and category-level cost breakdowns.
   - Charts help you quickly see which departments or categories consume the most budget.

4. **Run AI-powered analysis**
   - The **AI Analysis** tab uses the configured LLM and the procurement workflow to interpret the data.
   - The agent identifies cost issues, supplier risks, anomalies, and strategic recommendations.
   - The results are generated from both the LLM workflow and ML-based analysis in the backend.

5. **Check forecasting and optimization modules**
   - The **Demand Forecasting** tab reviews trends and predicts upcoming demand or spend levels.
   - The **Cost Optimization** tab highlights vendor comparisons, price opportunities, and savings strategies.
   - These modules help answer questions like: which vendor is best for a category, where are we overspending, and how should we plan future purchasing?

6. **Review reports**
   - The **Reports** tab presents a final summary of procurement insights, findings, and recommendations.
   - This is the place to review the practical actions the AI suggests for procurement planning.

### In simple terms
The app is a procurement decision-support system: it gathers hospital purchasing data, analyzes it with AI and forecasting models, and produces recommendations that help reduce cost, improve vendor selection, and plan future demand more efficiently.

## Usage

1. **Start the Application**: Run `streamlit run app.py`
2. **Initialize the AI Agent**: Select the model and click the initialize button in the sidebar
3. **Load or Upload Data**: Use sample data or provide your own purchase order and vendor data
4. **Review the Dashboard**: Analyze spend, vendors, and category trends
5. **Run AI Analysis**: Use the AI workflow for recommendations and insights
6. **Check Forecasts and Savings Opportunities**: Review forecasting and cost optimization tabs
7. **Use the Reports View**: Read the final recommendations for procurement decisions

## Key Components

### AI Agent (LangChain + LangGraph)
- Autonomous analysis of procurement data
- Multi-step reasoning workflow
- Cost-benefit analysis
- Vendor evaluation

### Demand Forecasting (Scikit-learn + XGBoost)
- Time series analysis
- Seasonal pattern detection
- Demand prediction models
- Inventory optimization

### Cost Optimization
- Vendor price comparison
- Bulk purchase optimization
- Contract negotiation insights
- Budget allocation strategies

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

MIT License - see LICENSE file for details.

## Contact:
for any inquiries : vikhrams@saveetha.ac.in
