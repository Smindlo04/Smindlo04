# Lethukuthula Sibiya (41566599)

#start
print("For the calculation of prime numbers;")
start = 1
end = int(input(" below a positive value: "))
print("\nPrime numbers between", start, "and", end, "are:")

#for loop
for number in range(start, end + 1):
 if number > 1:
   for i in range(2, number):

    if (number % i) == 0:

else:
      print(number, end=” “)
