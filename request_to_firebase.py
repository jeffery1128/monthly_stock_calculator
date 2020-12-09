import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import time

cred = credentials.Certificate("C:/Users/Chun Ho Tse/git/monthly_stock_calculator/monthly_stock_calculator/monthly-stock-calculator.json")

firebase_admin.initialize_app(cred,{ 
    'databaseURL': 'https://monthly-stock-calculator.firebaseio.com/'
})

def callback(event):
    print(event.data)
    print('result received!')

#firebase_admin.db.reference()

ref = db.reference('/request')
#ref.set({
    #'Employee':
        #{
            #'emp1':{
                #'name': 'Wing',
                #'lname':   'Hui',
                #'age':47
            #}
        #}
#})

ref.set({
    'ticker' :'QQQ',
    'month'  : 12,
    'quantity': 1
})

#ref = db.reference('/result')
#time.sleep(5)
#ref.listen(callback)
#
#while 1 :
#    pass
