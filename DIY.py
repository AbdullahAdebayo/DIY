#!/usr/bin/env python
# coding: utf-8

# # # EEE 254 ASSIGNMENT
# ## NAME : Olaitan Abdullahi Adebayo
# ## MATRIC NO : EEG/2021/116

# # DIY 1

# In[1]:


import time

start_time = time.time()

max_val = int(input("Enter an integer :"))
i = 0
while i < max_val:
    i += 1
    print(i)
end_time = time.time()

print("Time taken:" , end_time - start_time, "seconds")


# # DIY 2

# In[2]:


x = int(input("Enter an integer greater than 2: "))
smallest_divisor = None
for guess in range(2,x):
    if x%guess == 0:
        smallest_divisor = guess
        largest_divisor = x/smallest_divisor
        break
if smallest_divisor != None:
    print("Largest divisor of" , x , "is" , largest_divisor)
else:
    print(x, "is a prime number")


# # DIY 3

# In[3]:


def is_prime(n):
    if n<2:
        return False
    for i in range (2, int(n**0.5)+1):
        if n% i == 0:
            return False
        return True
    
sum = 0
for i in range (3,1000):
    if is_prime(i):
        sum += i

print (sum)


# # DIY 5

# In[4]:


import math
def log_product(num1, num2):
    """ num1:first number, num2: second number"""
    log_sum = math.log10(num1) + math.log10(num2)
    result = round(math.pow(10, log_sum), 2)
    return result
#Example usage
print(log_product(4,9))
print(log_product(10,30))


# # DIY 6

# In[ ]:import math

epsilon = 0.01
gain = float(input("Enter the value of gain: "))
x = 2 ** gain

# Find lower bound on ans
lower_bound = 0
while 2 ** lower_bound < x:
    lower_bound += 1
low = lower_bound - 1
high = lower_bound + 1

# Perform bisection research
ans = (high + low) / 2
while abs(2 ** ans - x) >= epsilon:
    if 2 ** ans < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2

# Convert ans to dB
dB = 10 * math.log10(x)

print(f"The gain is {gain}, which is equivalent to {dB:.2f} dB.")





