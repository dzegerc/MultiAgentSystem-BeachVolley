class BeachVolleyballEnvironment:
    def __init__(self, team_a="TeamA", team_b="TeamB", max_points_set=6):
        self.team_a = team_a
        self.team_b = team_b
        self.max_points_set = max_points_set  
        self.max_points_set_odlucujuci = 4   
        self.reset_round()
        self.score_team_a = 0
        self.score_team_b = 0
        self.sets_team_a = 0
        self.sets_team_b = 0

    def reset_round(self):
        self.ball_in_play = False
        self.phase = "SERVE"

    def reset_set(self):
        self.score_team_a = 0
        self.score_team_b = 0

    def update_score(self, team):
        if team == self.team_a:
            self.score_team_a += 1
        elif team == self.team_b:
            self.score_team_b += 1

    def print_score(self):
        print(f"Rezultat seta: {self.team_a} {self.score_team_a} - {self.team_b} {self.score_team_b}")
        print(f"Setovi: {self.team_a} {self.sets_team_a} - {self.team_b} {self.sets_team_b}")

    def check_set_winner(self):
        max_points = self.max_points_set
        if self.sets_team_a == 1 and self.sets_team_b == 1:
            max_points = self.max_points_set_odlucujuci
        if (self.score_team_a >= max_points or self.score_team_b >= max_points):
            if abs(self.score_team_a - self.score_team_b) >= 2:
                return self.team_a if self.score_team_a > self.score_team_b else self.team_b
        return None

    def get_match_winner(self):
        if self.sets_team_a >= 2:
            return self.team_a
        elif self.sets_team_b >= 2:
            return self.team_b
        return None
