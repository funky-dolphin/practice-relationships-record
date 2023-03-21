class Record():

    def __init__(self, title, artist, year):
        self.title = title
        self.year = year
        self.artist = artist
        self.songs = []

    def get_title(self):
        return self.title.title()
    
    def get_artist(self):
        return self.artist
    
    def get_year(self):
        return self.year
    
    def get_songs(self):
        return self.songs
   
    def total_runtime(self):
       return sum(song.runtime for song in self.songs)
    
    def has_song(self, song):
        if song in self.songs:
            return True 
        else: 
            return False
        
    def get_longest_song(self):
        longest = self.songs[0]
        for i in self.songs:
            if i.runtime > longest.runtime:
                longest = i 
            return longest
        

