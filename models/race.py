from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from models import Base

class Race(Base):
    __tablename__ = 'races'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)  # Name of the grand prix 
    circuit = Column(String(100), nullable=False)  # Circuit name
    location = Column(String(100), nullable=False)  # Location of the circuit
    date = Column(Date, nullable=False)  # Date of the grand prix
    laps = Column(Integer, nullable=False)  # Total number of laps in the grand prix
    distance_km = Column(Integer, nullable=False)  # Total distance of the grand prix in kilometers
    weather = Column(String(50), nullable=True)  # Weather conditions

    #relationships
    results = relationship("Result", back_populates="race")

    def __repr__(self):
        return (f"<race(id={self.id}, name='{self.name}', circuit='{self.circuit}',location='{self.location}', "
                f"date='{self.date}', laps={self.laps}, distance_km={self.distance_km}, weather='{self.weather}')>")