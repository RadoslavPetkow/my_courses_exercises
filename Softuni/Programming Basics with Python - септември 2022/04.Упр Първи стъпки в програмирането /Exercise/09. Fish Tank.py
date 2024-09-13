length = int(input())
width = int(input())
height = int(input())
percentage = float(input())

volume = length * width * height
liters = volume / 1000
final_percentage = percentage / 100
usable_liters = liters * (1 - final_percentage)

print(usable_liters)