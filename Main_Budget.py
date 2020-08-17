from dataclasses import dataclass


@dataclass()
class Expense:
    category: str
    amount: float
    split: bool

    @staticmethod
    def prompt_for_expense() -> Expense:
        cat = input('What category?')
        return Expense(cat, )


a = Expense.prompt_for_expense()