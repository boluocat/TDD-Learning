
class Finance:
    """
    This is a class which implements several
    finance formulas using the TDD
    approach:
    """

    def cash_flow(self, income, expenses):
        """
        This method calculates the cash flow, Income - Expenses = Cash Flow
        """
        
        if income < 0:  
            return
        return income - expenses
    
    def net_worth(self, assets, debts):
        """
        This method calculates the net worth, Assets - debts = Net Worth
        """
        
        if assets < 0:
            return
        return assets - debts
    
    def net_income(self, revenue, expenses):
        """
        This method calculates the net income, Revenue - expenses = Net Income
        """
        
        if revenue < 0:
            return
        return revenue - expenses
    
    def simple_interest(self, principal, rate, time):
        """
        This method calculates the simple interest, Principal * Rate * Time = Simple Interest"""
        
        if principal < 0:
            return
        return principal * rate * time
    
    def gain_or_lose(self, market_price, purchase_price):
        """
        This method calculates the gain or loss, Market Price - Purchase Price = Gain or Loss
        """
        
        try:
            gain_lose = (market_price - purchase_price) / purchase_price
        except ZeroDivisionError:
            return "Didn't sell anything"
        else:
            return gain_lose