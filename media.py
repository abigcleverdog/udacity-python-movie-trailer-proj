class Movie():
    '''movie class defines instance variables such as the title, box art,
    and movie trailer of a movie'''

    # constructor of Movie
    def __init__(self, title, art_url, trailer_url):
        
        self.title = title
        self.poster_image_url = art_url
        self.trailer_youtube_url = trailer_url
