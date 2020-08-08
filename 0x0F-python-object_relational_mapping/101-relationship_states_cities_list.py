#!/usr/bin/python3
"""Module."""
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

from relationship_state import State
from relationship_city import Base, City


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id)
    for s in states:
        print("{}: {}".format(s.id, s.name))
        for c in s.cities:
            print("\t{}: {}".format(c.id, c.name))
    session.close()
