import requests
import sys

content = ""
data = requests.get(sys.argv[1])
content = str(data.content)

pos = content.find("channel_id=")

id = content[pos+11:pos+35]
print(id)
print("https://www.youtube.com/feeds/videos.xml?channel_id=" + id)
