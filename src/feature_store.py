import pandas as pd

# Load events dataset
events = pd.read_csv("data/events.csv")

# Event weights
weights = {
    "view": 1,
    "cart": 3,
    "purchase": 5
}

# Convert events into scores
events["score"] = events["event"].map(weights)

print(events)