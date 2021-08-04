from matplotlib import pyplot as plt

agesX = [20, 25,30, 35, 40, 45, 50,55, 60,65]
salaryY = [18000, 20000,25000,28000,30000,35000,40000,45000,50000,50000]

agesX2 = [20, 25,30, 35, 40, 45, 50,55, 60,65]
salaryY2 = [16000, 18000,22000,24000,28000,30000,32000,35000,40000,45000]

plt.plot(agesX, salaryY,"--", label  = '2020')
plt.plot(agesX2, salaryY2,"x", label ='2010')

plt.xlabel('Ages')
plt.ylabel('Salary')
plt.title('This is a avarage salary in Uninted Kindom')
plt.legend()
plt.show()