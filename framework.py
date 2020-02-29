from flask import Flask, render_template
from config import Config

app = Flask(__name__)
# TODO: Change config for deployment later
app.config.from_object(Config)

if __name__ == "__main__":
    app.run()

#TODO: Add jinja to html when necessary
@app.route("/")
def landing_site():
    return render_template("fintech.html")

@app.route("/one-part-ddm", methods=['GET', 'POST'])
def one_part_ddm():
    return render_template("DividendConst.html")

@app.route("/two-part-ddm", methods=['GET', 'POST'])
def two_part_ddm():
    return render_template("2PartDDN.html")