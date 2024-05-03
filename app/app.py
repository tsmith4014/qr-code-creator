#Not using app.py currently trying the modular approach of using a __init__.py file, routes.py file, and forms.py file and run.py file to practice the modular approach of creating a Flask application verus the single file approach of using app.py.  This is supposed to be the more scalable approach to creating a Flask application.
#app.py 
from flask import Flask, render_template, send_file
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
import qrcode
from io import BytesIO
from dotenv import load_dotenv
import os

load_dotenv()

# Define the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default_secret_key_here')  # Fallback to a default if not found

# Define the form class
class InputForm(FlaskForm):
    info1 = StringField('Enter Information for Form 1')
    info1_additional1 = StringField('Enter Additional Information 1 for Form 1')
    submit1 = SubmitField('Generate QR Code for Form 1')
    info2 = StringField('Enter Information for Form 2')
    submit2 = SubmitField('Generate QR Code for Form 2')
    info3 = StringField('Enter Information for Form 3')
    submit3 = SubmitField('Generate QR Code for Form 3')
    info4 = StringField('Enter Information for Form 4')
    submit4 = SubmitField('Generate QR Code for Form 4')

# Define the route for handling the form
@app.route('/', methods=['GET', 'POST'])
def home():
    form = InputForm()
    if form.validate_on_submit():
        img_io = BytesIO()
        qr_data = ""
        if form.submit1.data:
            info1_data = form.info1.data.strip()
            info1_additional1_data = form.info1_additional1.data.strip()
            qr_data = f"{info1_data}\t{info1_additional1_data}"  # Join with a tab
            download_name = 'qr_code_form1.png'
        elif form.submit2.data:
            qr_data = form.info2.data.strip()
            download_name = 'qr_code_form2.png'
        elif form.submit3.data:
            qr_data = form.info3.data.strip()
            download_name = 'qr_code_form3.png'
        elif form.submit4.data:
            qr_data = form.info4.data.strip()
            download_name = 'qr_code_form4.png'
        img = qrcode.make(qr_data)
        img.save(img_io, 'PNG')
        img_io.seek(0)
        return send_file(img_io, mimetype='image/png', as_attachment=True, download_name=download_name)
    return render_template('home.html', form=form)

# Template directly in app for simplicity (can also place in a 'templates' directory as 'home.html')
'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>All Forms</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #e8f0fe; /* A light blue that complements the green buttons */
            margin: 0;
        }
        form {
            display: flex;
            flex-direction: column;
            gap: 20px;
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        div {
            display: flex;
            flex-direction: column;
        }
        input[type="text"], input[type="submit"] {
            padding: 10px;
            margin-top: 5px;
        }
        input[type="submit"] {
            background-color: #4caf50;
            color: white;
            cursor: pointer;
        }
        input[type="submit"]:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <form action="" method="post">
        {{ form.hidden_tag() }}
        <div>{{ form.info1.label }}<br>{{ form.info1(size=32) }}<br>{{ form.info1_additional1.label }}<br>{{ form.info1_additional1(size=32) }}<br>{{ form.submit1() }}</div>
        <div>{{ form.info2.label }}<br>{{ form.info2(size=32) }}<br>{{ form.submit2() }}</div>
        <div>{{ form.info3.label }}<br>{{ form.info3(size=32) }}<br>{{ form.submit3() }}</div>
        <div>{{ form.info4.label }}<br>{{ form.info4(size=32) }}<br>{{ form.submit4() }}</div>
    </form>
</body>
</html>
'''

if __name__ == "__main__":
    app.run(debug=True)

