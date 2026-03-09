#p3_2
from sklearn.metrics import average_precision_score

y_true = [0,1,1,0,1,1]
y_scores = [0.1,0.4,0.35,0.8,0.65,0.9]
average_precision = average_precision_score(y_true, y_scores)
print(f"Average Precision-Recall Score: {average_precision}")
