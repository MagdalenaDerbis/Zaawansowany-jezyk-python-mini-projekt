class Playlist:

    def __init__(self, songs: list):
        self.songs = songs

    def __str__(self):
        return f'{self.songs}'

    def __add__(self, other):
        if isinstance(other, Playlist):
            return Playlist(self.songs + other.songs)
        if isinstance(other, str):
            return Playlist(self.songs + [other])

    def __radd__(self, other):
        if isinstance(other, str):
            return Playlist(self.songs + [other])

    def __getitem__(self, song):
        return self.songs[song]

    def __setitem__(self, song, new_song):
        self.songs[song] = new_song


lista1 = Playlist(['song1', 'song2', 'song3'])
lista2 = Playlist(['song4', 'song5', 'song6'])
lista3 = lista1 + lista2
print(lista1)
print(lista3)
print(type(lista3))
print(lista1 + 'song7')
print('song7' + lista1)
print(lista3[2])
lista3[2] = 'song8'
print(lista3)