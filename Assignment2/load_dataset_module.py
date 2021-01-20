#!/usr/bin/env python
# coding: utf-8

# ### PCP Assignment 2 Module 1 - load_dataset_module

import pandas as pd # Load the library we need


# Use a metaclass to make classes iterable later
class IterRegistry(type):
    def __iter__(cls):
        return iter(cls.registry)

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
        return f'Artist: {self.artistname.strip("[]")}'
    
#     def __getitem__(self, index):
#         return self[index]
#         print(self[index])
    
    def __index__(self):
        return self.artistname
    
    def setName(self):
        pass

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
        return f'Song: {self.songname}, ID: {self.music_ID}, Acousticness: {self.acousticness}, Danceability: {self.danceability}, Energy: {self.energy}, Liveness: {self.liveness}, Loudness: {self.loudness}, Popularity: {self.popularity}, Speechiness: {self.speechiness}, Tempo: {self.tempo}, Valence: {self.valence}'
  
    def getFeatures(self):
        return f'Song: {self.songname}, Music ID: {self.music_ID}, Acousticness: {self.acousticness}, Danceability: {self.danceability}, Energy: {self.energy}, Liveness: {self.liveness}, Loudness: {self.loudness}, Popularity: {self.popularity}, Speechiness: {self.speechiness}, Tempo: {self.tempo}, Valence: {self.valence}'
    
    def getComparisonFeatures(self):
        return f'Acousticness: {self.acousticness}, Danceability: {self.danceability}, Energy: {self.energy}, Liveness: {self.liveness}, Loudness: {self.loudness}, Popularity: {self.popularity}, Speechiness: {self.speechiness}, Tempo: {self.tempo}, Valence: {self.valence}'
    
    def getSongName(self):
        return f'Song: {self.songname}'

class Extras(object):
    __metaclass__ = IterRegistry
    _registry = []
    
    def __init__(self, 
                 duration_ms,
                 explicit,
                 instrumentalness,
                 key,
                 mode,
                 release_date,
                 **kwargs):
        
        super().__init__(**kwargs)
        
        self._registry.append(self)
        
        self.duration_ms = duration_ms
        self.explicit = explicit
        self.instrumentalness = instrumentalness
        self.key = key
        self.mode = mode
        self.release_date = release_date
        
    # Returns object in string format for readability
    def __repr__(self):
        pass
        # Allows the ability to print out all names
        #return f'Song Name: {self.songname}, ID: {self.music_ID}, Acousticness: {self.acousticness}, Danceability: {self.danceability}, Energy: {self.energy}, Liveness: {self.liveness}, Loudness: {self.loudness}, Popularity: {self.popularity}, Speechiness: {self.speechiness}, Tempo: {self.tempo}, Valence: {self.valence}'
  
    def getExtras(self):
        return f'Duration: {self.duration_ms}, Explicit: {self.explicit}, Instrumentalness: {self.instrumentalness}, Key: {self.key}, Mode: {self.mode}, Release Date: {self.release_date}'
        

# Define a sub-class that inherits all features from the above classes

class Track(Artist, Song, Extras):
    __metaclass__ = IterRegistry
    _registry = []
    
    def __init__(self, an, sn, ID, acc, dan, en, live, loud, popu, spe, tem, val, dur, expl, instr, key, mode, reldat):
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
                         valence = val,
                         duration_ms = dur,
                         explicit = expl,
                         instrumentalness = instr,
                         key = key,
                         mode = mode,
                         release_date = reldat)
    
    # Override inherited repr so that the output is correct
    def __repr__(self):
        return f'Artist: {self.artistname.strip("[]")}, Song: {self.songname}, ID: {self.music_ID}, Acousticness: {self.acousticness}, Danceability: {self.danceability}, Energy: {self.energy}, Liveness: {self.liveness}, Loudness: {self.loudness}, Popularity: {self.popularity}, Speechiness: {self.speechiness}, Tempo: {self.tempo}, Valence: {self.valence}'
    
    def to_dict(self): # Extract the relevant features to a dictionary
        return {
            #'Artist': self.artistname,
            #'Song Name': self.songname,
            'Acousticness': self.acousticness,
            'Danceability': self.danceability,
            'Energy': self.energy,
            'Liveness': self.liveness,
            'Loudness': self.loudness,
            'Popularity': self.popularity,
            'Speechiness': self.speechiness,
            'Tempo': self.tempo,
            'Valence': self.valence, 
            'Explicit': self.explicit,
            'Instrumentalness': self.instrumentalness,
        }

class File_loader():
    __metaclass__ = IterRegistry
    _registry = []
    
    def __init__(self):
        self.filelist = []
        self.data = 'data.csv'
    
    def read_file(self):
        try:
            df_file = pd.read_csv(self.data, delimiter=',', low_memory=False)
            
            #Remove duplicate song entries
            df_file = df_file.drop_duplicates(subset=['artists', 'name'], keep='last')
            
            # Split the artists by the comma between multiple names
            artists = df_file.artists.str.split(',')
            
            # Take only the first name from each line
            artists = [artist[0] for artist in artists]
            df_file.rename(columns={'mode': 'modal'}, inplace = True)

            for value in zip(artists,
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
                             df_file.valence,
                             df_file.duration_ms,
                             df_file.explicit,
                             df_file.instrumentalness,
                             df_file.key,
                             df_file.modal,
                             df_file.release_date):

                self.filelist.append(Track(value[0],
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
                                       value[11],
                                       value[12],
                                       value[13],
                                       value[14],
                                       value[15],
                                       value[16],
                                       value[17]))
        
            return self.filelist
    
        except IOError as ioerr: # catch any file errors to prevent crashing of the program
            print('File error: ' + str(ioerr))
        finally:
            print('Finished reading the command for file loading.')

