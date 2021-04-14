from flask import Flask, render_template, request
import spacy
import sys,json
from nltk.tag import pos_tag
from flask import Flask
from flask import request

app  = Flask(__name__)

def getTitles(sentences):
	nlp = spacy.load("en_core_web_sm")
	doc = nlp(sentences)
	result =  list(doc.noun_chunks)
	return result

@app.route('/getTitles/', methods=['post', 'get'])
def getTitle():
    message = ''
    if request.method == 'POST':
        textualinfo = request.form.get('text')  # access the data inside
        sentences_with_nouns = []
        result = getTitles(textualinfo)
        for word in result:
            word_pos = pos_tag([str(word)])
            if word_pos[0][1] == 'NN' or word_pos[0][1] == 'NNS' or word_pos[0][1] == 'NNP':
                sentences_with_nouns.append(str(word))
            else:
                pass
        message = sentences_with_nouns
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)