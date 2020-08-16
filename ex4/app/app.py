from flask import Flask
app = Flask(__name__)

import nltk
from nltk import FreqDist

nltk.download('gutenberg')
from nltk.corpus import gutenberg

# 1.
nltk.download('stopwords')
from nltk.corpus import stopwords

@app.route("/")
def count_words():

    # 2.
    # Define the stopword set
    stopWords = set(stopwords.words('english'))

    # 3.
    # Grab Sense and Sensibility; tokenize; filter stop words;
    # get frequency distribution
    tokens = gutenberg.words('austen-sense.txt')
    tokens = [word.lower() for word in tokens if word.isalpha()]
    tokens = [word for word in tokens if word not in stopWords]
    fdist = FreqDist(tokens)

    common = fdist.most_common(500)

    words = []
    for word, frequency in common:
        words.append(word)
    words.sort()

    highCount = common[0][1]

    html= '<!DOCTYPE html><html><head><title>Word Cloud</title></head><body style="word-wrap: break-word;"><h1>Most Common Words in Sense and Sendsibility</h1>'

    for word in words:
        size = str(int(15 + fdist[word] / float(highCount) * 150))
        colour = str(hex(int(0.8 * fdist[word] / \
        float(highCount) * 256**3)))
        colour = colour[-(len(colour) - 2):]
        while len(colour) < 6:
            colour = "0" + colour
        html = html + f'<span style="font-size: {size}px; color: #{colour}">{word}</span>'

    return html + "</body></html>"

if __name__ == "__main__":
    app.run()
