#For project 2

#Global Scope
import csv
file_path = "Documents/CSE8A/AttendanceSheet.csv"


#Question 1
print("1. In the match between which two teams have the highest number of attendance for the World Cup 2022?") 

def find_match_with_highest_attendance(file_path): #Function to find the highest attended match
    highest_attendance = 0
    match = {}
    data = list(csv.reader(open(file_path)))
    for row in data[1:]:
        attendance = int(row[4])
        if attendance > highest_attendance:
            highest_attendance = attendance
            match = {'home_team': row[2], 'away_team': row[3], 'attendance': attendance} #3 keys:
    return match #return new dictionary to match
#Calling function 1
match = find_match_with_highest_attendance(file_path)
print(f"The match between {match['home_team']} and {match['away_team']} had the highest attendance of {match['attendance']} for the World Cup 2022.")

#Question 2
print ("2. What is the average attendance of any team in the World Cup 2022?") 

def get_valid_team_name(file_path): #Function for user to input their choice of team
    data = list(csv.reader(open(file_path)))
    while True: #while loops that would run forever until a return statement end the function.
        team_name = input("(Remember to capitalize the first letter) Enter the team name: ")
        for row in data[1:]:
            if row[2] == team_name or row[3] == team_name:  # If the team is either the home or away team
                return team_name #output of function 2, input for function 3
        print("Invalid team name. Please try again.") #if team doesn't exist

def calculate_average_attendance(file_path, team_name): #Function to find the average attendance of any team
    total_attendance = 0
    match_count = 0
    data = list(csv.reader(open(file_path)))
    for row in data[1:]: 
        if row[2] == team_name or row[3] == team_name:  # If the team is either the home or away team
            attendance = int(row[4])
            total_attendance += attendance
            match_count += 1 
    return round(total_attendance / match_count) #round to an integer instead of a float
#Calling function 2 and 3
team_name = get_valid_team_name(file_path)
average_number = calculate_average_attendance(file_path, team_name)
print(f"The average attendance across all matches for {team_name} is: {average_number}")

#Question 3
print("3. What is the gap between the highest and lowest number of attendance and how has the date, the teams that played, and the stadium impact the gap?") 

def find_attendance_gap(file_path): #Function to find the gap between most attended and least attended
    data = list(csv.reader(open(file_path)))
    lowest_match = {'attendance': 1000000} #use dictionary to set the key: (attendance) to a certain value
    highest_match = {'attendance': 0}

    for row in data[1:]:
        attendance = int(row[4])
        match = {'date': row[0], 'home_team': row[2], 'away_team': row[3], 'stadium': row[5], 'attendance': attendance}
        if attendance < lowest_match['attendance']: #comparing the value of attendance in data and in dictionary 
            lowest_match = match #change the dictionary of lowest_match when if statement is true
        if attendance > highest_match['attendance']:
            highest_match = match 

    attendance_gap = highest_match['attendance'] - lowest_match['attendance']
    return attendance_gap, lowest_match, highest_match #return numbers for attendance_gap and return new dictionary to the variables
#Calling function 4 
attendance_gap, lowest_match, highest_match = find_attendance_gap(file_path)
print(f"The gap between the highest and lowest attendance is {attendance_gap}.")
print(f"Lowest attendance is {lowest_match['home_team']} VS {lowest_match['away_team']}, at {lowest_match['stadium']}, on {lowest_match['date']}, with attendance of {lowest_match['attendance']}.")
print(f"Highest attendance is {highest_match['home_team']} VS {highest_match['away_team']}, at {highest_match['stadium']}, on {highest_match['date']}, with attendance of {highest_match['attendance']}.")