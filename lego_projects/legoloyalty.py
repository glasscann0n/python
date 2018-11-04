PointsToEarn5DollarDiscount = 100
DiscountFor100Points = 5.0



def legoloyalty(anyExistingLoyaltyPoints, doublePoint, cost,  response ):
    if response == "y":
        pointsUsed = anyExistingLoyaltyPoints // PointsToEarn5DollarDiscount * \
                     PointsToEarn5DollarDiscount
        discount = anyExistingLoyaltyPoints // PointsToEarn5DollarDiscount * \
                   DiscountFor100Points
    else:
        pointsUsed = 0
        discount = 0.0
    if doublePoint == "y":
        points = int(cost) * 2 - discount
    else:
        points = int(cost) - discount

    loyaltyPoints = anyExistingLoyaltyPoints - pointsUsed + points
    credit = loyaltyPoints// PointsToEarn5DollarDiscount * DiscountFor100Points
    print('after spending $', format( cost, ",.2f" ),', you have earned a total of ', int(points),' VIP points.',sep="" )

    print ( "You have ", int(loyaltyPoints), " points and a credit of $", credit ,'.', sep="" )
    return loyaltyPoints



def main():
    loyaltyPoints = 0
    anotherPurchase = 'y'
    response = 'n'
    while anotherPurchase == 'y':
        cost = float(input("What was the total spent at LEGO?"))
        doublePoint = str(input("Was this a double point purchase (Y/N)?"))
        doublePoint = doublePoint.lower()
        credit = loyaltyPoints // PointsToEarn5DollarDiscount * DiscountFor100Points
        if loyaltyPoints == 0:
            pass
        else:
            response = input("Do you want to use your VIP credit of $"+str(credit)+"(Y/N)?")
            response = response.lower()
        loyaltyPoints = legoloyalty(loyaltyPoints, doublePoint, cost,  response )
        anotherPurchase = input("Another purchase (Y/N)?")
main()

'''
What was the total spent at LEGO?100
Was this a double point purchase (Y/N)?n
after spending $100.00, you have earned a total of 100 VIP points.
You have 100 points and a credit of $5.0.
Another purchase (Y/N)?y
What was the total spent at LEGO?199.99
Was this a double point purchase (Y/N)?n
Do you want to use your VIP credit of $5.0(Y/N)?n
after spending $199.99, you have earned a total of 199 VIP points.
You have 299 points and a credit of $10.0.
Another purchase (Y/N)?y
What was the total spent at LEGO?199.99
Was this a double point purchase (Y/N)?y
Do you want to use your VIP credit of $10.0(Y/N)?n
after spending $199.99, you have earned a total of 398 VIP points.
You have 697 points and a credit of $30.0.
Another purchase (Y/N)?y
What was the total spent at LEGO?199.99
Was this a double point purchase (Y/N)?n
Do you want to use your VIP credit of $30.0(Y/N)?y
after spending $199.99, you have earned a total of 169 VIP points.
You have 266 points and a credit of $10.0.
Another purchase (Y/N)?n
'''