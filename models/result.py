from sqlalchemy import Column, Integer,String, ForeignKey
from sqlalchemy.orm import relationship
from models import Base

class Result(Base):
    __tablename__ = 'results'

    id = Column(Integer, primary_key=True)
    race_id = Column(Integer, ForeignKey('races.id') , nullable=False)
    driver_id = Column(Integer, ForeignKey('drivers.id'), nullable=False)
    team_id = Column(Integer, ForeignKey('teams.id'), nullable=False)
    position = Column(Integer, nullable=False)  # Position finished
    points = Column(Integer, nullable=False)  # Points scored inthe race
    laps_completed = Column(Integer, nullable=False)  # Laps completed by the driver
    status = Column(String, nullable=True) #eg completed or did not finish

    #relationships
    race = relationship("Race", back_populates="results")
    driver = relationship("Driver", back_populates="results")
    team = relationship("Team", back_populates="results")

    def __repr__(self):
        return f"<Result(id={self.id}, race_id={self.race_id}, driver_id={self.driver_id}, team_id={self.team_id}, " f"position={self.position}, points={self.points}, laps_completed={self.laps_completed}, status={self.status})>"