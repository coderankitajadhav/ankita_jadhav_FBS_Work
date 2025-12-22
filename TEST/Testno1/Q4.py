area = float(input("Enter wall area: "))
ci = float(input("Cost/interior wall: "))
ce = float(input("Cost/exterior wall: "))

ti = 8 * ci
te = 8 * ce
print("Total painting cost =", ti + te)