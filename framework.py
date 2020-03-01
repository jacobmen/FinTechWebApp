from flask import Flask, render_template, redirect
from config import Config
from forms import DividendConstForm, TwoPartDDNForm

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
    form = DividendConstForm()
    if (form.validate_on_submit()):
        return redirect("/process-one-part")
    print(form.errors)
    return render_template("DividendConst.html", form=form)

@app.route("/two-part-ddm", methods=['GET', 'POST'])
def two_part_ddm():
    form = TwoPartDDNForm()
    if (form.validate_on_submit()):
        return redirect("/process-two-part")

    return render_template("2PartDDM.html", form=form)

@app.route("/process-one-part", methods=['GET', 'POST'])
def process_one_part_ddm():
    #TODO: Process
    pass

@app.route("/process-two-part", methods=['GET', 'POST'])
def process_two_part_ddm():
    #TODO: Process
    pass