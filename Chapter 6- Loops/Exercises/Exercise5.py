sandwich_orders = ['vegetable','pastrami', 'cheese','pastrami' 'chicken', 'egg','pastrami']
finished_sandwiches = []

print("Deli has ran out of pastrami")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print("\n")
while sandwich_orders:
    preparing_sandwich = sandwich_orders.pop()
    print("I am making your " + preparing_sandwich + " sandwich.")
    finished_sandwiches.append(preparing_sandwich)

print('\n')
for sandwich in finished_sandwiches:
    print("I made your "+ sandwich, "sandwich") 
