# Multiplication function
def cookingTime(x, y):
    return x * y

# Init variables
Viande = ''
Poids = ''
Cuisson = ''




# Get input from user
Viande = input('Je cherche la cuisson parfaite pour ')
viande_uppercase = Viande.capitalize()

print('Veuillez me renseigner le poids de la viande en KG: ')

Poids = float(input(''))

print(f'Merci, donc nous avons la viande:\n {viande_uppercase}')

#print(f'Pour une cuisson {Cuisson}')

print(f'Pour un poids de:\n{Poids}kg')

print('Je vous calcule le temps pour une cuisson parfaite.')



#while True:

# Calculate based on user input
if Viande in ('Boeuf', 'boeuf'):
    tempsParKilo = 0.617
    print('Le temps de cuisson pour le roti de boeuf est de: ')

elif Viande in {'Poulet', 'poulet'}:
    tempsParKilo = 1
    print('Le temps de cuisson pour le poulet est de: ')

elif Viande in {'Porc' , 'porc'}:
    tempsParKilo = 1
    print('Le temps de cuisson pour le roti de porc est de: ')

elif Viande in {'Agneau' , 'agneau'}:
    tempsParKilo = 0.4
    print('Le temps de cuisson pour le roti d\'agneau est de: ')


tempsDeCuisson = tempsParKilo

        #break


# Convert float result to Time Format
minutes = cookingTime(Poids, tempsDeCuisson)*60
timeFormatted = divmod(minutes, 60)
print("%02d:%02d"%(timeFormatted))




