from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        returned = ""
        invested = ""
    elif request.method == 'POST':
        try:
            returned = float(request.form['returned'])
            invested = float(request.form['invested'])
            gain = returned - invested
            roi = (gain / invested) * 100
        except ValueError:
            returned = ""
            invested = ""
            gain = ""
            roi = ""
            
    return render_template("index.html", gain=gain, roi=roi)


if __name__ == '__main__':
  app.run(debug=True)
