import numpy as np
from scipy.optimize import minimize_scalar

def utility(wi, gamma):
    if gamma == 1:
        return np.log(wi)
    else:
        return (np.log(wi**(1-gamma))/(1-gamma))

# Define the coefficients of risk aversion for each farmer
gammas = [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5]
p = 1/9

# For each farmer, calculate the expected utility for each option
for i, gamma in enumerate(gammas):
    wi = 0.5
    eu_no_ins = p*utility(wi, gamma) + (1-p)*utility(wi+1, gamma)
    res = minimize_scalar(lambda x: -(p*utility(wi+1-x, gamma) + (1-p)*utility(wi+1, gamma)), bounds=(0,1), method='bounded')
    eu_traditional_ins = -res.fun
    res = minimize_scalar(lambda y: -((1/9)*p*utility(wi+1-y, gamma) + (8/9)*(1-p)*utility(wi+1, gamma)), bounds=(0,1), method='bounded')
    eu_index_ins = -res.fun

    # Compare the expected utility for each option to determine the best choice
    best_choice = max(eu_no_ins, eu_traditional_ins, eu_index_ins)
    if best_choice == eu_no_ins:
        print("Farmer {}: Best choice is to not purchase insurance, with expected utility {}".format(i+1, eu_no_ins))
    elif best_choice == eu_traditional_ins:
        print("Farmer {}: Best choice is to purchase traditional insurance, with expected utility {}".format(i+1, eu_traditional_ins))
    else:
        print("Farmer {}: Best choice is to purchase index insurance, with expected utility {}".format(i+1, eu_index_ins))
