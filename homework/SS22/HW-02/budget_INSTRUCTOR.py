# The Budget class. You'll need to edit/expand on this.
class Budget:
    """
    This class is designed to create and store budget information.

    This class has the following attributes:

        income [type: int or float]
            This is the monthly income for the budget.
        expenses [type: int or float]
            This is the total monthly expenses.
        categories [type: dictionary]
            This is a dictionary of expense categories (keys)
            and estimated cost associated with those categories (values).

    This class (currently) has the following methods:

        __init__(income)
            Initialize the budget and set the income based on user input.
            Set the initial expenses to 0 and initialize the dictionary
            of categories to be empty.

        get_income()
            Print the current income associated with this budget.

        add_expense(category, limit)
            Add an expense category to the budget with an associated limit.

        check_budget():
            Check to see if the budget is balanced and print the budget status.

        adjust_income(adjustment)
            Increment or decrement the budget based on the adjustment value.
    """

    def __init__(self, income):
        """
        Initializes the budget.
        Default expenses are 0 and no expense categories are defined
        (as indicated by the empty dictionary).

        Argument(s):
            income [type: int or float]
                Specifies the monthly income
        """
        self.income = income
        self.expenses = 0
        self.categories = {}

    def get_income(self):
        '''
        Prints the current income. Requires no arguments.
        '''
        print('Your current income is %i dollars' %self.income)

    def add_expense(self, category, limit):
        '''
        Adds an expense category and its associated spending limit.
        This limit is added to the total expenses for the budget.

        Argument(s):
            category [type: string]
                Defines the category for the expense
            limit [type: int or float]
                Sets the spending limit for this category
        '''
        self.categories[category] = limit
        self.expenses += limit

    def check_budget(self):
        '''
        This checks to see if the budget is balanced.
        If the expenses are less than or equal to the total income
        then is considered under budget and the amount remaining is printed.
        If the expenses exceed the income then the amount over
        budget is printed.

        Argument(s):
            category [type: string]
                Defines the category for the expense
            limit [type: int or float]
                Sets the spending limit for this category
        '''
        print('Income is %i dollars.' %self.income)
        print('Expenses total %i dollars.' %self.expenses)
        difference = self.income - self.expenses
        if difference >= 0:
            print("You are at or under budget. You have %i dollars remaining." %difference)
        else:
            print("You are %i dollars over budget! Adjust your expenses." %abs(difference))

    def adjust_income(self, adjustment):
        '''
        This updates the current income by the amount specified.

        Argument(s):
            adjustment [type: int or float]
                The amount to increment (or decrement) the current income.
        '''
        self.income += adjustment

class EnhancedBudget(Budget):
    '''
    This class builds slightly off of the Budget class.

    It has the same attributes as the Budget class as well as
    one new attribute:

        transactions [type: dictionary]
            This is used to store transactions in their corresponding
            categories to track expenses over the course of a month.
            This defaults to an empty dictionary.

    This class has one new method in addition to those already in Budget:

        log_transaction(category, amount)
            For each transaction, a category and amount must be specified.
            This transactions is then added to the transactions attribute.
    '''

    def __init__(self, income):
        '''
        Initialize EnhancedBudget class.
        '''
        # this calls initialization of the Budget class
        # and passes through the original income amount.
        super().__init__(income)
        self.transactions = {}

    def log_transaction(self,category,amount):
        if category in self.transactions:
            self.transactions[category].append(amount)
        else:
            self.transactions[category] = [amount]
