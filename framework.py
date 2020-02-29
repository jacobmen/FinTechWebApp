from flask import Flask, render_template

app = Flask(__name__)

if __name__ == "__main__":
    app.run()

#TODO: Add jinja to html when necessary
@app.route("/")
def landing_site():
    return render_template("fintech.html")
