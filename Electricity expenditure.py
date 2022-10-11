
#calculating electricity expenditure for token users in Kenya 
token =  2.59 #this is the lowest unit possible that can be purchased
cost = 50  #cost of the standard unit offered
value = float(input('Enter a value: '))
expenditure = int(value/token * cost)
print('Your electricity expenditure is '+str(expenditure)+' Ksh.')
