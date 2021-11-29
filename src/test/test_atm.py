import unittest

from src.controller import ATMController
from src.fake import account, fake_bank_api, fake_card_reader


class TestATMController(unittest.TestCase):
    def setUp(self):
        self.atm = ATMController(
            id="test1234",
            latitude="37.547076399306",
            longitude="127.04020267241",
        )

        self.atm.card_info = fake_card_reader.validate_card()
        PIN_number = self.atm.key_pad(number="0000")

        flag = fake_bank_api.validate_PIN(PIN=PIN_number)
        self.atm.is_validated = flag

        account.balance = 100

    def test_balance_success(self):
        print("Balance Success Test")
        message = self.atm.balance()

        self.assertEqual(
            first=message,
            second={
                "message": f"The amounts of balance are {account.balance}"
            },
        )

    def test_deposit_success(self):
        print("Deposit Success Test")
        DEPOSITED_CASH = 100
        balance = account.balance + DEPOSITED_CASH
        message = self.atm.deposit()

        self.assertEqual(
            first=message,
            second={
                "message": f"The amounts of balance after deposit are {balance}"  # noqa
            },
        )

    def test_withdraw_success(self):
        print("Withdraw Test")
        AMOUNTS = 50
        balance = account.balance - AMOUNTS
        message = self.atm.withdraw(amounts=AMOUNTS)

        self.assertEqual(
            first=message,
            second={
                "message": f"The amounts of balance after withdrawal are {balance}"  # noqa
            },
        )

    def test_withdraw_not_enough_balance(self):
        print("Withdraw Not Enough Balance Test")
        AMOUNTS = 120
        message = self.atm.withdraw(amounts=AMOUNTS)

        self.assertEqual(
            first=message,
            second={"message": f"Your balances are less than {AMOUNTS}"},
        )
