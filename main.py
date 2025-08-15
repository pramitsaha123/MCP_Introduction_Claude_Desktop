"""
FastMCP Simple Expense Tracker with persistence.
Run from the `examples/snippets/clients` directory:
    uv run server expense_tracker stdio
"""

from mcp.server.fastmcp import FastMCP
from datetime import datetime
from typing import List, Dict
import json
import os

# Create MCP server
mcp = FastMCP("ExpenseTracker")

# File to store expenses
DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "expenses.json")

# ----------------------
# Data Handling Functions
# ----------------------

def load_expenses() -> List[Dict]:
    """Load expenses from JSON file or return empty list if file not found."""
    try:
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        else:
            return []
    except Exception as e:
        print(f"Error loading expenses: {e}")
        return []


def save_expenses(data: List[Dict]):
    """Save expenses to JSON file."""
    try:
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=2)
        print(f"Debug: Successfully saved expenses to {DATA_FILE}")
    except Exception as e:
        print(f"Error saving expenses: {e}")


# Load initial expenses
expenses = load_expenses()


# ----------------------
# MCP Tools
# ----------------------

@mcp.tool()
def add_expense(category: str, date: str, amount: float) -> str:
    """
    Add an expense entry.
    date format: YYYY-MM-DD
    """
    try:
        datetime.strptime(date, "%Y-%m-%d")  # validate date format
    except ValueError:
        return "Invalid date format. Use YYYY-MM-DD."

    expense = {
        "category": category.lower(),
        "date": date,
        "amount": amount
    }
    expenses.append(expense)
    save_expenses(expenses)
    print(f"Debug: Added expense {expense}")
    print(f"Debug: Current expenses: {expenses}")
    return f"Expense added: {category} - {date} - {amount}"


@mcp.tool()
def list_expenses() -> List[Dict]:
    """List all recorded expenses"""
    return expenses


@mcp.tool()
def total_by_category(category: str) -> float:
    """Get total amount spent for a given category"""
    total = sum(e["amount"] for e in expenses if e["category"] == category.lower())
    return total


@mcp.tool()
def total_by_month(year: int, month: int) -> float:
    """Get total amount spent for a given month (1-12) and year"""
    total = 0.0
    for e in expenses:
        d = datetime.strptime(e["date"], "%Y-%m-%d")
        if d.year == year and d.month == month:
            total += e["amount"]
    return total


# Run the MCP server
if __name__ == "__main__":
    mcp.run()
