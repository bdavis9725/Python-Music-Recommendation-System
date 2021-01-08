#!/usr/bin/env python
# coding: utf-8

# ### PCP Assignment 2 Module 1 - load_dataset_module

# In[ ]:


import pandas as pd # Load the library we need
#import numpy as np


# ### Define the classes

# In[ ]:


# Use a metaclass to make classes iterable later
class IterRegistry(type):
    def __iter__(cls):
        return iter(cls.registry)


# In[ ]:


class Artist(object):
    __metaclass__ = IterRegistry
    _registry = []
    
    def __init__(self, artistname, **kwargs):
        self._registry.append(self)
        self.artistname = artistname
        
        super().__init__(**kwargs)
        
    # Returns object in string format for readability
    def __repr__(self):
        # Allows the ability to print out all names
        return "Name: % s" % (self.artistname)
        
    def getName(self):
        return f'Artist Name/s: {self.artistname.strip("[]")}'
    
#     def __getitem__(self, index):
#         return self[index]
#         print(self[index])
    
    def __index__(self):
        return self.artistname
    
    def setName(self):
        pass


# In[ ]:


class Song(object):
    __metaclass__ = IterRegistry
    _registry = []
    
    def __init__(self, 
                 songname, 
                 music_ID,
                 acousticness, 
                 danceability, 
                 energy, 
                 liveness, 
                 loudness, 
                 popularity, 
                 speechiness, 
                 tempo, 
                 valence,
                 **kwargs):
        
        super().__init__(**kwargs)
        
        self._registry.append(self)
        
        self.songname = songname
        self.music_ID = music_ID
        self.acousticness = acousticness
        self.danceability = danceability
        self.energy = energy
        self.liveness = liveness
        self.loudness = loudness
        self.popularity = popularity
        self.speechiness = speechiness
        self.tempo = tempo
        self.valence = valence
        
    # Returns object in string format for readability
    def __repr__(self):
        # Allows the ability to print out all names
        return f'Song Name: {self.songname}, ID: {self.music_ID}, Acousticness: {self.acousticness}, Danceability: {self.danceability}, Energy: {self.energy}, Liveness: {self.liveness}, Loudness: {self.loudness}, Popularity: {self.popularity}, Speechiness: {self.speechiness}, Tempo: {self.tempo}, Valence: {self.valence}'
  
    def getFeatures(self):
        return self.songname, self.music_ID, self.acousticness, self.danceability, self.energy, self.liveness, self.loudness, self.popularity, self.speechiness, self.tempo, self.valence
    
    def getComparisonFeatures(self):
        return self.acousticness, self.danceability, self.energy, self.liveness, self.loudness, self.popularity, self.speechiness, self.tempo, self.valence
    
    def getSongName(self):
        return f'Song Name: {self.songname}'


# In[ ]:


# Could use a class for the extra features from the csv, but not sure yet
# Left here just in case
class Extras():
    pass


# In[ ]:


# Define a sub-class that inherits all features from the above classes

class Track(Artist, Song):
    __metaclass__ = IterRegistry
    _registry = []
    
    def __init__(self, an, sn, ID, acc, dan, en, live, loud, popu, spe, tem, val):
        super().__init__(artistname = an,
                         songname = sn,
                         music_ID = ID,
                         acousticness = acc,
                         danceability = dan,
                         energy = en,
                         liveness = live,
                         loudness = loud,
                         popularity = popu,
                         speechiness = spe,
                         tempo = tem,
                         valence = val)
    
    # Override inherited repr so that the output is correct
    def __repr__(self):
        return f'Artist Name/s: {self.artistname.strip("[]")}, Song Name: {self.songname}, ID: {self.music_ID}, Acousticness: {self.acousticness}, Danceability: {self.danceability}, Energy: {self.energy}, Liveness: {self.liveness}, Loudness: {self.loudness}, Popularity: {self.popularity}, Speechiness: {self.speechiness}, Tempo: {self.tempo}, Valence: {self.valence}'
    
    def to_dict(self):
        return {
            'Artist Name': self.artistname,
            'Song Name': self.songname,
            'Music_ID': self.music_ID,
            'Acousticness': self.acousticness,
            'Danceability': self.danceability,
            'Energy': self.energy,
            'Liveness': self.liveness,
            'Loudness': self.loudness,
            'Popularity': self.popularity,
            'Speechiness': self.speechiness,
            'Tempo': self.tempo,
            'Valence': self.valence, 
        }


# In[ ]:


#print(help(Track))


# ### Create the Functions

# In[ ]:


def artist_music():
    try:
        df_artists = pd.read_csv("data.csv", encoding = 'utf8', delimiter = ',')
#         df_artists.index += 1
#         artists = df_artists.to_dict(orient='records')

        artist_list = []
        for name in df_artists.artists:
            name = name.strip("[]")
            artist_list.append(Artist(name))
            
        return artist_list       #return the dictionary for use
    
    except IOError as ioerr: # catch any file errors to prevent crashing of the program
        print('File error: ' + str(ioerr))
    finally:
        print('Finished reading the command for artist name file reading.')


# In[ ]:


def music_features():
    try:
        features = pd.read_csv('data.csv', encoding = 'utf8', delimiter=',', low_memory=False,
                                   usecols=['id', 'name', 'acousticness','danceability','energy','liveness','loudness','popularity','speechiness','tempo','valence'])
        
        song_features_list = []
        for value in zip(features.name,                          
                         features.id, 
                         features.acousticness, 
                         features.danceability, 
                         features.energy,
                         features.liveness,
                         features.loudness,
                         features.popularity,
                         features.speechiness,
                         features.tempo,
                         features.valence):

            song_features_list.append(Song(value[0],
                                           value[1],
                                           value[2],
                                           value[3],
                                           value[4],
                                           value[5],
                                           value[6],
                                           value[7],
                                           value[8],
                                           value[9],
                                           value[10]))
        
        return song_features_list
        del song_features_list # Delete from memory when finished 
        
    except IOError as ioerr: # catch any file errors to prevent crashing of the program
        print('File error: ' + str(ioerr))
    finally:
        print('Finished reading the command for music features file loading.')


# In[ ]:


def read_wholeFile():
    try:
        df_file = pd.read_csv('data.csv', encoding = 'utf8', delimiter=',', low_memory=False,
                              usecols=['artists', 'id', 'name', 'acousticness','danceability','energy','liveness','loudness','popularity','speechiness','tempo','valence'])
        
        file_list = []

        for value in zip(df_file.artists,
                         df_file.name,                          
                         df_file.id, 
                         df_file.acousticness, 
                         df_file.danceability, 
                         df_file.energy,
                         df_file.liveness,
                         df_file.loudness,
                         df_file.popularity,
                         df_file.speechiness,
                         df_file.tempo,
                         df_file.valence):

            file_list.append(Track (value[0],
                                    value[1],
                                    value[2],
                                    value[3],
                                    value[4],
                                    value[5],
                                    value[6],
                                    value[7],
                                    value[8],
                                    value[9],
                                    value[10],
                                    value[11]))
        
        return file_list
        del file_list # Delete from memory when finished 
        
    except IOError as ioerr: # catch any file errors to prevent crashing of the program
        print('File error: ' + str(ioerr))
    finally:
        print('Finished reading the command for full file loading.')

