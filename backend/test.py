from sqlalchemy import create_engine, MetaData,Table
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:simple@localhost:3306/adp"

## Define the MySQL engine using MySQL Connector/Python
engine = create_engine(SQLALCHEMY_DATABASE_URL)
metadata = MetaData()

battles = Table('battles',metadata,autoload=True,autoload_with=engine)

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Table('battles', MetaData(bind=None), Column('name', VARCHAR(length=52), table=<battles>), Column('year', INTEGER(display_width=3), table=<battles>), Column('battle_number', INTEGER(display_width=2), table=<battles>), Column('attacker_king', VARCHAR(length=24), table=<battles>), Column('defender_king', VARCHAR(length=24), table=<battles>), Column('attacker_1', VARCHAR(length=27), table=<battles>), Column('attacker_2', VARCHAR(length=9), table=<battles>), Column('attacker_3', VARCHAR(length=7), table=<battles>), Column('attacker_4', VARCHAR(length=6), table=<battles>), Column('defender_1', VARCHAR(length=16), table=<battles>), Column('defender_2', VARCHAR(length=9), table=<battles>), Column('defender_3', VARCHAR(length=10), table=<battles>), Column('defender_4', VARCHAR(length=10), table=<battles>), Column('attacker_outcome', VARCHAR(length=4), table=<battles>), Column('battle_type', VARCHAR(length=14), table=<battles>), Column('major_death', INTEGER(display_width=1), table=<battles>), Column('major_capture', INTEGER(display_width=1), table=<battles>), Column('attacker_size', VARCHAR(length=6), table=<battles>), Column('defender_size', VARCHAR(length=5), table=<battles>), Column('attacker_commander', VARCHAR(length=95), table=<battles>), Column('defender_commander', VARCHAR(length=109), table=<battles>), Column('summer', VARCHAR(length=1), table=<battles>), Column('location', VARCHAR(length=36), table=<battles>), Column('region', VARCHAR(length=15), table=<battles>), Column('note', VARCHAR(length=257), table=<battles>), schema=None)
if __name__ == "__main__":
    names = session.query(battles).all()
    winner = session.query(battles).filter(battles.c.attacker_outcome == 'win').all()

    kings =  session.query(battles).distinct(battles.c.attacker_king).all()
    print(kings)






