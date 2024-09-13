nylon = int(input())
paint = int(input())
diluent = int(input())
hours = int(input())

nylon_cost = (nylon + 2) * 1.50
paint_cost = (paint * 1.10) * 14.50
diluent_cost = diluent * 5.00
bags_cost = 0.40
total_material_cost = nylon_cost + paint_cost + diluent_cost + bags_cost
labor_cost = total_material_cost * 0.30 * hours
total_cost = total_material_cost + labor_cost

print(f"{total_cost:.2f}")