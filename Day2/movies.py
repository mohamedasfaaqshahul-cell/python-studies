top_x = int(input("Enter top x number (1-10): "))
actor = input("Enter actor name: ").lower()

if actor == "vijay":
    movies = ["Leo", "Master", "Thuppakki", "Ghilli", "Pokkiri",
              "Kaththi", "Bigil", "Mersal", "Sarkar", "Theri"]

elif actor == "rajinikanth":
    movies = ["Jailer", "Sivaji", "Enthiran", "Baasha", "Padayappa",
              "Kabali", "Petta", "Annaatthe", "Chandramukhi", "Darbar"]

elif actor == "kamal":
    movies = ["Vikram", "Indian", "Nayakan", "Dasavatharam", "Anbe Sivam",
              "Apoorva Sagodharargal", "Thevar Magan", "Vettaiyaadu Vilaiyaadu", "Panchathanthiram", "Virumaandi"]

elif actor == "sivakarthikeyan":
    movies = ["Amaran", "Doctor", "Don", "Remo", "Varuthapadatha Valibar Sangam",
              "Prince", "Maaveeran", "Namma Veettu Pillai", "Hero", "Rajini Murugan"]

elif actor == "vikram":
    movies = ["Anniyan", "I", "Saamy", "Dhool", "Pithamagan",
              "Ponniyin Selvan", "Gemini", "Deiva Thirumagal", "Kadhal Sadugudu", "Mahaan"]

else:
    print("Unknown Actor")
    movies = []

if movies:
    print(f"\nTop {top_x} Movies of {actor.title()}")

    for i in range(top_x):
        print(f"{i+1}. {movies[i]}")
