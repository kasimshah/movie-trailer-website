
import webbrowser


class Movie:
    #Used to initialze the class
    def __init__(self, movie_caption, movie_title, movie_actor, movie_rating, movie_poster, movie_trailer):

        self.title = movie_title #Movie title
        self.caption=movie_caption #Telling the user how to access the movie trailer
        self.actor=movie_actor #Telling the user the movie's lead actor
        self.rating=movie_rating #The rating the movie received on Rotten Tomatoes
        self.poster_image_url=movie_poster #The image of the movie
        self.trailer_youtube_url= movie_trailer #The youtube trailer for the movie

        
