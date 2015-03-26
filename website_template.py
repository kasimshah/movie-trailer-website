
import movie_class # File name where the class code is written

import fresh_tomatoes #Python file that contains the code for the html template to open the website 


#Movie is Toy Story and used to create instance that contains proper movie information. 
toy_story=movie_class.Movie("Toy Story",
                            "Click the poster to see the movie trailer",
                             "Starring: Tom Hanks",
                             " Rotten Tomatoes: 100%",
                             "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                             "https://www.youtube.com/watch?v=KYz2wyBy3kc")

#Movie is Interstellar and used to create instance that contains proper movie information.
interstellar=movie_class.Movie("Interstellar",
                               "Click the poster to see the movie trailer",
                             "Starring: Matthew McConaughey",
                            " Rotten Tomatoes: 72%",
                             "http://www.liveforfilms.com/wp-content/uploads/2014/09/Interstellar-Main-One-Sheet.jpg",
                             "https://www.youtube.com/watch?v=zSWdZVtXT7E")

#Movie is Skyfall and used to create instance that contains proper movie information.
skyfall=movie_class.Movie("Skyfall",
                          "Click the poster to see the movie trailer",
                             "Starring: Daniel Craig",
                            " Rotten Tomatoes: 92%",
                             "http://upload.wikimedia.org/wikipedia/en/a/a7/Skyfall_poster.jpg",
                             "https://www.youtube.com/watch?v=6kw1UVovByw")


movies = [toy_story,interstellar,skyfall] # Variable used to create a list of the movie classes

fresh_tomatoes.open_movies_page(movies) # Line of code used to open the website created













