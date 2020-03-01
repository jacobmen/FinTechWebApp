from flask import Flask, render_template, redirect, request
from config import Config
from forms import DividendConstForm, TwoPartDDNForm
from data.GraphGenerator import *

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
        if (not request.form["int_rate"]):
            return render_template("DividendConst.html", form=form, graph="graphs/ir_p.png")
            #graphIR(0, 100, request.form["initial_dividend_value"], request.form["time_btn_pay"], request.form["com_ratio"], request.form["stock_length"])
        elif (not request.form["initial_dividend_value"]):
            return render_template("DividendConst.html", form=form, graph="graphs/dv_p.png")            
            #return graphDividend(5, 100, request.form["time_btn_pay"], request.form["com_ratio"], request.form["int_rate"], request.form["stock_length"])
        elif (not request.form["time_btn_pay"]):
            return render_template("DividendConst.html", form=form, graph="graphs/pp_p.png")            
            #return graphInterval(0.1, 5, request.form["initial_dividend_value"], request.form["com_ratio"], request.form["int_rate"], request.form["stock_length"])
        elif (not request.form["com_ratio"]):
            return render_template("DividendConst.html", form=form, graph="graphs/cr_p.png")            
            #return graphCommonRatio(0, 100, request.form["initial_dividend_value"], request.form["time_btn_pay"], request.form["int_rate"], request.form["stock_length"])
        else:
            return render_template("DividendConst.html", form=form, graph="graphs/ls_p.png")
            #return graphStockLength(1, 100, request.form["initial_dividend_value"], request.form["time_btn_pay"], request.form["com_ratio"], request.form["int_rate"])

    return render_template("DividendConst.html", form=form)

@app.route("/two-part-ddm", methods=['GET', 'POST'])
def two_part_ddm():
    form = TwoPartDDNForm()
    if (form.validate_on_submit()):
        return request.form["initial_dividend_value"]

    return render_template("2PartDDM.html", form=form)

@app.route("/process-one-part", methods=['GET', 'POST'])
def process_one_part_ddm():
    #TODO: Process
    pass

@app.route("/process-two-part", methods=['GET', 'POST'])
def process_two_part_ddm():
    #TODO: Process
    pass