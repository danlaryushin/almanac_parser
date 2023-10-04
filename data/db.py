from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from data.models import Base, Basket


engine = create_engine('sqlite:///basket.db', echo=False)
Base.metadata.create_all(engine)
session = Session(engine)


def create(info, start_params, live_params):
    match = Basket(
        date = info['date'],
        league = info['league'],
        home_team = info['home_team'],
        away_team = info['away_team'],
        start_home_win =  start_params['start_home_win'],
        start_away_win =  start_params['start_away_win'],
        kickoff_home_win =  start_params['kickoff_home_win'],
        kickoff_away_win =  start_params['kickoff_away_win'],
        start_handicap =  start_params['start_handicap'],
        kickoff_handicap =  start_params['kickoff_handicap'],
        start_total  =  start_params['start_total'],
        kickoff_total  =  start_params['kickoff_total'],
        first_quater_home  = info['first_quater_home'],
        first_quater_away  = info['first_quater_away'],
        second_quater_home =  info['second_quater_home'],
        second_quater_away =  info['second_quater_away'],
        third_quater_home  =  info['third_quater_home'],
        third_quater_away  =  info['third_quater_away'],
        fourth_quater_home =  info['fourth_quater_home'],
        fourth_quater_away =  info['fourth_quater_away'],
        score_home = info['score_home'],
        score_away = info['score_away'],
        total = live_params['total'],
        over  = live_params['over'],
        under = live_params['under'],
    )
    session.add(match)
    session.commit()

create()
