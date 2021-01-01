# Importing libraries
import re
from datetime import timedelta
from googleapiclient.discovery import build

# Google API key
api_key = 'AIzaSyCGjPH8WZXo9U5MifzHvIW0VTnNvlVt2MY'

# API object of Youtube
youtube = build('youtube', 'v3', developerKey=api_key)

# REGEX compiler
hours_pattern = re.compile(r'(\d+)H')
minutes_pattern = re.compile(r'(\d+)M')
seconds_pattern = re.compile(r'(\d+)S')

# Requesting all video ID's from the playlist
pl_request =  youtube.playlistItems().list(
	part='contentDetails',
	playlistId='PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS',
	maxResults=50,
)

# Executing the request here
pl_response = pl_request.execute()

# Putting all video Id's in a list
vid_ids = []
for item in pl_response['items']:
	vid_ids.append(item['contentDetails']['videoId'])

# Requesting the video's via their respective ID's
vid_request = youtube.videos().list(
	part='contentDetails',
	id=[','.join(vid_ids)]
)

vid_response = vid_request.execute()

# Looping through all the videos and summing up total duration
total_seconds = 0
for item in vid_response['items']:
	duration = item['contentDetails']['duration']

	hours = hours_pattern.search(duration)
	minutes = minutes_pattern.search(duration)
	seconds = seconds_pattern.search(duration)

	hours = int(hours.group(1)) if hours else 0
	minutes = int(minutes.group(1)) if minutes else 0
	seconds = int(seconds.group(1)) if seconds else 0

	video_seconds = timedelta(
		hours=hours,
		minutes=minutes,
		seconds=seconds
	).total_seconds()

	total_seconds += video_seconds

# Convert total seconds to proper time

total_seconds = int(total_seconds)
minutes, seconds = divmod(total_seconds, 60)
hours, minutes = divmod(minutes, 60)

# Printing out the total time
print(f'{hours}:{minutes}:{seconds}')