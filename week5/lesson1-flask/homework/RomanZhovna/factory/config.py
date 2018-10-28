import json


class Config:
    DB = {}


class DevConfig(Config):
    DB = {
            "Player1": {"Full_name": "Full name Player1", "Age": "20", "Club": "Club1"},
            "Player2": {"Full_name": "Full name Player2", "Age": "20", "Club": "Club2"},
            "Player3": {"Full_name": "Full name Player3", "Age": "20", "Club": "Club3"},
     }


class TestConfig(Config):
    DB = {
            "Rooney": {"Full_name": "Wayne Mark Rooney", "Age": "32", "Club": "DC"},
            "Ibrahimovic": {"Full_name": "Zlatan Ibrahimovic", "Age": "37", "Club": "LA Galaxy"},
            "Messi": {"Full_name": "Lionel Messi", "Age": "31", "Club": "Barcelona"},
        }
    NEWS = [
                {
                    "Image": "static/calco.png",
                    "Title": "AC Milan: Gennaro Gattuso 'baffled' by performance against Real Betis",
                    "Text": "AC Milan boss Gennaro Gattuso accepts his job should be debated after they produced a 'terrible, embarrassing performance' against Real Betis"},
                {
                    "Image": "static/bundesliga.png",
                    "Title": "Borussia Dortmund: Is this their year to end Bayern Munich's reign?",
                    "Text": "Borussia Dortmund are one of Europe's top sides after an electrifying start to the season - unbeaten in 12 games in all competitions."},
                {
                    "Image": "static/england_league.png",
                    "Title": "Hugo Lloris: Spurs boss Mauricio Pochettino backs under-fire goalkeeper",
                    "Text": "Mauricio Pochettino has backed Tottenham keeper Hugo Lloris, saying 'we have short memories in football'."},
                {
                    "Image": "static/england_league.png",
                    "Title": "Tottenham matches to be played at Wembley until end of year",
                    "Text": "Tottenham will continue playing games at Wembley until the end of this year. Their new 62,000-seat arena was supposed to open on 15 September but safety concerns led to a delay."},
            ]


def runtime_config():
    with open("settings.json", "r") as f:
        settings = json.load(f)
        if settings['env'] == "DEV":
            return DevConfig
        if settings['env'] == "TEST":
            return TestConfig
        else:
            return Config
