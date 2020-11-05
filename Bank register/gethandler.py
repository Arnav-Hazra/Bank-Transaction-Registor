import tornado.web
import register
import json


class GetHandler(tornado.web.RequestHandler):
    def initialize(self, register):
        self.register = register
        
    def get(self):
        sum = self.register.get_Sum()
        self.write('{}'.format(sum))
