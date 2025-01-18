# Sample dictionary with gender and age
dict = [
    { "gender": "female", "age": 20},
    { "gender": "male", "age": 17},
    {"gender": "female", "age": 25},
    { "gender": "male", "age": 22},
    { "gender": "female", "age": 16},
    { "gender": "male", "age": 19},
    { "gender": "male", "age": 25},
    { "gender": "male", "age": 15},
    {"gender": "female", "age": 24},
    { "gender": "male", "age": 22},
]

# Initializing counters
total_girls = 0
total_boys = 0
girls_above_18 = 0
boys_above_18 = 0

# Iterating through the list of people
for person in dict:
    if person["gender"] == "female":
        total_girls += 1
        if person["age"] > 18:
            girls_above_18 += 1
    elif person["gender"] == "male":
        total_boys += 1
        if person["age"] > 18:
            boys_above_18 += 1

print("Total number of girls:", total_girls)
print("Total number of boys:", total_boys)
print("Number of girls above the age of 18:", girls_above_18)
print("Number of boys above the age of 18:", boys_above_18)
