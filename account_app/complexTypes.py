from spyne import ComplexModel,Integer,Double,Unicode,Date, DateTime
class Client(ComplexModel):
    cin = Unicode
    name=Unicode
    familyName=Unicode
    Email=Unicode

class Bank(ComplexModel):
    id=Integer
    name=Unicode
    creationDate=Date
    address=Unicode

class Account(ComplexModel):
    RIB=Unicode
    balance=Double
    creationDate=Date
    client=Client


class Transaction(ComplexModel):
    id=Integer
    amount=Double
    date=Date
    transactionType=Unicode
    ownerAccount=Account
    transfer_to_rib=Unicode