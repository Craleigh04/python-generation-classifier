def getGeneration(birthYearParm): 
    if birthYearParm <= 1946 and birthYearParm >= 1928: 
        return ("silent generation.")
    elif birthYearParm <= 1965 and birthYearParm >= 1947: 
        return ("boomer generation ")
    elif birthYearParm <= 1981 and birthYearParm >= 1966:
        return ("gen x generation")
    elif birthYearParm <= 1998 and birthYearParm >= 1982: 
        return ("millenial generation")
    elif birthYearParm <= 2014 and birthYearParm >= 1999: 
        return ("Post-millenial generation")
    else: 
        return ("Please enter your correct birth year in YYYY Format")

#to do 1 - implement the remaning if statements using elif syntax
