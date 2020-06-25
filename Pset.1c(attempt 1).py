# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 12:00:12 2020

@author: selin
"""


#inputs
annual_salary= float(input("Annual salary:"))

#variables that are fixed
monthly_salary= annual_salary/12
semi_annual_raise=.07
monthly_rate_of_return=0.04/12
down_payment= 250000
epsilon= .001
months = 36


#function definitions
initial_high=10000
high= initial_high
low=0
months = 36
current_savings=0.0
portion_saved= (high+low)/2
steps=0


while abs(current_savings-down_payment)>= epsilon:
    steps+=1
    current_savings==0
    monthly_deposit = monthly_salary*(portion_saved/10000)
    for months in range(1,months+1):
        monthly_salary= annual_salary/12#gives me the monthly salary
    # figuring out potion saved
        amount_saved_monthly= monthly_salary*(portion_saved/10000)
        if months % 6 ==0:
            annual_salary= annual_salary*semi_annual_raise + annual_salary
            amount_saved_monthly= monthly_salary*(portion_saved/10000)
    current_savings = current_savings + float(current_savings*monthly_rate_of_return) + amount_saved_monthly
    prev_portion_saved = portion_saved
    
    if current_savings>down_payment:
        high = portion_saved
    else:
        low= portion_saved
    if prev_portion_saved== portion_saved:
        break
if prev_portion_saved == portion_saved and portion_saved== initial_high:
    print("It is not possible to pay the down payement in three years.")
else:
    print("Best saving rate:", portion_saved/10000)
    print("steps in bisection search:", steps)