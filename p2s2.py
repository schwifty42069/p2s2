import json
import requests
from bs4 import BeautifulSoup as Soup


class StatScraper(object):
    def __init__(self):
        self.website = "https://www.nfl.com/scores"
        self.sp_header = "\n| Team | Quarter | Type | Description |\n|:--:|:--:|:--:|:--|"
        self.sbq_header = "\n| Team | Q1 | Q2 | Q3 | Q4 | Total |\n|:--:|:--:|:--:|:--:|:--:|:--:|"
        self.box_header = "\n| Team | Penalties | Rushing Yards | Net Passing Yards | Scrim. Yards| Time of Possession " \
                          "| Turnovers |\n|:--:|:--:|:--:|:--:|:--:|:--:|:--:|"
        self.score_by_quarter = []
        self.scoring_plays = []
        self.box = []

    def get_recap_link(self):
        json_data = {}
        req = requests.get(self.website)
        bsoup = Soup(req.text, 'html.parser')
        for s in bsoup.findAll("script"):
            if "__INITIAL_DATA__" in s.text:
                json_data = json.loads(s.text.split("__INITIAL_DATA__ = ")[1].split(";\n")[0])
        for game in json_data['uiState']['scoreStripGames']:
            if not game['status']['isUpcoming'] and "patriots" in game['status']['gameLink']:
                return "https://www.nfl.com" + game['status']['gameLink']

    def get_game_json(self):
        req = requests.get(self.get_recap_link())
        bsoup = Soup(req.text, 'html.parser')
        for s in bsoup.findAll("script"):
            if "__INITIAL_DATA__" in s.text:
                return json.loads(s.text.split("__INITIAL_DATA__ = ")[1].split(";\n")[0])

    def fetch_scoring_plays(self):
        sp_json = self.get_game_json()
        score_type = ''
        for p in sp_json['instance']['gameDetails']['plays']:
            if p['scoringPlay'] and p['playType'] != "XP_KICK":
                if "TOUCHDOWN" in p['shortDescription']:
                    score_type = "TD"
                elif "FIELD GOAL" in p['shortDescription']:
                    score_type = "FG"
                elif "SAFETY" in p['shortDescription']:
                    score_type = "SAFETY"
                self.format_scoring_plays(p['scoringTeam']['nickName'], p['quarter'], score_type, p['shortDescription'])
        return

    def fetch_score_by_quarter(self):
        sbq_json = self.get_game_json()
        vt = sbq_json['instance']['gameDetails']['visitorTeam']['nickName']
        ht = sbq_json['instance']['gameDetails']['homeTeam']['nickName']
        vt_q1 = sbq_json['instance']['gameDetails']['visitorPointsQ1']
        vt_q2 = sbq_json['instance']['gameDetails']['visitorPointsQ2']
        vt_q3 = sbq_json['instance']['gameDetails']['visitorPointsQ3']
        vt_q4 = sbq_json['instance']['gameDetails']['visitorPointsQ4']
        vt_total = sbq_json['instance']['gameDetails']['visitorPointsTotal']
        ht_q1 = sbq_json['instance']['gameDetails']['homePointsQ1']
        ht_q2 = sbq_json['instance']['gameDetails']['homePointsQ2']
        ht_q3 = sbq_json['instance']['gameDetails']['homePointsQ3']
        ht_q4 = sbq_json['instance']['gameDetails']['homePointsQ4']
        ht_total = sbq_json['instance']['gameDetails']['homePointsTotal']
        self.format_score_by_quarter(vt, vt_q1, vt_q2, vt_q3, vt_q4, vt_total)
        self.format_score_by_quarter(ht, ht_q1, ht_q2, ht_q3, ht_q4, ht_total)
        return

    def fetch_box(self):
        box_json = self.get_game_json()
        keys = ['awayTeamStats', 'homeTeamStats']
        for key in keys:
            team = box_json['instance']['teamStats'][key][0]['team']['abbreviation']
            pens = box_json['instance']['teamStats'][key][0]['teamGameStats']['penaltiesTotal']
            rush_yds = box_json['instance']['teamStats'][key][0]['teamGameStats']['rushingYards']
            pass_yds = box_json['instance']['teamStats'][key][0]['teamGameStats']['passingNetYards']
            scrm_yds = box_json['instance']['teamStats'][key][0]['teamGameStats']['scrimmageYds']
            top = "{}:{}".format(int(str(float(box_json['instance']['teamStats'][key][0]['teamGameStats']['timeOfPossSeconds']) / 60)
                                     .split(".")[0]), str(float(str(float(box_json['instance']['teamStats']['awayTeamStats'][0]['teamGameStats']['timeOfPossSeconds']) / 60)
                                                                .split(".")[1]) * 6).split(".")[0])
            turnovers = "{}".format(int(box_json['instance']['teamStats'][key][0]['teamGameStats']['passingInterceptions'])
                                    + int(box_json['instance']['teamStats'][key][0]['teamGameStats']['fumblesLost']))
            self.format_box(team, pens, rush_yds, pass_yds, scrm_yds, top, turnovers)

    def get_title_info(self):
        title_json = self.get_game_json()
        teams_title = "#{} at {}\n\n".format(title_json['instance']['game']['awayTeam']['fullName'],
                                             title_json['instance']['game']['homeTeam']['fullName'])
        start_date = "{} Eastern".format(input("\nEnter game date and time:\n"))
        return "{}{} - {}\n***".format(teams_title, title_json['instance']['gameDetails']['stadium'], start_date)

    def format_scoring_plays(self, team, q, play_type, desc):
        self.scoring_plays.append('| {} | {} | {} | {} |'.format(team, q, play_type, desc))

    def format_score_by_quarter(self, team, q1, q2, q3, q4, total):
        self.score_by_quarter.append("| {} | {} | {} | {} | {} | {} |".format(team, q1, q2, q3, q4, total))

    def format_box(self, team, penalties, rush_yds, net_pass_yds, scrm_yds, top, turnovers):
        self.box.append("| {} | {} | {} | {} | {} | {} | {} |".format(team, penalties, rush_yds, net_pass_yds,
                                                                      scrm_yds, top, turnovers))


def main():
    ss = StatScraper()
    ss.fetch_score_by_quarter()
    ss.fetch_scoring_plays()
    ss.fetch_box()
    print("\n" + ss.get_title_info())
    print(ss.sbq_header)
    for s in ss.score_by_quarter:
        print(s)
    print("\n**Scoring Plays**\n")
    print(ss.sp_header)
    for s in ss.scoring_plays:
        print(s)
    print(ss.box_header)
    for s in ss.box:
        print(s)


if __name__ in "__main__":
    main()
