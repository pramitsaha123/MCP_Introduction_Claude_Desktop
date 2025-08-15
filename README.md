# FastMCP Expense Tracker

A simple expense tracking application built with FastMCP and Streamlit that allows you to manage your expenses through natural language commands.

## Features

- Add expenses with category, date, and amount
- List all expenses
- View expenses by category
- Calculate total expenses by month
- Calculate total expenses by category
- Natural language interface for all operations

## Requirements

- Python 3.12+
- Model Context Protocol (MCP)
- Streamlit
- OpenAI API key (for natural language processing)

## Setup

1. Install dependencies:
```bash
pip install model-context-protocol streamlit python-dotenv openai
```

2. Set up your environment variables in a `.env` file:
```
OPENAI_API_KEY=your_api_key_here
OPENAI_API_BASE=https://api.openai.com/v1
```

## Running the Application

1. Start the MCP server:
```bash
python main.py
```

2. In a separate terminal, start the Streamlit interface:
```bash
streamlit run expense_tracker_streamlit.py
```

## Usage Examples

You can interact with the expense tracker using natural language commands:

- Add an expense: "Add expense food 2025-08-14 50.00"
- List all expenses: "Show me all expenses"
- View category total: "What are my total food expenses?"
- View monthly total: "Show expenses in August 2025"
- Get overall total: "What are my total expenses?"

## Data Storage

Expenses are stored in `expenses.json` in the following format:
```json
[
  {
    "category": "food",
    "date": "2025-08-01",
    "amount": 250.0
  }
]
```

## Project Structure

- `main.py`: MCP server implementation with core expense tracking functionality
- `expense_tracker_streamlit.py`: Streamlit web interface with natural language processing
- `expenses.json`: JSON file storing all expense records

## License

MIT License
