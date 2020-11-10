#!/usr/bin/env python
# coding: utf-8

# ### PCP Module 1 - load_dataset_module

# In[43]:


def artist_music():
    import csv
    try:
        artists = {}
        counter = 1
        with open('data.csv', encoding='utf8') as csv_file:
            next(csv_file) #skip the headers
            reader = csv.reader(csv_file, delimiter=',')
            for row in reader:
        
                d = {}
                d['ID'] = row[6]
                d['Artists'] = row[1]
                d['Song Name'] = row[12]
                d['Accoustiness'] = row[0]
                d['Danceability'] = row[2]
                d['Energy'] = row[4]
                d['Liveness'] = row[9]
                d['Loudness'] = row[10]
                d['Popularity'] = row[13]
                d['Speechiness'] = row[15]
                d['Tempo'] = row[16]
                d['Valence'] = row[17]
                artists[counter] = d
                counter+=1 
   
            return artists
            csv_file.close()
        
    except IOError as ioerr:
        print('File error: ' + str(ioerr))
    finally:
        print('Finished reading the command for artist music.')


# In[44]:


print(len(artist_music()))


# In[45]:


artist_music()[2]


# In[46]:


def music_features():
    import csv
    try:
        music = {}
        counter = 1
        with open('data.csv', encoding='utf8') as csv_file:
            next(csv_file) #skip the headers
            reader = csv.reader(csv_file, delimiter=',')
            for row in reader:
        
                #ID = row[6]
        
                d = {}
                d['ID'] = row[6]
                d['Song Name'] = row[12]
                d['Accoustiness'] = row[0]
                d['Danceability'] = row[2]
                d['Energy'] = row[4]
                d['Liveness'] = row[9]
                d['Loudness'] = row[10]
                d['Popularity'] = row[13]
                d['Speechiness'] = row[15]
                d['Tempo'] = row[16]
                d['Valence'] = row[17]
                #add more features here
                music[counter] = d
                counter+=1 
   
            return music
            csv_file.close()
        
    except IOError as ioerr:
        print('File error: ' + str(ioerr))
    finally:
        print('Finished reading the command for music features.')


# In[47]:


print(len(music_features()))


# In[48]:


music_features()[5]


# In[50]:


#import pandas as pd

#music_data = pd.read_csv('data.csv', header = 0)
#music_data.head()


# In[ ]:


#print(load_artist_songs('data.csv'))
#print(len(load_artist_songs('data.csv')))

#with open('data.csv', encoding='utf8') as file:
#    d = {}
    #keys = ['ID']
#    next(file)
#    for line in file:
#        artist_name_start = line.strip().split('[')
#        artist = artist_name_start[1].split(']')
        
        #song_name = csvDetails2[11].csvDetails2[12])
        
#        csvDetails = line.split(',')
        #csvDetails2 = artist[1].strip().split(',')
        
 #       for line in enumerate(csvDetails):
  #          entry = {
                
   #             'ID': csvDetails[6],
    #            'Artists': artist[0],
                #'Song Name': song_name[0],
     #           'Accoustiness': csvDetails[0],
      #          'Danceability': csvDetails[2],
       #         'Energy': csvDetails[4],
        #        'Liveness': csvDetails[9],
         #       'Loudness': csvDetails[10],
          #      'Popularity': csvDetails[13],
           #     'Speechiness': csvDetails[15],
            #    'Tempo': csvDetails[16],
            #    'Valence': csvDetails[17]
            #}

            #d[i+1] = entry
        
       # print(entry)
    #file.close()


# In[ ]:


#with open('data.csv', 'r', encoding='utf8') as file:
#    final_dict = {}
 #   counter=1
 #   next(file) #skips the header
    #for line in file:
    #    Acc = line.split(',')[0:1]
    #    artist_name_start = line.strip().split('[')
    #    artist = artist_name_start[1].split(']')
        
    #    for value in artist:
    #        ID = value.split(',')[5:6]
           # duration = value.split(',')
        
        #Acc = line.split(',')[:1]
        #Name = line.split(',')[12:14]
        
        #csvDetails2 = artist[1].strip().split(',')
        
    #    d = {}
    #    d['ID'] = ID
    #    d['Artists'] = artist[0]
        #d['Song Name'] = csvDetails[12]
    #    d['Accoustiness'] = Acc
        #d['Danceability'] = dance
        #d['Energy'] = csvDetails[4]
        #d['Liveness'] = csvDetails[9]
        #d['Loudness'] = csvDetails[10]
        #d['Popularity'] = csvDetails[13]
        #d['Speechiness'] = csvDetails[15]
        #d['Tempo'] = csvDetails[16]
        #d['Valence'] = csvDetails[17]
   #     final_dict[counter] = d
   #     counter+=1 

    #print(counter)
        
   # print(final_dict[ID])
   # file.close()


# In[ ]:


#def load_song_information():
    


# In[ ]:




