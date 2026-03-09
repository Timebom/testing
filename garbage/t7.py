from collections import Counter

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize

nltk.download("punkt")
nltk.download("stopwords")

def generate_summary(text, n):
    sentences = sent_tokenize(text)
    stop_words = set(stopwords.words("english"))
    words = [word.lower() for word in word_tokenize(text) if word.lower() not in stop_words and word.isalnum()]
    word_freq = Counter(words)
    sentence_scores = {}
    for sentence in sentences:
        sentence_words = [word.lower() for word in word_tokenize(sentence) if word.lower() not in stop_words and word.isalnum()]
        sentence_score = sum([word_freq[word] for word in sentence_words])
        if len(sentence_words) < 20:
            sentence_scores[sentence] = sentence_score + 1
    summary_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:n]
    summary = "\n".join(summary_sentences)
    return summary

text = '''
Weather is the day-to-day or hour-to-hour change in the atmosphere.
Weather includes wind, lightning, storms, hurricanes, tornadoes (also known as twisters), rain, hail, snow, and lots more.
Energy from the Sun affects the weather too.
Climate tells us what kinds of weather usually happen in an area at different times of the year.
Changes in weather can affect our mood and life. We wear different clothes and do different things in different weather conditions.
We choose different foods in different seasons.
Weather stations around the world measure different parts of weather.
Ways to measure weather are wind speed, wind direction, temperature and humidity.
People try to use these measurements to make weather forecasts for the future.
These people are scientists that are called meteorologists.
They use computers to build large mathematical models to follow weather trends.'''

summary = generate_summary(text, 5)
# summary_sentences = summary.split('.')
# formatted_summary = '\n'.join(summary_sentences)
print("\n\nSummary :")
print(summary)
