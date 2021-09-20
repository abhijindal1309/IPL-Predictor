# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
# Load the Random Forest CLassifier model
filename = 'first-innings-score.pkl'
filename1 = 'second-innings-lgr-model1.pkl'
regressor = pickle.load(open(filename, 'rb'))
lin = pickle.load(open(filename1, 'rb'))
temp_array = list()

x_train = pd.read_csv('X_train.csv')
sc.fit(x_train)
x = sc.transform(x_train)
# temp_array = temp_array + [0,0,0,0,0,0,0,1]
# temp_array = temp_array + [overs, runs, wickets, runs_in_prev_5, wickets_in_prev_5]
# my_prediction = int(regressor.predict(data)[0])

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('dash.html')

@app.route('/first_innings')
def fin():
    return render_template('index.html')

@app.route('/second_innings')
def sin():
    return render_template('index1.html')        

@app.route('/predict', methods=['POST'])
def predict():
    temp_array = list()
    
    if request.method == 'POST':
        
        batting_team = request.form['batting-team']
        if batting_team == 'Chennai Super Kings':
            temp_array = temp_array + [1,0,0,0,0,0,0,0]
        elif batting_team == 'Delhi Capitals':
            temp_array = temp_array + [0,1,0,0,0,0,0,0]
        elif batting_team == 'Kolkata Knight Riders':
            temp_array = temp_array + [0,0,1,0,0,0,0,0]
        elif batting_team == 'Mumbai Indians':
            temp_array = temp_array + [0,0,0,1,0,0,0,0]
        elif batting_team == 'Punjab Kings':
            temp_array = temp_array + [0,0,0,0,1,0,0,0]    
        elif batting_team == 'Rajasthan Royals':
            temp_array = temp_array + [0,0,0,0,0,1,0,0]
        elif batting_team == 'Royal Challengers Bangalore':
            temp_array = temp_array + [0,0,0,0,0,0,1,0]
        elif batting_team == 'Sunrisers Hyderabad':
            temp_array = temp_array + [0,0,0,0,0,0,0,1]
            
            
        bowling_team = request.form['bowling-team']
        if bowling_team == 'Chennai Super Kings':
            temp_array = temp_array + [1,0,0,0,0,0,0,0]
        elif bowling_team == 'Delhi Capitals':
            temp_array = temp_array + [0,1,0,0,0,0,0,0]
        elif bowling_team == 'Kolkata Knight Riders':
            temp_array = temp_array + [0,0,1,0,0,0,0,0]
        elif bowling_team == 'Mumbai Indians':
            temp_array = temp_array + [0,0,0,1,0,0,0,0]
        elif bowling_team == 'Punjab Kings':
            temp_array = temp_array + [0,0,0,0,1,0,0,0]    
        elif bowling_team == 'Rajasthan Royals':
            temp_array = temp_array + [0,0,0,0,0,1,0,0]
        elif bowling_team == 'Royal Challengers Bangalore':
            temp_array = temp_array + [0,0,0,0,0,0,1,0]
        elif bowling_team == 'Sunrisers Hyderabad':
            temp_array = temp_array + [0,0,0,0,0,0,0,1]
            
            
        overs = float(request.form['overs'])
        runs = int(request.form['runs'])
        wickets = int(request.form['wickets'])
        runs_in_prev_5 = int(request.form['runs_in_prev_5'])
        wickets_in_prev_5 = int(request.form['wickets_in_prev_5'])
        
        temp_array = temp_array + [overs, runs, wickets, runs_in_prev_5, wickets_in_prev_5]
        
        # data = np.array([temp_array])
        # my_prediction = int(regressor.predict(data)[0])

        prediction=regressor.predict([temp_array])
        output=int(prediction[0])
              
        return render_template('result.html', score = output)


@app.route('/predict1', methods=['POST'])
def predict1():
    temp_array1 = list()
    
    if request.method == 'POST':
        
        batting_team = request.form['batting-team']
        if batting_team == 'Chennai Super Kings':
            temp_array1 = temp_array1 + [1,0,0,0,0,0,0,0]
        elif batting_team == 'Delhi Capitals':
            temp_array1 = temp_array1 + [0,1,0,0,0,0,0,0]
        elif batting_team == 'Kolkata Knight Riders':
            temp_array1 = temp_array1 + [0,0,1,0,0,0,0,0]
        elif batting_team == 'Mumbai Indians':
            temp_array1 = temp_array1 + [0,0,0,1,0,0,0,0]
        elif batting_team == 'Punjab Kings':
            temp_array1 = temp_array1 + [0,0,0,0,1,0,0,0]    
        elif batting_team == 'Rajasthan Royals':
            temp_array1 = temp_array1 + [0,0,0,0,0,1,0,0]
        elif batting_team == 'Royal Challengers Bangalore':
            temp_array1 = temp_array1 + [0,0,0,0,0,0,1,0]
        elif batting_team == 'Sunrisers Hyderabad':
            temp_array1 = temp_array1 + [0,0,0,0,0,0,0,1]
            
            
        bowling_team = request.form['bowling-team']
        if bowling_team == 'Chennai Super Kings':
            temp_array1 = temp_array1 + [1,0,0,0,0,0,0,0]
        elif bowling_team == 'Delhi Capitals':
            temp_array1 = temp_array1 + [0,1,0,0,0,0,0,0]
        elif bowling_team == 'Kolkata Knight Riders':
            temp_array1 = temp_array1 + [0,0,1,0,0,0,0,0]
        elif bowling_team == 'Mumbai Indians':
            temp_array1 = temp_array1 + [0,0,0,1,0,0,0,0]
        elif bowling_team == 'Punjab Kings':
            temp_array1 = temp_array1 + [0,0,0,0,1,0,0,0]    
        elif bowling_team == 'Rajasthan Royals':
            temp_array1 = temp_array1 + [0,0,0,0,0,1,0,0]
        elif bowling_team == 'Royal Challengers Bangalore':
            temp_array1 = temp_array1 + [0,0,0,0,0,0,1,0]
        elif bowling_team == 'Sunrisers Hyderabad':
            temp_array1 = temp_array1 + [0,0,0,0,0,0,0,1]
            
            
        overs = float(request.form['overs'])
        runs = int(request.form['runs'])
        wickets = int(request.form['wickets'])
        runs_in_prev_5 = int(request.form['runs_in_prev_5'])
        wickets_in_prev_5 = int(request.form['wickets_in_prev_5'])
        target = int(request.form['target'])
        
        temp_array1 = temp_array1 + [overs, runs, wickets, runs_in_prev_5, wickets_in_prev_5, target]
        
        # data = np.array([temp_array])
        # my_prediction = int(regressor.predict(data)[0])

        # prediction=lin.predict_proba([temp_array1])
        # output=int(prediction[0]*100)
        # data = np.array([temp_array])
        # my_prediction = (lin.predict(data)[0])
        print("hello")
        new_prediction = lin.predict_proba(sc.transform(np.array([temp_array1])))
        print("hello11")
        output = int(new_prediction[0][1]*100)
        print(output)
              
        return render_template('result1.html', team = batting_team, prob = output)


if __name__ == '__main__':
	app.run(debug=True)
