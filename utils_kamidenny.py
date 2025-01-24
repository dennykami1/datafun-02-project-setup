"""
Module: utils_kamidenny

Purpose: Reusable Module for My Analytics Projects

Description: This module provides a great example of how to create a
byline for my analytics projects. When we work hard to write useful code,
we want it to be reusable. This module displays how statistics, variables,
and F-Strings can be incorporated into our code.

Author: Kami Denny

"""

#####################################
# Import Modules
#####################################

# Import helpful modules from the Python Standard library
# See more at: https://docs.python.org/3/library/

import statistics  # provides mean(), stdev() and more....

#####################################
# Declare Global Variables
#####################################

# declare a boolean variable (has a value True or False)
has_401k_matching = True

# declare integer variables 
years_in_operation: int = 10

count_of_holidays: int = 11

# declare a floating point variable
average_employee_satisfaction: float = 4.7

# declare a list of strings 
skills_offered: list = ["Data Analysis", "Machine Learning", "Business Intelligence"]

benefits_offered: list = ["Unlimited PTO", "Health Insurance", "Life Insurance", "Remote Work Options"]

# declare a list of numbers so we can illustrate statistics skills
employee_satisfaction_scores: list = [4.3, 4.6, 4.9, 4.5, 4.2, 4.0]
years_until_promotion: list = [1.8, 2.4, 1.1, 1.3, 2.0, 1.6]

# Calculate basic statistics using built-in Python functions and the statistics module
min_score: float = min(employee_satisfaction_scores)  
max_score: float = max(employee_satisfaction_scores)  
mean_score: float = statistics.mean(employee_satisfaction_scores)  
stdev_score: float = statistics.stdev(employee_satisfaction_scores)

min_years: float = min(years_until_promotion)  
max_years: float = max(years_until_promotion)  
mean_years: float = statistics.mean(years_until_promotion)  
stdev_years: float = statistics.stdev(years_until_promotion)

# Use a Python formatted string (f-string) to show information
byline: str = f"""
---------------------------------------------------------
Stellar Analytics: Delivering Professional Insights
---------------------------------------------------------
Skills Offered:              {skills_offered}
Years in Operation:          {years_in_operation}
Benefits Offered:            {benefits_offered}
Offers 401k Matching:        {has_401k_matching}
Number of Paid Holidays:     {count_of_holidays}
Employee Satisfaction Scores:  {employee_satisfaction_scores}
Minimum Satisfaction Score:    {min_score}
Maximum Satisfaction Score:    {max_score}
Mean Satisfaction Score:       {mean_score:.2f}
Standard Deviation of Satisfaction Scores:  {stdev_score:.2f}
Years Until Employees Achieve Promotion:    {years_until_promotion}
Minimum Years until Promotion:              {min_years}
Maximum Years until Promotion:              {max_years}
Mean Years until Promotion:                 {mean_years:.2f}
Standard Deviation Years until Promotion:   {stdev_years:.2f}
"""

#####################################
# Define global functions (resuable instructions)
#####################################

def get_byline() -> str:
    '''
    Get a byline for my analytics projects.
       
    Returns a string byline that illustrates my specific skills.

    A function is a block of code that performs a task.
    This function just returns our byline.
    We can call this (or other functions) in later modules 
    so we can write it once and reuse it. 
    We use a type hint to indicate this function returns a string
    (that is, it has a Python type of str).
    It doesn't need any additional information passed in, 
    so there's nothing needed inside the parentheses.
    Everything afer the colon must be indented consistently (usually 4 spaces)
    '''
    return byline

#####################################
# Define main function for this module.
#####################################

def main() -> None:
    '''
    Print results of get_byline() when main() is called.

    This function just prints the byline to the console when we run this as a script.
    The type hint indicates this function doesn't return anything when called 
    (that is, it has a Python type of None).
    It doesn't need any additional information passed in, 
    so there's nothing inside the parentheses.
    Everything afer the colon must be indented consistently (usually 4 spaces)
    '''

    print("Starting........")
    print(get_byline())
    print("Complete.......")

#####################################
# Conditional Execution
#####################################

# If we are running this file as a script then call main()
# and verify our code works as expected.

if __name__ == '__main__':
    main()

#TODO: Run this as a script and verify all code works as intended.
