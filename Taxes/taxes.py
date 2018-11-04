Y = "Y"
N = "N"
def main():

    employees = "Y"
    while employees == "Y":
        name = input("Give the name of the employee: ")
        rate = int(input("Give the hourly pay rate: " ))
        hours = int(input("Give the number of hours worked: " ))
        married = input("Is the employee married?(respond Y/N) ")
        married = married.upper()
        if hours <= 40:
            grossPay = hours * rate
        elif hours > 40 and hours <=  50:
            
            grossPay = int((hours * rate) + (.5 * (hours - 40) * rate))
        else:
            grossPay = int((hours * rate) + (.5 * 10 * rate)+ (hours - 50)*rate)
        if grossPay <= 2000:
            socialTax = int(grossPay * .062)
        elif grossPay > 2000:
            socialTax = 124
        if married == "N":
            if grossPay <= 500:
                federalTax = int(grossPay * .15)
            elif grossPay >= 500 and grossPay <= 1000:
                federalTax = int((grossPay-500) * .2 + 75)
            elif grossPay >= 1000:
                federalTax = int((grossPay-1000) * .25 + 175)
            netPay = int(grossPay - federalTax - socialTax)
        elif married == "Y":
            if grossPay <= 800:
                federalTax = int(grossPay * .13)
            elif grossPay >= 800 and grossPay <= 1900:
                federalTax = int((grossPay-800) * .18 + 104)
            elif grossPay >= 1900:
                federalTax = int((grossPay-1900) * .22 + 302)
            netPay = int(grossPay - federalTax - socialTax)
        print(name," had a gross pay of $", grossPay,'.', sep="" )
        print("Are they married?", married, ".", sep="" )
        print('Social security tax deduction is $',socialTax,'.', sep="")
        print('Federal tax deduction is $',federalTax,'.', sep="")
        print('Net pay is $',netPay,'.', sep="")
        employees = input("Another employee? Y/N")
        print()
        employees = employees.upper()

        
main()
"""
Give the name of the employee: Fred Flintstone
Give the hourly pay rate: 50
Give the number of hours worked: 60
Is the employee married?(respond Y/N) n
Fred Flintstone had a gross pay of $3750.
Are they married?N.
Social security tax deduction is $124.
Federal tax deduction is $862.
Net pay is $2764.
Another employee? Y/Ny

Give the name of the employee: Barney Rubble
Give the hourly pay rate: 50
Give the number of hours worked: 60
Is the employee married?(respond Y/N) n
Barney Rubble had a gross pay of $3750.
Are they married?N.
Social security tax deduction is $124.
Federal tax deduction is $862.
Net pay is $2764.
Another employee? Y/Nn
"""
