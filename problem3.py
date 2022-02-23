# Write a Python program to calculate the compound interest based on the given formula. Read inputs
# from the user.
# A = P * (1 + R/100)^T where P is the principle amount, R is the interest rate and T is time (in years).
# Define a function named as compound_interest_<your-student-id> in your program.
def compound_interest_(P,R,T):
    A=P*(1+R/100)**T
    print(f"The compound interest: {A}")
compound_interest_(2019,260,29)