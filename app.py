from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        message = "" 
    elif request.method == 'POST':
        returned = request.form['returned']
        invested = request.form['invested']

    ret = str(returned)
    inv = str(invested)
    gain = float(ret) - float(inv)
    roi = (gain / float(inv))
    return render_template("index.html", gain=gain, roi=roi)


if __name__ == '__main__':
  app.run(debug=True)
