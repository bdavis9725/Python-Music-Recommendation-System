#!/usr/bin/env python
# coding: utf-8

# ### PCP Assignment 2 Module 2 - similarity_module

# In[ ]:


from load_dataset_module import Artist, Song, Track, IterRegistry, Extras, File_loader # Classes
import pandas as pd
import numpy as np
import math
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.spatial import distance 
from numpy.linalg import norm
from sklearn.metrics.pairwise import manhattan_distances
from sklearn.neighbors import NearestNeighbors as knn
from sklearn.preprocessing import MinMaxScaler

# Disable warnings, these are not required for the user to see (might be removed)
import warnings
warnings.filterwarnings('ignore')


# In[ ]:


class Searcher(object):
    __metaclass__ = IterRegistry
    _registry = []
    
    def __init__(self, list_name):
        self.list_name = list_name
        
    def search_artist(self):
        list_name = self.list_name
        
        try:
            fName = str(input("Please enter the first name of the artist you want to find. Please start with a capital letter: ").strip())
            lName = str(input("Please enter the surname of the artist you want to find. Please start with a capital letter: ").strip())
    
            # Create empty lists for the inputs
            result_names = []
            result_songs = []
            result_id = []
            num = 0 # Index for printing results
            
            # Loop through the dictionary, extract all matching artist + song values
            for i in range(len(list_name)): # range of the whole class-based list
                if lName != "":  # If the last name entry is not left blank
                    if fName + " " + lName in list_name[i].getName():
                        result_names.append(list_name[i].getName())
                        result_songs.append(list_name[i].getSongName())
                        result_id.append(i) 
                else:  # If the artist only has one name e.g. Nirvana
                    if fName in list_name[i].getName():
                        result_names.append(list_name[i].getName())
                        result_songs.append(list_name[i].getSongName())
                        result_id.append(i) 
                
            if len(result_id) == 0: # If the length of the list above is 0, we found no matches
                print("Your search returned no results.")
            else:
                # return an assignable dictionary using the First Name and Surname Initial for the indexable ID
                print("Your search returned {} results.".format(len(result_id)))
                output = str(input("Would you like to view results? ").strip().capitalize())
                if output == "Yes":
                    for k in range(0, len(result_id)):
                        print("ID: {} | {} | {} | ".format(result_id[num], result_names[num], result_songs[num]))
                        num+=1
                else:
                    print("Search complete.")
            
            return result_id  # Return the id to pull details if wanted
    
        # Error handling for the function is written here
        except KeyError:
            return(print("You have entered an incorrect value, please check your entry."))
        except TypeError:
            return(print("You can't enter a number or symbol here, please enter a string dictionary name."))
        except IndexError:
            return(print("You must enter at least an Initial into the Surname box."))
        
    def search_song(self):
        list_name = self.list_name
        
        try:
            song_name = input("Please insert the word/s you would like to find in a song: ").capitalize()
            song_name = song_name.rstrip()   # remove end of input whitespace
            song_name = song_name.split(' ') # split the words into individual words to detect how many we have

            result_id = []
            result_names = []
            result_songs = []
            num = 0 # Index for printing results
        
            if len(song_name) == 1: # Check if the input is 1 word or many words
                song_name = ''.join(song_name) # if it is 1 word, reconnect the word through the join command
                for i in range(0, len(list_name)): # range of the whole class-based list
                    if song_name in list_name[i].getSongName():
                        # Add matching values to assignable lists 
                        result_id.append(i)      
                        result_names.append(list_name[i].getName())
                        result_songs.append(list_name[i].getSongName()) 
                    
            else: # Loop the list and match each word with a value
                for i in range(0, len(list_name)): # range of the whole dictionary +1 as end of dictionary is missed otherwise
                    song_name = [item.capitalize() for item in song_name] # capitalise each string
                    for j in range(0, len(song_name)):
                        if song_name[j] in list_name[i].getSongName(): # search each word for a match
                            # Add matching values to assignable lists
                            result_id.append(i)     
                            result_names.append(list_name[i].getName())
                            result_songs.append(list_name[i].getSongName())

            if len(result_id) == 0: # If the length of the list is 0, we found no matches
                print("Your search returned no results.")
            else:
                print("Your search returned {} results.".format(len(result_id)))
                output = str(input("Would you like to view results? ").strip().capitalize())
                if output == "Yes":
                    for k in range(0, len(result_id)):
                        print("ID: {} | {} | {}".format(result_id[num], result_names[num], result_songs[num]))
                        num+=1
                else:
                    print("Search complete.")
                    
        # Error handling for the function is written here
        except KeyError as keyerror:
            return(print("You have entered an incorrect value, please check your entry.", keyerror))
        except TypeError as typeerror:
            return(print("You can't enter a number or symbol here, please enter a string dictionary name.", typeerror)) 


# In[ ]:


class Similarity_metric(object):
    __metaclass__ = IterRegistry
    _registry = []
    
    def __init__(self, list_name, value1, value2):
        self.list_name = list_name
        self.target = value1
        self.library = value2
        
    # Returns object in string format for readability
    def __repr__(self):
        return f'Target: {self.target}, Comparison: {self.library}'
    
    def euclidean(self):
        a = self.target
        b = self.library
        return np.linalg.norm(a - b)
        
    def manhattan(self):
        a = self.target
        b = self.library
        return manhattan_distances([a, b])[1,0]
        
    def cosine(self):
        a = self.target
        b = self.library
        return 1 - distance.cosine(a, b)

    def jaccard(self):
        a = self.target
        b = self.library
        return distance.jaccard(a, b)
    
    def pearson(self):
        a = self.target
        b = self.library
        return np.corrcoef([a, b])[1,0]
    
    def feature_select(self):
        feature_select = ["Acousticness", "Danceability", "Energy", "Liveness", "Loudness", "Popularity", "Speechiness", "Tempo", "Valence", "Explicit", "Instrumentalness"]
        for number, feature in enumerate(feature_select, start=1):
            print(number, feature) # Present a list of options to the user for feature choice
    
    def metric_choice(self):
        id1 = self.target
        id2 = self.library
        
        metric = int(input("Which metric would you like to use from the selection: Enter the number: "))
        if metric == 1:
            return Similarity_metric(self.list_name, id1, id2).euclidean()
        elif metric == 2:
            return Similarity_metric(self.list_name, id1, id2).cosine()
        elif metric == 3:
            return np.corrcoef([id1, id2]) # Issues with Pearson, do it manually
        elif metric == 4:
            return Similarity_metric(self.list_name, id1, id2).jaccard()
        elif metric == 5:
            return Similarity_metric(self.list_name, [id1], [id2]).manhattan()
        else:
            print("Your selection is incorrect. Defaulting to Euclidean.")
            return Similarity_metric(self.list_name, id1, id2).euclidean()
    
    def metric_selection(self):
        metric_select = ["Euclidean", "Cosine", "Pearson", "Jaccard", "Manhattan"]
        for number, metric in enumerate(metric_select, start=1):
            print(number, metric) # Present a list of options to the user for metric choice 


# In[ ]:


# Part 1 Code is here
class Comparison(Similarity_metric):
    __metaclass__ = IterRegistry
    _registry = []
    
    def __init__(self, list_name, id1, id2):
        self.list_name = list_name
        self.target = id1
        self.library = id2

    def measure_feature(self):
        list_name = self.list_name
        id1 = self.target
        id2 = self.library
        
        try:
            #id1 = id1
            #id2 = id2
            id1 = int(input("Please insert your first id for music features: "))
            id2 = int(input("Please insert your second id for music features: "))

            if id1 == id2: # check to see if the IDs match
                print("Similarity measure for ID {} and ID {} is 1".format(id1, id2))
            else:
                Comparison(list_name, id1, id2).feature_select()
                query = input("Which feature do you want to use for comparison? Enter the feature name or enter 'No' to compare all features. ").strip().capitalize()

                if query == '' or query == "No".strip().capitalize(): # if query entry is no or left empty, go here
                    print("Comparing all respective features. \n")
                    Comparison(list_name, id1, id2).metric_selection()
                    response = int(input("Which metric would you like to use from the selection: Enter the number: "))
                    # take values from the dictionary from the end,to avoid the string values at the beginning
                    feature_list = list(list_name.iloc[id1])
                    feature_list2 = list(list_name.iloc[id2])
                    column_list = [str(i) for i in list_name] # take the associated column names
            
                    for i in range(0,11): # Loop through the 11 expected features
                        # take values over the loop and compare them
                        for value in feature_list, feature_list2: 
                            x = (feature_list[i])
                            y = (feature_list2[i])
                            if response == 1:
                                distance = Comparison(list_name, x, y).euclidean()
                            elif response == 2:
                                distance = Comparison(list_name, x, y).cosine()
                            elif response == 3: # Issues with Pearson, do it manually
                                distance = np.corrcoef([x, y])
                            elif response == 4:
                                distance = Comparison(list_name, x, y).jaccard()
                            else: # Response is 5
                                distance = Comparison(list_name, [x],[y]).manhattan()

                        print(column_list[i] + ':', round(distance, 3)) # print all feature metrics
                else:
                    x = list_name[query][id1]
                    y = list_name[query][id2]
                    Comparison(list_name, id1, id2).metric_selection()
                    distance = Comparison(list_name, x, y).metric_choice() 
                    print("The Similarity of {} for ID {} and ID {} is".format(query, id1, id2), round(distance, 3))
       
        except IndexError:
            print("The ID you entered was too large, please enter a value between 0 and 156608")
        except KeyError as keyerror:
            print("That feature doesn't exist.", keyerror)
            Comparison(list_name, '','').measure_feature()
        except ValueError:
            print("Your entry is invalid, please make sure your entry was the correct format.")
            Comparison(list_name, '','').measure_feature()
        except TypeError:
            print("Invalid type entered.")
        except ZeroDivisionError:
            print("Sorry, but you cannot divide by 0, metric will restart.")
            Comparison(list_name, '','').measure_feature()
        except AttributeError as attrerror:
            print(attrerror)
            Comparison(list_name, '','').measure_feature()


# In[ ]:


class Recommendation(Similarity_metric):
    
    def __init__(self, list_name, class_list):
        self.list_name = list_name
        self.class_list = class_list
        
    def metric_choice(self):
        metric = int(input("Which metric would you like to use from the selection: Enter the number: "))
        if metric == 1:
            return 1
        elif metric == 2:
            return 2
        elif metric == 3:
            return 3
        elif metric == 4:
            return 4
        elif metric == 5:
            return 5
        else:
            print("Your selection is incorrect. Defaulting to Euclidean.")
            return 1 

    def get_artist_recommendation(self):
        try:
            list_name = self.list_name
            class_list = self.class_list
            #scaler = MinMaxScaler() # To normalise the values for the engine
        
            # Define needed variables
            results = []
            id_num = int(input("Please enter the ID number of an artist: "))
            j = 0
            #recom_artists = [] # a set will remove duplicates
        
            Recommendation(list_name, class_list).metric_selection()
            response = Recommendation(list_name, class_list).metric_choice()
            n = int(input("Please specify how many recommendations you want as a multiple of 5: "))
            if n % 5 == 0 and n != 0:
                # Create an array copy of the dataframe
                copy_df = np.array(list_name) 

                # Assign the target
                target = copy_df[id_num]  

                # Remove the entered value from the dataframe using 'drop'
                list_name = list_name.drop([id_num])

                # Apply an array transform to the dataframe
                list_name = np.array(list_name) 
                
                # Loop to get the similarity score for each song against the target
                for i in range(len(list_name)):
                    compare = list_name[i]
                    if response == 1:
                            metric_inUse = Similarity_metric(list_name, target, compare).euclidean()
                    elif response == 2:
                            metric_inUse = Similarity_metric(list_name, target, compare).cosine()
                    elif response == 3: 
                            metric_inUse = Similarity_metric(list_name, target, compare).pearson()
                    elif response == 4:
                            metric_inUse = Similarity_metric(list_name, target, compare).jaccard()
                    else: # Response is 5
                        metric_inUse = Similarity_metric(list_name, target, compare).manhattan()
                
                    results.append(metric_inUse)

                if response == 1 or response == 4 or response == 5:
                    sorted_results = sorted(range(len(results)), key=lambda x: results[x], reverse=False)
                else:
                    # Sort the results, if cosine or pearson we need to reverse these results
                    sorted_results = sorted(range(len(results)), key=lambda x: results[x], reverse=True)
    
                # Print the chosen artist to the user
                print('Your Chosen '+ class_list[id_num].getName())
                print('The {} most similar artists to your chosen artist are: '.format(n))

                # Print the n recommendations for the user
                for element in sorted_results:
                    # Skip if the artist name is the same as the target
                    if class_list[element].getName() == class_list[id_num].getName():
                        continue
                    
                    print(class_list[element].getName())
                    j += 1
                    if j >= n:
                        break
            else:
                print("Please select an n value as a multiple of 5. Entry cannot be 0.")
                Recommendation(list_name, class_list).get_artist_recommendation()
                
        except IndexError:
            print("The ID you entered was too large, please enter a value between 0 and 156608")
            Recommendation(list_name, class_list).get_artist_recommendation()
        except ValueError:
            print("Your entry is invalid, please make sure your entry was the correct format.")
            Recommendation(list_name, class_list).get_artist_recommendation()
        except TypeError:
            print("Invalid type entered.")
            Recommendation(list_name, class_list).get_artist_recommendation()
    
    def get_song_recommendation(self):
        try:
            list_name = self.list_name
            class_list = self.class_list
            #scaler = MinMaxScaler()
        
            # Define needed variables
            results = []
            id_num = int(input("Please enter the ID number of a song: "))
            j = 0
        
            Recommendation(list_name, class_list).metric_selection()
            response = Recommendation(list_name, class_list).metric_choice()
            n = int(input("Please specify how many recommendations you want as a multiple of 5: "))
            if n % 5 == 0 and n != 0:
                # Create an array copy of the dataframe
                copy_df = np.array(list_name) 

                # Assign the target
                target = copy_df[id_num]  

                # Remove the entered value from the dataframe using 'drop'
                list_name = list_name.drop([id_num])

                # Apply an array transform to the dataframe
                list_name = np.array(list_name) 
                
                # Loop to get the similarity score for each song against the target
                for i in range(len(list_name)):
                    compare = list_name[i]
                    if response == 1:
                            metric_inUse = Similarity_metric(list_name, target, compare).euclidean()
                    elif response == 2:
                            metric_inUse = Similarity_metric(list_name, target, compare).cosine()
                    elif response == 3: 
                            metric_inUse = Similarity_metric(list_name, target, compare).pearson()
                    elif response == 4:
                            metric_inUse = Similarity_metric(list_name, target, compare).jaccard()
                    else: # Response is 5
                        metric_inUse = Similarity_metric(list_name, target, compare).manhattan()
            
                    results.append(metric_inUse)

                if response == 1 or response == 4 or response == 5:
                    sorted_results = sorted(range(len(results)), key=lambda x: results[x], reverse=False)
                else:
                    # Sort the results, if cosine or pearson we need to reverse these results
                    sorted_results = sorted(range(len(results)), key=lambda x: results[x], reverse=True)
    
                # Print the chosen artist to the user
                print('Your Chosen '+ class_list[id_num].getSongName())
                print('The {} most similar songs to your song are: '.format(n))
    
                # Print the n recommendations for the user
                for element in sorted_results:
                    print(class_list[element].getSongName(), "by", class_list[element].getName())
                    j += 1
                    if j >= n:
                        break
            else:
                print("Please select an n value as a multiple of 5. Entry cannot be 0.")
                Recommendation(list_name, class_list).get_song_recommendation()    
    
        except IndexError:
            print("The ID you entered was too large, please enter a value between 0 and 156608")
            Recommendation(list_name, class_list).get_song_recommendation()
        except ValueError:
            print("Your entry is invalid, please make sure your entry was the correct format.")
            Recommendation(list_name, class_list).get_song_recommendation()
        except TypeError:
            print("Invalid type entered.")
            Recommendation(list_name, class_list).get_song_recommendation()
    
    def get_target_recommendation(self):
        try:
            list_name = self.list_name
            class_list = self.class_list
            #scaler = MinMaxScaler()

            # Define needed variables
            results = []
            id_num = int(input("Please enter the ID number of the artist: "))
            j = 0

            Recommendation(list_name, class_list).metric_selection()
            response = Recommendation(list_name, class_list).metric_choice()
            n = int(input("Please specify how many recommendations you want as a multiple of 5: "))
            if n % 5 == 0 and n != 0:
                # Create an array copy of the dataframe
                copy_df = np.array(list_name) 

                # Assign the target
                target = copy_df[id_num]  

                # Remove the entered value from the dataframe using 'drop'
                list_name = list_name.drop([id_num])

                # Apply an array transform to the dataframe
                list_name = np.array(list_name) 

                # Loop to get the similarity score for each song against the target
                for i in range(len(list_name)):
                    compare = list_name[i]
                    if response == 1:
                            metric_inUse = Similarity_metric(list_name, target, compare).euclidean()
                    elif response == 2:
                            metric_inUse = Similarity_metric(list_name, target, compare).cosine()
                    elif response == 3: # Issues with Pearson, do it manually
                            metric_inUse = Similarity_metric(list_name, target, compare).pearson()
                    elif response == 4:
                            metric_inUse = Similarity_metric(list_name, target, compare).jaccard()
                    else: # Response is 5
                        metric_inUse = Similarity_metric(list_name, target, compare).manhattan()

                    results.append(metric_inUse)

                if response == 1 or response == 4 or response == 5:
                    sorted_results = sorted(range(len(results)), key=lambda x: results[x], reverse=False)
                else:
                    # Sort the results, if cosine or pearson we need to reverse these results
                    sorted_results = sorted(range(len(results)), key=lambda x: results[x], reverse=True)

                # Print the chosen artist to the user
                print('Your Chosen '+ class_list[id_num].getName())
                print('The {} most similar Tracks to your Artist are: '.format(n))

                # Print the n recommendations for the user
                for element in sorted_results:
                    print(class_list[element].getSongName(), "by", class_list[element].getName())
                    j += 1
                    if j >= n:
                        break
            else:
                print("Please select an n value as a multiple of 5. Entry cannot be 0.")
                Recommendation(list_name, class_list).get_target_recommendation()
                
        except IndexError:
            print("The ID you entered was too large, please enter a value between 0 and 156608")
            Recommendation(list_name, class_list).get_target_recommendation()
        except ValueError:
            print("Your entry is invalid, please make sure your entry was the correct format.")
            Recommendation(list_name, class_list).get_target_recommendation()
        except TypeError:
            print("Invalid type entered.")
            Recommendation(list_name, class_list).get_target_recommendation()

    def get_knn_recommendation(self):
        try:
            list_name = self.list_name
            class_list = self.class_list
            #scaler = MinMaxScaler()

            # Define needed variables
            results = []
            id_num = int(input("Please enter the ID number of the artist: "))
            j = 0

            Recommendation(list_name, class_list).metric_selection()
            response = Recommendation(list_name, class_list).metric_choice()
            n = int(input("Please specify how many recommendations you want as a multiple of 5: "))
            if n % 5 == 0 and n != 0:
                # Create an array copy of the dataframe
                copy_df = np.array(list_name) 

                # Assign the target
                target = copy_df[id_num]  
                target = target.reshape(1,-1)

                # Remove the entered value from the dataframe using 'drop'
                list_name = list_name.drop([id_num])

                # Apply an array transform to the dataframe
                list_name = np.array(list_name) 

                # The metric choice decides which metric is used for the KNN
                if response == 1:
                    chosen_metric = "euclidean"
                elif response == 2:
                    chosen_metric = "cosine"
                elif response == 3: 
                    chosen_metric = "correlation"
                elif response == 4:
                    chosen_metric = "jaccard"
                else: # Response is 5
                    chosen_metric = "manhattan"

                # Print the chosen artist to the user
                print('Your Chosen '+ class_list[id_num].getName())
                print('The {} most similar Tracks to your Artist are: '.format(n))

                # Print n results to the user
                neigh = knn(metric = chosen_metric, n_neighbors = n, n_jobs=1)
                neigh.fit(list_name)   
                knn_result = neigh.kneighbors(target, return_distance=False)
                knn_result = knn_result.flatten()
                for element in knn_result:
                    print(class_list[element].getName(), class_list[element].getSongName())

            else:
                print("Please select an n value as a multiple of 5. Entry cannot be 0.")
                Recommendation(list_name, class_list).get_knn_recommendation()    
            
        except IndexError:
            print("The ID you entered was too large, please enter a value between 0 and 156608")
            Recommendation(list_name, class_list).get_knn_recommendation()
        except ValueError:
            print("Your entry is invalid, please make sure your entry was the correct format.")
            Recommendation(list_name, class_list).get_knn_recommendation()
        except TypeError:
            print("Invalid type entered.")
            Recommendation(list_name, class_list).get_knn_recommendation()

