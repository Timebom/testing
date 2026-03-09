from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import silhouette_score

documents = [
    "Football is popular sport",
    "The team won the match",
    "The government passed a new law",
    "The president gave a speech",
    "The player scored a goal",
    "Election will be held soon"
]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(documents)

K = 2
kmeans = KMeans(n_clusters=K, random_state=42)
kmeans.fit(X)

print("Clustering Documents: ")
for i, doc in enumerate(documents):
    print(f"Cluster {kmeans.labels_[i]}: {doc}")

print(f"\nSilhouette Score: {silhouette_score(X, kmeans.labels_)}")
