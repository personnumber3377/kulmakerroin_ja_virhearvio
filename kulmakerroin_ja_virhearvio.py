
l = 0.90 # m
D = 0.00008 # 0.008 # mm
lambda_1 = 635*(10**(-9)) # nm

k1 = l*lambda_1/D
print("Value for k1: "+str(k1))

kdiff = ((l+0.0001)*lambda_1/D)-(l*lambda_1/D)

print("Difference: "+str(kdiff))

d = 0.005 # This is in meters# 0.5 mm

k2 = l*lambda_1/d
print("Value for k1: "+str(k2))

'''
These are the respective values:

0.00714375
0.00011430000000000001

'''


dl = 0.001 # in meters # 0.1 #cm
dk = kdiff # 0.001 # Some placeholder value...

dD = -(l*lambda_1)/(k1**2)*dk + lambda_1/k1*dl

print("Value of dD: "+str(dD))

