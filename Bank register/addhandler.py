import tornado.web
import register
import json


class AddHandler(tornado.web.RequestHandler):
    def initialize(self, register):
        self.register = register
        
    def get(self):
        account_no = self.get_argument('account_no')
        date = self.get_argument('date')
        type = self.get_argument('type')
        amount = self.get_argument('amount')
        result = self.register.add_Transaction(account_no, date, type, amount)
        self.write(result)
