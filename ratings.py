"""Restaurant rating lister."""

filename = "scores.txt"


def list_restaurant_ratings():

    """TODO: prints Restaurants and ratings in alphabetical order by Restaurants"""
    #Create a restaurant dictionary
    restaurant_dict = {}
    #Opening a file to read and calling it restaurant file
    resturant_file = open(filename, "r")
    #Iterating through each line in the restaurant file
    for line in resturant_file:
        #We are removing the last character and then splitting on the colon and storing it in a list
        restaurant_list = line.strip().split(":")
        #We are storing the key as the rest name and the rating as the value in a dictionary called restaurant_dict
        restaurant_dict[restaurant_list[0]] = restaurant_list[1]
    #cestaurant_dictitem() returns a list of tuple of all key/value pairs in dic
    #sort the list, saving it in sort_restaurant_list
    sort_restaurant_list = sorted(restaurant_dict.items())
    #iterating through list and printing
    for restaurant in sort_restaurant_list:
        #printing out the formatted string
        print "This is the restaurant: " + restaurant[0] + " and the rating is: " + restaurant[1]

list_restaurant_ratings()
