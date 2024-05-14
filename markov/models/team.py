from dataclasses import dataclass


@dataclass(frozen=True)
class Team:
    team_id: int
