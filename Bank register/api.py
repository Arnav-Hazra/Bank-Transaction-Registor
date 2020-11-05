import tornado.ioloop
import tornado.web
from register import Register
from addhandler import AddHandler
from gettransaction import GetTransaction
from gethandler import GetHandler

register = Register()

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Bank Transaction Register")


def make_app():
    return tornado.web.Application([
        (r"/v1", MainHandler),
        (r"/v1/addtransaction", AddHandler, dict(register = register)),
        (r"/v1/gettransaction", GetTransaction, dict(register = register)),
        (r"/v1/getsum", GetHandler, dict(register = register)),
        ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

# instructions for Bank Transaction Register
# -by Arnav Hazra (BT17GCS014)

# To start the app, open terminal and cd to the folder and run
# 	python api.py

# in browser:
# >to start the app
# http://localhost:8888/v1

# >to add transactions
# http://localhost:8888/v1/addtransaction?account_no=12345&date="05October20"&type="deposit"&amount=1200
# http://localhost:8888/v1/addtransaction?account_no=12345&date="10October20"&type="deposit"&amount=1500
# http://localhost:8888/v1/addtransaction?account_no=123456&date="05November20"&type="deposit"&amount=2000
# http://localhost:8888/v1/addtransaction?account_no=123456&date="05October20"&type="withdraw"&amount=500

# >to get transactions
# http://localhost:8888/v1/gettransaction?account_no=123456
# http://localhost:8888/v1/gettransaction?account_no=12345

# >to get Sum of deposits
# http://localhost:8888/v1/getsum
  