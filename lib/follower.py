from .bloodoath import BloodOath

class Follower:

    all = []
    
    def __init__(self, name, age, life_motto):
        self.name = name
        self.age = age
        self.life_motto = life_motto
        self.__class__.all.append(self)
        print(f"{self.name} is avail for cults!")
        

    def cults(self):
        # print([oath.cult.name for oath in BloodOath.all if oath.follower == self])
        return [oath.cult for oath in BloodOath.all if oath.follower == self]
        
    def join_cult(self, new_cult):
        from .cult import Cult
        if isinstance(new_cult, Cult):
            BloodOath("02/06/2024", self, new_cult)
        else:
            raise Exception("new_cult must be of class instance Cult")
    
    def of_a_certain_age(find_age):
        # print([follower.name for follower in Follower.all if follower.age == find_age])
        return [follower for follower in Follower.all if follower.age == find_age]
    
    def my_cults_slogan(self):
        for cult in self.cults():
            print(cult.slogan)
    
    @classmethod
    def most_active(cls):
        active_follower = None
        cults = 0
        for follower in cls.all:
            if len(follower.cults()) > cults:
                active_follower = follower
                cults = len(follower.cults())
        # print(active_follower.name)
        return active_follower

    @classmethod
    def top_ten(cls):
        sorted_followers = sorted(cls.all, key = lambda follower : not len(follower.cults()))
        # for follower in sorted_followers:
            # print(f"{follower.name} | {len(follower.cults())}")
        top_ten_followers = []
        count = 0
        while count < 10:
            top_ten_followers.append(sorted_followers[count])
            count += 1
        print([follower.name for follower in top_ten_followers])
        return(top_ten_followers)
            
