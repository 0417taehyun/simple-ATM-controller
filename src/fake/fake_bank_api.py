from src.fake.fake_account_model import account


def validate_PIN(PIN, FAKE_PIN="0000"):
    """
    A fake bank API to validate PIN number
    """
    return True if PIN == FAKE_PIN else False


def see_balance(card_info):
    """
    A fake bank API to see balance
    """
    balance = account.balance
    return balance


def deposit(card_info, amounts):
    """
    A fake bank API to Deposit
    """
    account.balance += amounts
    return True


def withdraw(card_info, amounts):
    """
    A fake bank API to withdraw
    """
    if account.balance >= amounts:
        account.balance -= amounts
        return True
    else:
        return False
