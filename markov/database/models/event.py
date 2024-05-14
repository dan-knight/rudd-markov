from sqlalchemy.orm import Mapped, mapped_column

from markov.database.models import Base


class Event(Base):
    __tablename__ = "events"

    event_id: Mapped[int] = mapped_column(primary_key=True)
    match_id: Mapped[int] = mapped_column(nullable=False)
    period: Mapped[int] = mapped_column(nullable=False)
    second: Mapped[float] = mapped_column(nullable=False)
    event_type: Mapped[int] = mapped_column(nullable=False)
    x: Mapped[float] = mapped_column(nullable=False)
    y: Mapped[float] = mapped_column(nullable=False)
