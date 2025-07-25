## MONTHLY RENT CALCULATOR

'''INPUT:

1. No. of people living in flat/room.

2. Monthly Electricity bill.

3. Monthly rent.

4. Total food ordered.

'''

try:
    n = int(input("Enter no. of people living in flat/room :    "))
    print('\n')
    r = float(input("Enter Monthly Rent :   Rs"))
    print('\n')
    e = float(input("Enter Monthly Electricity bill :     Rs"))
    print('\n')
    f = int(input("Enter no. of food ordered :      "))
    print('\n')

    Total = r + e + f

    individual = Total // n

    print(f'''
Total bill : Rs{Total}

Each individual will pay Rs{individual}
''')


except:
    print("Invalid input. Try again.\n")
