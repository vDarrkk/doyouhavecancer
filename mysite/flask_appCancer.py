from flask import Flask, render_template, request
import config

app = Flask(__name__)
symptoms = config.symptoms

@app.route('/')
def home_page():
    return render_template('index.html', symptoms=symptoms)


@app.route('/search')
def search():
    cancers = config.cancers
    selections_dict = request.args
    selections = []

    for item in selections_dict.keys():
        selections.append(selections_dict[item].lower())

    result = [ [], [], [], [], [] ]

    for item in cancers:
        cancer = item.split('~')
        name = cancer[0]
        count = 0
        for i in range(1, len(cancer)):
            if (cancer[i].lower() in selections):
                count += 1
        if count >= 1:
            percent = round((count / (len(cancer)-1)) * 100)
            if percent >= 80:
                result[0].append(tuple([name, percent]))
            elif percent >= 60:
                result[1].append(tuple([name, percent]))
            elif percent >= 40:
                result[2].append(tuple([name, percent]))
            elif percent >= 20:
                result[3].append(tuple([name, percent]))
            else:
                result[4].append(tuple([name, percent]))

    for i in range(0, 5):
        result[i].sort(key=lambda cancer: cancer[1], reverse=True)

    if len(result[0]) > 0 or len(result[1]) > 0 or len(result[2]) > 0 or len(result[3]) > 0 or len(result[4]) > 0:
        return render_template('cancer.html', result=result)

    return render_template('cancerfree.html')


@app.route('/support')
def support():
    return render_template('support.html')
