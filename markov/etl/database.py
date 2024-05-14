from markov.models.event import Event
from markov.database.models.event import Event as DBEvent

def event_to_database(event: Event) -> DBEvent:
    return DBEvent(
        match_id=event.match_id,
        period=event.match_time.period,
        second=event.match_time.match_second,
        event_type=event.event_type,
        x=event.location.x,
        y=event.location.y
    )
