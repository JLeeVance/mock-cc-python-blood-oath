from .bloodoath import BloodOath

class Cult:
    
    all = []

    def __init__(self, name, location, founding_year, slogan):
        self.name = name
        self.location = location
        self.founding_year = founding_year
        self.slogan = slogan
        self.__class__.all.append(self)
        print(f"The cult - {self.name} - has been created!")

    def recruit_follower(self, follower):
        from .follower import Follower
        if isinstance(follower, Follower):
            BloodOath("02/06/2024",follower, self)
        else:
            raise Exception("follower must be of class instance Follower")
        
    def followers(self):
       return [oath.follower for oath in BloodOath.all if oath.cult == self]
        
    def cult_population(self):
        # print(len(self.followers()))
        return len(self.followers())
    
    @classmethod
    def find_by_name(cls, cult_name):
        # print([cult.name for cult in cls.all if cult.name.lower() == cult_name.lower()])
        return [cult for cult in cls.all if cult.name.lower() == cult_name.lower()]
    
    @classmethod
    def find_by_location(cls, cult_location):
        # print([cult.location for cult in cls.all if cult.location.lower() == cult_location.lower()])
        return [cult for cult in cls.all if cult.location.lower() == cult_location.lower()]
    
    def find_by_founding_year(year):
        # print([cult.name for cult in Cult.all if cult.founding_year == year])
        return [cult for cult in Cult.all if cult.founding_year == year]
    
    def average_age(self):
        return round(sum([p.age for p in self.followers()]) / len(self.followers()), 2)
    
    def my_followers_mottos(self):
        for follower in self.followers():
            print(f"{follower.life_motto}")
    
    @classmethod
    def least_popular(cls):
        least = None
        low_f = 100
        for cult in cls.all:
            if cult.population() <= low_f:
                least = cult
                low_f = cult.population()
        # print(least.name)
        return least
    
    @classmethod
    def most_common_location(cls):
        cult_locations = {}
        for cult in cls.all:
            if cult.location not in cult_locations:
                cult_locations[cult.location] = 1
            else:
                cult_locations[cult.location] += 1
        # print(max(cult_locations, key= lambda location : cult_locations[location]))
        return max(cult_locations, key= lambda location : cult_locations[location])

        
        




