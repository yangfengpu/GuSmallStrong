from flask import Flask
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = 'gugustrong'
app.config['RECAPTCHA_PARAMETERS'] = {'hl': 'zh', 'render': 'explicit'}
app.config['RECAPTCHA_DATA_ATTRS'] = {'theme': 'dark'}
app.config['RECAPTCHA_PUBLIC_KEY'] = '6LeYIbsSAAAAACRPIllxA7wvXjIE411PfdB2gt2J'
app.config['RECAPTCHA_PRIVATE_KEY'] = '6LeYIbsSAAAAAJezaIq3Ft_hSTo0YtyeFG-JgRtu'

import greency.views