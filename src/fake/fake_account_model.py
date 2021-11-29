from pydantic import BaseModel


class Account(BaseModel):
    """
    A fake account model to test
    """

    balance = 100


account = Account()
