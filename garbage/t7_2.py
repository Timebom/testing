from txtai.pipeline import Questions

qa = Questions("distilbert-base-cased-distilled-squad")

Data = [
"Australia is the only country that is also a continent.",
"The Great Barrier Reef is the world's largest living structure and can be seen from space.",
"Australia is home to a variety of unique wildlife, including kangaroos, koalas and platypuses.",
"The world's oldest known civilization, the Aboriginal culture, is believed to have originated in Australia around 50,000 years ago.",
"Australia is famous for its large number of deadly animals, such as snakes, spiders, and marine creatures.",
"The Australian Alps, or Snowy Mountains, receive more snowfall than Switzerland.",
"Australia has over 10,000 beaches, more than any other country.",
"The Outback, a vast, remote area of Australia, covers most of the country's landmass.",
"Australia has a large area of vineyards and is known for producing high-quality wines.",
"Opera House, an iconic building and UNESCO World Heritage Site, is in Sydney."
]

question = "Where is Opera House in Australia?"
context = " ".join(Data)

answer = qa([question], [context])

print(f"Question: {question}")
print(f"Answer: {answer}")
