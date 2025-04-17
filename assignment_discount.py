def  calculate_discount(price, discount_percent):
    discountPrice = price * (discount_percent/100)
    
    totalPrice = price + discountPrice
    
    if discount_percent < 20:
        return price
    
    return totalPrice

if __name__ == "__main__":
    price = int(input('please enter the price of prodouct: '))
    discount_percent = int(input('please enter the discount you need: '))
    
    print(calculate_discount(price, discount_percent))
# end main