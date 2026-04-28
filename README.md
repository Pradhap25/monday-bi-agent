# 📊 Monday.com BI Agent

This project is an AI-powered Business Intelligence Agent that answers founder-level queries using Monday.com data.

## 🚀 Features

- Connects to Monday.com boards via API
- Cleans messy real-world data
- Answers business questions using AI
- Handles missing and inconsistent data

## 🛠 Setup

1. Install dependencies:
   pip install -r requirements.txt

2. Add your API keys:
   - Monday API Key → monday_api.py
   - OpenAI API Key → agent.py

3. Add your board IDs in app.py

4. Run:
   python -m streamlit run app.py

## 🌐 Deployment

Deploy easily using Streamlit Cloud.

## 🧠 Example Queries

- How is our pipeline this quarter?
- Which sector is performing best?
- What are the revenue trends?

## 📌 Notes

- Data is fetched dynamically from Monday.com
- No CSV is hardcoded
- Handles missing values gracefully