
import re
from googleapiclient.discovery import build

api_key = 'AIzaSyCGjPH8WZXo9U5MifzHvIW0VTnNvlVt2MY'

youtube = build('youtube', 'v3', developerKey=api_key)

pl_request =  youtube.playlistItems().list(
	part='contentDetails',
	playlistId='PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS'
)

pl_response = pl_request.execute()

#print(pl_response)

vid_ids = []
for item in pl_response['items']:
	vid_ids.append(item['contentDetails']['videoId'])

vid_request = youtube.videos().list(
	part='contentDetails',
	id=[','.join(vid_ids)]
)

vid_response = vid_request.execute()

for item in vid_response['items']:
	duration = item['contentDetails']['duration']
	print(duration)
	print()
