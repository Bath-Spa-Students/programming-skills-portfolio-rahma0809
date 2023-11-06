invitation=['Ms.Sadaf','Ms.Steena','Taniya']
print(f'Greetings!,',invitation[0],'You are invited for a dinner party at the Benz hotel on Oct 29 at 8:30 pm.'
       'Looking forward to meet you')
print(f'Good Morning!,',invitation[1],'Why dont we get together at the Benz hotel on Oct 29 at 8:30 pm? We all will have lots of fun')
print(f'Heyy!,',invitation[2],'Let us meet for a dinner party at the Benz hotel on Oct 29 at 8:30 pm.'
       'It was long week let us take some break and enjoy our day')
print(invitation[2],'can not come for the dinner party')
invitation[2]='Ammara'
print(invitation)
print(f'Greetings!,',invitation[0],'You are invited for a dinner party at the Benz hotel on Oct 29 at 8:30 pm.'
       'Looking forward to meet you')
print(f'Good Morning!,',invitation[1],'Why dont we get together at the Benz hotel on Oct 29 at 8:30 pm? We all will have lots of fun')
print(f'Heyy!,',invitation[2],'Let us meet for a dinner party at the Benz hotel on Oct 29 at 8:30 pm.'
       'It was long week let us take some break and enjoy our day')
print('My dinner table won’t arrive in time for the dinner, so because of that we have space only for two people')
name= invitation.pop(2)
print((name),'Sincere apologies but I can invite only two people for the dinner party.Let us meet next time')
print(f'Hey!',invitation[0],'You are still invited for the dinner party')
print(f'Hii!',invitation[1],'You are still invited for the dinner party')
del invitation[0]
del invitation[0]
print(invitation)