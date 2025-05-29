from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models import Base

class Driver(Base):
    __tablename__ = 'drivers'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)  # Age of the driver
    nationality = Column(String(50), nullable=False)
    titles_won = Column(Integer, default=0)  # Number of championships won
    points_scored = Column(Integer, default=0)  # Total points scored
    role = Column(String(20), nullable=False)  # e.g., main or reserve driver
    team_id = Column(Integer, ForeignKey('teams.id'))
    team = relationship('Team', back_populates='drivers')
    results = relationship('Result', back_populates='driver')
   

    def __repr__(self):
        return f"<Driver(name='{self.name}'),nationality='{self.nationality}', age={self.age}, titles_won={self.titles_won}, points={self.points}, role='{self.role}'>"