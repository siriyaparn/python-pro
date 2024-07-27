# Nesting
capitals = {
    "France":"Paris",
    "Germany":"Berlin"
}

# Nesting a List in a Dictionary
travel_log = {
    "France":["Paris", "Lille", "Dijon"],
    "German":["Berlin", "Hamburg", "Stuttgart"]
}

# Nesting a Dictionary in a Dictionary
travel_log = {
    "France":{"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "German":{"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits":5}
}

# Nesting a Dictionary in a List
travel_log = [
    {
        "country":"France", 
        "cities_visited": ["Paris", "Lille", "Dijon"], 
        "total_visits": 12
    },
    {
        "country":"German", 
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits":5
    }
]