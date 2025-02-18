import uuid
from datetime import datetime

class Expense:
    def __init__(self, title, amount):
        """
        Initializes an Expense object with the given title and amount.
        Sets the unique id, created_at, and updated_at timestamps.
        """
        self.id = str(uuid.uuid4())  # unique identifier
        self.title = title
        self.amount = amount
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at

    def update(self, title=None, amount=None):
        """
        Updates the title and/or amount of the expense and updates the updated_at timestamp.
        """
        if title:
            self.title = title
        if amount is not None:
            self.amount = amount
        self.updated_at = datetime.utcnow()  # Update timestamp on change

    def to_dict(self):
        """
        Returns a dictionary representation of the expense.
        """
        return {
            'id': self.id,
            'title': self.title,
            'amount': self.amount,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

class ExpenseDB:
    def __init__(self):
        """
        Initializes an ExpenseDB object with an empty list of expenses.
        """
        self.expenses = []

    def add_expense(self, expense):
        """
        Adds an expense to the database.
        """
        self.expenses.append(expense)

    def remove_expense(self, expense_id):
        """
        Removes an expense from the database by its ID.
        """
        self.expenses = [expense for expense in self.expenses if expense.id != expense_id]

    def get_expense_by_id(self, expense_id):
        """
        Retrieves an expense from the database by its ID.
        """
        for expense in self.expenses:
            if expense.id == expense_id:
                return expense
        return None  # Return None if not found

    def get_expense_by_title(self, title):
        """
        Retrieves a list of expenses by their title.
        """
        return [expense for expense in self.expenses if expense.title == title]

    def to_dict(self):
        """
        Returns a list of dictionaries representing all expenses in the database.
        """
        return [expense.to_dict() for expense in self.expenses]
