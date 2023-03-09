# Create a function that given a list which represents street lights given as a parameter(l_street),
# determine if an outage has occurred.
# A street light is represented as a “T” or “F”.

# A street with a total number of “F” greater than or equal to
# 2 returns “Outage”, anything below returns “Power”

# Example Input
# [ ‘T’, ‘F’, ‘F’, ‘F’ ]
#
# Example Output:
# “Outage”

def streetLights(l_street): #function that takes a parameter
   Fs = l_street.count("F") #counts number of F's in a string
   if Fs >= 2: #if there are 2 or more F's
      print("Outage") #print Outage
   else: #if there are less than 2 F's
      print("Power") #print Power

streetLights(["T", "F", "T", "T"]) #should print Power
streetLights(["T", "F", "F", "F"]) #should print Outage