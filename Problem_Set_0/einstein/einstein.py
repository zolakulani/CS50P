# Calculates energy (E=mc²) from user-input mass,
# where c is the speed of light (~3e8 m/s)
mass = int(input("Please Enter mass: "))
c = 300000000
energy = mass * pow(c, 2)
print("E", energy)