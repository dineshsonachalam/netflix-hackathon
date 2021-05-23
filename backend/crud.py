from sqlalchemy import create_engine, MetaData, Table, func, text, inspect
from sqlalchemy.pool import NullPool
from sqlalchemy.orm import sessionmaker
from elo import Rating
import json

SQLALCHEMY_DATABASE_URL = "postgresql://dinesh:simple@postgres:5432/dinesh-micro-apps"

def get_sql_session():
    # Define the Postgres engine using Postgres Connector/Python
    db = create_engine(SQLALCHEMY_DATABASE_URL, poolclass=NullPool)
    metadata = MetaData()
    table = Table('battles', metadata, autoload=True, autoload_with=db)  
    session = sessionmaker(bind=db)
    session = session()
    return table, session

def check_if_table_exists():
    try:
        table = 'adult'
        db = create_engine(SQLALCHEMY_DATABASE_URL, poolclass=NullPool)
        return inspect(db).has_table(table)
    except Exception as e:
        print("Exception: ", e)

def check_if_table_is_empty():
    try:
        table, session = get_sql_session()
        table_count = session.query(table).count()
        if table_count>1:
            return False
        else:
            return True
    except Exception as e:
        print("Exception: ", e)

def execute_sql_file():
    if((check_if_table_exists() == False) or (check_if_table_is_empty() == True)):
        db = create_engine(SQLALCHEMY_DATABASE_URL, poolclass=NullPool)
        file = open("./adp.sql")
        query = text(file.read())
        session = sessionmaker(bind=db)
        session = session()
        session.execute(query)

def get_battle_statistics():
    # Define the Postgres engine using Postgres Connector/Python
    db = create_engine(SQLALCHEMY_DATABASE_URL, poolclass=NullPool)
    metadata = MetaData()

    battles = Table('battles', metadata, autoload=True, autoload_with=db)

    session = sessionmaker(bind=db)
    session = session()
    try:
        battle_info = session.query(battles).with_entities(battles.c.attacker_king, battles.c.defender_king,
                                                        battles.c.attacker_outcome, battles.c.year).all()                                              
        battle_stats = {}
        battle_details = {}
        battle_details["info"] = []
        battle_details["win_loss_data"] = [] 
        for attacker_king, defender_king, attacker_outcome, year in battle_info:
            if attacker_king == defender_king:
                continue
            if battle_stats.get(attacker_king) is None:
                battle_stats[attacker_king] = {}
                battle_stats[attacker_king]["win_loss_stats"] = []
            if battle_stats.get(defender_king) is None:
                battle_stats[defender_king] = {}
                battle_stats[defender_king]["win_loss_stats"] = []
                
            if battle_stats.get(attacker_king).get('rating') is None:
                attacker_rating = 1000
            else:
                attacker_rating = battle_stats.get(attacker_king).get('rating')

            if battle_stats.get(defender_king).get('rating') is None:
                defender_rating = 1000
            else:
                defender_rating = battle_stats.get(defender_king).get('rating')

            
            
            attacker_rating, defender_rating = Rating(attacker_rating, defender_rating, attacker_outcome).find_rating()
            attacker_rating = round(attacker_rating, 5)
            defender_rating = round(defender_rating, 5)

            

            
            attacker_king_battle_details = battle_stats.get(attacker_king).get('battle_details', [])
            defender_king_battle_details = battle_stats.get(defender_king).get('battle_details', [])

            attacker_king_rating_info = battle_stats.get(attacker_king).get('rating_info', [])
            defender_king_rating_info = battle_stats.get(defender_king).get('rating_info', [])

            if len(attacker_outcome) > 0 and attacker_outcome == "win":
                attacker_king_battle_details.append({
                    "key": battle_stats.get(attacker_king).get('battles', 0) + 1,
                    "year": year,
                    "role": "Attacker",
                    "opponent": defender_king,
                    "battle_outcome": "Win",
                    "rating": attacker_rating
                })
                defender_king_battle_details.append({
                    "key": battle_stats.get(defender_king).get('battles', 0) + 1,
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
                    "rating": attacker_rating,
                    "battle_details": attacker_king_battle_details
                }

                battle_stats[defender_king] = {
                    "wins": battle_stats.get(defender_king).get('wins', 0),
                    "battles": battle_stats.get(defender_king).get('battles', 0) + 1,
                    "loss": battle_stats.get(defender_king).get('loss', 0) + 1,
                    "rating": defender_rating,
                    "battle_details": defender_king_battle_details
                }
            elif len(attacker_outcome) > 0 and attacker_outcome == "loss":
                attacker_king_battle_details.append({
                    "key": battle_stats.get(attacker_king).get('battles', 0) + 1,
                    "year": year,
                    "role": "Attacker",
                    "opponent": defender_king,
                    "battle_outcome": "Loss",
                    "rating": attacker_rating
                })
                defender_king_battle_details.append({
                    "key": battle_stats.get(defender_king).get('battles', 0) + 1,
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
                    "rating": attacker_rating,
                    "battle_details": attacker_king_battle_details
                }
                battle_stats[defender_king] = {
                    "wins": battle_stats.get(defender_king).get('wins', 0) + 1,
                    "battles": battle_stats.get(defender_king).get('battles', 0) + 1,
                    "loss": battle_stats.get(defender_king).get('loss', 0),
                    "rating": defender_rating,
                    "battle_details": defender_king_battle_details
                }
            attacker_winning_percentage = ((battle_stats.get(attacker_king).get('wins')/battle_stats.get(attacker_king).get('battles'))*100)
            attacker_lose_percentage = 100 - attacker_winning_percentage
            defender_winning_percentage = ((battle_stats.get(defender_king).get('wins')/battle_stats.get(defender_king).get('battles'))*100)
            defender_lose_percentage = 100 -  defender_winning_percentage
            battle_stats[attacker_king]["win_loss_stats"] = [
                {
                "type": 'Win',
                "value": round(attacker_winning_percentage,5),
                },
                {
                "type": 'Loss',
                "value": round(attacker_lose_percentage,5),
                }
            ]
            battle_stats[defender_king]["win_loss_stats"] = [
                {
                "type": 'Win',
                "value": round(defender_winning_percentage, 5),
                },
                {
                "type": 'Loss',
                "value": round(defender_lose_percentage, 5),
                }
            ]
            
        

            attacker_king_rating_info.append({
                    "battle": battle_stats.get(attacker_king).get('battles'),
                    "rating": battle_stats.get(attacker_king).get('rating')
            })
            defender_king_rating_info.append({
                    "battle": battle_stats.get(defender_king).get('battles'),
                    "rating": battle_stats.get(defender_king).get('rating')
            })
            battle_stats[attacker_king]["rating_info"] = attacker_king_rating_info
            battle_stats[defender_king]["rating_info"] = defender_king_rating_info
        if battle_stats.get(''):
            battle_stats.pop('')

        key = 1
        
        for king, _ in battle_stats.items():
            battle_info = {
                "key": key,
                "king": king,
                "rating":  battle_stats.get(king).get("rating"),
                "wins": battle_stats.get(king).get("wins"),
                "loss": battle_stats.get(king).get("loss"),
                "battles": battle_stats.get(king).get("battles")
            }
            battle_details["win_loss_data"].append({
                "name": "Total Battles",
                "king": king,
                "value": battle_stats.get(king).get("battles")
            })
            battle_details["win_loss_data"].append({
                "name": "Total Wins",
                "king": king,
                "value": battle_stats.get(king).get("wins")
            })
            battle_details["win_loss_data"].append({
                "name": "Total Loss",
                "king": king,
                "value": battle_stats.get(king).get("loss")
            })

            battle_details["info"].append(battle_info)
            key = key + 1
        
        
        king_battles_rating = sorted(battle_details.get("info"), key=lambda k: k['rating'], reverse=True)
        king_updated_rating = []
        rank = 1
        for king_battle_rating in king_battles_rating:
            king_battle_rating["rank"] = rank
            rank = rank + 1
            king_updated_rating.append(king_battle_rating)

        battle_details["info"] = king_updated_rating
        
        battle_details["stats"] = battle_stats
        return json.dumps(battle_details)
    except Exception as e:
        session.rollback()

