class Expense:
    def __init__(self, name, category, cost):
        self.name = name
        self.category = category
        self.cost = cost

    def __repr__(self):
        return f'<Expense(name={self.name}, Category={self.category}, cost=${self.cost:.2f})>'

