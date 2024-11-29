import pandas as pd
import random
from datetime import datetime, timedelta

# Define households and appliances
households = {
    "Household 1": {"lifestyle": "Eco-Friendly", "base_load": 100},
    "Household 2": {"lifestyle": "Working Professionals", "base_load": 200},
    "Household 3": {"lifestyle": "Family with Kids", "base_load": 300},
    "Household 4": {"lifestyle": "Tech Enthusiasts", "base_load": 400},
}

appliances = {
    "LED Light": (10, 15),
    "Ceiling Fan": (50, 75),
    "Air Conditioner": (1500, 2500),
    "Refrigerator": (150, 250),
    "Microwave Oven": (800, 1200),
    "Washing Machine": (500, 1500),
    "Television": (50, 150),
    "Desktop Computer": (100, 250),
    "Laptop": (50, 100),
    "Electric Kettle": (1000, 1500),
    "Smart Home Devices": (10, 30),
    "Electric Vehicle Charger": (3000, 7000),
}

# Generate random usage data
def generate_usage(base_load, hours):
    data = []
    for hour in range(hours):
        fluctuation = random.uniform(-50, 50)
        load = base_load + fluctuation
        data.append(max(load, 0))  # Prevent negative values
    return data

# Create the dataset
start_date = datetime.now() - timedelta(days=100)
data = []

for day in range(100):
    current_date = start_date + timedelta(days=day)
    for household, details in households.items():
        usage = generate_usage(details["base_load"], 24)
        for hour, load in enumerate(usage):
            timestamp = current_date + timedelta(hours=hour)
            data.append({
                "Household": household,
                "Timestamp": timestamp,
                "Power Usage (kW)": round(load, 2)
            })

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("household_power_usage.csv", index=False)

print("Dataset generated and saved as 'household_power_usage.csv'.")
