import tornado.web
import register
import json


class GetTransaction(tornado.web.RequestHandler):
    def initialize(self, register):
        self.register = register
        
    def get(self):
        account_no = int(self.get_argument('account_no'))
        result = self.register.get_Transaction(account_no)
        if len(result) == 0:
            self.write("Account number not found")
        else:
            self.write("Transactions are:\n{}".format(result))
