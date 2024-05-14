import json
from pathlib import Path
from typing import Any, cast

from markov.models.event import Event


def load_events(path: Path) -> list[Event]:
    with open(path, mode='r') as file:
        json_events = json.load(file)

    if not isinstance(json_events, list):
        raise TypeError(f"Event data must be a list (received {type(json_events)}).")
    json_events = cast(list[Any], json_events)

    def parse_event_(json_event: Any) -> Event:
        if not isinstance(json_event, dict):
            raise TypeError(f"Event must be a dict (received {type(json_events)}).")
        return parse_json_event(cast(dict[str, Any],json_event))
    
    return [parse_event_(json_event) for json_event in json_events[:5]]

def parse_json_event(json_event: dict[str, Any]) -> Event:
    pass

