# Variables

## Simple Variables

### Integers

i = 1
n = 5

m = i + n

### Strings

greeting = "Hello, world!"

first_word = "Hello, "
second_word = "world!"

full_greeting = first_word + second_word


### Boolean

World_is_flat = True


### Conditionals

# if World_is_flat == False:
#     print("NASA was right!")
# if World_is_flat == True:
#     print("I fell off the edge")

### Complex Variables (lists, dictionaries)

# planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
# i = 1
# for item in planets:
#     print("The", i, "planet from the sun is:", item)
#     i = i + 1 

### Dictionary (key/value pairs)

startrek = { "Enterprise": { "Captain": "Kirk", "FO": "Spock" },
        "Voyager": { "Captain": "Janeway", "FO": "Chakotay" },
        "Reliant": { "Captain": "Khan", "FO": "Woyon" }, 
        "Enterprises": ['1701', '1701-A', '1701-B', '1701-C', '1701-D', '1701-E', '1701-F', '1701-J'] }

for ship in startrek['Enterprises']:
    print(ship)