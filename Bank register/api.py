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
