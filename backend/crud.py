from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker
from elo import Rating
import json

SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:simple@127.0.0.1:3306/adp"

# Define the MySQL engine using MySQL Connector/Python
engine = create_engine(SQLALCHEMY_DATABASE_URL)
metadata = MetaData()

battles = Table('battles', metadata, autoload=True, autoload_with=engine)

DBSession = sessionmaker(bind=engine)
session = DBSession()


def get_battle_statistics():
    battle_info = session.query(battles).with_entities(battles.c.attacker_king, battles.c.defender_king,
                                                       battles.c.attacker_outcome, battles.c.year).all()
    battle_stats = {}
    for attacker_king, defender_king, attacker_outcome, year in battle_info:
        if battle_stats.get(attacker_king) is None:
            battle_stats[attacker_king] = {}
        if battle_stats.get(defender_king) is None:
            battle_stats[defender_king] = {}

        if battle_stats.get(attacker_king).get('ratings') is None:
            attacker_rating = 1000
        else:
            attacker_rating = battle_stats.get(attacker_king).get('ratings')

        if battle_stats.get(defender_king).get('ratings') is None:
            defender_rating = 1000
        else:
            defender_rating = battle_stats.get(defender_king).get('ratings')

        attacker_rating, defender_rating = Rating(attacker_rating, defender_rating, attacker_outcome).find_rating()

        
        attacker_king_battle_details = battle_stats.get(attacker_king).get('battle_details', [])
        defender_king_battle_details = battle_stats.get(defender_king).get('battle_details', [])
        

        if len(attacker_outcome) > 0 and attacker_outcome == "win":
            attacker_king_battle_details.append({
                "year": year,
                "role": "Attacker",
                "opponent": defender_king,
                "battle_outcome": "Win",
                "rating": attacker_rating
            })
            defender_king_battle_details.append({
                "year": year,
                "role": "Defender",
                "opponent": attacker_king,
                "battle_outcome": "Loss",
                "rating": defender_rating
            })
            
            battle_stats[attacker_king] = {
                "wins": battle_stats.get(attacker_king).get('wins', 0) + 1,
                "battles": battle_stats.get(attacker_king).get('battles', 0) + 1,
                "loss": battle_stats.get(attacker_king).get('loss', 0),
                "ratings": attacker_rating,
                "battle_details": attacker_king_battle_details
            }

            battle_stats[defender_king] = {
                "wins": battle_stats.get(defender_king).get('wins', 0),
                "battles": battle_stats.get(defender_king).get('battles', 0) + 1,
                "loss": battle_stats.get(defender_king).get('loss', 0) + 1,
                "ratings": defender_rating,
                "battle_details": defender_king_battle_details
            }
        elif len(attacker_outcome) > 0 and attacker_outcome == "loss":
            attacker_king_battle_details.append({
                "year": year,
                "role": "Attacker",
                "opponent": defender_king,
                "battle_outcome": "Loss",
                "rating": attacker_rating
            })
            defender_king_battle_details.append({
                "year": year,
                "role": "Defender",
                "opponent": attacker_king,
                "battle_outcome": "Win",
                "rating": defender_rating
            })
            battle_stats[attacker_king] = {
                "wins": battle_stats.get(attacker_king).get('wins', 0),
                "battles": battle_stats.get(attacker_king).get('battles', 0) + 1,
                "loss": battle_stats.get(attacker_king).get('loss', 0) + 1,
                "ratings": attacker_rating,
                "battle_details": attacker_king_battle_details
            }
            battle_stats[defender_king] = {
                "wins": battle_stats.get(defender_king).get('wins', 0) + 1,
                "battles": battle_stats.get(defender_king).get('battles', 0) + 1,
                "loss": battle_stats.get(defender_king).get('loss', 0),
                "ratings": defender_rating,
                "battle_details": defender_king_battle_details
            }

    if battle_stats.get(''):
        battle_stats['Unknown'] = battle_stats.pop('')

    return json.dumps(battle_stats)
