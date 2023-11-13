'''Write a Python program that uses the elif statement to determine the season based on the
month provided as input.'''

# Get the month as input from the user
month = input("Enter the month (e.g., January, February, etc.): ")
month = (month)

if month in ['december', 'january', 'february']:
    season = 'Winter'
elif month in ['march', 'april', 'may']:
    season = 'Spring'
elif month in ['june', 'july', 'august']:
    season = 'Summer'
elif month in ['september', 'october', 'november']:
    season = 'Fall'
else:
    season = 'Invalid Month'

print(f"The season for {month} is {season}.")
