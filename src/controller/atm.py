from src.fake import fake_bank_api, fake_deposit_slot


class ATMController:
    def __init__(self, id, latitude, longitude):
        """
        id: the unique id of each ATM
        latitude: for the location of each ATM
        longitude: for the location of each ATM
        is_validated: to check the PIN number is validated
        card_info: to communicate with bank API for transactions
        """
        self.id = id
        self.latitude = latitude
        self.longitude = longitude
        self.is_validated = False
        self.card_info = None

    def key_pad(self, number):
        """
        It receives PIN number that user enters for validation and return it.
        """
        return number

    def balance(self):
        """
        To see balances with Bank API
        Users are required to insert card and validate the PIN number first
        """
        if not (self.card_info and self.is_validated):
            return {"message": "Authenticate your card first"}

        balance = fake_bank_api.see_balance(card_info=self.card_info)
        return {"message": f"The amounts of balance are {balance}"}

    def deposit(self):
        """
        To deposit with Bank API, deposit slot
        Users are required to insert card and validate the PIN number first

        Deposit slot would pick out conterfeit cash

        Using flag to check Bank API success
        """
        if not (self.card_info and self.is_validated):
            return {"message": "Authenticate your card first"}

        validated_cash = fake_deposit_slot.collect_cash()
        if not validated_cash:
            return {"message": "Nothing in deposit slot"}

        flag = fake_bank_api.deposit(
            card_info=self.card_info, amounts=validated_cash
        )
        if flag:
            balance = fake_bank_api.see_balance(card_info=self.card_info)
            return {
                "message": f"The amounts of balance after deposit are {balance}"  # noqa
            }

    def withdraw(self, amounts):
        """
        To withdraw with Bank API, deposit slot
        Users are required to insert card and validate the PIN number first

        Deposit slot would return cash that user requested

        Using flag to check Bank API success
        If balances are less than user's requests, it would return False
        """
        if not (self.card_info and self.is_validated):
            return {"message": "Authenticate your card first"}

        if not fake_deposit_slot.return_cash(amounts):
            return {"message": "Cash bin empty"}

        flag = fake_bank_api.withdraw(
            card_info=self.card_info, amounts=amounts
        )

        if flag:
            balance = fake_bank_api.see_balance(card_info=self.card_info)
            return {
                "message": f"The amounts of balance after withdrawal are {balance}"  # noqa
            }
        else:
            return {"message": f"Your balances are less than {amounts}"}
