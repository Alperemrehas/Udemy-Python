# Define a dictionary of vehicles
vehicles = {
    'dream': 'Honda 250T',
    'roadster': 'BMW R1100',
    'er5': 'Kawasaki ER5',
    'can-am': 'Bombardier Can-Am 250',
    'virago': 'Yamaha XV250',
    'tenere': 'Yamaha XT650',
    'jimny': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford Fiesta Ghia 1.4',
}

# Access and assign a specific vehicle to the variable 'my_car'
my_car = vehicles['fiesta']
print(my_car)  # Print the value of 'my_car'

# Access and assign another specific vehicle to the variable 'commuter'
commuter = vehicles['virago']
print(commuter)  # Print the value of 'commuter'

# Access a vehicle using the 'get' method and assign it to the variable 'learner'
learner = vehicles.get("er5")
print(learner)  # Print the value of 'learner'

# Iterate over the keys in the 'vehicles' dictionary and print each key-value pair
for key in vehicles:
    print(key, vehicles[key], sep=", ")

# Iterate over the key-value pairs in the 'vehicles' dictionary and print each pair
for key, value in vehicles.items():
    print(key, value, sep=", ")
