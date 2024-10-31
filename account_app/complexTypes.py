from spyne import ComplexModel, Unicode, Integer, Double,Date

class Client(ComplexModel):
    name=Unicode
    familyName=Unicode
    cin=Unicode
    email=Unicode
class Account(ComplexModel):
    rib=Unicode
    client=Client
    balance=Double
    creationDate=Date
class Transaction(ComplexModel):
    id=Integer
    account=Account
    amount=Double
    transactionType=Unicode
    date=Date
    transferToAccount=Unicode
    