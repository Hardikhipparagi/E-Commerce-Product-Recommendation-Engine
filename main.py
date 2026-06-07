import heapq
import pandas as pd

# ==========================
# PRODUCT CLASS
# ==========================

class Product:

    def __init__(self, id, title, category, brand, price):
        self.id = id
        self.title = title
        self.category = category
        self.brand = brand
        self.price = price


# ==========================
# USER CLASS
# ==========================

class User:

    def __init__(self, user_id):
        self.user_id = user_id
        self.views = []
        self.cart = []
        self.purchases = []
        self.searches = []
        
        


# ==========================
# LOAD DATASETS
# ==========================

items = pd.read_csv("data/items.csv")
events = pd.read_csv("data/events.csv")


# ==========================
# PRODUCT HASHMAP
# ==========================

product_map = {}

for _, row in items.iterrows():

    product_map[row["item_id"]] = {
        "title": row["title"],
        "category": row["category"],
        "brand": row["brand"],
        "price": row["price"]
    }


# ==========================
# USER HASHMAP
# ==========================

users = {}

for _, row in events.iterrows():

    user_id = row["user_id"]

    if user_id not in users:
        users[user_id] = User(user_id)

    if row["event"] == "view":
        users[user_id].views.append(row["item_id"])

    elif row["event"] == "cart":
        users[user_id].cart.append(row["item_id"])

    elif row["event"] == "purchase":
        users[user_id].purchases.append(row["item_id"])
        
# ==========================
# SEARCH HISTORY
# ==========================

users["U001"].searches.extend([
    "Mobile",
    "Smartphone"
])

users["U002"].searches.extend([
    "Fashion",
    "Shoes"
])        


# ==========================
# DISPLAY USERS
# ==========================

print("\n===== USER PROFILES =====\n")

for user_id, user in users.items():

    print("User:", user_id)
    print("Views:", user.views)
    print("Cart:", user.cart)
    print("Purchases:", user.purchases)
    print("-" * 40)


# ==========================
# SCORING FUNCTION
# ==========================

def calculate_score(user, product_id):

    score = 0

    category = product_map[product_id]["category"]

    # Purchase Weight = 5
    for item in user.purchases:

        if product_map[item]["category"] == category:
            score += 5

    # Cart Weight = 3
    for item in user.cart:

        if product_map[item]["category"] == category:
            score += 3

    # View Weight = 1
    for item in user.views:

        if product_map[item]["category"] == category:
            score += 1

    return score


# ==========================
# CATEGORY RECOMMENDATION
# ==========================

def recommend_by_category(user_id):

    user = users[user_id]

    categories = []

    for item in user.purchases:
        categories.append(
            product_map[item]["category"]
        )

    recommendations = []

    for product_id, data in product_map.items():

        if data["category"] in categories:

            if product_id not in user.purchases:
                recommendations.append(product_id)

    return recommendations


# ==========================
# PRODUCT RANKING
# ==========================

def rank_products(user_id):
    
    

    user = users[user_id]

    rankings = []

    for product_id in product_map:

        if product_id in user.purchases:
            continue

        score = calculate_score(user, product_id)

        rankings.append(
            (product_id, score)
        )

    rankings.sort(
        key=lambda x: x[1],
        reverse=True
    )

    return rankings

def top_n_recommendations(user_id, n=3):

    rankings = rank_products(user_id)

    top_products = heapq.nlargest(
        n,
        rankings,
        key=lambda x: x[1]
    )

    return top_products

def similar_products(product_id):

    target = product_map[product_id]

    target_category = target["category"]

    recommendations = []

    for pid, pdata in product_map.items():

        if pid == product_id:
            continue

        score = 0

        # Same category
        if pdata["category"] == target_category:
            score += 10

        # Similar price range
        if abs(pdata["price"] - target["price"]) <= 20000:
            score += 5

        recommendations.append(
            (pid, score)
        )

    recommendations.sort(
        key=lambda x: x[1],
        reverse=True
    )

    return recommendations[:5]

# ==========================
# TEST USER
# ==========================

test_user = "U001"

print("\n===== CATEGORY RECOMMENDATIONS =====\n")

print(
    recommend_by_category(test_user)
)

print("\n===== RANKED PRODUCTS =====\n")

rankings = rank_products(test_user)

for product_id, score in rankings:

    print(
        product_id,
        "|",
        product_map[product_id]["title"],
        "| Score:",
        score
    )
    
print("\n===== TOP 3 RECOMMENDATIONS =====\n")

top_recs = top_n_recommendations("U001", 3)

for product_id, score in top_recs:

    print(
        product_id,
        "|",
        product_map[product_id]["title"],
        "| Score:",
        score
    )    
    
print("\n===== SIMILAR PRODUCTS =====\n")

similar = similar_products("P001")

for pid, score in similar:

    print(
        pid,
        "|",
        product_map[pid]["title"],
        "| Score:",
        score
    )    
def personalized_recommendations(user_id):

    user = users[user_id]

    rankings = []

    for pid, pdata in product_map.items():

        if pid in user.purchases:
            continue

        score = calculate_score(user, pid)

        rankings.append((pid, score))

    rankings.sort(
        key=lambda x: x[1],
        reverse=True
    )

    return rankings[:5]    
def generate_report(user_id):

    recommendations = personalized_recommendations(user_id)

    filename = f"outputs/report_{user_id}.txt"

    with open(filename, "w") as file:

        file.write("E-Commerce Recommendation Report\n")
        file.write("=" * 40 + "\n\n")

        file.write(f"User ID: {user_id}\n\n")

        file.write("Recommended Products:\n")

        for pid, score in recommendations:

            file.write(
                f"{pid} | "
                f"{product_map[pid]['title']} | "
                f"Score: {score}\n"
            )

    print(f"\nReport saved to: {filename}")  
print("\n===== REPORT GENERATION =====\n")

generate_report("U001") 