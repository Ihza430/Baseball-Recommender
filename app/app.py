"""
Modified from Lesson 5.4
Inspired by https://briannalytle7.medium.com/reclassifying-nba-players-using-machine-learning-c2a316875fd1
"""

# Libraries Used
from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html')

@app.route('/result', methods=["GET", "POST"])

def player_submit():
    
    user_input = request.args
    
    name = user_input['PlayerName'].title()
    
    #Get names of recommended players
    players = pickle.load(open('../pickles/recommendation.pkl', 'rb'))
    players = players[name].sort_values()[1:11].index
    
    #Get file with player stats
    stats = pickle.load(open('../pickles/forecast.pkl', 'rb'))
    
    player_stats = stats[stats['name'] == name]
    
    player_stats = player_stats.values
    
    #Get salary based on forecasted stats
    salary = pickle.load(open('../pickles/pred_salary.pkl', 'rb'))
    
    player_salary = salary[salary.index == name]
    
    player_salary = round(player_salary['salary'][0], 2)
    
    related_players = []
    
    headings = stats.columns
    
    #Get name and salary of recommended players
    for player in players: 
        
        rec_salary = salary[salary.index == player]
        
        rec_salary = round(rec_salary['salary'][0], 2)
        
        info_player = stats[stats['name'] == player]
        
        info = info_player.values
        
        related_players.append({'name':player, 'salary': rec_salary, 'info':info})
    
    return render_template('results.html', PlayerName = name, playerStats = player_stats, playerSalary = player_salary, related_players = related_players, headings = headings)


@app.route('/table', methods=["GET", "POST"])

def table():
    
    #Get file with player stats
    data = pickle.load(open('../pickles/forecast.pkl', 'rb'))
    
    headings = data.columns.tolist()
    
    headings.append('salary')
    
    players = data['name']
    stats = []
    
    for player in players:
        info_player = data[data['name'] == player]
        
        info = info_player.values.tolist()
        
        #Get salary based on forecasted stats
        salary = pickle.load(open('../pickles/pred_salary.pkl', 'rb'))

        player_salary = salary[salary.index == player]
        
        player_salary = np.rint(player_salary['salary'].values)
        
        info[0].extend(player_salary)
        
        stats.append({'player': player, 'info':info})
        
    return render_template('table.html', headings = headings, players = players, stats=stats )



if __name__ == '__main__':
    app.run(host='localhost', port='5000', debug=True)