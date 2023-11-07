sandwich_orders = ['vegetable', 'cheese', 'chicken', 'egg']
finished_sandwiches = []
while sandwich_orders:
    now_preparing = sandwich_orders.pop(0)
    print(f"I am making your {now_preparing} sandwich.")
    finished_sandwiches.append(now_preparing)

print('\n')
for sandwich in finished_sandwiches:
    print("I made your "+ sandwich, "sandwich")

