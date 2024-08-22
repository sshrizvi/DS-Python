class ATM:
    """
    A class representing an Automated Teller Machine (ATM) with basic functionalities
    such as creating a PIN, changing a PIN, checking balance, withdrawing money, and 
    depositing money.

    Attributes
    ----------
    pin : str
        The user's PIN for accessing the ATM.
    balance : float
        The user's account balance.

    Methods
    -------
    menu()
        Displays the main menu and processes user choices.
    create_pin()
        Allows the user to create a new PIN if they do not already have one.
    change_pin()
        Allows the user to change their existing PIN.
    check_balance()
        Allows the user to check their account balance after entering the correct PIN.
    withdraw_money()
        Allows the user to withdraw money from their account after entering the correct PIN.
    deposit_money()
        Allows the user to deposit money into their account.
    """

    def __init__(self, pin='', balance=0.0) -> None:
        """
        Initializes the ATM with a PIN and a balance, and displays the main menu.

        Parameters
        ----------
        pin : str, optional
            The initial PIN for the user (default is an empty string).
        balance : float, optional
            The initial balance of the user (default is 0.0).
        """
        self.pin = pin
        self.balance = balance
        self.menu()
    
    def menu(self) -> None:
        """
        Displays the main menu and prompts the user to select an option. 
        Based on the user's choice, the corresponding method is called.
        """
        print(f'{' MENU '.center(50,'-')}')
        choice = int(input('''
            1. Create Pin
            2. Change Pin
            3. Check Balance
            4. Withdraw Money
            5. Deposit Money
            Note : Enter 0 to Exit
            Enter your choice : '''))
        print(f'{''.center(50,'-')}')
        
        match choice:
            case 0:
                exit()
            case 1:
                self.create_pin()
            case 2:
                self.change_pin()
            case 3:
                self.check_balance()
            case 4:
                self.withdraw_money()
            case 5:
                self.deposit_money()
            case _:
                print('You entered a wrong choice :(')
    
    def create_pin(self) -> None:
        """
        Allows the user to create a new PIN if they do not already have one.
        If a PIN already exists, prompts the user to change the PIN instead.
        """
        if self.pin != '':
            print('\033[1;37;41m Error \033[0m You already have a PIN.')
            print('\033[1;37;44m Suggestion \033[0m Try changing the PIN :)')
        else:
            pin = input('Enter your PIN : ')
            self.pin = pin
            print('\033[1;37;42m Success \033[0m PIN created successfully... :)')
        
        self.menu()
    
    def change_pin(self) -> None:
        """
        Allows the user to change their existing PIN. 
        If no PIN exists, prompts the user to create one instead.
        """
        if self.pin == '':
            print('You do not have a PIN.')
            print('\033[1;37;44m Suggestion \033[0m Try creating the PIN :)')
        else:
            new_pin = input('Enter new PIN : ')
            if self.pin != new_pin:
                self.pin = new_pin
                print('\033[1;37;42m Success \033[0m PIN changed successfully... :)')
            else:
                print('\033[1;37;41m Error \033[0m New PIN cannot be the same as the old PIN :(')

        self.menu()

    def check_balance(self) -> None:
        """
        Allows the user to check their account balance after entering the correct PIN.
        If the PIN is incorrect, an error message is displayed.
        """
        pin = input('Enter your PIN : ')

        if self.pin == pin:
            print('\033[1;37;42m Success \033[0m Your balance is Rs.{}'.format(self.balance))
        else:
            print('\033[1;37;41m Error \033[0m Wrong PIN :(')

        self.menu()

    def withdraw_money(self) -> None:
        """
        Allows the user to withdraw money from their account after entering the correct PIN.
        If the balance is insufficient or the PIN is incorrect, an error message is displayed.

        Parameters
        ----------
        amount : float
            The amount of money to be withdrawn.
        """
        amount = float(input('Enter the amount to be withdrawn : '))
        pin = input('Enter your PIN : ')

        if self.pin == pin:
            if self.balance >= amount:
                self.balance -= amount
                print('\033[1;37;42m Success \033[0m Amount withdrawn successfully... :)')
            else:
                print('\033[1;37;41m Error \033[0m Insufficient balance :(')
        else:
            print('\033[1;37;41m Error \033[0m Wrong PIN :(')

        self.menu()

    def deposit_money(self) -> None:
        """
        Allows the user to deposit money into their account.

        Parameters
        ----------
        amount : float
            The amount of money to be deposited.
        """
        amount = float(input('Enter the amount to be deposited : '))
        
        self.balance += amount
        print('\033[1;37;42m Success \033[0m Amount deposited successfully... :)')

        self.menu()

# Driver Code   
user = ATM(pin=1234, balance=25000)