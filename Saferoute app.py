print("SAFEROUTE APP")

routes={
    "college road":7,
    "market area":6,
    "hospital road":8,
    "bus stand":5,
    "park street":9,
    "supermarket road":6
}

current_location=input("enter current location:")
destination=input("enter a destination:")

if destination in routes:
    score=routes[destination]

    print("ROUTE:",destination)
    print("SAFETY SCORE:",score)

    if score>=7:
        print("status:SAFE ROUTE")
    elif score>=5:
        print("status:MODERATE ROUTE")
    else:
        print("status:RISKY ROUTE")
else:
    print("Destination not available in this route")
    
    
