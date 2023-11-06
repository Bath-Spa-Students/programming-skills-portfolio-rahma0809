#store pets in list
Pets=[]
#storing in list
Pet={'animal':'kitten',
     'name':'Luna',
     'ownwe':'James',
     'colour':'orange',
     'species':'persian'}
Pets.append(Pet)

Pet={'animal':'dog',
     'name':'muffin',
     'ownwe':'Stena',
     'colour':'white and black',
     'species':'husky'}
Pets.append(Pet)

Pet={'animal':'fish',
     'name':'sun',
     'ownwe':'Aina',
     'colour':'yellow and silver',
     'species':'goldfish'}
Pets.append(Pet)
\
#Displaying the onformation about the pet 
for Pet in Pets:
    print('\nThings i know about the pet',Pet['animal'],':')
    




