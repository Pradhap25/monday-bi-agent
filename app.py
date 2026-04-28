import streamlit as st
from monday_api import fetch_board_data
from data_processing import clean_data
from agent import ask_llm

st.set_page_config(page_title="Monday BI Agent", page_icon="📊")

st.title("📊 Monday.com BI Agent")
st.caption("Ask founder-level business questions across Deals & Work Orders")

DEALS_BOARD_ID = 5028115615
WORK_ORDERS_BOARD_ID = 5028115615  # <-- change this

query = st.text_input("Ask your business question:")

if not query:
    st.info("""
    Example questions:
    • How is our pipeline this quarter?
    • Energy sector performance
    • Which deals are at risk?
    """)
else:
    try:
        with st.spinner("Fetching data from Monday.com..."):
            deals_raw = fetch_board_data(DEALS_BOARD_ID)
            work_raw = fetch_board_data(WORK_ORDERS_BOARD_ID)

        with st.spinner("Cleaning data..."):
            deals_df = clean_data(deals_raw)
            work_df = clean_data(work_raw)

        if deals_df.empty and work_df.empty:
            st.warning("No data found. Check board IDs or API access.")
            st.stop()

        with st.spinner("Analyzing..."):
            answer = ask_llm(
                query,
                deals_df.head(10).to_string(),
                work_df.head(10).to_string()
            )

        st.success("Answer:")
        st.write(answer)

    except Exception as e:
        st.error("Something went wrong ❌")
        st.exception(e)
