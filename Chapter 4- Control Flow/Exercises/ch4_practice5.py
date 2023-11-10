# elif statement

month = input("Enter a month (e.g., January, February, etc.): ")

month = month.lower()

if month in ["december", "january", "february"]:
    season = "Winter"
elif month in ["march", "april", "may"]:
    season = "Spring"
elif month in ["june", "july", "august"]:
    season = "Summer"
elif month in ["september", "october", "november"]:
    season = "Fall"
else:
    season = "Unknown"

if season == "Unknown":
    print("The provided month is not valid.")
else:
    print(f"The season for {month.capitalize()} is {season}.")
