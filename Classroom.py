'''Price=float(input('Enter the Price:'))
discount=20
if Price > 130000:
    discount = 450
else:
    discount = 0
print('your Discount:',discount)


invitation=int(input('Enter youranswer:'))
card=1
if invitation > 1:
    card = 'Received'
else:
    card="not received"
print('Your card:', card)'''

earning=int(input('Enter your earning'))
work_experience= float (input('Enter your work experience'))

if earning>30000:
    if work_experience >=2:
        print('You are eligibe for loan')
    else:
        print('sorry your work experience is less than 2 years')
else:
    print('your earning is less than 30000')
