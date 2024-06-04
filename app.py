from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        message = "" 
    elif request.method == 'POST':
        returned = request.form.get['returned']
        invested = request.form.get['invested']

    ret = float(returned)
    inv = float(invested)
    gain = ret - inv
    roi = (gain / inv) * 100
    return render_template("index.html", gain=gain, roi=roi)


if __name__ == '__main__':
  app.run(debug=True)
