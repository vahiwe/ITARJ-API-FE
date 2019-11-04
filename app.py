from flask import Flask, render_template, url_for, request
import requests


app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def home():
    if request.method == 'POST':
        company = str(request.form['message'])
        address = str(request.form['address'])
        invite = str(request.form['invite'])
        url = 'https://itarj-cors.appspot.com/https://isthisarealjob-api.appspot.com/form'
        payload = {'company': company,
        'address': address,
        'invite': invite}
        files = {}
        headers = {
        'Origin': 'x-requested-with'
        }
        response = requests.request('POST', url, headers = headers, data = payload, files = files, allow_redirects=False)
        report = response.text
        report = report.replace("{","").replace("}","")
        report = report.split(":")[1]
        return render_template('home.html', report=report)
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
