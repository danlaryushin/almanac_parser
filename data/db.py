from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from data.models import Base, Basket

engine = create_engine('sqlite:///basket.db', echo=False)
Base.metadata.create_all(engine)
session = Session(engine)


def create(info, start_params, live_params):
    obj = Basket(
        info['date'],
        info['league'],
        info['home_team'],
        info['away_team'],
        info['first_quater_home'],
        info['first_quater_away'],
        info['second_quater_home'],
        info['second_quater_away'],
        info['third_quater_home'],
        info['third_quater_away'],
        info['fourth_quater_home'],
        info['fourth_quater_away'],
        info['score_home'],
        info['score_away'],
        start_params['start_total'],
        start_params['kickoff_total'],
        start_params['start_handicap'],
        start_params['kickoff_handicap'],
        start_params['start_home_win'],
        start_params['kickoff_home_win'],
        start_params['start_away_win'],
        start_params['kickoff_away_win'],
        live_params['total'],
        live_params['over'],
        live_params['under'],
    )
    session.add(obj)
    session.commit()
