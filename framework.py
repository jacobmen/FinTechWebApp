from flask import Flask, render_template
from config import DevelopmentConfig

app = Flask(__name__)
# TODO: Change config for deployment later
app.config.from_object(DevelopmentConfig)

if __name__ == "__main__":
    app.run()

#TODO: Add jinja to html when necessary
@app.route("/")
def landing_site():
    return render_template("fintech.html")

@app.route("/one-part-ddm")
def one_part_ddm():
    return "TEMP LANDING"

@app.route("/two-part-ddm")
def two_part_ddm():
    return "TEMP LANDING"