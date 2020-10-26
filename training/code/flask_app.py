import os
os.urandom(16)

phone_number = '+31629712502'
from flask import Flask, render_template, request
from messaging import get_token, provision, senmd_sms

app = Flask(__name__)
app.secret_key = '130948123890fd890sadf780a8dsfda9s870124312'

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/sms', methods=['GET'])
def sms_form():
    return render_template('sms.html')


@app.route('/sms', methods=['POST'])
def sms_post():
    message = request.form['message']
    token = get_token()
    provision(token)
    return send_sms(phone_number, message, token)
    return f'Message was {message}'

if __name__ == '__main__':
    app.run(debug=True, port=5000)
