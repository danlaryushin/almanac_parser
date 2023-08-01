import requests

from settings import BETS_API_TOKEN, URL_LIVE


def parse_live(game_id):
    headers = {'token': {BETS_API_TOKEN}, 'evend_id': game_id}
    response = requests.get(URL_LIVE, headers=headers).json()
    bet = response['results']['odds']['18_3']
    try:
        total = float(
            [
                i['handicap']
                for i in bet
                if (i['time_str'] is not None and i['time_str'][0] == '2')
            ][0]
        )
    except KeyError:
        total = None
    try:
        over = float(
            [
                i['over_od']
                for i in bet
                if (i['time_str'] is not None and i['time_str'][0] == '2')
            ][0]
        )
    except KeyError:
        over = None
    try:
        under = float(
            [
                i['under_od']
                for i in bet
                if (i['time_str'] is not None and i['time_str'][0] == '2')
            ][0]
        )
    except KeyError:
        under = None

    live_params = {
        'total': total,
        'over': over,
        'under': under,
    }
    return live_params
