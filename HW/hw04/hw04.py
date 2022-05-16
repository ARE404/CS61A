def merge(lst1, lst2):
    """Merges two sorted lists.

    >>> merge([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    >>> merge([], [2, 4, 6])
    [2, 4, 6]
    >>> merge([1, 2, 3], [])
    [1, 2, 3]
    >>> merge([5, 7], [2, 4, 6])
    [2, 4, 5, 6, 7]
    """
    # if max(len(lst1),len(lst2))==0:
    #     return []
    # edge case, either is empty
    if not lst1:
        return lst2
    if not lst2:
        return lst1
    # judge the first element
    if lst1[0]>lst2[0]:
        return [lst2[0]]+merge(lst1,lst2[1:])
    elif lst1[0]<lst2[0]:
        return [lst1[0]]+merge(lst1[1:],lst2)
    else:
        return [lst1[0]]+merge(lst1[1:],lst2[1:])


class Mint:
    """A mint creates coins by stamping on years.

    The update method sets the mint's stamp to Mint.present_year.

    >>> mint = Mint()
    >>> mint.year
    2021
    >>> dime = mint.create(Dime)
    >>> dime.year
    2021
    >>> Mint.present_year = 2101  # Time passes
    >>> nickel = mint.create(Nickel)
    >>> nickel.year     # The mint has not updated its stamp yet
    2021
    >>> nickel.worth()  # 5 cents + (80 - 50 years)
    35
    >>> mint.update()   # The mint's year is updated to 2101
    >>> Mint.present_year = 2176     # More time passes
    >>> mint.create(Dime).worth()    # 10 cents + (75 - 50 years)
    35
    >>> Mint().create(Dime).worth()  # A new mint has the current year
    10
    >>> dime.worth()     # 10 cents + (155 - 50 years)
    115
    >>> Dime.cents = 20  # Upgrade all dimes!
    >>> dime.worth()     # 20 cents + (155 - 50 years)
    125
    """
    present_year=2021
    
    def __init__(self):
        self.year=self.present_year

    def create(self, coin):
        if coin is Nickel:
            return Nickel(self.year)
        if coin is Dime:
            return Dime(self.year)
        
    def update(self):
        self.year=self.present_year

class Coin:
    cents = None  # will be provided by subclasses, but not by Coin itself

    def __init__(self, year):
        self.year = year

    def worth(self):
        return self.cents+max((Mint.present_year-self.year-50),0)

class Nickel(Coin):
    cents = 5


class Dime(Coin):
    cents = 10


class VendingMachine:
    """A vending machine that vends some product for some price.
    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Nothing left to vend. Please restock.'
    >>> v.add_funds(15)
    'Nothing left to vend. Please restock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must add $10 more funds.'
    >>> v.add_funds(7)
    'Current balance: $7'
    >>> v.vend()
    'You must add $3 more funds.'
    >>> v.add_funds(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.add_funds(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.add_funds(15)
    'Nothing left to vend. Please restock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.add_funds(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    # attributes: name,price,stock
    def __init__(self,name,price):
        self.name=name
        self.price=price
        self.stock=0
        self.balance=0
    # f vend(), no parameter, return a string
    # check for stock remaining
    # if there is no stock remain, hint
    # if there is stock remain, check for balance
    # if balance is not enough, hint
    # if balance is enough, return a string, included stock name and a change
    def vend(self):
        if self.stock==0:
            print(f"'Nothing left to vend. Please restock.'")
        elif self.balance>self.price:
            print(f"'Here is your {self.name} and ${self.balance-self.price} change.'")
            self.balance=0
            self.stock-=1
        elif self.balance==self.price:
            print(f"'Here is your {self.name}.'")
            self.balance=0
            self.stock-=1
        else:
            print(f"'You must add ${self.price-self.balance} more funds.'")
    # add_funds(self,balance)
    # add funds to balance, return a string hint remaining funds
    def add_funds(self,funds):
        if self.stock==0:
            print(f"'Nothing left to vend. Please restock. Here is your ${funds}.'")
        else:
            self.balance+=funds
            print(f"'Current balance: ${self.balance}'")
    # restock(self,newstock)
    def restock(self,newstock):
        self.stock+=newstock
        print(f"'Current {self.name} stock: {self.stock}'")