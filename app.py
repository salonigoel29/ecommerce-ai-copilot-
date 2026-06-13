import streamlit as st
import pandas as pd
import plotly.express as px
from groq import Groq
import os

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

st.set_page_config(page_title="Ecommerce AI Copilot", page_icon="🛒", layout="wide")
st.title("🛒 Ecommerce AI Copilot")
st.caption("Upload your sales data and ask questions in plain English")

@st.cache_data
def load_sample_data():
    import random
    random.seed(42)
    categories = ["Electronics", "Clothing", "Home & Garden", "Sports", "Beauty", "Books"]
    regions = ["North", "South", "East", "West"]
    rows = []
    for month in range(1, 13):
        for _ in range(50):
            rows.append({
                "date": f"2024-{month:02d}-{random.randint(1,28):02d}",
                "category": random.choice(categories),
                "region": random.choice(regions),
                "orders": random.randint(10, 500),
                "revenue": round(random.uniform(500, 50000), 2),
                "returns": random.randint(0, 30),
                "avg_order_value": round(random.uniform(20, 300), 2),
            })
    return pd.DataFrame(rows)

with st.sidebar:
    st.header("Upload Data")
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
    if st.button("Use sample data instead"):
        st.session_state["use_sample"] = True

    st.markdown("---")
    st.markdown("**Example questions:**")
    st.markdown("- Which category has the highest revenue?")
    st.markdown("- Show me monthly revenue trends")
    st.markdown("- Which region is underperforming?")
    st.markdown("- What are the top insights from this data?")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success(f"Loaded {len(df)} rows from {uploaded_file.name}")
elif st.session_state.get("use_sample"):
    df = load_sample_data()
    st.info("Using sample ecommerce dataset (2024 sales data)")
else:
    df = None

if df is not None:
    st.subheader("Data Preview")
    st.dataframe(df.head(10), use_container_width=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Rows", f"{len(df):,}")
    with col2:
        st.metric("Columns", len(df.columns))
    with col3:
        if "revenue" in df.columns:
            st.metric("Total Revenue", f"${df['revenue'].sum():,.0f}")

    st.markdown("---")
    st.subheader("Ask a Question")
    question = st.text_input("What do you want to know about your data?", placeholder="e.g. Which category has the highest revenue?")

    if question:
        with st.spinner("Analyzing..."):
            data_summary = f"""
Dataset shape: {df.shape}
Columns: {list(df.columns)}
Data types: {df.dtypes.to_dict()}
Sample (first 5 rows):
{df.head(5).to_string()}

Summary statistics:
{df.describe().to_string()}
"""
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": f"""You are an ecommerce data analyst. Analyze this dataset and answer the question.

Dataset info:
{data_summary}

Question: {question}

Provide:
1. A direct answer to the question
2. Key insight or recommendation for the business
3. One specific action the business should take

Be concise and business-focused."""}]
            )
            answer = response.choices[0].message.content

        st.markdown("### AI Analysis")
        st.markdown(answer)

        st.markdown("---")
        st.subheader("Quick Charts")

        if "category" in df.columns and "revenue" in df.columns:
            fig = px.bar(
                df.groupby("category")["revenue"].sum().reset_index().sort_values("revenue", ascending=False),
                x="category", y="revenue", title="Revenue by Category",
                color="revenue", color_continuous_scale="Blues"
            )
            st.plotly_chart(fig, use_container_width=True)

        if "date" in df.columns and "revenue" in df.columns:
            df["month"] = pd.to_datetime(df["date"]).dt.to_period("M").astype(str)
            monthly = df.groupby("month")["revenue"].sum().reset_index()
            fig2 = px.line(monthly, x="month", y="revenue", title="Monthly Revenue Trend", markers=True)
            st.plotly_chart(fig2, use_container_width=True)

        if "region" in df.columns and "orders" in df.columns:
            fig3 = px.pie(df.groupby("region")["orders"].sum().reset_index(), values="orders", names="region", title="Orders by Region")
            st.plotly_chart(fig3, use_container_width=True)
else:
    st.markdown("### Get Started")
    st.markdown("Upload a CSV file or click **'Use sample data instead'** in the sidebar to try the app.")
