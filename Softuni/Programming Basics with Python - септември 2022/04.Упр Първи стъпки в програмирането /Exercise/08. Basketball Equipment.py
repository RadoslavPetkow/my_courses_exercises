annual_fee = float(input())

sneakers = annual_fee - (annual_fee * 0.40)
outfit = sneakers - (sneakers * 0.20)
ball = outfit / 4
accessories = ball / 5
final_price = annual_fee + sneakers + outfit + ball + accessories

print(final_price)