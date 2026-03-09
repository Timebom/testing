def cal_metrics(retrieved_set, relevent_set):
    tp = len(retrieved_set.intersection(relevent_set))
    fp = len(retrieved_set.difference(relevent_set))
    fn = len(relevent_set.difference(retrieved_set))

    print(f"True Positive: {tp}")
    print(f"False Positive: {fp}")
    print(f"False Negative: {fn}")

    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f_measure = 2 * ((precision * recall) / (precision + recall))

    return precision, recall, f_measure

retrieve_set = set(['doc1', 'doc2', 'doc3'])
relevent_set = set(['doc1', 'doc4'])
p, r, f = cal_metrics(retrieve_set, relevent_set)
print(f"Precision : {p}")
print(f"Recall : {r}")
print(f"F1 Score : {f}")
