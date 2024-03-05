from flask import Flask, request,render_template
import re

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('regex.html')

@app.route('/results', methods = ['POST'])
def result():
    match= ''
    pattern = request.form.get('regex')
    string = request.form.get('string')
    try:
        match = re.findall(pattern, string)
        if not match:
            match = 'No matches found'
        else:
            match =', '.join(match)
    except re.error:
            match = 'Invalid regular expression'
    return render_template('regex.html',pattern=pattern, string=string, match=match)

@app.route('/email_validation')
def email_validation():
    return render_template('email_validation.html')

@app.route('/valid_email', methods=["POST"])
def valid_email():
    e_address= ''
    e_pattern =  r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    e_mail= str(request.form.get('e_mail')).strip()
    e_address = re.findall(e_pattern, e_mail)
    if not e_address:
       return 'Invalid Email Address'
    else:
        e_address =' '.join(e_address)
    return f'{e_address } is a valid mail'

if __name__ == "__main__":
    app.run(debug = True, host="0.0.0.0")