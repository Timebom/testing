from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)

gaussian_model = GaussianNB()
gaussian_model.fit(X_train, y_train)
y_predict = gaussian_model.predict(X_test)

print(f"Gaussian Naive Bayes Accuracy Score: {accuracy_score(y_test, y_predict)}")
