def validate_card(DEBIT_CARD=True):
    """
    The Card Reader validates the card if it can be used with ATM or not
    """
    return "1234-5678-9999-000" if DEBIT_CARD else False
