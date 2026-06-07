# E-Commerce Product Recommendation Engine

## Project Overview

This project is a DSA-based E-Commerce Product Recommendation Engine developed using Python. It simulates how modern e-commerce platforms recommend products to users based on their browsing history, cart activity, purchases, and product similarity.

The project demonstrates the use of core Data Structures and Algorithms concepts such as HashMaps, Lists, Sorting, Priority Queues (Heap), and Recommendation Scoring.

---

## Features

* Product Management
* User Activity Tracking
* Category-Based Recommendations
* Personalized Recommendations
* Similar Product Suggestions
* Product Ranking System
* Top-N Recommendations using Heap
* Recommendation Report Generation
* HashMap-Based Data Storage

---

## Technologies Used

* Python
* Pandas
* Heapq
* CSV Data Storage
* Object-Oriented Programming

---

## Project Structure

```text
E-Commerce-Product-Recommendation-Engine/
│
├── data/
│   ├── items.csv
│   └── events.csv
│
├── outputs/
│   └── report_U001.txt
│
├── images/
│
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

## DSA Concepts Implemented

### HashMap (Dictionary)

Used for:

* Product Lookup
* User Profile Storage

Time Complexity:

```text
Search: O(1)
Insert: O(1)
```

### Lists

Used for:

* Views
* Cart Items
* Purchases
* Search History

### Sorting

Used for ranking recommendation scores.

Time Complexity:

```text
O(n log n)
```

### Priority Queue (Heap)

Used to retrieve Top-N recommendations efficiently.

Time Complexity:

```text
O(n log k)
```

---

## Dataset

### Product Dataset

Contains:

* Product ID
* Title
* Category
* Brand
* Price
* Tags

### User Events Dataset

Contains:

* User ID
* Product ID
* Event Type
* Timestamp

Event weights:

| Event    | Score |
| -------- | ----- |
| View     | 1     |
| Cart     | 3     |
| Purchase | 5     |

---

## Recommendation Logic

### Personalized Recommendations

The recommendation score is calculated using:

```text
Purchase = +5
Cart = +3
View = +1
```

Products belonging to categories frequently interacted with by the user receive higher scores.

---

### Similar Products

Similarity is calculated using:

* Category Match
* Price Similarity

Products with the highest similarity scores are recommended.

---

## Sample Output

### Top Recommendations

```text
P008 | Sony Headphones | Score: 8
P001 | iPhone 15 | Score: 1
P002 | Samsung S24 | Score: 1
```

### Similar Products

```text
P002 | Samsung S24 | Score: 15
P010 | OnePlus 13 | Score: 15
```

---

## Report Generation

The system automatically generates recommendation reports:

```text
outputs/report_U001.txt
```

---

## Future Enhancements

* TF-IDF Similarity Search
* FAISS ANN Search
* LightGBM Ranking Model
* FastAPI Integration
* Evaluation Metrics (Recall@K, NDCG@K)
* React Frontend Dashboard

---

## Author

Hardik Hipparagi

Final Year Engineering Project
