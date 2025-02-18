# Expense---Tracker
A simple expense tracker with python
## Description
This project is an expense tracker that allows you to manage your financial expenses. It includes two main classes:

- `Expense`: Represents an individual financial expense.
- `ExpenseDB`: Manages a collection of expenses.

## How to Clone the Repository

1. Clone the repository to your local machine:

```bash
git clone https://github.com/Outstanding-dot/Expense---Tracker.git
```

## Usage

Here's an example of how to use the `Expense` and `ExpenseDB` classes:

```python
from expense import Expense, ExpenseDB

# Create an expense
expense1 = Expense("Coffee", 5.99)

# Create a database and add an expense
db = ExpenseDB()
db.add_expense(expense1)

# Get all expenses
print(db.to_dict())

# Update an expense
expense1.update(title="Morning Coffee", amount=6.50)
print(expense1.to_dict())
```

