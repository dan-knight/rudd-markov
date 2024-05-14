from sqlalchemy.orm import Session


class Repository:
    def __init__(self, session: Session):
        self._session: Session = session
