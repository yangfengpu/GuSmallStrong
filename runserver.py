from greency import app
import os


app.secret_key = os.urandom(24)

app.run(debug=True, port=9000)