chicken = int(input())
fish = int(input())
vegetarian = int(input())
delivery_cost = 2.50

chicken_price = chicken * 10.35
fish_price = fish * 12.40
vegetarian_price = vegetarian * 8.15
total_price = chicken_price + fish_price + vegetarian_price
dessert = total_price * 0.20
final_price = total_price + dessert + delivery_cost

print(final_price)