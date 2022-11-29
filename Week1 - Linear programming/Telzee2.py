from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable
import numpy


# Create the model
model = LpProblem(name="Telzee-problem2", sense=LpMaximize)

matrix = [[[LpVariable(name="x"+str(j)+str(j), lowBound=0)] for j in range(5)] for i in range(84)]
print(matrix)

sigma = 0
for i in range(0,84):
    sigma =  matrix[i][0] + matrix[i][1] + matrix[i][2] + matrix[i][3]

# Add the constraints to the model
for i in range(1,84):
     model += (matrix[i][0] + matrix[i][1] + matrix[i][2] + matrix[i][3] <= 1, "One customer can use atmost one extra GB"+str(i))

model += (150 * sigma <= 8000, "x")
# #Objective function and adding to the model
obj_func = (250 * 867) + (250-150) * sigma
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