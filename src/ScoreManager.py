class ScoreManager(object):
    def __init__(self, nb_players: int):
        self.nb_players = nb_players
        self.scores = dict.fromkeys(range(1, nb_players), 0)

    def add_score(self, player_key: str, points: int):
        self.scores[player_key] += points

    def get_score(self, player_key: str):
        return self.scores[player_key]

    def display_scoreboard(self):
        print("{:<8} {:<15}".format('Player', 'Score'))
        for player, score in self.scores.items():
            print("{:<8} {:<15}".format(player, score))
