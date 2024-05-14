from markov.models.team import Team


class Event:
    def __init__(self, team: Team) -> None:
        self.team: Team = team
