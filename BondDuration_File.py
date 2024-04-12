def getBondDuration(y, face, couponRate, m, ppy=1):
    # Calculate the coupon payment
    couponPayment = face * couponRate / ppy
    
    bondDuration = 0
    
    # Calculate the present value of each coupon payment and its time-weighted value
    for t in range(1, m * ppy + 1):
        pv_coupon = couponPayment / ((1 + y / ppy) ** t)
        bondDuration += pv_coupon * t
    
    # Calculate the present value of the face value and its time-weighted value
    pv_face = face / ((1 + y / ppy) ** (m * ppy))
    bondDuration += pv_face * m * ppy
    
    # Calculate the price of the bond
    bondPrice = pv_face
    for t in range(1, m * ppy + 1):
        bondPrice += couponPayment / ((1 + y / ppy) ** t)
    
    # Divide by the bond price and adjust for payment periods per year
    bondDuration /= bondPrice
    bondDuration /= ppy
    
    return bondDuration
