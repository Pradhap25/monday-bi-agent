import requests

API_KEY = ""   # 🔴 put your real key here
URL = "https://api.monday.com/v2"

HEADERS = {
    "Authorization": API_KEY,
    "Content-Type": "application/json",
    "API-Version": "2023-10"   # ensures items_page works
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

    # --- Always parse safely ---
    try:
        data = resp.json()
    except Exception:
        raise Exception(f"Non-JSON response (status {resp.status_code}): {resp.text[:300]}")

    # --- Show real API errors instead of KeyError ---
    if "errors" in data:
        raise Exception(f"Monday API Error: {data['errors']}")

    if "data" not in data or not data["data"].get("boards"):
        raise Exception(f"Invalid/empty response. Check API key & board access.\nResponse: {data}")

    board = data["data"]["boards"][0]

    if not board.get("items_page") or not board["items_page"].get("items"):
        # No items is not a crash—just return empty list
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