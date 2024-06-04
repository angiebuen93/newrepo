from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        message = "" 
    elif request.method == 'POST':
        returned = request.form['returned']
        invested = request.form['invested']

    gain = float(returned) - float(invested)
    roi = (gain / float(invested))
    return render_template("index.html", message=message)


if __name__ == '__main__':
  app.run(debug=True)
