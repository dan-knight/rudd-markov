from sqlalchemy.orm import Query

from markov.database.repository import Repository
from markov.database.models.event import Event as DBEvent
from markov.models.event import Event
from markov.models.team import Team


class EventRepository(Repository):
    def get_by_match(self, match_id: int) -> list[Event]:
        query: Query[DBEvent] = self._session.query(DBEvent).filter_by(match_id=match_id)
        query = self._order_query(query)
    
        db_events: list[DBEvent] = query.all()
        return [self._db_to_model(db_event) for db_event in db_events]
    
    def get_by_team(self, team_id: int) -> list[Event]:
        query: Query[DBEvent] = self._session.query(DBEvent).filter_by(team_id=team_id)
        query = self._order_query(query)
    
        db_events: list[DBEvent] = query.all()
        return [self._db_to_model(db_event) for db_event in db_events]
    
    def _order_query(self, query: Query[DBEvent]) -> Query[DBEvent]:
        return query.order_by(
            DBEvent.period, DBEvent.second
        )

    def _db_to_model(self, db_event: DBEvent) -> Event:
        return Event(
            match_id=db_event.match_id,
            period=db_event.period,
            match_second=db_event.second,
            event_type=db_event.event_type,
            x=db_event.x,
            y=db_event.y,
            team=Team(team_id=db_event.team_id)  # TODO: Add team to DB
        )