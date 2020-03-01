from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DecimalField, IntegerField, ValidationError, validators
from wtforms.validators import DataRequired

def input_is_valid(num_required_inputs):
    def _input_is_valid(form, field):
        input_count = 0
        
        if (form.initial_dividend_value.data):
            input_count = input_count + 1
        
        if (form.stock_length.data):
            input_count = input_count + 1   
        
        if (form.time_btn_pay.data):
            input_count = input_count + 1
       
        if (form.com_ratio.data):
            input_count = input_count + 1
        
        if (form.int_rate.data):
            input_count = input_count + 1    

        if (input_count < num_required_inputs):
            raise ValidationError("Invalid Input")

    return _input_is_valid

class DividendConstForm(FlaskForm):
    initial_dividend_value = DecimalField("Initial Dividend Value", validators=[input_is_valid(4), validators.Optional()])

    stock_length = IntegerField("Stock Length", validators=[validators.Optional()])
    time_btn_pay = IntegerField("Time Between Payments", validators=[validators.Optional()])

    com_ratio = DecimalField("Common Ratio", validators=[validators.Optional()])
    int_rate = DecimalField("Interest Rate", validators=[validators.Optional()])

    submit = SubmitField("Calculate", validators=[input_is_valid(4), validators.Optional()])

class TwoPartDDNForm(FlaskForm):
    initial_dividend_value = DecimalField("Initial Dividend Value", validators=[validators.Optional()])
    
    stock_length_1 = IntegerField("Stock Length (1)", validators=[validators.Optional()])
    stock_length_2 = IntegerField("Stock Length (2)", validators=[validators.Optional()])
    
    time_btn_pay = IntegerField("Time Between Payments", validators=[validators.Optional()])

    com_ratio_1 = DecimalField("Common Ratio (1)", validators=[validators.Optional()])
    com_ratio_2 = DecimalField("Common Ratio (2)", validators=[validators.Optional()])

    int_rate = DecimalField("Interest Rate", validators=[validators.Optional()])

    submit = SubmitField("Calculate", validators=[input_is_valid(6), validators.Optional()])
