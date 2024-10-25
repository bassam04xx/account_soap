from django.db import models

class Client(models.Model):
    cin=models.CharField(max_length=9,primary_key=True)
    name = models.CharField(max_length=255)
    familyName = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    def __str__(self):
        return f'cin = {self.cin}, email={self.email}'

    class Meta:
        ordering=['email','cin']
        db_table='clients'

class Account(models.Model):
    balance=models.DecimalField(max_digits=15,decimal_places=3)
    client=models.ForeignKey(Client, on_delete=models.SET_NULL,null=True)
    creation_date=models.DateField(auto_now_add=True)
    def __str__(self):
        return f'client : {self.client}, balance= {self.balance}'
    class Meta:
        db_table='accounts'
class TransactionType(models.TextChoices):
    WITHDRAW=("WTD",'withdraw transaction')
    DEPOSIT=("DEP",'deposit transaction')
    TRANSFER=('TRAN','transfer transaction')
    
class Transaction(models.Model):
    amount=models.DecimalField( max_digits=9, decimal_places=3)
    date=models.DateTimeField(auto_now_add=True)
    transactionType=models.CharField(max_length=20,choices=TransactionType.choices)
    account=models.ForeignKey(Account,on_delete=models.CASCADE)
    