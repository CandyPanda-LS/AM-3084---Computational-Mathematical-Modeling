import math

# Define the utility function for a given wealth and coefficient of risk aversion
def utility(wealth, gamma):
    if gamma == 1:
        return math.log(wealth)
    else:
        return (wealth ** (1 - gamma)) / (1 - gamma)

# Define the expected utility for each option for a given farmer
def expected_utility(gamma, option, c):
    if option == 1:
        return 0.5 * utility(0.5, gamma) + (2/3) * utility(1.5, gamma) + (1/3) * utility(0.5, gamma)
    elif option == 2:
        return (2/3) * utility(1 - c + 0.5, gamma) + (1/3) * utility(1 - c + 0.5, gamma)
    elif option == 3:
        return (8/9) * utility(1 - c + 0.5, gamma) + (1/9) * utility(0.5, gamma)
    else:
        return None

# List of coefficients of risk aversion for each farmer
gammas = [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5]

# For each farmer, calculate the expected utility for each option
for i, gamma in enumerate(gammas):
    print(f"Farmer {i+1} (gamma = {gamma})")
    for option in [1, 2, 3]:
        for c in [0, 0.1, 0.2, 0.3, 0.4, 0.5]:
            eu = expected_utility(gamma, option, c)
            print(f"  Option {option} (c = {c}): {eu}")
    print()
