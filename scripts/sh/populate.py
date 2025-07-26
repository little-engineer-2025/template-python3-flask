#!/usr/bin/env python3

import random
import requests

first_names = ["John", "Jane", "Michael", "Emily", "Chris", "Katie", "David", "Sarah", "James", "Laura"]
last_names = ["Doe", "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez"]

# Generate a list of random names
data = [f"{random.choice(first_names)} {random.choice(last_names)}" for _ in range(5)]

for item in data:
    try:
        response = requests.post(
            'http://localhost:5000/api/service/v1/hellos',
            json={
                "name": item,
            }
        )
        print(response)
    except Exception as e:
        print(e)
