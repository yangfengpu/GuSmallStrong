from flask_wtf import Form, RecaptchaField 
from wtforms import TextField, PasswordField, validators

class PurchaseOrderForm(Form):
    payment_term = TextField('Payment payment_term', [validators.Required()]) 
    est_delivery = TextField(["Est, Delivery", validators.Required()])
    delivery_term = TextField(["Delivery Term", validators.Required()])
    delivery_port = TextField(["Delivery Port", validators.Required()])
    bank_info = TextField(["Bank Info.", validators.Required()])
    remark = TextField(["Delivery Port", validators.Required()])

