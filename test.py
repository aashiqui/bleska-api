import psutil

import platform

# Architecture
print("Architecture: " + platform.architecture()[0])

# machine
print("Machine: " + platform.machine())

# node
print("Node: " + platform.node())

# system
print("System: " + platform.system())

# distribution
dist = platform.dist()
dist = " ".join(x for x in dist)
print("Distribution: " + dist)




# gives a single float value
print(psutil.cpu_percent())
# gives an object with many fields
print(psutil.virtual_memory())
# you can convert that object to a dictionary 
print(dict(psutil.virtual_memory()._asdict()))
# you can have the percentage of used RAM
print(psutil.virtual_memory().percent)
#79.2
# you can calculate percentage of available memory
print(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total)