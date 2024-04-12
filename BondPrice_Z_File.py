def getBondPrice_Z(face, couponRate, times, yc): 
    # Calculate the coupon payment
    couponPayment = face * couponRate
    
    bondPrice = 0
    
    # Calculate the present value of the coupon payments and the face value
    for time, y in zip(times, yc):
        # Discount the coupon payment for the current time period
        bondPrice += couponPayment / ((1 + y) ** time)
        
        # If it's the last time period, also discount the face value
        if time == times[-1]:
            bondPrice += face / ((1 + y) ** time)
    
    return bondPrice
