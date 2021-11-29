def validate_cash(cash):
    """
    A fake deposit slot function to validate cash (counterfeit cash)
    """
    return cash


def collect_cash(CASH=100):
    """
    A fake deposit slot function to collect cash that user inputs
    """
    validated_cash = validate_cash(cash=CASH)

    return validated_cash


def return_cash(cash):
    """
    A fake deposit slot function to return cash
    that user requests with withdrawal transaction
    """
    return True if cash else False
