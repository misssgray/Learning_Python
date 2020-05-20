#Learning how to cast Python data types

#STRING TO INT
age = "30"
print(type(age))
age_cast = int(age)
print(type(age_cast))

#STRING TO FLOAT
age_float = "30"
print(type(age_float))
age_cast_float = float(age_float)
print(type(age_cast_float))
print(age_float)

#STRING TO BOOL
age_bool = "30"
print(type(age_bool))
age_cast_bool = bool(age_bool)
print(type(age_cast_bool))
print(age_cast_bool)

#INT TO STRING
age = 26
print(str(age))
print("My age is " + str(age))

#INT TO FLOAT
age = 26
print(float(age))

#INTO TO BOOL
age = 26
print(bool(age))

#FLOAT TO INT
price = 4.99
print(int(price))

#FLOAT TO STRING
price = 4.99
print(str(price))

#FLOAT TO BOOL
price = 0
print(bool(price))

#BOOL TO STRING
broke = True
print(str(broke))

#BOOL TO INT
broke = True
print(int(broke))

#BOOL TO FLOAT
broke = True
print(float(broke))