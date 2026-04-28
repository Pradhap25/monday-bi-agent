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

  
1. Why did you use an LLM instead of a rule-based system?

Answer (simple + strong):

I chose an LLM-based approach because founder-level queries are usually ambiguous and conversational.
A rule-based system would require defining many patterns and still fail on edge cases.
Using an LLM allows flexible interpretation of queries like “How’s our pipeline this quarter?” without hardcoding rules.


 2. How did you handle messy data?

Answer:

I created a data cleaning layer using Pandas.

Missing values are handled using defaults like “Unknown” or excluded in calculations
Dates are normalized using flexible parsing
Numeric fields use coercion to avoid crashes

I also surface data quality issues instead of hiding them, so users are aware of gaps.



 3. How does your system understand user queries?

Answer:

The system uses an LLM to interpret queries and extract:

Required dataset (Deals or Work Orders)
Filters (sector, time period)
Metrics (revenue, count, pipeline value)

This allows it to convert natural language into structured analysis steps.

 4. Why did you choose Pandas instead of a database?

Answer:

Pandas was chosen for rapid prototyping and simplicity.
It allowed fast data transformation without setting up a database.

If this were scaled, I would move to a proper database or data warehouse.

 5. How do you ensure your answers are meaningful and not just raw data?

Answer:

I structured responses to include:

Summary metrics (e.g., total pipeline value)
Observations (e.g., sector trends)
Risk indicators (e.g., missing data, stalled deals)

The focus is on decision-making insights, not just numbers.

 6. What happens if data is missing or inconsistent?

Answer:

The system handles it gracefully:

Ignores invalid values in calculations
Uses fallback values
Clearly communicates issues like missing sectors or dates

This ensures users still get useful results instead of errors.

 7. What would you improve if given more time?

Answer:

I would:

Add caching for API calls
Build a structured query planner before LLM
Improve entity normalization (e.g., sector mapping)
Add dashboards and visualizations
Enable multi-turn conversation memory

 8. How did you interpret ‘leadership updates’?

Answer:

I interpreted it as generating concise executive summaries.

The system provides:

Revenue overview
Pipeline health
Sector performance
Risk indicators

This matches what leadership typically expects in updates.

 9. What are the limitations of your system?

Answer:

Limited scalability due to Pandas
LLM responses depend on prompt quality
No deep historical trend analysis

However, it works well as a fast, flexible prototype.

 10. Why should we hire you based on this project?

Answer (IMPORTANT):

This project shows I can:

Handle ambiguity and make decisions quickly
Build a working system under time constraints
Focus on business value, not just code

I prioritized delivering a usable solution rather than overengineering.
