from flask import Flask, render_template, url_for, redirect


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

## @app.route('/membership')
## def membership():
##    return render_template('membership.html') *

@app.route('/about')
def about():
    return render_template('about.html')

# Processing For Invalid URL
@app.route('/<userInput>')
def reset(userInput):
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
