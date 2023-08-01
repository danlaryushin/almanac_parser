import requests

from settings import BETS_API_TOKEN, URL_PREMATCH


def parse_start(game_id):
    headers = {'token': {BETS_API_TOKEN}, 'evend_id': game_id}
    response = requests.get(URL_PREMATCH, headers=headers).json()
    try:
        start_total = float(
            response['results']['Bet365']['odds']['start']['18_3']['handicap']
        )
    except KeyError:
        start_total = None
    try:
        kickoff_total = float(
            response['results']['Bet365']['odds']['kickoff']['18_3']['handicap']
        )
    except KeyError:
        kickoff_total = None
    try:
        start_handicap = float(
            response['results']['Bet365']['odds']['start']['18_2']['handicap']
        )
    except KeyError:
        start_handicap = None
    try:
        kickoff_handicap = float(
            response['results']['Bet365']['odds']['kickoff']['18_2']['handicap']
        )
    except KeyError:
        kickoff_handicap = None
    try:
        start_home_win = float(
            response['results']['Bet365']['odds']['start']['18_1']['home_od']
        )
        start_away_win = float(
            response['results']['Bet365']['odds']['start']['18_1']['away_od']
        )
    except KeyError:
        start_home_win = None
        start_away_win = None
    try:
        kickoff_home_win = float(
            response['results']['Bet365']['odds']['kickoff']['18_1']['home_od']
        )
        kickoff_away_win = float(
            response['results']['Bet365']['odds']['kickoff']['18_1']['away_od']
        )
    except KeyError:
        kickoff_home_win = None
        kickoff_away_win = None

    start_params = {
        'start_total': start_total,
        'kickoff_total': kickoff_total,
        'start_handicap': start_handicap,
        'kickoff_handicap': kickoff_handicap,
        'start_home_win': start_home_win,
        'kickoff_home_win': kickoff_home_win,
        'start_away_win': start_away_win,
        'kickoff_away_win': kickoff_away_win,
    }
    return start_params
