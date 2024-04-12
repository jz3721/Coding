def getBondPrice_E(face, couponRate, m, yc):
    # Calculate the coupon payment
    couponPayment = face * couponRate

    bondPrice = 0
    
    # Calculate the present value of the coupon payments and the face value
    for year, y in enumerate(yc, start=1):
        # Discount the coupon payment for the current year
        bondPrice += couponPayment / ((1 + y) ** year)
        
        # If it's the last year, also discount the face value
        if year == m:
            bondPrice += face / ((1 + y) ** year)
    
    return bondPrice
