import math

sen46 = math.sin(math.radians(46))
sen58 = math.sin(math.radians(58))
cos46 = math.cos(math.radians(46))
cos58 = math.cos(math.radians(58))

m2 = 0.07272
g = 9.81

Tab = (m2 * g * sen46)/(cos58 * sen46 + cos46 * sen58)
dTab = 0.77453
Tac = (m2 * g * sen58)/(cos58 * sen46 + cos46 * sen58)
dTac = 0.7006109

print(f"Tac: {Tac}")
print(f"Tab: {Tab}")

print(f"m1: {Tac/g}")
print(f"dm1: {dTac/g}")
print(f"m3: {Tab/g}")
print(f"dm3: {dTab/g}")

