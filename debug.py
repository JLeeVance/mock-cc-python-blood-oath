import ipdb
from lib import *


print("\n" *2)

jay = Follower("Jay", 10, "Fuck it.")
cecilia = Follower("Cecilia", 30, "It is ALL about Pickles")
tim = Follower("Tim", 77, "One time in seal camp.")
kylie = Follower("Kylie", 28, "I am SO happy")
tyler = Follower("Tyler", 22, "I have a bike.")
joe = Follower("Joe", 22, "I like peas.")
korn = Follower("Korn", 75, "This is Korn")
bean = Follower("Bean", 1, "I am a baby bean")
cactus = Follower("Cactus", 300, "I am old.")
pam = Follower("pam", 35, "I like Jim")
jim = Follower("jim", 33, "I like Pam")


pickles = Cult("Pickles", "New Mexico", 2019, "Midnight zoomies for the win.")
prudence = Cult("Prudence", "New Mexico", 2012, "All about the ZZZzzzz's" )
aspen = Cult("aspen", "Indiana" , 2022, "I may be small, but I will fuck you up.")

oath1 = BloodOath("02/06/2024", cecilia, prudence)
prudence.recruit_follower(jay)

list = [jay, cecilia, tim, kylie, tyler, joe, korn, bean, cactus, pam]
list2 = [jay, cecilia, tim, kylie]

count = 0
while count < 10:
    for person in list:
        pickles.recruit_follower(person)
        count += 1

counts = 0
while count < 4:
    for person in list2:
        aspen.recruit_follower(person)
        count += 1

# print("\n" *2)

# pickles.cult_population()
# Cult.find_by_name("pickles")
# Cult.find_by_location("indiana")
# Cult.find_by_founding_year(2019)
# print("\n" *2)
# cecilia.join_cult(aspen)
# cecilia.cults()
# Follower.of_a_certain_age(30)
# print("\n" *2)
# print(pickles.average_age())



# cecilia.my_cults_slogan()


Follower.top_ten()

print( "Mwahahaha!" )

# ipdb.set_trace()