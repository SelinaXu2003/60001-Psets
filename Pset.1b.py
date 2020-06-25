# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 13:04:48 2020

@author: selina
"""


###PSET.1B
total_cost= float(input("Total cost:"))
annual_salary= float(input("Annual salary:"))
portion_saved= float(input("Portion saved as percentage:"))
semi_annual_raise= float(input("Semi annual salary raise:"))

#down payment
down_payment= total_cost*0.25

#finding the number of months
epsilon = 0.0001
current_savings = 0
r=0.04
months=0

while abs(current_savings-down_payment)>= epsilon and current_savings<=down_payment:
    months+=1
    if months in range(7,int(down_payment)+1,6):
        annual_salary= annual_salary*semi_annual_raise + annual_salary
        monthly_salary= annual_salary/12
    else:
        monthly_salary= annual_salary/12
    amount_saved_monthly=portion_saved*monthly_salary
    current_savings= current_savings+current_savings*r/12 + amount_saved_monthly
print("Number of months", months)
