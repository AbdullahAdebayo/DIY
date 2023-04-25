# age = 3*3
# print(age)
# print(0x123)
# print(0o326)
# print(6.5e3)
# print('i like "you"')
# print("Obi is 'boy'")
# print("I'm a boy")
# print('I\'m a girl.')
# print(True > False)

# print("I'm"
# "learning"
# """Python""")

# print(print((5 * ((25 % 13) + 100) / (2 * 13)) // 2))
# a = 3.0
# b = 4.0
# c = (a ** 2 + b ** 2) ** 0.5 
# print("c =", c)

# var = 2
# print(var)

# var = 3
# print(var)

# var += 1
# print(var)

# a = '1'
# b = "1"
# print(a + b)

# x = int(input("Enter an integer: "))
# ans = 0
# while ans**3 < abs(x):
#     ans = ans + 1
#     if ans**3 != abs(x) :
#         print(x, "is not a perfect cube")
#     else:
#         if x < 0:
#             ans = -ans
#             print("Cube root of" , x, "is" , ans)

# import time

# start_time = time.time()

# max_val = int(input("Enter an integer :"))
# i = 0
# while i < max_val:
#     i += 1
#     print(i)
# end_time = time.time()

# print("Time taken:" , end_time - start_time, "seconds")

#x = int(input("Enter an integer greater than 2: "))
#largest_divisor = None
#for guess in range(2,x):
    #if x%guess == 0:
        #largest_divisor = guess
       # break
#if largest_divisor != None:
    #print("Largest divisor of" , x , "is" , largest_divisor)
#else:
    #print(x, "is a prime number")

# def is_prime(n):
#     if n<2:
#         return False
#     for i in range (2, int(n**0.5)+1):
#         if n% i == 0:
#             return False
#         return True
    
# sum = 0
# for i in range (3,1000):
#     if is_prime(i):
#         sum += i

# print (sum)
 
# x = 25

# epsilon = 0.01
# step = epsilon**2
# num_guesses = 0
# ans = 0.0
# while abs(ans**2 - x) >= epsilon and ans <= x:
#     ans += step
#     num_guesses += 1
#     print("number of guesses =" , num_guesses)
#     if abs(ans**2 - x) >= epsilon:
#         print("Failed on square root of" ,x)
# else: 
#     print(ans, "is close to square root of" ,x)
