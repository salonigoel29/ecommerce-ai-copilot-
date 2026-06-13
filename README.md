# Ecommerce AI Copilot

An AI-powered analytics assistant for ecommerce businesses. Upload your sales data and ask questions in plain English — get instant insights, charts, and actionable recommendations.

## Demo

<img width="2876" height="1322" alt="image" src="https://github.com/user-attachments/assets/ce6ed08b-fd08-4903-a517-f075859e1531" />

<img width="2876" height="1322" alt="image" src="https://github.com/user-attachments/assets/6aa1dcd2-862b-4944-9a94-aa8e5f41843a" />

<img width="2876" height="1322" alt="image" src="https://github.com/user-attachments/assets/f20517c4-bb87-454f-9876-f3c32b302330" />

<img width="2876" height="1322" alt="image" src="https://github.com/user-attachments/assets/58b1edf0-0c40-4e96-8bea-e1ed7db9f6cd" />




## Features

- Upload any CSV sales dataset or use the built-in sample data
- Ask questions in natural language (e.g. "Which category has the highest revenue?")
- AI generates business insights and recommendations instantly
- Auto-generates charts: revenue by category, monthly trends, orders by region

## Tech Stack

- **Frontend:** Streamlit
- **AI:** Groq API (Llama 3.3 70B)
- **Data:** Pandas
- **Charts:** Plotly

## Getting Started

1. Clone the repo
   ```bash
   git clone https://github.com/salonigoel29/ecommerce-ai-copilot-.git
   cd ecommerce-ai-copilot-
   ```

2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

3. Set your Groq API key (free at [console.groq.com](https://console.groq.com))
   ```bash
   export GROQ_API_KEY="your-key-here"
   ```

4. Run the app
   ```bash
   streamlit run app.py
   ```

## Example Questions

- Which category has the highest revenue?
- What are the top insights from this data?
- Which region is underperforming?
- Show me monthly revenue trends

## Use Case

Built for ecommerce and retail teams who want to explore sales data without writing SQL or Python. Ask business questions, get analyst-quality answers instantly.
