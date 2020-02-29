from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DecimalField, IntegerField, ValidationError
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
    initial_dividend_value = DecimalField("Initial Dividend Value", validators=[input_is_valid(4)])

    stock_length = IntegerField("Stock Length", validators=[input_is_valid(4)])
    time_btn_pay = IntegerField("Time Between Payments", validators=[input_is_valid(4)])

    com_ratio = DecimalField("Common Ratio", validators=[input_is_valid(4)])
    int_rate = DecimalField("Interest Rate", validators=[input_is_valid(4)])

    submit = SubmitField("Calculate", validators=[input_is_valid(4)])

class TwoPartDDNForm(FlaskForm):
    initial_dividend_value = DecimalField("Initial Dividend Value", validators=[input_is_valid(6)])
    
    stock_length_1 = IntegerField("Stock Length (1)", validators=[input_is_valid(6)])
    stock_length_2 = IntegerField("Stock Length (2)", validators=[input_is_valid(6)])
    
    time_btn_pay = IntegerField("Time Between Payments", validators=[input_is_valid(6)])

    com_ratio_1 = DecimalField("Common Ratio (1)", validators=[input_is_valid(6)])
    com_ratio_2 = DecimalField("Common Ratio (2)", validators=[input_is_valid(6)])

    int_rate = DecimalField("Interest Rate", validators=[input_is_valid(6)])

    submit = SubmitField("Calculate", validators=[input_is_valid(6)])
