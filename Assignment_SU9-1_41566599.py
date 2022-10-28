# Lethukuthula Sibiya (41566599)

# Obtain variables from user
var_1=int(input("Please provide the first variable: "))
var_2=int(input("Please provide the second variable: "))

# product of the two variables
multiplication=var_1*var_2


if var_1<0 or var_2<0 :
    print("Error, the input should be greater then 0")
else :
    print("The numbers from 0 to the product of the two variables are: ")

# for loop
for count in range(0,multiplication+1,1) :
    print(count,end=" ")
