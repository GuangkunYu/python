import os

tuples = os.walk("demo")

for tuple in tuples:
    print(tuple, "\n")

print('--------------------')

print(os.listdir('demo'))