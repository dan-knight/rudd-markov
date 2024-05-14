from dataclasses import dataclass
from enum import IntEnum
from markov.models.team import Team


class EventType(IntEnum):
    PASS = 8


@dataclass(frozen=True)
class PitchLocation:
    x: float
    y: float


@dataclass(frozen=True)
class MatchTime:
    period: int
    match_second: float


class Event:
    def __init__(
        self,
        event_type: int,
        match_id: int,
        period: int,
        match_second: float,
        x: float,
        y: float,
        team: Team
    ) -> None:
        self.event_type: int = event_type
        self.match_id: int = match_id
        self.match_time: MatchTime = MatchTime(
            period=period,
            match_second=match_second
        )
        self.team: Team = team
        self.location: PitchLocation = PitchLocation(x=x, y=y)
