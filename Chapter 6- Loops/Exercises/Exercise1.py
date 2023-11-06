while True:
    toppings=input('Enter the topping of your choice:(or type quit to finish:)' )
    if toppings=='quit':
        print('You have customized your pizza toppings')
        break
    else:
        print(f'we will add',(toppings),'to your pizza')
