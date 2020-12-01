#!/usr/bin/env python
# coding: utf-8

# ### PCP Module 1 - load_dataset_module

# In[ ]:


def artist_music():
    import re 
    
    try:
        # defines the opening of the file as read only mode, with encoding as utf-8
        with open('data.csv', 'r', encoding='utf8') as file:
            artist_music_dict = {}
            index=1 # This will be used for the indexable ID
            next(file) #skips the header

            for line in file:
                #Use regex to find all commas at the end of a string
                line = re.sub(r'(?!(([^"]*"){2})*[^"]*$),', "/", line)
                csvData = line.split(',')
        
                #removing the square brackets and single quotes from artists
                artist_names = csvData[1]
                artist_names = [i.strip('[]') for i in artist_names]
                artist_names = [i.strip("\\'") for i in artist_names]
                artist_names = ''.join(artist_names)
        
                # create and populate the dictionary with variables from the file
                d = {}
                d['ID'] = csvData[6]
                d['Artists'] = artist_names
                d['Song Name'] = csvData[12]
                d['Duration'] = csvData[3]
                d['Key'] = csvData[8]
                d['Explicit'] = csvData[5]
                d['Release Date'] = csvData[14]
                d['Accoustiness'] = float(csvData[0])
                d['Danceability'] = float(csvData[2])
                d['Energy'] = float(csvData[4])
                d['Liveness'] = float(csvData[9])
                d['Loudness'] = float(csvData[10])
                d['Popularity'] = float(csvData[13])
                d['Speechiness'] = float(csvData[15])
                d['Tempo'] = float(csvData[16])
                d['Valence'] = float(csvData[17])
                # Assign the created dictionary values to a new dictionary with an added iterable index
                artist_music_dict[index] = d
                index+=1 # iterate the index until we reach the end of the file
        
            return artist_music_dict
            file.close()
            
    except IOError as ioerr: # catch any file errors to prevent crashing of the program
        print('File error: ' + str(ioerr))
    finally:
        print('Finished reading the command for artist music.')


# In[ ]:


def music_features():
    import re 
    
    try:
        # defines the opening of the file as read only mode, with encoding as utf-8
        with open('data.csv', 'r', encoding='utf8') as file:
            features_dict = {}
            index=1 # This will be used for the indexable ID
            next(file) #skips the header
            
            for line in file:
                #Use regex to find all commas at the end of a string
                line = re.sub(r'(?!(([^"]*"){2})*[^"]*$),', "/", line)
                csvData = line.split(',')

                # create and populate the dictionary with variables from the file
                d = {}
                d['ID'] = csvData[6]
                d['Song Name'] = csvData[12]
                d['Accoustiness'] = float(csvData[0])
                d['Danceability'] = float(csvData[2])
                d['Energy'] = float(csvData[4])
                d['Liveness'] = float(csvData[9])
                d['Loudness'] = float(csvData[10])
                d['Popularity'] = float(csvData[13])
                d['Speechiness'] = float(csvData[15])
                d['Tempo'] = float(csvData[16])
                d['Valence'] = float(csvData[17])
                # Assign the created dictionary values to a new dictionary with an added iterable index
                features_dict[index] = d
                index+=1 # iterate the index until we reach the end of the file
        
            return features_dict
            file.close()
            
    except IOError as ioerr: # catch any file errors to prevent crashing of the program
        print('File error: ' + str(ioerr))
    finally:
        print('Finished reading the command for music features.')


# In[ ]:




