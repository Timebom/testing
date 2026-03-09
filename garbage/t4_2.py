import nltk
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

documents = [
    "The quick brown fox jumps over the lazy dog",
    "A brown dog chased the fox",
    "The dog is lazy"
]

nltk.download("punkt")
nltk.download("punkt_tab")

query = "brown dog"
tokenized_documents = [word_tokenize(doc) for doc in documents]
tokenized_query = word_tokenize(query)
preprocessed_documents = [" ".join(doc) for doc in tokenized_documents]
preprocessed_query = " ".join(tokenized_query)

vectorized = TfidfVectorizer()
metrix = vectorized.fit_transform(preprocessed_documents)
query_vector = vectorized.transform([preprocessed_query])
cosine_values = cosine_similarity(query_vector, metrix)[0]
results = list(zip(documents, cosine_values))
results.sort(key=lambda x: x[1], reverse=True)
for doc, similarity in results:
    print(f"Similarity: {similarity:.2f}\n{doc}\n")
