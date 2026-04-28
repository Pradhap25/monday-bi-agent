import streamlit as st
from monday_api import fetch_board_data
from data_processing import clean_data
from agent import ask_llm

st.set_page_config(page_title="Monday BI Agent", page_icon="📊")

st.title("📊 Monday.com BI Agent")
st.caption("Ask founder-level business questions across Deals & Work Orders")

# 👉 Replace with your actual board IDs
DEALS_BOARD_ID = 5028115615
WORK_ORDERS_BOARD_ID = 5028115615   # (for testing, use same ID)

query = st.text_input("Your Question:")

if not query:
    st.info("Example questions:\n- How is our pipeline?\n- Energy sector performance this quarter\n- Which deals are at risk?")
else:
    try:
        with st.spinner("Fetching data from Monday.com..."):
            deals_raw = fetch_board_data(DEALS_BOARD_ID)
            work_raw = fetch_board_data(WORK_ORDERS_BOARD_ID)

        with st.spinner("Cleaning data..."):
            deals_df = clean_data(deals_raw)
            work_df = clean_data(work_raw)

        with st.spinner("Analyzing..."):
            answer = ask_llm(query, deals_df, work_df)

        st.success("Answer:")
        st.write(answer)

    except Exception as e:
        st.error("Something went wrong ❌")
        st.exception(e)