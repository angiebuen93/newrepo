from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    returned = 0
    invested = 0
    gain = 0
    roi = 0
    if request.method == 'GET':
        returned = ""
        invested = ""
    elif request.method == 'POST':
        try:
            returned = float(request.form['returned'])
            invested = float(request.form['invested'])
            gain = returned - invested
            roi = (gain / invested) * 100
            roi = round(roi, 2)
        except ValueError:
            returned = ""
            invested = ""
            gain = ""
            roi = ""
            
    return render_template("index.html", returned=returned, invested=invested, gain=gain, roi=roi)


if __name__ == '__main__':
  app.run(debug=True)

#this is update to a code file