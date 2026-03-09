d1 = "The quick fox jumped over the dog"
d2 = "The lazy dog slept quick in the sun"
d3 = "The lazy fox jumped over the dog"

token1 = d1.lower().split()
token2 = d2.lower().split()
token3 = d3.lower().split()

terms = list(set(token1+token2+token3))
inv_idx = {}

for term in terms:
    documents = []
    if term in token1:
        documents.append("Document 1")

    if term in token2:
        documents.append("Document 2")

    if term in token3:
        documents.append("Document 3")

    inv_idx[term] = documents

for term, documents in inv_idx.items():
    print(f"{term} -> {", ".join(documents)}")

print()
words = input("Enter two words: ")
print(f"Query : {words}")
words = words.lower().split()
final_list = []

for token in words:
    for t, v in inv_idx.items():
        if t == token:
            final_list.append(set(v))

print("\nAfter intersection the documents related are:")
list3 = list(final_list[0].intersection(final_list[1]))
print(list3)
