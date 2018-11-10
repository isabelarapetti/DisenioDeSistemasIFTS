from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Section, Base, Article, User

engine = create_engine('sqlite:///articledump.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

# create a dummy users
User1 = User(name="Jose Primero", email="joseprimero@gmail.com",
             picture='https://unsplash.it/200/300/?random')
session.add(User1)
session.commit()

User2 = User(name="Ana Perez", email="anaperez@gmail.com",
             picture='https://unsplash.it/200/300/?random')
session.add(User2)
session.commit()

User3 = User(name="Carlos Rodriguez", email="crodz@gmail.com",
             picture='https://unsplash.it/200/300/?random')
session.add(User3)
session.commit()

# Looping Section 
economySection = Section(name = "economy")

session.add(economySection)
session.commit()

article1 = Article(title = "War for the Planet of the Apes",
			body = "Caesar and his apes are forced into a deadly conflict with an army of humans led by a ruthless Colonel. After the apes suffer unimaginable losses, Caesar wrestles with his darker instincts and begins his own mythic quest to avenge his kind. As the journey finally brings them face to face, Caesar and the Colonel are pitted against each other in an epic battle that will determine the fate of both their species and the future of the planet",
			datetime = "Matt Reeves",
			image = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTeJ2_YwH8yyg_x-GOd9kjgkrNBblmvbSYMpqvlvLfCC0eWd2BF",
			section = economySection,
            user_id = 1)
session.add(article1)
session.commit()

article2 = Article(title = "Spider-Man: Homecoming",
			body = "Thrilled by his experience with the Avengers, Peter returns home, where he lives with his Aunt May, under the watchful eye of his new mentor Tony Stark, Peter tries to fall back into his normal daily routine - distracted by thoughts of proving himself to be more than just your friendly neighborhood Spider-Man - but when the Vulture emerges as a new villain, everything that Peter holds most important will be threatened",
			datetime = "Jon Watts",
			image = "https://images-na.ssl-images-amazon.com/images/M/MV5BNTk4ODQ1MzgzNl5BMl5BanBnXkFtZTgwMTMyMzM4MTI@._V1_SY1000_CR0,0,658,1000_AL_.jpg",
			section = economySection,
            user_id = 1)
session.add(article2)
session.commit()

tecnhologySection = Section(name = "tecnhology")

article3 = Article(title = "Despicable Me 3",
			body = "After he is fired from the Anti-Villain League for failing to take down the latest bad guy to threaten humanity, Gru finds himself in the midst of a major identity crisis. But when a mysterious stranger shows up to inform Gru that he has a long-lost twin brother-a brother who desperately wishes to follow in his twin's despicable footsteps-one former super-villain will rediscover just how good it feels to be bad.",
			datetime = "Kyle Balda",
			image = "https://images-na.ssl-images-amazon.com/images/M/MV5BNjUyNzQ2MTg3Ml5BMl5BanBnXkFtZTgwNzE4NDM3MTI@._V1_SY1000_CR0,0,631,1000_AL_.jpg",
			section = tecnhologySection)
session.add(article3)
session.commit()

article4 = Article(name = "Cars 3",
			body = "Blindsided by a new generation of blazing-fast racers, the legendary Lightning McQueen is suddenly pushed out of the sport he loves. To get back in the game, he will need the help of an eager young race technician with her own plan to win, inspiration from the late Fabulous Hudson Hornet, and a few unexpected turns. Proving that #95 isn't through yet will test the heart of a champion on Piston Cup Racing's biggest stage!",
			datetime = "Brian Fee",
			image = "https://images-na.ssl-images-amazon.com/images/M/MV5BMTc0NzU2OTYyN15BMl5BanBnXkFtZTgwMTkwOTg2MTI@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
			section = tecnhologySection)
session.add(article4)
session.commit()

comedySection = Section(name = "comedy")

article5 = Article(title = "Jumanji: Welcome to the Jungle",
			body = "In a brand new Jumanji adventure, four high school kids discover an old video game console and are drawn into the game's jungle setting, literally becoming the adult avatars they chose. What they discover is that you don't just play Jumanji - you must survive it. To beat the game and return to the real world, they'll have to go on the most dangerous adventure of their lives, discover what Alan Parrish left 20 years ago, and change the way they think about themselves - or they'll be stuck in the game forever, to be played by others without break.",
			datetime = "Jake Kasdan",
			image = "https://images-na.ssl-images-amazon.com/images/M/MV5BMTU3NTQ0OTU0M15BMl5BanBnXkFtZTgwNTY4NTY3MjI@._V1_SY1000_CR0,0,658,1000_AL_.jpg",
			section = comedySection)
session.add(article5)
session.commit()
