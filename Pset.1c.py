# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 21:48:43 2020

@author: selin
"""


# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 15:18:23 2020

@author: selin
"""

# User input
annual_salary = float(input("Annual salary:"))

# Known variables
total_cost = 1000000

semi_annual_raise = 0.07

r = 0.04

down_payment = total_cost*0.25

months = 36


# Function from part b.

def calculate_current_savings(r, annual_salary, portion_saved, semi_annual_raise, months): 

    current_savings = 0

    monthly_salary = annual_salary/12

    counter = 0

    while counter < months:

        counter += 1

        if counter % 6 == 0:

            annual_salary += annual_salary*semi_annual_raise

            monthly_salary = annual_salary/12
        
        else:
            
            monthly_salary= annual_salary/12

        amount_saved_monthly=portion_saved*monthly_salary

        current_savings= current_savings+current_savings*r/12 + amount_saved_monthly

    return current_savings



achievable = True

while achievable:

    high_rate = 10000 

    low_rate = 0    

    best_rate = 0
    
    error_range_in_dollars = 100 

    current_savings = 0

    steps = 0
    
    

    current_savings = calculate_current_savings(r, annual_salary, high_rate/10000, semi_annual_raise, months)

    if( current_savings < (down_payment - error_range_in_dollars)):

        print("can't save enough down payment in 3 years")
        
        achievable = False

        break
    
    while abs(current_savings - down_payment) > error_range_in_dollars:

        best_rate = int((high_rate + low_rate) / 2)

        current_savings  =  calculate_current_savings(r, annual_salary, best_rate/10000, semi_annual_raise, months)

        steps += 1


        if(current_savings > down_payment ):

            high_rate = best_rate 

        else:

            low_rate = best_rate
        achievable = False
print("Current savings ", current_savings)

print("Best saving rate: ",best_rate/10000)

print("Bisection steps is: ", steps)

   



