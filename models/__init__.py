from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
from .driver import Driver
from .team import Team
from .race import Race
from .result import Result
