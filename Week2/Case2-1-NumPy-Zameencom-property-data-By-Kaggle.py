#zameencom-property-data-By-Kaggle.csv
import numpy as np

ids, price , long , lat = np.genfromtxt('Week2/zameencom-property-data-By-Kaggle-short.csv', delimiter=';', usecols=(0,4,8,9), unpack=True, dtype=None,skip_header=1)

print(ids)
print(price)
print(long)
print(lat)

# Zameen.com price  - statistics operations
print("Zameen.com Price mean: " , np.mean(price))
print("Zameen.com Price average: " , np.average(price))
print("Zameen.com Price std: " , np.std(price))
print("Zameen.com Price median: " , np.median(price))
print("Zameen.com Price percentile - 25: " , np.percentile(price,25))
print("Zameen.com Price percentile  - 75: " , np.percentile(price,75))
print("Zameen.com Price percentile  - 3: " , np.percentile(price,3))
print("Zameen.com Price min : " , np.min(price))
print("Zameen.com Price max : " , np.max(price))

# Zameen.com price  - maths operations
print("Zameen.com Price square: " , np.square(price))
print("Zameen.com Price sqrt: " , np.sqrt(price))
print("Zameen.com Price pow: " , np.power(price,price))
print("Zameen.com Price abs: " , np.abs(price))



# Perform basic arithmetic operations
addition = long + lat
subtraction = long - lat
multiplication = long * lat
division = long / lat

print(" Zameen.com Long - lat - Addition:", addition)
print(" Zameen.com Long - lat - Subtraction:", subtraction)
print(" Zameen.com Long - lat - Multiplication:", multiplication)
print(" Zameen.com Long - lat - Division:", division)


#Trigonometric Functions

pricePie = (price/np.pi) +1
# Calculate sine, cosine, and tangent
sine_values = np.sin(pricePie)
cosine_values = np.cos(pricePie)
tangent_values = np.tan(pricePie)

print("Zameen.com Price - div - pie  - Sine values:", sine_values)
print("Zameen.com Price - div - pie Cosine values:", cosine_values)
print("Zameen.com Price - div - pie Tangent values:", tangent_values)

print("Zameen.com Price - div - pie  - Exponential values:", np.exp(pricePie))


# Calculate the natural logarithm and base-10 logarithm
log_array = np.log(pricePie)
log10_array = np.log10(pricePie)

print("Zameen.com Price - div - pie  - Natural logarithm values:", log_array)
print("Zameen.com Price - div - pie  = Base-10 logarithm values:", log10_array)

#Example: Hyperbolic Sine
# Calculate the hyperbolic sine of each element
sinh_values = np.sinh(pricePie)
print("Zameen.com Price - div - pie   - Hyperbolic Sine values:", sinh_values)


#Hyperbolic Cosine Using cosh() Function
# Calculate the hyperbolic cosine of each element
cosh_values = np.cosh(pricePie)
print("Zameen.com Price - div - pie   - Hyperbolic Cosine values:", cosh_values)

#Example: Hyperbolic Tangent
# Calculate the hyperbolic tangent of each element
tanh_values = np.tanh(pricePie)
print("Zameen.com Price - div - pie   -Hyperbolic Tangent values:", tanh_values)

#Example: Inverse Hyperbolic Sine

# Calculate the inverse hyperbolic sine of each element
asinh_values = np.arcsinh(pricePie)
print("Zameen.com Price - div - pie   -Inverse Hyperbolic Sine values:", asinh_values)

#Example: Inverse Hyperbolic Cosine
# Calculate the inverse hyperbolic cosine of each element
acosh_values = np.arccosh(pricePie)
print("Zameen.com Price - div - pie   -Inverse Hyperbolic Cosine values:", acosh_values)


#Zameen.com Long Plus Lat - 2 dimentional arrary
D2LongLat = np.array([long,
                  lat])

print ("Zameen.com Long Plus Lat - 2 dimentional arrary - " ,D2LongLat)

# check the dimension of array1
print("Zameen.com Long Plus Lat - 2 dimentional arrary - dimension" , D2LongLat.ndim) 
# Output: 2

# return total number of elements in array1
print("Zameen.com Long Plus Lat - 2 dimentional arrary - total number of elements" ,D2LongLat.size)
# Output: 6

# return a tuple that gives size of array in each dimension
print("Zameen.com Long Plus Lat - 2 dimentional arrary - gives size of array in each dimension" ,D2LongLat.shape)
# Output: (2,3)

# check the data type of array1
print("Zameen.com Long Plus Lat - 2 dimentional arrary - data type" ,D2LongLat.dtype) 
# Output: int64

# Splicing array
D2LongLatSlice=  D2LongLat[:1,:5]
print("Zameen.com Long Plus Lat - 2 dimentional arrary - Splicing array - D2LongLat[:1,:5] " , D2LongLatSlice)
D2LongLatSlice2=  D2LongLat[:1, 4:15:4]
print("Zameen.com Long Plus Lat - 2 dimentional arrary - Splicing array - D2LongLat[:1, 4:15:4] " , D2LongLatSlice2)



# Indexing array
D2LongLatSliceItemOnly=  D2LongLatSlice[0,1]
print("Zameen.com Long Plus Lat - 2 dimentional arrary - Index array - D2LongLatSlice[1,5] " , D2LongLatSliceItemOnly)
D2LongLatSlice2ItemOnly=  D2LongLatSlice2[0, 2]
print("Zameen.com Long Plus Lat - 2 dimentional arrary - index array - D2LongLatSlice2[0, 2] " , D2LongLatSlice2ItemOnly)


#You should use the builtin function nditer, if you don't need to have the indexes values.
for elem in np.nditer(D2LongLat):
    print(elem)

#EDIT: If you need indexes (as a tuple for 2D table), then:
for index, elem in np.ndenumerate(D2LongLat):
    print(index, elem)

"""# for loop
rows = np.shape(D2LongLat[0])[0]
cols = np.shape(D2LongLat[1])[0]
for i in range(0, (rows + 1)):
    for j in range(0, (cols + 1)):
        print (D2LongLat[i,j])
"""


# 2 x 149 ========>>>>> 1  x 298 - reshape
D2LongLat1TO298 = np.reshape(D2LongLat, (1, 298))
print("Zameen.com Long Plus Lat - 2 dimentional arrary - np.reshape(D2LongLat, (1, 298)) : " , D2LongLat1TO298)
print("Zameen.com Long Plus Lat - 2 dimentional arrary - np.reshape(D2LongLat, (1, 298)) : Size " , D2LongLat1TO298.size)
print("Zameen.com Long Plus Lat - 2 dimentional arrary - np.reshape(D2LongLat, (1, 298)) : ndim " , D2LongLat1TO298.ndim)
print("Zameen.com Long Plus Lat - 2 dimentional arrary - np.reshape(D2LongLat, (1, 298)) : shape " , D2LongLat1TO298.shape)
print("Zameen.com Long Plus Lat - 2 dimentional arrary - np.reshape(D2LongLat, (1, 298)) : ndim " , D2LongLat1TO298.ndim)




print()

