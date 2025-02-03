l = 0.90 # m
D = 0.00008 # 0.08 mm
lambda_1 = 635*(10**(-9)) # nm
k1 = l*lambda_1/D
print("Value for k1: "+str(k1))
kdiff = ((l+0.0001)*lambda_1/D)-(l*lambda_1/D)
print("Difference: "+str(kdiff))
d = 0.0005 # This is in meters# 0.5 mm
k2 = l*lambda_1/d
print("Value for k2: "+str(k2))
dl = 0.001 # in meters # 0.1 #cm
dk = kdiff # 0.001 # Some placeholder value...
dD = -(l*lambda_1)/(k1**2)*dk + lambda_1/k1*dl
print("Value of dD: "+str(dD))
print("Value of k1: "+str(k1))
new_D = l*lambda_1/k1
print("Value of D (in meters): "+str(new_D))
