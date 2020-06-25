# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 13:13:05 2020

@author: selin
"""


#inputs
annual_salary= float(input("Annual salary:"))

# known variables
semi_annual_raise= 0.07 #7%
annual_return= 0.04 #4%
down_payment= 1000000*0.25
months_in_total= 36
epsilon=100 #100 dollars
current_savings=0
steps =0
monthly_salary= annual_salary/12
initial_high=10000
high= initial_high
low=0
portion_saved= (high + low)/2 # divide by 10000 to get  % potion saved

while abs(current_savings-down_payment)>= epsilon and current_savings<=down_payment:
    steps+=1
    if months_in_total in range(7,months_in_total +1,6):
        annual_salary= annual_salary*semi_annual_raise + annual_salary
        monthly_salary= annual_salary/12 #gives me the monthly salary
        amount_saved_monthly= monthly_salary*(portion_saved/10000)
    else:
        monthly_salary= annual_salary/12#gives me the monthly salary
    # figuring out potion saved
        amount_saved_monthly= monthly_salary*(portion_saved/10000)
    current_savings = current_savings + float(current_savings*annual_return/12) + amount_saved_monthly
    prev_portion_saved = portion_saved
    if current_savings>=down_payment:
        high = portion_saved
    else:
        low = portion_saved
    
    if prev_portion_saved== portion_saved:
        break
if prev_portion_saved == portion_saved and portion_saved== initial_high:
    print("It is not possible to pay the down payement in three years.")
else:
    print("Best saving rate:", portion_saved/10000)
    print("steps in bisection search:", steps)

