from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    # path = "mysql+mysqldb://{}:{}@localhost/{}".format(
    #     argv[1],
    #     argv[2],
    #     argv[3])

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        argv[1],
        argv[2],
        argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)

    state_list = session.query(State).order_by(State.id).first()

    if state_list:
        print("{}: {}".format(state_list.id, state_list.name))
    else:
        print("Nothing")
    session.close()
