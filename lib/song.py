class Song:
    # Class attribute to keep track of the total number of songs created
    count = 0
    
    # Class attribute to store unique genres
    genres = []
    
    # Class attribute to store unique artists
    artists = []
    
    # Class attribute to store the count of songs for each genre
    genre_count = {}
    
    # Class attribute to store the count of songs for each artist
    artist_count = {}
    
    def __init__(self, name, artist, genre):
        # Initialize instance attributes
        self.name = name
        self.artist = artist
        self.genre = genre
        
        # Increment the count of songs and add the song's genre and artist
        Song.add_song_to_count()
        self.add_to_genres()
        self.add_to_artists()
        
    @classmethod
    def add_song_to_count(cls):
        # Increment the count of songs
        cls.count += 1
        
    def add_to_genres(self):
        # Add the song's genre to the genres list if it's not already present
        if self.genre not in Song.genres:
            Song.genres.append(self.genre)
        
    def add_to_artists(self):
        # Add the song's artist to the artists list if it's not already present
        if self.artist not in Song.artists:
            Song.artists.append(self.artist)
        
    @classmethod
    def add_to_genre_count(cls, genre):
        # Initialize genre_count dictionary if not already initialized
        if not cls.genre_count:
            cls.genre_count = {genre: 0 for genre in cls.genres}
        
        # Increment the count of songs for the song's genre
        cls.genre_count[genre] += 1