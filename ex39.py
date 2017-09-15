states= {
    "Oregon" : "OR",
    "Florida": "FL",
    "California": "CA",
    "New York": "NY",
    "Michigan": "MI"
}

cities = {
    "CA": "San Francisco" ,
    "MI" : "Detroit" ,
    "FL" : "Jacksonville"
}

cities["NY"] = "New York"
cities["OR"] = "Portland"

print "NY State has: ", cities["NY"]
print "OR State has:" , cities["OR"]
print
print "Michigan is" , states["Michigan"]
print "Florida is", states["Florida"]
print
print "City state: ", cities[states['Michigan']]
print
for state, abbrev in states.items():
    print "%s is abbreviated %s " % (state, abbrev)
