def getBondPrice(y, face, couponRate, m, ppy=1):
    # Calculate the coupon payment
    couponPayment = face * couponRate / ppy
    
    bondPrice = 0
    
    # Calculate the present value of the coupon payments
    for i in range(1, m * ppy + 1):
        bondPrice += couponPayment / ((1 + y / ppy) ** i)
    
    # Calculate the present value of the face value
    bondPrice += face / ((1 + y / ppy) ** (m * ppy))
    
    return bondPrice
