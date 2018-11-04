
PointsToEarn5DollarDiscount = 100
DiscountFor100Points = 5.0
TexasSalesTax = 0.0825

def doLEGOloyalty( anyExistingLoyaltyPoints, howMany, cost, answer ):
     if answer == "y":
          pointsUsed = anyExistingLoyaltyPoints // PointsToEarn5DollarDiscount * \
               PointsToEarn5DollarDiscount
          discount = anyExistingLoyaltyPoints // PointsToEarn5DollarDiscount * \
               DiscountFor100Points
     else:
          pointsUsed = 0
          discount = 0.0
     grossSaleBeforDiscout = cost * howMany
     grossSaleWoTax = grossSaleBeforDiscout - discount
     grossSale = grossSaleWoTax + (TexasSalesTax * grossSaleWoTax)
     loyaltyPoints = anyExistingLoyaltyPoints - pointsUsed + int( grossSaleWoTax )
     print( "You have ", loyaltyPoints, " loyalty points after sale.", sep="" )
     print( "Your sale amount is $", format( grossSale, ",.2f" ), ".", sep="" )
     print()
     return loyaltyPoints

def main():
     loyaltyPoints = 0
     quantityPurchased = int( input( "How many were puchased? " ) )
     while quantityPurchased > 0:
          salePrice = float( input( "How much is each set? " ) )
          response = input( "Do you want to use the points? (y=yes; n=no)" )
          response = response.lower()
          loyaltyPoints = doLEGOloyalty( loyaltyPoints, quantityPurchased, salePrice,
                                         response )
          quantityPurchased = int( input( "How many were puchased? " ) )

def test():
     loyaltyPoints = doLEGOloyalty( 0, 1, 100., "y" )     
     loyaltyPoints = doLEGOloyalty( loyaltyPoints, 1, 100., "N" )     
     loyaltyPoints = doLEGOloyalty( loyaltyPoints, 1, 100., "n" )
     loyaltyPoints = doLEGOloyalty( loyaltyPoints, 1, 100., "n" )
     loyaltyPoints = doLEGOloyalty( loyaltyPoints, 1, 100., "n" )
     loyaltyPoints = doLEGOloyalty( loyaltyPoints, 1, 100., "y" )

main()

# test()
