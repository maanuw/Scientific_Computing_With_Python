def add_time(start, duration, day = None):
    days = {1:"Sunday", 2:"Monday", 3:"Tuesday", 4:"Wednesday" , 5:"Thursday", 6:"Friday", 7:"Saturday"}
    start_time = start.split(" ")
    durat = duration.split(":")
    time = start_time[0].split(":")

    given = False
    #lowercase input from Day parameter and makes first character uppercase.
    if day!=None:
        day = day.lower()
        day = day.capitalize()
        i=1
        for i in range(1, 8):
            if days[i] == day:
                given=True
                givendayvalue = i
    #print(given)
                
    #Adjust mins and hours in duration.
    if int(durat[1]) >=60:
        hrs = int(durat[1])//60
        mins = int(durat[1])%60
        durat[0]=str(hrs)
        durat[1]=str(mins)
        
    #convert start time to military format.  
    if start_time[1] == "PM" and time[0]!=12:
        military = int(time[0]) + 12
    else:
        military = int(time[0])

    #Add duration time to converted military time.
    totalmilitaryhrs = military + int(durat[0])
    totalmins = int(time[1]) + int(durat[1])
    

    #Adjust total minutes to hours if applicable.
    if totalmins >= 60:
        totalmilitaryhrs = totalmilitaryhrs + (totalmins//60)
        totalmins = totalmins%60
    if totalmins < 10:
            totalmins = "0" + str(totalmins)
    
    #Calculating same day time.
    if totalmilitaryhrs < 24:
        if totalmilitaryhrs > 12:
            new_hrs = totalmilitaryhrs - 12
            new_time = str(new_hrs) + ":" + str(totalmins) + " PM"
        if totalmilitaryhrs < 12:
            new_hrs = totalmilitaryhrs 
            new_time = str(new_hrs) + ":" + str(totalmins) + " AM"
        if totalmilitaryhrs == 12:
            new_hrs = totalmilitaryhrs
            new_time = str(new_hrs) + ":" + str(totalmins) + " PM"

    #Calculating next day time.
    if totalmilitaryhrs >= 24 and totalmilitaryhrs < 48:
        new_hrs = totalmilitaryhrs%24
        ndays = 1
        if new_hrs > 12:
            new_hrs = new_hrs -12 
            new_time = new_time = str(new_hrs) + ":" + str(totalmins) + " PM" + " (next day)"
        else:
            new_time = new_time = str(new_hrs) + ":" + str(totalmins) + " AM" + " (next day)"

    #Calculating n days time.
    elif totalmilitaryhrs >=48:
        ndays = totalmilitaryhrs//24
        new_hrs =  totalmilitaryhrs%24
        if new_hrs > 12:
            new_hrs = new_hrs -12 
            new_time = new_time = str(new_hrs) + ":" + str(totalmins) + " PM" + " ("+ str(ndays)+" days later)"
        else:
            if new_hrs == 0:
                new_hrs = 12
            new_time = new_time = str(new_hrs) + ":" + str(totalmins) + " AM" + " ("+ str(ndays)+" days later)"

    #Mention the day if the day is given by the user.
 
        
    if given == True and totalmilitaryhrs < 24:
        
        resultday = days[givendayvalue]
        if totalmilitaryhrs > 12:
            new_hrs = totalmilitaryhrs - 12
            new_time = str(new_hrs) + ":" + str(totalmins) + " PM, " + resultday
        if totalmilitaryhrs <= 12:
            new_hrs = totalmilitaryhrs 
            new_time = str(new_hrs) + ":" + str(totalmins) + " AM, " + resultday

        #Calculating next day time.
    if given == True and totalmilitaryhrs >= 24 and totalmilitaryhrs < 48:
        new_hrs = totalmilitaryhrs%24
        ndays = 1
        resultdayvalue = (ndays+givendayvalue)%7
        resultday = days[resultdayvalue]
        if new_hrs > 12:
            new_hrs = new_hrs -12 
            new_time = new_time = str(new_hrs) + ":" + str(totalmins) + " PM, " + resultday +" (next day)"
        else:
            new_time = new_time = str(new_hrs) + ":" + str(totalmins) + " AM, " + resultday +" (next day)"

    #Calculating n days time.
    elif given==True and totalmilitaryhrs >=48:
        ndays = totalmilitaryhrs//24
        new_hrs =  totalmilitaryhrs%24
        resultdayvalue = (ndays+givendayvalue)%7
        resultday = days[resultdayvalue]
        if new_hrs > 12:
            new_hrs = new_hrs -12 
            new_time = new_time = str(new_hrs) + ":" + str(totalmins) + " PM, " + resultday + " ("+ str(ndays)+" days later)"
        else:
            if new_hrs == 0:
                new_hrs = 12
            new_time = new_time = str(new_hrs) + ":" + str(totalmins) + " AM, " + resultday + " ("+ str(ndays)+" days later)"



    return new_time
