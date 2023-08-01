import logging
from datetime import datetime as dt
from time import sleep

import requests

from data.db import create
from parse_game.live_odds import parse_live
from parse_game.start_odds import parse_start
from settings import (BETS_API_TOKEN, FORMAT, LOG_FILE, LOG_FORMAT, MAIN_URL,
                      MAX_COUNT, MAX_PAGE, PAGE, RETRY_TIME, SPORT_ID,
                      TIME_LIMIT)

logging.basicConfig(
    format=LOG_FORMAT,
    level=logging.INFO,
    filename=LOG_FILE,
    filemode='a',
    encoding='utf-8',
)


def match_info(league_id):
    global PAGE
    count = 0
    while PAGE <= MAX_PAGE or count <= MAX_COUNT:
        headers = {
            'sport_id': SPORT_ID,
            'skip_esports': 'True',
            'league_id': league_id,
            'page': str(PAGE),
            'token': BETS_API_TOKEN,
        }
        try:
            response = requests.get(MAIN_URL, headers=headers).json()
        except Exception as error:
            logging.error(f'Проблемы с соединением: {error}', exc_info=True)
            sleep(RETRY_TIME)
            continue
        if response['success'] == 1:
            for key in response['results']:
                game_id = key['id']
                match_time = dt.fromtimestamp(int(key['time']))
                end = int(key['time'])
                if end < TIME_LIMIT:
                    break
                status = key['time_status']
                score = key['ss']
                if score is None:
                    count += 1  # Игра не завершена
                    logging.info(f'Пропущен матч. Статус {status}')
                    continue
                try:
                    match_info = {
                        'date': match_time.strftime(FORMAT),
                        'league': key['league']['name'],
                        'home_team': key['home']['name'],
                        'away_team': key['away']['name'],
                        'first_quater_home': int(key['scores']['1']['home']),
                        'first_quater_away': int(key['scores']['1']['away']),
                        'second_quater_home': int(key['scores']['2']['home']),
                        'second_quater_away': int(key['scores']['2']['away']),
                        'third_quater_home': int(key['scores']['4']['home']),
                        'third_quater_away': int(key['scores']['4']['away']),
                        'fourth_quater_home': int(key['scores']['5']['home']),
                        'fourth_quater_away': int(key['scores']['5']['away']),
                        'score_home': int(key['scores']['7']['home']),
                        'score_away': int(key['scores']['7']['away']),
                    }
                except KeyError:
                    match_info = None
                if match_info is not None:
                    start_params = parse_start(game_id)
                    live_params = parse_live(game_id)
                else:
                    continue
                count += 1
                create(match_info, start_params, live_params)
            PAGE += 1
            print(PAGE)
        else:
            logging.info('Проблемы с авторизацией')
            return
