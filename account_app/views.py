from spyne.service import ServiceBase,Unicode,rpc
from spyne.protocol.soap import Soap11
from .complexTypes import Account as ComplexAccount
from .models import Account as ModelAccount, Client as ModelClient
class AccountService(ServiceBase):
    @rpc(ComplexAccount, _returns=Unicode)
    def add_account(self, account:ComplexAccount)->str:
        #store the account on the database
        if ModelAccount.objects.get(pk=account.rib).exists():
            return f"An account with RIB {account.rib} already exists"
        (client,created)=ModelClient.objects.get_or_create(
            cin=account.client.cin,
            defaults={
                "id":account.client.id,
                "name":account.client.name,
                "familyName":account.client.familyName,
                "email":account.client.email,
                "cin":account.client.cin
            }
        )
        acc1=ModelAccount(account.rib,account)
        