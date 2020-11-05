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
