#!/usr/bin/env python
# coding: utf-8

# ### PCP Module 2 - similarity_module

# In[ ]:


def search_artist(dict_name):
    try:
        fName = str(input("Please enter the first name of the artist you want to find: ").capitalize().rstrip())
        lName = str(input("Please enter the surname of the artist you want to find (entry can be left blank). If the first name of both artists is the same, you will need to enter a surname initial: "                         ).capitalize().rstrip())
        feature = str(input("Please enter the feature you want to find for the artists' songs: ").capitalize().rstrip())
    
        # Create empty dictionary and lists for the inputs
        results_dict = {}
        results = []
        # Loop through the dictionary, extract all matching artist + song values
        for i in range(1, len(dict_name)+1): # range of the whole dictionary +1 as end of dictionary is missed otherwise
            if fName + " " + lName in dict_name[i]['Artists']:
                print("ID:", i, "|", "Artist/s:", dict_name[i]['Artists'], "|", "Song:", dict_name[i]['Song Name'])
                results.append(dict_name[i][feature]) # Add matching feature values to an assignable list
                
        if len(results) == 0: # If the length of the list above is 0, we found no matches
            return None       # So we will simply return nothing
        else:
            # return an assignable dictionary using the First Name and Surname Initial for the indexable ID
            results_dict[fName + " " + lName[0]] = results
    
        return results_dict # return the created nested dictionary
    
    # Error handling for the function is written here
    except KeyError:
        return(print("You have entered an incorrect value, please check your entry."))
    except TypeError:
        return(print("You can't enter a number or symbol here, please enter a string dictionary name."))


# In[ ]:


def search_song(dict_name):
    try:
        song_name = input("Please insert the word/s you would like to find in a song: ").capitalize()
        song_name = song_name.rstrip()   # remove end of input whitespace
        song_name = song_name.split(' ') # split the words into individual words to detect how many we have

        if len(song_name) == 1: # Check if the input is 1 word or many words
            song_name = ''.join(song_name) # if it is 1 word, reconnect the word through the join command
            for i in range(1, len(dict_name)+1): # range of the whole dictionary +1 as end of dictionary is missed otherwise
                if song_name in dict_name[i]['Song Name']:
                    print("ID:", i, "|", "Artist/s:", dict_name[i]['Artists'], "|", "Song:", dict_name[i]['Song Name'])   
        else: # Loop the list and match each word with a value
            for i in range(1, len(dict_name)+1): # range of the whole dictionary +1 as end of dictionary is missed otherwise
                song_name = [item.capitalize() for item in song_name] # capitalise each string
                for j in range(1, len(song_name)):
                    if song_name[j] in dict_name[i]['Song Name']:
                        print("ID:", i, "|", "Artist/s:", dict_name[i]['Artists'], "|", "Song:", dict_name[i]['Song Name'])
                    else:
                        pass
                    
                    #song_search = any(item in song_name for item in .split(','))
                    #if song_search == True:
                        
                    #else:
                    #    pass
                
                        #if song_name[j] in dict_name[i]['Song Name']: # For each word in the list, search the dictionary for matches
                #print("ID:", i, "|", "Artist/s:", dict_name[i]['Artists'], "|", "Song:", dict_name[i]['Song Name'])   
        
    # Error handling for the function is written here
    except KeyError as keyerror:
        return(print("You have entered an incorrect value, please check your entry.", keyerror))
    except TypeError as typeerror:
        return(print("You can't enter a number or symbol here, please enter a string dictionary name.", typeerror)) 


# In[ ]:


def join_artist_dict(dict_a, dict_b): # Function to join two lists together, maintaining unique keys
    try:
        dict_a = dict_a
        dict_b = dict_b
        dict_a.update(dict_b)
        return dict_a
    
    # Error handling for the function is written here
    except KeyError:
        return(print("You have entered an incorrect value, please check your entry."))
    except TypeError:
        return(print("You can't enter a number or symbol here, please enter a string dictionary name."))


# ## Euclidean Similarity Function 

# ![image.png](attachment:image.png)

# In[ ]:


def euclidean_similarity(dict_name, id1, id2):
    import math
    
    try:   
        dict_name = dict_name
    
        if id1 == '': # If the positional argument is entered as '', then ask for an int ID
            id1 = int(input("Please insert your first id for music features: "))
        else:
            id1 = id1
        
        if id2 == '': # If the positional argument is entered as '', then ask for an int ID
            id2 = int(input("Please insert your second id for music features: "))
        else:
            id2 = id2
                
        if id1 == id2: # check to make sure the user is not entering the same ID twice
            print("You can't have the same ID, please choose 2 different IDs.")
        else:
            print("If you are working with defined artist lists, enter 'Yes'")
            query = input("Do you want to compare a specific feature? Enter no or leave the entry blank if you want to compare all features. ").capitalize()

            if query == '' or query == "No".capitalize(): # if query entry is no or left empty, go here
                print("Comparing all respective features.\n")
                # take values from the dictionary from the end,to avoid the string values at the beginning
                feature_list = list(dict_name[id1].values())[-9:] 
                feature_list2 = list(dict_name[id2].values())[-9:]
                key_list = str(list(dict_name[id1].keys())[-9:]).split(',') # take the associated key names
            
                for i in range(0,9): # Loop through the 9 expected features
                    for value in feature_list, feature_list2: # take values over the loop and compare them
                        x = (feature_list[i]) 
                        y = (feature_list2[i]) 
                        distance = math.sqrt((x - y) ** 2 ) #one-dimensional euclidean formula
                    print(key_list[i].strip('[]').strip(' '), round(distance, 3)) # print all feature metrics
            
            else:
                if query == 'Yes' and len(dict_name) == 2: # must be working with chosen artists
                    x = []
                    y = []
                    
                    # To avoid issues with math such as sqrt, create 2 new lists and assign all values to those lists
                    for value in dict_name[id1]:
                        x.append(value)
                    for value in dict_name[id2]:
                        y.append(value)
                    distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)])) # multi-dimensional euclidean
                    return(print("Euclidean distance from x to y:", round(distance, 3)))
                
                else: # must be working with default dictionary and values
                    # Assign our queried features to our x and y variables
                    x = dict_name[id1][query]
                    y = dict_name[id2][query]
                    distance = math.sqrt((x - y) ** 2 ) #one-dimensional euclidean formula   
                    print("Euclidean Distance of", query, "is", round(distance, 3))
            
    # Error handling for the function is written here
    except KeyError as keyerror:
        print("That feature doesn't exist.", keyerror)
    except ValueError as valueerror:
        print("Your entry is invalid, please make sure your entry was the correct format.")
    except TypeError as typeerror:
        print("Invalid type entered.")
    except IndexError:
        print("There was a problem, did you enter your dictionary name correctly?")
    except ZeroDivisionError:
        print("Sorry, but you cannot divide by 0.")
    except AttributeError:
        print("You can't compare all features of an artist you have defined.")


# ## Cosine Similarity Function

# ![image.png](attachment:image.png)

# In[ ]:


def cosine_similarity(dict_name, id1, id2):
    import math
    
    def square_rooted(x): # define the sqrt for the cosine function
        return round(math.sqrt(sum([a*a for a in x])),3)
    
    def cosine(x, y): # define the cosine function to avoid re-using code
        numerator = sum(a*b for a,b in zip(x,y))
        denominator = square_rooted(x)*square_rooted(y)
        return round(numerator/float(denominator),3)
    
    try:   
        dict_name = dict_name
    
        if id1 == '': # If the positional argument is entered as '', then ask for an int ID
            id1 = int(input("Please insert your first id for music features: "))
        else:
            id1 = id1
        
        if id2 == '': # If the positional argument is entered as '', then ask for an int ID
            id2 = int(input("Please insert your second id for music features: "))
        else:
            id2 = id2
                
        if id1 == id2: # check to make sure the user is not entering the same ID twice
            print("You can't have the same ID, please choose 2 different IDs.")
        else:
            print("If you are working with defined artist lists, enter 'Yes'")
            query = input("Do you want to compare a specific feature? Enter no or leave the entry blank if you want to compare all features. ").capitalize()

            if query == '' or query == "No".capitalize(): # if query entry is no or left empty, go here
                print("Comparing all respective features.\n")
                # take values from the dictionary from the end,to avoid the string values at the beginning
                feature_list = list(dict_name[id1].values())[-9:]
                feature_list2 = list(dict_name[id2].values())[-9:]
                key_list = str(list(dict_name[id1].keys())[-9:]).split(',') # take the associated key names
            
                for i in range(0,9): # Loop through the 9 expected features
                    for value in feature_list, feature_list2: # take values over the loop and compare them
                        if i == 5: #divisible by zero issue comes up if this is not present
                            continue
                        x = (feature_list[i]) 
                        y = (feature_list2[i]) 
                        distance = cosine([x],[y]) # Use the cosine function defined above to get the metric
                    print(key_list[i].strip('[]').strip(' '), round(distance, 3)) # print all feature metrics
            
            else: 
                if query == 'Yes' and len(dict_name) == 2: # must be working with chosen artists
                    x = []
                    y = []
                
                    # To avoid issues with math such as sqrt, create 2 new lists and assign all values to those lists
                    for value in dict_name[id1]:
                        x.append(value)
                    for value in dict_name[id2]:
                        y.append(value)
                    
                    distance = cosine(x,y) # Use the cosine function defined above to get the metric
                    print("Cosine Similarity of x and y is:", round(distance, 3))
                    
                else: # must be working with default dictionary
                    # Assign our queried features to our x and y variables
                    x = dict_name[id1][query] 
                    y = dict_name[id2][query]
                
                    distance = cosine([x],[y]) # Use the cosine function defined above to get the metric
                    print("Cosine Similarity of", query, "is", round(distance, 3))
    
    # Error handling for the function is written here
    except KeyError as keyerror:
        print("That feature doesn't exist.", keyerror)
    except ValueError as valueerror:
        print("Your entry is invalid, please make sure your entry was the correct format.", valueerror)
    except TypeError as typeerror:
        print("Invalid type entered.")
    except IndexError:
        print("There was a problem, did you enter your dictionary name correctly?")
    except ZeroDivisionError:
        print("Sorry, but you cannot divide by 0.")
    except AttributeError:
        print("You can't compare all features of an artist you have defined.")


# ## Pearson Correlation Similarity Function

# ![image.png](attachment:image.png)

# In[ ]:


def pearson_similarity(dict_name, id1, id2):
    import math
    import numpy as np
    
    try:   
        dict_name = dict_name
    
        if id1 == '': # If the positional argument is entered as '', then ask for an int ID
            id1 = int(input("Please insert your first id for music features: "))
        else:
            id1 = id1
        
        if id2 == '': # If the positional argument is entered as '', then ask for an int ID
            id2 = int(input("Please insert your second id for music features: "))
        else:
            id2 = id2
                
        if id1 == id2: # check to make sure the user is not entering the same ID twice
            print("You can't have the same ID, please choose 2 different IDs.")
        else:
            print("If you are working with defined artist lists, enter 'Yes'")
            query = input("Do you want to compare a specific feature? Enter no or leave the entry blank if you want to compare all features. ").capitalize()

            if query == '' or query == "No".capitalize(): # if query entry is no or left empty, go here
                print("Comparing all respective features.\n")
                # take values from the dictionary from the end,to avoid the string values at the beginning
                feature_list = list(dict_name[id1].values())[-9:]
                feature_list2 = list(dict_name[id2].values())[-9:]
                key_list = str(list(dict_name[id1].keys())[-9:]).split(',') # take the associated key names
            
                for i in range(0,9): # Loop through the 9 expected features
                    for value in feature_list, feature_list2: # take values over the loop and compare them
                        if i == 5: #skip popularity
                            continue
                        x = (feature_list[i]) 
                        y = (feature_list2[i]) 
                        n = len(feature_list) # create our n value, in this case this would have a value of 9
                        
                        # creating the correlation formula in rough form
                        numerator = n*(x + y) - (x * y)
                        denominator = ((n*(x**2)) - (x)**2) * ((n*(y**2)) - (y**2))

                        # This result won't be accurate
                        #pearson_corr = (numerator / math.sqrt(denominator))
                        # Due to issues, numpy correlation will be used instead to get the output
                        pearson_corr = np.corrcoef([x, y])

                    print(key_list[i].strip('[]').strip(' '), pearson_corr) # print all feature metrics
            
            else:
                # This is not possible unless the two artists 
                # have the exact same number of songs in the dictionary
                if query == 'Yes' and len(dict_name) == 2: # must be working with chosen artists
                    x = []
                    y = []
                    
                    # To avoid issues with math, create 2 new lists and assign all values to those lists
                    for value in dict_name[id1]:
                        x.append(value)
                    for value in dict_name[id2]:
                        y.append(value)
     
                    # Due to issues, numpy correlation will be used instead to get the output
                    pearson_corr = np.corrcoef(x,y)
                    return(pearson_corr)
                
                else: # must be working with default dictionary and values
                    # Assign our queried features to our x and y variables
                    x = dict_name[id1][query]
                    y = dict_name[id2][query]
                    n = 1 
               
                    # creating the correlation formula in rough form
                    numerator = n*(x + y) - (x * y)
                    denominator = ((n*(x**2)) - (x)**2) * ((n*(y**2)) - (y**2))
                
                    # There will be an error here, as we will always divide by 0 with a length of 1
                    #pearson_corr = (numerator / math.sqrt(denominator))
                    # Due to issues, numpy correlation will be used instead to get the output
                    pearson_corr = np.corrcoef([x,y])
                    return(pearson_corr)
    
    # Error handling for the function is written here
    except KeyError as keyerror:
        print("That feature doesn't exist.", keyerror)
    except ValueError as valueerror:
        print("Your entry is invalid, please make sure your entry was the correct format.", valueerror)
    except TypeError as typeerror:
        print("Invalid type entered.")
    except IndexError:
        print("There was a problem, did you enter your dictionary name correctly?")
    except ZeroDivisionError as zeroerror:
        print("Sorry, but you cannot divide by 0.")
    except AttributeError:
        print("You can't compare all features of an artist you have defined.")


# In[ ]:


# Code left for analysis, working example with same lengths lists to compare

#x = [5,10, 43, 12, 89, 100, 21, 89, 71]
#y = [2,4, 12, 13, 43, 54, 65, 77, 100, 1000]
#n = 10
#
#import math
#
#sum_xy = []
#x2 = []
#y2 = []
#
#for num1, num2 in zip(x, y):
#    sum_xy.append(num1 * num2)
#sum_xy = sum(sum_xy)
#
#numerator = n*(sum_xy) - (sum(x)*sum(y))
#
#x2 = [i **2 for i in x]
#y2 = [i **2 for i in y]
#
#denominator = ((n*sum(x2)) - (sum(x)**2)) * ((n*sum(y2)) - (sum(y)**2))
#print(numerator / math.sqrt(denominator))


# ## Jaccard Similarity Function

# J(A, B) = |A∩B| / |A∪B|

# In[ ]:


def jaccard_similarity(dict_name, id1, id2):
    import math
    
    def jaccard(x, y): # define the jaccard function to avoid re-using code
        intersection = len(list(set(x).intersection(y)))
        union = (len(x) + len(y)) - intersection
        return float(intersection) / union
    
    try:   
        dict_name = dict_name
    
        if id1 == '': # If the positional argument is entered as '', then ask for an int ID
            id1 = int(input("Please insert your first id for music features: "))
        else:
            id1 = id1
        
        if id2 == '': # If the positional argument is entered as '', then ask for an int ID
            id2 = int(input("Please insert your second id for music features: "))
        else:
            id2 = id2
                
        if id1 == id2: # check to make sure the user is not entering the same ID twice
            print("You can't have the same ID, please choose 2 different IDs.")
        else:
            print("If you are working with defined artist lists, enter 'Yes'")
            query = input("Do you want to compare a specific feature? Enter no or leave the entry blank if you want to compare all features. ").capitalize()

            if query == '' or query == "No".capitalize(): # if query entry is no or left empty, go here
                print("Comparing all respective features.\n")
                # take values from the dictionary from the end,to avoid the string values at the beginning
                feature_list = list(dict_name[id1].values())[-9:]
                feature_list2 = list(dict_name[id2].values())[-9:]
                key_list = str(list(dict_name[id1].keys())[-9:]).split(',') # take the associated key names
            
                for i in range(0,9): # Loop through the 9 expected features
                    for value in feature_list, feature_list2: # take values over the loop and compare them
                        x = (feature_list[i]) 
                        y = (feature_list2[i]) 
                        distance = jaccard([x],[y]) # Use the jaccard function defined above to get the metric
                        # print all feature metrics
                    print("Jaccard Similarity:", key_list[i].strip('[]').strip(' '), round(distance, 3))
                    #print("Jaccard Distance:  ", key_list[i].strip('[]').strip(' '), (1 - round(distance, 3)))
            
            else:
                if query == 'Yes' and len(dict_name) == 2: # must be working with chosen artists
                    # Assign each artist to a different value of x or y
                    x = dict_name[id1]
                    y = dict_name[id2]
                        
                    distance = jaccard(x,y) # Use the jaccard function defined above to get the metric
                    return(print("Jaccard Similarity of x to y:", round(distance,3)))
                
                else: # must be working with default dictionary and values
                    # Assign our queried features to our x and y variables
                    x = dict_name[id1][query]
                    y = dict_name[id2][query]
                    
                    distance = jaccard([x],[y]) # Use the jaccard function defined above to get the metric
                    print("Jaccard Similarity of", query, "is", round(distance, 3))
                    #print("Jaccard Distance of", query, "is", (1 - round(distance, 3)))
    
    # Error handling for the function is written here
    except KeyError as keyerror:
        print("That feature doesn't exist.", keyerror)
    except ValueError as valueerror:
        print("Your entry is invalid, please make sure your entry was the correct format.")
    except TypeError as typeerror:
        print("Invalid type entered.")
    except IndexError:
        print("There was a problem, did you enter your dictionary name correctly?")
    except ZeroDivisionError:
        print("Sorry, but you cannot divide by 0.")
    except AttributeError:
        print("You can't compare all features of an artist you have defined.")


# ## Manhattan Similarity Function

# ![image.png](attachment:image.png)

# In[ ]:


def manhattan_similarity(dict_name, id1, id2):
    import math
    
    try:   
        dict_name = dict_name
    
        if id1 == '': # If the positional argument is entered as '', then ask for an int ID
            id1 = int(input("Please insert your first id for music features: "))
        else:
            id1 = id1
        
        if id2 == '': # If the positional argument is entered as '', then ask for an int ID
            id2 = int(input("Please insert your second id for music features: "))
        else:
            id2 = id2
                
        if id1 == id2: # check to make sure the user is not entering the same ID twice
            print("You can't have the same ID, please choose 2 different IDs.")
        else:
            print("If you are working with defined artist lists, enter 'Yes'")
            query = input("Do you want to compare a specific feature? Enter no or leave the entry blank if you want to compare all features. ").capitalize()

            if query == '' or query == "No".capitalize(): # if query entry is no or left empty, go here
                print("Comparing all respective features.\n")
                # take values from the dictionary from the end,to avoid the string values at the beginning
                feature_list = list(dict_name[id1].values())[-9:]
                feature_list2 = list(dict_name[id2].values())[-9:]
                key_list = str(list(dict_name[id1].keys())[-9:]).split(',') # take the associated key names
            
                for i in range(0,9): # Loop through the 9 expected features
                    for value in feature_list, feature_list2: # take values over the loop and compare them
                        x = (feature_list[i]) 
                        y = (feature_list2[i]) 
                        distance = abs(x - y) #one-dimensional manhattan
                    print(key_list[i].strip('[]').strip(' '), round(distance, 3)) # print all feature metrics
            
            else:
                if query == 'Yes' and len(dict_name) == 2: # must be working with chosen artists
                    # Assign each artist to a different value of x or y
                    x = dict_name[id1]
                    y = dict_name[id2]
                    
                    distance = abs(sum([(a - b) for a, b in zip(x, y)])) # Multi-dimensional manhattan
                    return(print("Manhattan Distance from x to y:", round(distance,3)))
                
                else: # must be working with default dictionary and values
                    # Assign our queried features to our x and y variables
                    x = dict_name[id1][query]
                    y = dict_name[id2][query]
                
                distance = abs(x - y) #one-dimensional manhattan  
                return(print("Manhattan Distance of", query, "is", round(distance, 3)))
    
    # Error handling for the function is written here
    except KeyError as keyerror:
        print("That feature doesn't exist.", keyerror)
    except ValueError as valueerror:
        print("Your entry is invalid, please make sure your entry was the correct format.")
    except TypeError as typeerror:
        print("Invalid type entered.")
    except IndexError:
        print("There was a problem, did you enter your dictionary name correctly?")
    except ZeroDivisionError:
        print("Sorry, but you cannot divide by 0")
    except AttributeError:
        print("You can't compare all features of an artist you have defined.")

