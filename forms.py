from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DecimalField, IntegerField
from wtforms.validators import DataRequired

class DividendConstForm(FlaskForm):
    initial_dividend_value = DecimalField("Initial Dividend Value")
    stock_length = IntegerField("Stock Length (1)")
    time_btn_pay = IntegerField("Time Between Payments")
    com_ratio = DecimalField("Common Ratio (1)")
    int_rate = DecimalField("Interest Rate")

    submit = SubmitField('Calculate')

class TwoPartDDNForm(FlaskForm):
    initial_dividend_value = DecimalField("Initial Dividend Value")
    
    stock_length_1 = IntegerField("Stock Length (1)")
    stock_length_2 = IntegerField("Stock Length (2)")
    
    time_btn_pay = IntegerField("Time Between Payments")

    com_ratio_1 = DecimalField("Common Ratio (1)")
    com_ratio_2 = DecimalField("Common Ratio (2)")

    int_rate = DecimalField("Interest Rate")

    submit = SubmitField('Calculate')
