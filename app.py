from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
# load the model
model = pickle.load(open('Earthquack.pkl', 'rb'))

@app.route('/')
def home():
    result = ''
    return render_template('User.html', **locals())


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    magnitude = float(request.form['magnitude'])
    date_time = float(request.form['date_time'])
    cdi = float(request.form['cdi'])
    mmi = float(request.form['mmi'])
    alert= float(request.form['alert'])
    tsunami= float(request.form['tsunami'])
    sig= float(request.form['sig'])
    net= float(request.form['net'])
    nst= float(request.form['nst'])
    dmin= float(request.form['dmin'])
    gap= float(request.form['gap'])
    magType= float(request.form['magType'])
    depth= float(request.form['depth'])
    latitude= float(request.form['latitude'])
    longitude = float(request.form['longitude'])
    location = float(request.form['location'])
    continent = float(request.form['continent'])
    country = float(request.form['country'])
    result = model.predict([['magnitude','magnitude','date_time','cdi','mmi','alert','tsunami','sig','net','nst','dmin','gap','magType','depth','latitude','longitude''location','continent','country']])
    return render_template('User.html', **locals())
    
if __name__ == '__main__':
    app.run(debug=True)
