# Bank-Transaction-Registor

instructions for Bank Transaction Register
-by Arnav Hazra

To start the app, open terminal and cd to the folder and run
	python api.py

in browser:
>to start the app
http://localhost:8888/v1

>to add transactions
http://localhost:8888/v1/addtransaction?account_no=12345&date="05October20"&type="deposit"&amount=1200
http://localhost:8888/v1/addtransaction?account_no=12345&date="10October20"&type="deposit"&amount=1500
http://localhost:8888/v1/addtransaction?account_no=123456&date="05November20"&type="deposit"&amount=2000
http://localhost:8888/v1/addtransaction?account_no=123456&date="05October20"&type="withdraw"&amount=500

>to get transactions
http://localhost:8888/v1/gettransaction?account_no=123456
http://localhost:8888/v1/gettransaction?account_no=12345

>to get Sum of deposits
http://localhost:8888/v1/getsum
  
