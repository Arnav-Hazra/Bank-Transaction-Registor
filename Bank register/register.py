import json


class Register:

    def __init__(self):
        self.register = []

    def add_Transaction(self, account_no, date, type, amount):
        new_transaction = {}
        new_transaction["Account_no"] = account_no
        new_transaction["Date"] = date
        new_transaction["Type"] = type
        new_transaction["Amount"] = amount
        self.register.append(new_transaction)
        print(": {0}".format(new_transaction))
        return json.dumps(new_transaction)


    def get_Transaction(self, account_no):
        temp = []
        for i in range(len(self.register)):
            if int(self.register[i]['Account_no']) == int(account_no):
                temp.append(self.register[i])
        return temp
    
    def get_Sum(self):
        sum = 0
        for i in range(len(self.register)):
            if self.register[i]['Type'] == u'"deposit"' :
                sum = sum + int(self.register[i]['Amount'])
        return sum

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
  