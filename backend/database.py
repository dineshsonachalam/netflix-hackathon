from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sqlalchemy

SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:simple@localhost:3306/adp"

## Define the MySQL engine using MySQL Connector/Python
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

Base = declarative_base(engine)



class Places(Base):
    """"""
    __tablename__ = 'battles'

    id = Column(Integer, primary_key=True)
    url = Column(String)
    title = Column(String)
    rev_host = Column(String)
    visit_count = Column(Integer)
    hidden = Column(Integer)
    typed = Column(Integer)
    favicon_id = Column(Integer)
    frecency = Column(Integer)
    last_visit_date = Column(Integer)

    # ----------------------------------------------------------------------
    def __init__(self, id, url, title, rev_host, visit_count,
                 hidden, typed, favicon_id, frecency, last_visit_date):
        """"""
        self.id = id
        self.url = url
        self.title = title
        self.rev_host = rev_host
        self.visit_count = visit_count
        self.hidden = hidden
        self.typed = typed
        self.favicon_id = favicon_id
        self.frecency = frecency
        self.last_visit_date = last_visit_date

    # ----------------------------------------------------------------------
    def __repr__(self):
        """"""
        return "<places -="" '%s':="" '%s'="">" % (self.id, self.title,
                                                   self.url)


# ----------------------------------------------------------------------
def loadSession():
    """"""
    metadata = Base.metadata
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


if __name__ == "__main__":
    session = loadSession()
    res = session.query(Places).all()
    print
    res[1].title

