#!/usr/bin/python3
"""Start link class to table in database
"""


import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine, join
from sqlalchemy.orm import Session


if __name__ == "__main__":
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                               .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                               pool_pre_ping=True)
        Base.metadata.create_all(engine)
        session = Session(engine)
        for res in session.query(State, City)\
                          .filter(State.id == City.state_id)\
                          .order_by(City.id).all():
                print("{}: ({}) {}".format(res.State.name,
                                           res.City.id, res.City.name))
        session.commit()
        session.close()
