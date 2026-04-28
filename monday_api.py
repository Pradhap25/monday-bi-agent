import requests
import streamlit as st

# 🔐 Read API key from Streamlit Secrets
API_KEY = st.secrets["MONDAY_API_KEY"]

URL = "https://api.monday.com/v2"

HEADERS = {
    "Authorization": API_KEY,
    "Content-Type": "application/json",
    "API-Version": "2023-10"
}

def fetch_board_data(board_id: int):
    query = f"""
    query {{
      boards(ids: {board_id}) {{
        id
        name
        items_page(limit: 100) {{
          items {{
            id
            name
            column_values {{
              id
              text
              column {{
                title
              }}
            }}
          }}
        }}
      }}
    }}
    """

    resp = requests.post(URL, json={"query": query}, headers=HEADERS, timeout=30)

    # --- Safe JSON parsing ---
    try:
        data = resp.json()
    except Exception:
        raise Exception(f"Non-JSON response (status {resp.status_code}): {resp.text[:300]}")

    # --- API errors ---
    if "errors" in data:
        raise Exception(f"Monday API Error: {data['errors']}")

    if "data" not in data or not data["data"].get("boards"):
        raise Exception(f"Invalid/empty response. Check API key & board access.\nResponse: {data}")

    board = data["data"]["boards"][0]

    if not board.get("items_page") or not board["items_page"].get("items"):
        return []

    items = board["items_page"]["items"]

    result = []
    for item in items:
        row = {"name": item.get("name", "")}

        for col in item.get("column_values", []):
            col_title = (col.get("column") or {}).get("title") or col.get("id")
            row[col_title] = col.get("text")

        result.append(row)

    return result
