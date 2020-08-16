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
    html= '<!DOCTYPE html><html><head><title>Word Cloud</title></head><body style="word-wrap: break-word;"><h1>Most Common Words in Sense and Sendsibility</h1>'

    # h. and i.
    for word in words:
        size = str(int(15 + fdist[word] / float(highCount) * 150))
        colour = str(hex(int(0.8 * fdist[word] / \
        float(highCount) * 256**3)))
        colour = colour[-(len(colour) - 2):]
        while len(colour) < 6:
            colour = "0" + colour
        html = html + f'<span style="font-size: {size}px; color: #{colour}">{word}</span>'

    # j.
    return html + "</body></html>"

if __name__ == "__main__":
    app.run()
