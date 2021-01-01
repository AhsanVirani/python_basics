import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

urls = '''
https://www.google.com
http://ahsanvs.com
https://www.youtube.com
https://www.nasa.gov
'''

sentence = 'Start a sentence and then bring it to an end'

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')


subbed_urls = pattern.sub(r'\2\3', urls)

print(subbed_urls)

# with open('data.txt', 'r') as f:
#     contents = f.read()
    
#     matches = pattern.finditer(urls)

#     for match in matches:
#         print(match.group(2))



# pattern = re.compile(r'start', re.I)

# matches = pattern.search(sentence)

# print(matches)
