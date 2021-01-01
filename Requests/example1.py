import requests

# r = requests.get("https://xkcd.com/353/")

# print(r)

# # attributes and methods within this request object
# print(dir(r))
# # Help with attributes, methods
# print(help(r))

# # Html of the page
# print(r.text)

# # requesting image
# img = requests.get("https://imgs.xkcd.com/comics/python.png")
# print(img.status_code) # or print(img.ok)
# # Prints out bytes from that image
# print(img.content)

# # Downloading the image 
# with open('comic.png', 'wb') as f:
#     f.write(img.content)


# # Less error prone
# payload = {'page': 2, 'count': 25}
# r = requests.get('https://httpbin.org/get', params=payload)
# print(r.url)

# Post data
payload = {'username': 'Ahsan', 'password': 'testing'}
r = requests.post('https://httpbin.org/post', data=payload)
print(r.text)
# A json methods instead
print(r.json())
# Capture that in a python dict to parse
r_dict = r.json()
print(r_dict['form'])

