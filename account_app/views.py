from spyne.service import ServiceBase
from spyne.protocol.soap import Soap11
class AccountService(ServiceBase):
    def add_account(self, account):
        #store the account on the database
        pass