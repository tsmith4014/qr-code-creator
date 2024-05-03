# routes.py
from flask import render_template, send_file
from .forms import InputForm
import qrcode
from io import BytesIO

def init_app(app):
    @app.route('/', methods=['GET', 'POST'])
    def home():
        form = InputForm()
        if form.validate_on_submit():
            img_io = BytesIO()
            qr_data = ""
            if form.submit1.data:
                # Strip whitespace and join data with a space
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
            # Generate QR code with the cleaned data
            img = qrcode.make(qr_data)
            img.save(img_io, 'PNG')
            img_io.seek(0)
            return send_file(img_io, mimetype='image/png', as_attachment=True, download_name=download_name)
        return render_template('home.html', form=form)
