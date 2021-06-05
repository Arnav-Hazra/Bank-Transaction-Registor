# Bank-Transaction-Registor

instructions for Bank Transaction Register
-by Arnav Hazra

To start the app,

* clone this repository, open terminal  
* cd Bank-Transaction-Registor  
* Will also require tornado to run this app, to install tornado
  - pip install tornado
* To run the app:
  - python api.py  

in browser:  
> enter the following to use the apps different functions  
* to start the app  
  - http://localhost:8888/v1

* to add transactions:  
 > Can change the variables according to need  
  - http://localhost:8888/v1/addtransaction?account_no=12345&date="05October20"&type="deposit"&amount=1200  
  - http://localhost:8888/v1/addtransaction?account_no=12345&date="10October20"&type="deposit"&amount=1500  
  - http://localhost:8888/v1/addtransaction?account_no=123456&date="05November20"&type="deposit"&amount=2000  
  - http://localhost:8888/v1/addtransaction?account_no=123456&date="05October20"&type="withdraw"&amount=500  

* to get transactions:  
  - http://localhost:8888/v1/gettransaction?account_no=123456  
  - http://localhost:8888/v1/gettransaction?account_no=12345  
- >an account that doesn't exist  
  - http://localhost:8888/v1/gettransaction?account_no=1234  

* to get Sum of total amount in bank:  
  - http://localhost:8888/v1/getsum  
  
