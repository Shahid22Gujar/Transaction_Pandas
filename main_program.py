import pandas as pd
from datetime import datetime,timedelta
import numpy as np
from enum import Enum
 
class Transaction_Parameters(Enum):
    DT = 'Debit Transaction'
    CT = 'Credit Transaction'
    CD = 'Cash Deposits'
    CW = 'Cash Withdrawls'
    ATMW = 'ATM Withdrawls'
    CCT ='Credit Cheque Transaction'
    DCT ='Debit Cheque Transaction'
    DCBT ='Debit Cross Border Transaction'
    CCBT ='Debit Cross Border Transaction'
    

columns=['Transaction_Date','Location','Payer','Entry_Type','Amount']
df=pd.read_csv('TransactionList2.csv',encoding = "ISO-8859-1", engine='c',usecols=columns,parse_dates=['Transaction_Date'])
df=df.dropna(how='any')
#calculating total no of cash deposits and cash withdrawls
cash_deposits_withdrawls=df['Entry_Type'].isin([Transaction_Parameters.CD.value,Transaction_Parameters.CW.value])
cash_deposits_withdrawls_row=df[cash_deposits_withdrawls]
# print(cash_deposits_withdrawls_row)
print(">>Total No.Of Cash Deposits + Cash Withdrawls for past 90 days=>",len(cash_deposits_withdrawls_row))
#Filtering Total No. of Cash Deposits + Cash Withdrawls for past 90 days
current_datetime=datetime.now()
last_90_day_date=current_datetime - timedelta(days=90)
# print(current_datetime.date(),last_90_day_date.date())
# format_to_filter=f'last_90_day_date.date()} date <= {current_datetime.date()}'
print()
print(cash_deposits_withdrawls_row[(cash_deposits_withdrawls_row['Transaction_Date'] >= str(last_90_day_date.date())) & (cash_deposits_withdrawls_row['Transaction_Date'] <= str(current_datetime.now()))])
print()
print("Printing No. of cash withdrawls  and cash deposits between 9000.00-9999.999")

#range value between 9000-9999.99
value_9000_to_10000=np.arange(9000,10000,.01).round(decimals=3)

cash_deposits_withdrawls_9000_to_10000=cash_deposits_withdrawls_row['Amount'].isin(value_9000_to_10000)
print(cash_deposits_withdrawls_row[cash_deposits_withdrawls_9000_to_10000])

print()
print("No. of all transactions (any transcation) between 9000-9999.99 ")
print()
all_transaction_between_9000_to_10000=df['Amount'].isin(value_9000_to_10000)
transaction_in_betwn_range=df[all_transaction_between_9000_to_10000]
print(transaction_in_betwn_range)
print()
print("Mail sent to xyz@gmail.com Regarding below transacaction from which have done>>")
print(transaction_in_betwn_range['Location'].value_counts())
