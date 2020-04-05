from flask import Flask, render_template
import requests
app = Flask(__name__)

raw = requests.get('https://api.covid19india.org/data.json')
data = raw.json()
daily_report = data['cases_time_series'][-1]
statewise = data['statewise']

raw = requests.get('https://api.covid19india.org/state_district_wise.json')
data = raw.json()
districtData = data['Andhra Pradesh']['districtData']

@app.route('/')
def hello_name():
   return render_template('hello.html', result =[daily_report,statewise,districtData])

@app.route('/states')
def states():
   return render_template('states.html', result =[daily_report,statewise,districtData])

@app.route('/districts')
def districts():
   return render_template('districts.html', result =[daily_report,statewise,districtData])

