import pandas as pd

def clean_data(data):
    cleaned = []

    for row in data:
        new_row = {}
        for key, value in row.items():
            if value is None or value == "":
                new_row[key] = "Unknown"
            else:
                new_row[key] = str(value).strip().lower()
        cleaned.append(new_row)

    # ✅ Convert list → DataFrame (THIS WAS MISSING)
    df = pd.DataFrame(cleaned)

    # Optional: normalize column names
    df.columns = [c.lower().strip() for c in df.columns]

    return df
