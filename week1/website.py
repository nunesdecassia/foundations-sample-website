from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('concept.html', page_title="CODE Concept", color="color1")


@app.route('/study')
def first_page():
    return render_template('studyprograms.html', page_title="CODE Study Programs", color="color3")


@app.route('/admission')
def second_page():
    return render_template('admission.html', page_title=" CODE Admission", color="color2")

# add additonal pages here using a similar format as above


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
