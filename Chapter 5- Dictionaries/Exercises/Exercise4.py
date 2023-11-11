rivers = {'Nile': 'Egypt', 'Amazon': 'Brazil', 'Lena': 'Russia'}

# Loop to print a sentence 
for river, country in rivers.items():
    print(f"The {river} runs through {country}.")

print("\nRivers:")
for river in rivers.keys():
    print(river)

# Loop to print the name of each country
print("\nCountries:")
for country in rivers.values():
    print(country)
