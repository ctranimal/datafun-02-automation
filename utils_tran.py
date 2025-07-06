"""
File: utils_tran.py

Purpose: Reusable Module for My Analytics Projects

Description: This module provides a byline for my analytics projects. 
When we work hard to write useful code, we want it to be reusable.
A good byline could be used in every Python analytics project we do.

Author: Canh Tran
"""

#####################################
# Import Modules
#####################################

# Import helpful modules from the Python Standard library
# See more at: https://docs.python.org/3/library/

import statistics


#####################################
# Declare Global Variables
#####################################

# declare a boolean variables (have a value True or False)
ct_has_international_clients: bool = True

# declare integer variables
ct_years_num_operational: int = 1

# declare a floating point variables
ct_avg_client_satisfaction: float = 4.7

# declare lists of strings
ct_skills_offered: list = ["Data Engineering", "BI Dashboards", "Data Storytelling"]


# declare lists of numbers to illustrate statistics skills
ct_client_satisfaction_scores: list = [1.9, 1.7, 1.8, 1.0, 1.6]

# Calculate basic statistics using built-in Python functions and the statistics module
min_score: float = min(ct_client_satisfaction_scores)  
max_score: float = max(ct_client_satisfaction_scores)  
mean_score: float = statistics.mean(ct_client_satisfaction_scores)  
stdev_score: float = statistics.stdev(ct_client_satisfaction_scores)

# Use a Python formatted string (f-string) to show information

byline: str = f"""
--------------------------------------------------------------
Mr Tran's Stellar Analytics: Delivering Professional Insights
--------------------------------------------------------------
Has International Clients:  {ct_has_international_clients}
Years in Operation:         {ct_years_num_operational}
Skills Offered:             {ct_skills_offered}
Client Satisfaction Scores: {ct_client_satisfaction_scores}
Minimum Satisfaction Score: {min_score}
Maximum Satisfaction Score: {max_score}
Mean Satisfaction Score: {mean_score:.2f}
Standard Deviation of Satisfaction Scores: {stdev_score:.2f}
"""

#####################################
# Define global functions
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
    Everything after the colon must be indented consistently (usually 4 spaces)
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
    Everything after the colon must be indented consistently (usually 4 spaces)
    '''

    print("START main() in utils_tran.py")
    print(get_byline())
    print("END main() in utils_tran.py")

#####################################
# Conditional Execution
#####################################

# If we are running this file as a script then call main()
# and verify our code works as expected.

if __name__ == '__main__':
    main()