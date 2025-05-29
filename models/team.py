from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models import Base

class Team(Base):
    __tablename__ = 'teams'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)  # Team name
    base = Column(String, nullable=False)  # Base location of the team
    Team_principal = Column(String(50), nullable=False)  # Team principal's name
    championships_won = Column(Integer, default=0)  # Number of championships won
    points = Column(Integer, default=0)  # Total points scored by the team

  #relationships to 2 drivers and one reserve driver
    drivers = relationship("Driver", back_populates="team", cascade="all, delete-orphan")

#  relationship to results
    results = relationship("Result", back_populates="team",)


    def __repr__(self):
        return f"<Team(name='{self.name}', base='{self.base}', principal='{self.principal}', championships_won={self.championships_won}, points={self.points})>"