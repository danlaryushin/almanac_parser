from parse_game.match_info import match_info
from settings import LEAGUES


def main():
    for league_id in LEAGUES:
        match_info(league_id)


if __name__ == "__main__":
    main()
