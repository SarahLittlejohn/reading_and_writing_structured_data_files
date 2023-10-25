import json

# Sample solution
group = {
    "Jill": {
        "age": 26,
        "job": "biologist",
        "relations": {
            "Zalika": "friend",
            "John": "partner"
        }
    },
    "Zalika": {
        "age": 28,
        "job": "artist",
        "relations": {
            "Jill": "friend"
        }
    },
    "John": {
        "age": 27,
        "job": "writer",
        "relations": {
            "Jill": "partner"
        }
    },
    "Nash": {
        "age": 34,
        "job": "chef",
        "relations": {
            "John": "cousin",
            "Zalika": "landlord"
        }
    }
}

# Save the dictionary to a JSON file
with open("group.json", "w") as file:
    json.dump(group, file, indent=4)

# Load the dictionary from the JSON file
with open("group.json", "r") as file:
    loaded_group = json.load(file)

# Print the loaded dictionary to verify
print(loaded_group)
