from flask import Flask
app = Flask(__name__)

# a.
import nltk
from nltk import FreqDist

nltk.download('gutenberg')
from nltk.corpus import gutenberg

@app.route("/")
# b.
def count_words():

    # c.
    tokens = gutenberg.words('austen-sense.txt')
    tokens = [word.lower() for word in tokens if word.isalpha()]

    # d.
    fdist = FreqDist(tokens)
    common = fdist.most_common(500)

    # e.
    words = []
    for word, frequency in common:
        words.append(word)
    words.sort()

    # f.
    highCount = common[0][1]

    # g.
    html

if __name__ == "__main__":
    app.run()
