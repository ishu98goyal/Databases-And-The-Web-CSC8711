import pymongo
from pymongo import MongoClient
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

client = MongoClient()
db = client.baseballDB

@app.route('/baseball/standings/')
def standings():
    standings = []
    for i in db.teams.find():
        wins, loss, tie = 0, 0, 0
        for j in db.games.find({'$or': [{'visit_team': i['_id']}, {'home_team': i['_id']}] }):
            if j['visit_team'] == i['_id']:
                if j['visit_score'] > j['home_score']:
                    wins += 1
                elif j['visit_score'] < j['home_score']:
                    loss += 1
                else:
                    tie += 1
            else:
                if j['visit_score'] > j['home_score']:
                    loss += 1
                elif j['visit_score'] < j['home_score']:
                    wins += 1
                else:
                    tie += 1
        l = {'losses': loss, 'percent': round(float((float(wins) + 0.5 * tie) / float(wins + loss + tie)), 3),
             'tcode': i['_id'], 'ties': tie, 'tname': i['tname'], 'wins': wins}
        standings.append(l)
    return jsonify({'standings': standings})

@app.route('/baseball/results/<string:tcode>/')
def results(tcode):
    results = []
    for j in db.games.find({'$or': [{'visit_team': tcode}, {'home_team': tcode}]}).sort([('gdate', 1)]):
        if j['visit_team'] == tcode:
            r = "WIN" if j['visit_score'] > j['home_score'] else "LOSS" if j['visit_score'] < j['home_score'] else "TIE"
            l = {'gdate': j['gdate'], 'opponent': "at " + j['home_team'], 'result': r, 'them': j['home_score'], 'us': j['visit_score']}
        else:
            r = "LOSS" if j['visit_score'] > j['home_score'] else "WIN" if j['visit_score'] < j['home_score'] else "TIE"
            l = {'gdate': j['gdate'], 'opponent': j['visit_team'], 'result': r, 'them': j['visit_score'], 'us': j['home_score']}
        results.append(l)
    tloc = db.teams.find({'_id': tcode}, {"tlocation": 1})[0]['tlocation']
    tname = db.teams.find({'_id': tcode}, {"tname": 1})[0]['tname']
    return jsonify({'results': results, 'tloc': tloc, 'tname': tname})

if __name__ == '__main__':
    app.run(debug=True)
