import random
celebrities = ["Elon Musk", "Virat Kohli", "Cristiano Ronaldo", "Taylor Swift",
                "Akshay Kumar", "Sundar Pichai", "Mark Zuckerberg"]
action = ["buys", "sells", "donates", "launches", "announces", "reveals"
          , "criticizes", "supports"]
objects = ["a new startup", "a charity", "a new product", "a movie",
           "a book", "a music album", "a sports team", "a social media platform"]
locations = ["in Silicon Valley", "in New York", "in London", "in Mumbai",
             "in Los Angeles", "in Dubai", "in Tokyo"]

while True:
    Cele = random.choice(celebrities)
    act = random.choice(action)
    obj = random.choice(objects)
    loc = random.choice(locations)

    Headline = f"Breaking News: {Cele} {act} {obj} {loc}"
    print("----------------------------------------------------------------------------------------------")
    print(Headline)
    print("----------------------------------------------------------------------------------------------")
    another = input("Do you want to generate another headline? (y/n): ").lower()
    print("\n")
    if another != 'y':
        print("Goodbye!")
        break
