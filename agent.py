import streamlit as st
from openai import OpenAI
import os

# 🔐 Read API key safely (Cloud + Local)
GROQ_API_KEY = st.secrets.get("GROQ_API_KEY", os.getenv("GROQ_API_KEY"))

client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1"
)

def ask_llm(query, deals_data, work_data):

    context = f"""
You are a senior business intelligence advisor supporting founders and leadership teams.

Your role:
- Answer business questions conversationally
- Provide executive-level insights (not raw data)
- Focus on decisions, risks, and performance

IMPORTANT RULES:
- Do NOT mention raw task names (e.g., "task 1")
- Do NOT list raw rows or data dumps
- Always summarize at business level
- Be concise, structured, and actionable

DATA:
Deals Data:
{deals_data[:10]}

Work Orders Data:
{work_data[:10]}

RESPONSE GUIDELINES:

If the query is broad (pipeline, revenue, performance, sector overview), include:

🔹 Leadership Update:
- Pipeline Health
- Key Metrics (counts, trends, performance)
- Risks
- Action Items

Then provide:

1. Summary
2. Key Insights
3. Risks
4. Data Quality Notes
5. Recommendation

If the query is specific, skip the leadership block and answer directly with insights.

Always:
- Highlight missing or inconsistent data
- Mention assumptions if data is incomplete
- Focus on decision-making, not description
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": context},
            {"role": "user", "content": query}
        ]
    )

    return response.choices[0].message.content
