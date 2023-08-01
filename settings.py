import os

from dotenv import load_dotenv

load_dotenv('.env')

PAGE = 1
SPORT_ID = '18'
MAX_PAGE = 35
MAX_COUNT = 999
TIME_LIMIT = 1630454400
RETRY_TIME = 60
FORMAT = '%Y-%m-%d'
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOG_FILE = 'main.log'
BETS_API_TOKEN = os.getenv('BETS_API_TOKEN')
MAIN_URL = os.getenv('MAIN_URL')
URL_LIVE = os.getenv('URL_LIVE')
URL_PREMATCH = os.getenv('URL_PREMATCH')
LEAGUES = [os.getenv('LEAGUES')]
