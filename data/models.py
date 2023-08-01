from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import declarative_base, declared_attr


class Base:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()


Base = declarative_base(cls=Base)


class Basket(Base):
    id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    league = Column(String)
    home_team = Column(String)
    away_team = Column(String)
    start_home_win = Column(Integer)
    start_away_win = Column(Integer)
    kickoff_home_win = Column(Integer)
    kickoff_away_win = Column(Integer)
    start_handicap = Column(Integer)
    kickoff_handicap = Column(Integer)
    start_total = Column(Integer)
    kickoff_total = Column(Integer)
    first_quater_home = Column(Integer)
    first_quater_away = Column(Integer)
    second_quater_home = Column(Integer)
    second_quater_away = Column(Integer)
    third_quater_home = Column(Integer)
    third_quater_away = Column(Integer)
    fourth_quater_home = Column(Integer)
    fourth_quater_away = Column(Integer)
    score_home = Column(Integer)
    score_away = Column(Integer)
    total = Column(Integer)
    over = Column(Integer)
    under = Column(Integer)

    def __repr__(self):
        return f'Game {self.league}: {self.home_team} - {self.away_team}'
