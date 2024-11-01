from spyne.service import ServiceBase
from spyne.protocol.soap import Soap11
from .complexTypes import Account
class AccountService(ServiceBase):
    def add_account(self, account:Account):
        #store the account on the database
        pass