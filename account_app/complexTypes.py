from spyne import ComplexModel, Unicode, Integer, Double,Date

class Client(ComplexModel):
    name=Unicode
    familyName=Unicode
    cin=Unicode
class Account(ComplexModel):
    id=Integer
    client=Client
    balance=Double
class Transaction(ComplexModel):
    id=Integer
    account=Account
    amount=Double
    transactionType=Unicode
    date=Date
    