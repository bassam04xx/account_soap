from spyne.service import ServiceBase,Unicode,rpc,Iterable,Application
from spyne.protocol.soap import Soap11
from .complexTypes import Account as ComplexAccount
from .models import Account as ModelAccount, Client as ModelClient

class AccountService(ServiceBase):
    @rpc(ComplexAccount, _returns=Unicode)
    def add_account(self, account:ComplexAccount)->str:
        acc=ModelAccount.objects.get(pk=account.RIB)
        if acc is not None:
            return 'This account already exists.'
        #verify if the client already exist
        #clt=ModelClient.objects.get(pk=account.client.cin)
        clt=ModelClient.objects.get(email__iexact=account.client.email)
        if clt is None:
            #create the client
            clt=ModelClient()
            clt.cin=account.client.cin
            clt.name=account.client.name
            clt.familyName=account.client.familyName
            clt.email=account.client.email
            clt.save()
        #Create a new instance of Account (ModelAccount)
        acc=ModelAccount()
        acc.RIB=account.RIB
        acc.creation_date=account.creation_date
        acc.balance=account.balance
        acc.client=clt
        acc.save()
        return 'The account has been created successfully.'

    @rpc(_returns=Iterable(ComplexAccount))
    def get_allAccounts(self):
        accounts=ModelAccount.objects.all()
        lstAccComplex=[]
        for account in accounts:
            lstAccComplex.append(ComplexAccount(account.RIB,account.client,account.balance,account.creationDate))

        for x in lstAccComplex:
            yield x

    @rpc(Unicode, _returns=ComplexAccount)
    def get_account_by_RIB(self, account_rib):
        #get the account from the database
        acc=ModelAccount.objects.get(RIB=account_rib)
        if acc is None:
            raise ValueError("Could not find account")
        #return the account as a ComplexAccount
        complexAcc=ComplexAccount()
        complexAcc.RIB=acc.RIB
        complexAcc.creation_date=acc.creation_date
        complexAcc.balance=acc.balance
        complexAcc.client=acc.client
        return complexAcc

#configure the SOAP API
application =Application(
    [AccountService],
    tns='bank.isg.tn',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11(),
)
django_app=DjangoApplication(application)
bank_soap_app=csrf_except(django_app)