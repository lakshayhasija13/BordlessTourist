# git init
# Initialize git repository

# git add script.py
# git commit -m "initial commit"
# Set up version control

# Task 4: Create list of destinations
destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "Sao Paulo, Brazil", "Cairo, Egypt"]

# Task 5: Create test traveler with name, destination, and interests
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

# git add script.py
# git commit -m "Added test objects"
# Commit test data

# Task 8-10: Define function to get destination index
def get_destination_index(destination):
    """Returns the index of a destination in the destinations list"""
    destination_index = destinations.index(destination)
    return destination_index

# Task 11-13: Test get_destination_index function
print(get_destination_index("Los Angeles, USA"))  # Should print 2
print(get_destination_index("Paris, France"))     # Should print 0
# print(get_destination_index("Hyderabad, India")) # Raises ValueError - not in list

# Task 15-18: Define function to get traveler's destination index
def get_traveler_location(traveler):
    """Returns the destination index for a given traveler"""
    traveler_destination = traveler[1]
    traveler_destination_index = destinations.index(traveler_destination)
    return traveler_destination_index

# Task 19-20: Test get_traveler_location with test_traveler
test_destination_index = get_traveler_location(test_traveler)
print(test_destination_index)  # Should print 1 (Shanghai, China is at index 1)

# git add script.py
# git commit -m "Added logic to find traveler destinations and convert to internal data"
# Commit traveler location functions

# Task 24-26: Create attractions list - empty list for each destination
attractions = [[] for destination in destinations]
print(attractions)  # Should print [[], [], [], [], []]

# Task 27-28: Define function to add attractions to a destination
def add_attraction(destination, attraction):
    """Adds an attraction to the attractions list for a given destination"""
    destination_index = get_destination_index(destination)
    attractions_for_destination = attractions[destination_index]
    attractions_for_destination.append(attraction)
    return

# Task 33-34: Test add_attraction function
add_attraction("Los Angeles, USA", ['Venice Beach', ['beach']])
print(attractions)  # Should show Venice Beach added to LA

# Task 35: Add attractions to various destinations
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("Sao Paulo, Brazil", ["Sao Paulo Zoo", ["zoo"]])
add_attraction("Sao Paulo, Brazil", ["Patio do Colegio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

# git add script.py
# git commit -m "Created attractions and functionality for adding new attractions"
# Commit attractions data and add_attraction function

# Task 38-46: Define function to find attractions matching traveler interests
def find_attractions(destination, interests):
    """Returns list of attraction names matching any of the given interests"""
    destination_index = get_destination_index(destination)
    attractions_in_city = attractions[destination_index]
    attractions_with_interest = []
    
    # Loop through each attraction in the destination
    for possible_attraction in attractions_in_city:
        attraction_tags = possible_attraction[1]  # Get tags at index 1
        
        # Check if any interest matches the attraction tags
        for interest in interests:
            if interest in attraction_tags:
                attractions_with_interest.append(possible_attraction[0])  # Only append name
                break  # Don't add same attraction twice
    
    return attractions_with_interest

# Task 47-48: Test find_attractions function
la_arts = find_attractions("Los Angeles, USA", ['art'])
print(la_arts)  # Should print ['LACMA']

# git add script.py
# git commit -m "Added interest finder logic"
# Commit find_attractions function

# Task 53-62: Define function to generate personalized message for traveler
def get_attractions_for_traveler(traveler):
    """Returns a personalized message with attractions for the traveler"""
    traveler_destination = traveler[1]
    traveler_interests = traveler[2]
    traveler_attractions = find_attractions(traveler_destination, traveler_interests)
    
    # Build the greeting message
    interests_string = "Hi "
    interests_string += traveler[0]  # Add traveler name
    interests_string += ", we think you'll like these places around "
    interests_string += traveler_destination + ": "
    
    # Add each attraction with commas
    for i in range(len(traveler_attractions)):
        if i < len(traveler_attractions) - 1:
            interests_string += traveler_attractions[i] + ", "
        else:
            interests_string += traveler_attractions[i]
    
    interests_string += "."
    return interests_string

# Task 61-62: Test get_attractions_for_traveler function
smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])
print(smills_france)  # Should print personalized message

# git add script.py
# git commit -m "Added function to generate message for traveler and present attractions they might be interested in."
# Commit final traveler attraction function