

# #  calculate the electricity bill

# a = int(input("Enter units: "))
# def calculate_bill(units):
#     fixed_charge = 50
#     bill = 0
    
#     if units <= 100:
#         bill = units * 5
#     elif units <= 300:
#         bill = (100 * 5) 
#     else:
#         bill = (100 * 5) + (200 * 7) + ((units - 300) * 10)
#     bill += fixed_charge
#     return bill
# total_bill = calculate_bill(a)
# print(f" electricity bill  {a} units is ₹{total_bill}")



 

## 3. FizzBuzz 
# def fizz_buzz(n):
#     for i in range(1, n+1):
#         if i % 3 == 0 and i % 5 == 0:
#             print("Fizz")
#         elif i % 3 == 0:
#             print("Buzz")
#         elif i % 5 == 0:
#             print("Fizz Buzz")
#         else:
#             print(i)
# fizz_buzz(20)





## 6. factorial of a number

def factorial(s):
    result = 1
    for i in range(1, s + 1):
        result *= i
    return result
print(factorial(7))
