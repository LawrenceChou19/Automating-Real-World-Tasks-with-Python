people = [
    {
        "name": "Sabrina Green",
        "username": "sgreen",
        "phone": "802-867-5309",
        "department": "IT Infrastructure",
        "role": "Systems Administrator"
    },
    {
        "name": "Eli Jones",
        "username": "ejones",
        "phone": "684-348-1127",
        "department": "IT Infrastructure",
        "role": "IT Specialist"
    },
]

import json

with open('people.json', 'w') as people_json:
    json.dump(people, people_json, indent=2)

import yaml

with open('people.yaml', 'w') as people_yaml:
    yaml.safe_dump(people, people_yaml)