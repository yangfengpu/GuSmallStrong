from flask_wtf import Form, RecaptchaField 
from wtforms import TextField, PasswordField, validators
from flask_wtf.html5 import DecimalField

class PurchaseItemForm(Form):
    item = TextField('Item' , [validators.Required()]) 
    description = TextField("Description",[ validators.Required()])
    qty = TextField("QTY", [validators.Required()])
    unit_price = DecimalField("Unit Price",[ validators.Required()])
    unit_price_unit = TextField("Unit",[ validators.Required()]) #select this option before entering price
    amount = TextField("Amount", [validators.Required()])

    