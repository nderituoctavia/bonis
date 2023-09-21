# Step 0: Sample Data (replace this with real data)
data = {
    "age": [64, 60, 44, 59, 57, 60, 59, 54, 57, 60, 59, 57, 57],
    "hometown": ["Brussels", "Athens", "Brussels", "Sofia", "Zagreb", "Tallinn", "Dublin", "Helsinki", "Paris", "Rome", "Riga", "Vilnius", "Warsaw"],
    "full_name": ["Charles Michel", "Kyriakos Mitsotakis", "Alexander De Croo", "Kiril Petkov", "Andrej Plenković", "Kaja Kallas", "Micheál Martin", "Sanna Marin", "Élisabeth Borne", "Mario Draghi", "Krišjānis Kariņš", "Ingrida Šimonytė", "Mateusz Morawiecki"],
    "years_in_service": [1, 2, 2, 1, 6, 2, 2, 1, 1, 1, 1, 1, 3],
    "marital_status": ["Married", "Married", "Married", "Married", "Married", "Married", "Married", "Single", "Divorced", "Married", "Married", "Married", "Married"]
}

# Step 1: Feature Extraction
import pandas as pd

df = pd.DataFrame(data)

# One-hot encoding for hometown and marital_status. This might not be meaningful for the name.
df = pd.get_dummies(df, columns=["hometown", "marital_status"])

# Step 2: Train a K-means classifier
from sklearn.cluster import KMeans

X = df.drop('full_name', axis=1)  # Removing the name column
kmeans = KMeans(n_clusters=3)  # Example: 3 clusters
df['cluster'] = kmeans.fit_predict(X)

# Step 3: Displaying Results
print(df)

# Step 4: Interpretation
# This step is largely qualitative. Examine members of each cluster and see if there are any common patterns or characteristics.
