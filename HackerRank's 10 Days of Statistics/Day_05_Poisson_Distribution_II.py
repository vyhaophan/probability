X, Y = [float(i) for i in input().split()]

machineA = 160 + 40 * (X + X**2)
machineB = 128 + 40 * (Y + Y**2)

print(round(machineA, 3))
print(round(machineB, 3))