from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable

total_revenue_from_last_month = 216750
# Create the model
model = LpProblem(name="Telzee-problem", sense=LpMaximize)

# Initialize the decision variables
x1 = LpVariable(name="x1", lowBound=0)
x2 = LpVariable(name="x2", lowBound=0)
x3 = LpVariable(name="x3", lowBound=0)
x4 = LpVariable(name="x4", lowBound=0)

# Add the constraints to the model
model += (x1 + x2 + x3 + x4 <= 83, "One customer can use atmost one extra GB")
model += (150 * x1 + 150 * x2 + 150 * x3 + 150 * x4 <= 8000, "The company is willing to spend a capital cost of 8000 for promotion")

# #Objective function and adding to the model
obj_func = (250 - 150) * (x1 + x2 + x3 + x4) + total_revenue_from_last_month
model += obj_func

print(model)
print()
print()
print("----------------------------------------------------------------")
print()
print()


# Solve the problem
status = model.solve()
print(f"status: {model.status}, {LpStatus[model.status]}")
print(f"objective: {model.objective.value()}")
for var in model.variables():
    print(f"{var.name}: {var.value()}")