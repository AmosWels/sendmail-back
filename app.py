from flask import Flask
from flask_mail import Mail, Message
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
mail= Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'doep40077@gmail.com'
app.config['MAIL_PASSWORD'] = 'peter!@#'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route('/sendmail')
def index():
    try:
        msg = Message('Hello', sender = 'doep40077@gmail.com', recipients = ['martinkatamba@gmail.com', 'amoswelike@gmail.com'])
        msg.body = "This is the email body for testing"
        mail.send(msg)
        return "Your email has been Sent"
    except Exception as e:
        return(str(e))

if __name__ == '__main__':
    app.run(debug=True)