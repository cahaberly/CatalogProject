#!/usr/bin/python2.7
# Clay Haberly 4/24/2018

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, CategoryItem, User

engine = create_engine('sqlite:///catalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Create dummy user
User1 = User(name="Clay Haberly", email="cahaberly@gmail.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')  # noqa
session.add(User1)
session.commit()

# Football items
category1 = Category(user_id=1, category_name="Football", image="football.jpg")

session.add(category1)
session.commit()

category_item1 = CategoryItem(user_id=1, item_name="Youth Football Helmet",
                              description="Help protect your star player\'s \
                                head as he faces tough opponents.",
                              price="$15.00", season="Fall",
                              category=category1)

session.add(category_item1)
session.commit()


category_item2 = CategoryItem(user_id=1, item_name="Football",
                              description="Quarterbacks can take \
                                advantage of tactified laces for excellent\
                                pass control, while catching is made easier \
                                with active grip technology. ",
                              price="$12.99", season="Fall",
                              category=category1)

session.add(category_item2)
session.commit()

category_item3 = CategoryItem(user_id=1, item_name="Football Kickoff Tee",
                              description="The 3-leg design offers plenty of \
                                stability when it's time to kick.",
                              price="$8.67", season="Fall",
                              category=category1)

session.add(category_item3)
session.commit()

category_item4 = CategoryItem(user_id=1, item_name="Football Glove",
                              description="The gloves help enhance a \
                              receiver\'s ability to grab and hold onto the \
                              ball in practice and in games.",
                              price="$14.99", season="Fall",
                              category=category1)

session.add(category_item4)
session.commit()

category_item5 = CategoryItem(user_id=1, item_name="Mouth Gaurd",
                              description="Designed to protect your young \
                              athlete\'s teeth during practices and games.",
                              price="$2.99", season="Fall",
                              category=category1)

session.add(category_item5)
session.commit()

category_item6 = CategoryItem(user_id=1, item_name="Shoulder Pad",
                              description="Lightweight, all-purpose design \
                              and elastic strap attachment is flexible for \
                              an easy fit",
                              price="$23.50", season="Fall",
                              category=category1)

session.add(category_item6)
session.commit()


# Baseball items
category2 = Category(user_id=1, category_name="Baseball", image="baseball.jpg")

session.add(category2)
session.commit()


category_item1 = CategoryItem(user_id=1, item_name="Baseball Catcher\'s Mitt",
                              description="Padded leather glove for the \
                                catcher",
                              price="$45.99", season="Summer",
                              category=category2)

session.add(category_item1)
session.commit()

category_item2 = CategoryItem(user_id=1, item_name="Baseball Fielder\'s Mitt",
                              description="Padded leather glove for the out \
                              field.", price="$42.50", season="Summer",
                              category=category2)

session.add(category_item2)
session.commit()

category_item3 = CategoryItem(user_id=1, item_name="Catcher\'s Mask",
                              description="Steel enforced cage to protect the \
                              face.",
                              price="$32.67", season="Summer",
                              category=category2)

session.add(category_item3)
session.commit()

category_item4 = CategoryItem(user_id=1, item_name="Catcher\'s Shin Gaurds ",
                              description="Sturdy polymer plastic \
                              construction.",
                              price="$34.99", season="Summer",
                              category=category2)

session.add(category_item4)
session.commit()

category_item5 = CategoryItem(user_id=1, item_name="Aluminum Baseball Bat",
                              description="The All-Sports grip provides a \
                              tacky, cushioned feel beneath your palms, so \
                              you can confidently swing for the fences.",
                              price="$67.99", season="Summer",
                              category=category2)

session.add(category_item5)
session.commit()

# Snowboarding items
category1 = Category(
    user_id=1, category_name="Snowboarding", image="snowboard.jpg")

session.add(category1)
session.commit()


category_item1 = CategoryItem(user_id=1, item_name="Snowboard",
                              description="Quality buit fiberglass \
                              snowboard.",
                              price="$125.00", season="Winter",
                              category=category1)

session.add(category_item1)
session.commit()

category_item2 = CategoryItem(user_id=1, item_name="Snow Goggles",
                              description="Super comfortable high strength \
                              eye protection.",
                              price="$23.78", season="Winter",
                              category=category1)

session.add(category_item2)
session.commit()

category_item3 = CategoryItem(user_id=1, item_name="Ski Boots",
                              description="Best quality boots for hitting \
                              the slopes.",
                              price="$97.25", season="Winter",
                              category=category1)

session.add(category_item3)
session.commit()

# Frisbee items
category1 = Category(user_id=1, category_name="Frisbee", image="frisbee.jpg")

session.add(category1)
session.commit()


category_item1 = CategoryItem(user_id=1, item_name="Frisbee",
                              description="Professional grade frisbee.",
                              price="$14.99", season="Mixed",
                              category=category1)

session.add(category_item1)
session.commit()

category_item2 = CategoryItem(user_id=1, item_name="Frisbee Bag",
                              description="Carry all of your specalized \
                              frisbees in this durable bag.",
                              price="$23.00", season="Mixed",
                              category=category1)

session.add(category_item2)
session.commit()

# Hockey Items
category1 = Category(user_id=1, category_name="Hockey", image="hockey.jpg")

session.add(category1)
session.commit()

category_item1 = CategoryItem(user_id=1, item_name="Goalie Mask",
                              description="Durable mask to help protect \
                              that beautiful smile!",
                              price="$56.68", season="Winter",
                              category=category1)

session.add(category_item1)
session.commit()

category_item2 = CategoryItem(user_id=1, item_name="Hockey Stick",
                              description="Professionally built hockey stick.",
                              price="$92.69", season="Winter",
                              category=category1)

session.add(category_item2)
session.commit()

category_item3 = CategoryItem(user_id=1, item_name="Hockey Puck",
                              description="Professional grade hockey puck.",
                              price="$4.99", season="Winter",
                              category=category1)

session.add(category_item3)
session.commit()

# Basketball items
category1 = Category(user_id=1, category_name="Basketball",
                     image="basketball.jpg")

session.add(category1)
session.commit()


category_item1 = CategoryItem(user_id=1, item_name="Basketball",
                              description="League quality offical sized \
                              basketball.",
                              price="$18.95", season="Winter",
                              category=category1)

session.add(category_item1)
session.commit()

category_item2 = CategoryItem(user_id=1, item_name="Basketball Net",
                              description="Regulation sized, nylon \
                              construction.",
                              price="$3.45", season="Winter",
                              category=category1)

session.add(category_item2)
session.commit()

# Tennis Items
category1 = Category(user_id=1, category_name="Tennis", image="tennis.jpg")

session.add(category1)
session.commit()

category_item1 = CategoryItem(user_id=1, item_name="Tennis Raquet",
                              description="High quality raquet.",
                              price="$45.99", season="Summer",
                              category=category1)

session.add(category_item1)
session.commit()


category_item2 = CategoryItem(user_id=1, item_name="Tennis Balls",
                              description="HIgh quality tennis balls to play \
                              your best game.",
                              price="$12.99", season="Summer",
                              category=category1)

session.add(category_item2)
session.commit()

# Soccer Items
category1 = Category(user_id=1, category_name="Soccer", image="soccer.jpg")

session.add(category1)
session.commit()


category_item1 = CategoryItem(user_id=1, item_name="Shin Gaurds",
                              description="Durable plastic gaurds for the \
                              shins.",
                              price="$28.78", season="Fall",
                              category=category1)

session.add(category_item1)
session.commit()

category_item2 = CategoryItem(user_id=1, item_name="Soccer Ball",
                              description="Offical sized soccer ball.",
                              price="$12.50", season="Fall",
                              category=category1)

session.add(category_item2)
session.commit()

# Golf Items
category1 = Category(user_id=1, category_name="Golf", image="golf.jpg")
session.add(category1)
session.commit()

category_item1 = CategoryItem(user_id=1, item_name="Golf Club Bag",
                              description="Extra durable bag to hold your \
                              best golf clubs",
                              price="$124.99", season="All",
                              category=category1)

session.add(category_item1)
session.commit()

category_item2 = CategoryItem(user_id=1, item_name="Golf Shoe",
                              description="Extra comfortable spiked shoe.",
                              price="$89.99", season="All",
                              category=category1)

session.add(category_item2)
session.commit()

print("Added catalog items!")
