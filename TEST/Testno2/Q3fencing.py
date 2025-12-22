import math


radius = 20      
rect_length = 50
rect_breadth = 40 
cost_per_meter = 35  

semi_circumference = math.pi * radius + 2 * radius


rect_perimeter = 2 * (rect_length + rect_breadth)


total_length = (semi_circumference + rect_perimeter) * 5


total_cost = total_length * cost_per_meter

print(f"Total cost of fencing the field = Rs {total_cost:.2f}")