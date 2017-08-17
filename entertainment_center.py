import media
import fresh_tomatoes

# initiate individual movies with three variables, title, poster, and trailer_url
finding_dory = media.Movie("Finding Dory",
                           "https://upload.wikimedia.org/wikipedia/en/thumb/3/3e/Finding_Dory.jpg/220px-Finding_Dory.jpg",
                           "https://www.youtube.com/watch?v=JhvrQeY3doI")

rogue_one_st = media.Movie("Rogue One: A Star Wars Story",
                           "https://upload.wikimedia.org/wikipedia/en/thumb/d/d4/Rogue_One%2C_A_Star_Wars_Story_poster.png/220px-Rogue_One%2C_A_Star_Wars_Story_poster.png",
                           "https://www.youtube.com/watch?v=frdj1zb9sMY")

captain_amer = media.Movie("Captain America: Civil War",
                           "https://upload.wikimedia.org/wikipedia/en/thumb/5/53/Captain_America_Civil_War_poster.jpg/220px-Captain_America_Civil_War_poster.jpg",
                           "https://www.youtube.com/watch?v=dKrVegVI0Us")

the_secret_l = media.Movie("The Secret Life of Pets",
                           "https://upload.wikimedia.org/wikipedia/en/6/64/The_Secret_Life_of_Pets_poster.jpg",
                           "https://www.youtube.com/watch?v=eWI_Jsw9qUs")

the_jungle_b = media.Movie("The Jungle Book",
                           "https://upload.wikimedia.org/wikipedia/en/a/a4/The_Jungle_Book_%282016%29.jpg",
                           "https://www.youtube.com/watch?v=HcgJRQWxKnw")

deadpool = media.Movie("Deadpool",
                       "https://upload.wikimedia.org/wikipedia/en/thumb/c/ca/Deadpool.png/220px-Deadpool.png",
                       "https://www.youtube.com/watch?v=9vN6DHB6bJc")

zootopia = media.Movie("Zootopia",
                       "https://upload.wikimedia.org/wikipedia/en/e/ea/Zootopia.jpg",
                       "https://www.youtube.com/watch?v=jWM0ct-OLsM")

# create a list for all the movies
movies = [finding_dory, rogue_one_st, captain_amer, the_secret_l,
          the_jungle_b, deadpool, zootopia]

# use open_movies_page function in fresh_tomatoes to generate the dynamic page
fresh_tomatoes.open_movies_page(movies)
