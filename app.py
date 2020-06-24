from flask import Flask, request, jsonify
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
@app.route('/sendmail', methods=['POST'])
def index():
    if request.method=='POST':
        posted_data = request.get_json()
        data = posted_data['data']
        name = data['name']
        price = data['price']
        email = data['email']
    try:
        msg = Message('Hello customer care', sender = 'doep40077@gmail.com', recipients = ['martinkatamba@gmail.com', email])
        msg.body = "This is %s \n and i would like agro-chemicals at a price of %s ugx" % (name, price)
        mail.send(msg)
        return jsonify({"message":"Your email has been Sent"})
    except Exception as e:
        return(str(e))

if __name__ == '__main__':
    app.run(debug=True)