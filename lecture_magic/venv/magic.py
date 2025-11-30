from enum import StrEnum
from typing import Self
class Names(StrEnum):
    JOHN = "John Lennon"
    PAUL = "Paul McCartney"
    GEORGE = "George Harrison"
    RING = "Ring Starr"


class Mosquito:
    health_points = 100
    name = Names.JOHN
    
    def __init__ (self, health_points = 100, name = Names.JOHN):
        
        self.health_points = health_points
        self.name = name
    
    
    
    
    #def attack(self, other: Self):
        
    #    print(f"{self.name} attacking {other.name}")
    #   other.health_points -= 10
        
    

if __name__  == '__main__':
    m1 = Mosquito()
    m2 = Mosquito()
    print(m1.name)
    print(f"{m2.health_points}")
    