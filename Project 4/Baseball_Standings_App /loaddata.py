import sys
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient()

# Drop any existing data and create the database and collections
client.drop_database('baseballDB')
db = client['baseballDB']
teams_col = db['teams']
games_col = db['games']

# Load teams data
with open(sys.argv[1]) as f:
    for line in f:
        team_info = line.strip().split(':')
        team = {
            '_id': team_info[2],
            'tname': team_info[0],
            'tlocation': team_info[1]
        }
        # Insert team only if tcode is not already in the database
        if not teams_col.find_one({'_id': team['_id']}):
            teams_col.insert_one(team)

# Load games data
with open(sys.argv[2]) as f:
    for line in f:
        game_info = line.strip().split(':')
        game = {
            'gdate': game_info[0],
            'visit_team': game_info[1],
            'home_team': game_info[2],
            'visit_score': int(game_info[3]),
            'home_score': int(game_info[4])
        }
        # Only insert game if both teams are in the teams collection
        visit_team = teams_col.find_one({'_id': game['visit_team']})
        home_team = teams_col.find_one({'_id': game['home_team']})
        if visit_team and home_team:
            games_col.insert_one(game)
