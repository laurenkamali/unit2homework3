'''
Name: Lauren Kamali
Date: 10/07/24
Description: if-elif layouts comparison 
'''

'''
Age     |   Category    |   Price
0-6         KITTEN          250
7-11        TEENAGER        225
12-95       ADULT           150
>96         SENIOR          85 
'''

cat_age = int(input("Enter the age of Cat in months:"))

#approach 1

if cat_age <= 6:
    print(f"The price of the kitten is $250")
elif cat_age <= 11:
    print(f"The price of the teenager cat is $225")
elif cat_age <= 95:
    print(f"The price of the adult cat is $150")
elif cat_age >= 96:
    print(f"The price of the senior cat is $85")

#approach 2

cat_age = int(input("Enter the age of Cat in months:"))


if cat_age >= 96:
    print(f"The price of the senior cat is $85")
elif cat_age <= 95:
    print(f"The price of the adult cat is $150")
elif cat_age <= 11:
    print(f"The price of the teenager cat is $225")
elif cat_age <= 6:
    print(f"The price of the kitten is $250")

#approach 3

cat_age = int(input("Enter the age of Cat in months:"))

if cat_age <= 6:
    print(f"The price of the kitten is $250")
if cat_age <= 11:
    print(f"The price of the teenager cat is $225")
if cat_age <= 95:
    print(f"The price of an adult cat is $150")
if cat_age >= 96:
    print(f"The price of a senior cat is $85")

#approach 4 

cat_age = int(input("Enter the age of Cat in months:"))

if cat_age >= 96:
    print(f"The price of a senior cat is $85")
if cat_age <= 95:
    print(f"The price of an adult cat is $150")
if cat_age <= 11:
    print(f"The price of the teenager cat is $225")
if cat_age <= 6:
    print(f"The price of the kitten is $250")