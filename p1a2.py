# Names: Kelsey Dang, Adam Sellers, Brian Escobar
# Due Date: 2/26/23
# Filename: p1a2.py
# Project Name: Project 1 Algorithm 2

from datetime import datetime, timedelta

# define test case
person1_Schedule = [['7:00', '8:30'], ['12:00', '13:00'], ['16:00', '18:00']]
person1_DailyAct = ['9:00', '19:00']

person2_Schedule = [['9:00', '10:30'], ['12:20', '14:30'], ['14:00', '15:00'], ['16:00', '17:00']]
person2_DailyAct = ['9:00', '18:30']

duration_of_meeting = 30

# make test case a list so algorithm works for n schedules
list_of_schedules = [person1_Schedule, person2_Schedule]
# make test case a list so algortihm works for n daily active periods
list_of_activity = [person1_DailyAct, person2_DailyAct]

# combine two lists
combined_schedule = list()
for schedule in list_of_schedules:
    combined_schedule += schedule

combined_activity = list()
for activity in list_of_activity:
    combined_activity.append(activity)

# convert into datetime values
for event in combined_schedule:
    event[0] = datetime.strptime(event[0], '%H:%M')
    event[1] = datetime.strptime(event[1], '%H:%M')
for activity in combined_activity:
    activity[0] = datetime.strptime(activity[0], '%H:%M')
    activity[1] = datetime.strptime(activity[1], '%H:%M')
duration_of_meeting = timedelta(minutes = duration_of_meeting)

# sort the list by latest end time !!python sort is O(nlog(n))!!
def sortEndTime(elem):
    return elem[1]
combined_schedule.sort(key = sortEndTime)

# get the daily activity that starts the latest * start = [0]
latest_start_time = combined_activity[0][0]
for activity in combined_activity:
    if activity[0] > latest_start_time:
        latest_start_time = activity[0]

# get the daily activity that ends the earliest * end = [1]
earliest_end_time = combined_activity[0][1]
for activity in combined_activity:
    if activity[1] < earliest_end_time:
        earliest_end_time = activity[1]

# kill events that start before the latest start time
# (since sorted, stop looping once a time passes the check)
for i, event in enumerate(combined_schedule):
    if event[0] < latest_start_time:
        combined_schedule.pop(i)
    else:
        break

# kill events that end after the earliest end time
# (since sorted, stop looping once a time passes the check)
for i, event in enumerate(combined_schedule[::-1]):
    if event[1] > earliest_end_time:
        combined_schedule.pop(i)
    else:
        break

# add lastest start time to the front of the list as an event of [TIME, TIME]
combined_schedule.insert(0, [latest_start_time, latest_start_time])
# add latest end time to the back of the list as an event of [TIME, TIME]
combined_schedule.append([earliest_end_time, earliest_end_time])

# the magic move: take the end time of one event ans the start of the next to
# inverse the unavailability events to availability events
# kill events that are below the meeting duration (negative times also get killed)
final_times = list()
for i, event in enumerate(combined_schedule[:-1]):
    event[0] = combined_schedule[i][1]
    event[1] = combined_schedule[i + 1][0]
    if event[1] - event[0] >= duration_of_meeting:
        final_times.append(event)

# convert finished time intervals back into strings
for event in final_times:
    event[0] = datetime.strftime(event[0], '%H:%M')
    event[1] = datetime.strftime(event[1], '%H:%M')

print("Algorithm 2\n")
print("Available times:\n", final_times)
