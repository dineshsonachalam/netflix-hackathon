from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.pool import NullPool
from sqlalchemy.orm import sessionmaker
import json

SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:simple@mysql:3306/adp"

if __name__ == "__main__":
    # Define the MySQL engine using MySQL Connector/Python
    db = create_engine(SQLALCHEMY_DATABASE_URL, poolclass=NullPool)
    metadata = MetaData()

    battles = Table('battles', metadata, autoload=True, autoload_with=db)

    session = sessionmaker(bind=db)
    session = session()

    battle_info = session.query(battles).with_entities(battles.c.attacker_king, battles.c.defender_king,
                                                        battles.c.attacker_outcome, battles.c.year).all() 

    print("Battle info: ",battle_info)