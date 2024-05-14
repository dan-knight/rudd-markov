import json
from pathlib import Path
import re
from typing import Any, cast

from markov.models.event import Event
from markov.models.team import Team


def load_events(path: Path) -> list[Event]:
    with open(path, mode='r') as file:
        json_events = json.load(file)

    if not isinstance(json_events, list):
        raise TypeError(f"Event data must be a list (received {type(json_events)}).")
    json_events = cast(list[Any], json_events)

    def parse_event_(json_event: Any) -> Event:
        if not isinstance(json_event, dict):
            raise TypeError(f"Event must be a dict (received {type(json_event)}).")
        return parse_json_event(cast(dict[str, Any],json_event))
    
    return [parse_event_(json_event) for json_event in json_events]

def parse_json_event(json_event: dict[str, Any]) -> Event:
    event_type = json_event.get("eventId")
    if not isinstance(event_type, int):
        raise TypeError(f"\"eventId\" must be an int (received {type(event_type)}).")
    
    match_id = json_event.get("matchId")
    if not isinstance(match_id, int):
        raise TypeError(f"\"matchId\" must be an int (received {type(match_id)}).")

    json_period: str = str(json_event.get("matchPeriod", ""))
    match_period = re.split("[a-zA-z]", json_period, maxsplit=1)[0]
    if match_period == "":
        raise ValueError(f"\"matchPeriod\" must contain an integer (received {match_period}).")
    match_period = int(match_period)
    
    json_match_second: Any = json_event.get("eventSec")
    try:
        match_second: float = float(json_match_second)
    except ValueError:
        raise ValueError(f"\"eventSecond\" must be a float (received {json_match_second}).")
    
    event_positions: Any = json_event.get("positions")
    if not isinstance(event_positions, list):
        raise TypeError(f"\"positions\" must be a list (received {type(event_positions)}).")
    event_positions = cast(list[Any], event_positions)
    if len(event_positions) == 0:
        raise ValueError("\"positions\" does not contain entries.")
    position = event_positions[0]
    if not isinstance(position, dict):
        raise TypeError(f"\"positions\" entries must be dicts (receieved {type(position)}).")
    position = cast(dict[str, Any], position)

    json_x: Any = position.get("x")
    try:
        x: float = float(json_x)
    except ValueError:
        raise ValueError(f"Position \"x\" must be a float (received {json_x}).")
    json_y: Any = position.get("y")
    try:
        y: float = float(json_y)
    except ValueError:
        raise ValueError(f"Position \"y\" must be a float (received {json_y}).")
    
    json_match_second: Any = json_event.get("eventSec")
    try:
        match_second: float = float(json_match_second)
    except ValueError:
        raise ValueError(f"\"eventSecond\" must be a float (received {json_match_second}).")

    
    return Event(
        event_type=event_type,
        match_id=match_id,
        period=match_period,
        match_second=match_second,
        x=x,
        y=y,
        team=Team(team_id=10)
    )
