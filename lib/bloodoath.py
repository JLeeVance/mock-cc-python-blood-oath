class BloodOath:
    
    all = []

    def __init__(self, initiation_date, follower, cult):
        self.cult = cult
        self.follower = follower
        self.initiation_date = initiation_date
        self.__class__.all.append(self)
        print(f"{self.follower.name} has joined {self.cult.name}")
    
    @property
    def follower(self):
        return self._follower
    
    @follower.setter
    def follower(self, new_follower):
        from .follower import Follower
        if isinstance(new_follower, Follower):
            self._follower = new_follower
        else:
            raise Exception("follower must be of class instance Follower")
    
    @property
    def cult(self):
        return self._cult
    
    @cult.setter
    def cult(self, new_cult):
        from .cult import Cult
        if isinstance(new_cult, Cult):
            self._cult = new_cult
        else:
            raise Exception("cult must be of class instance Cult")
        
    
