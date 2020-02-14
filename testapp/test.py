import json
import urllib.request

url = 'https://api.line.me/v2/bot/message/reply'
data = {
    'foo': 123,
}
headers = {
    'Content-Type': 'application/json',
}

req = urllib.request.Request(url, json.dumps(data).encode(), headers)
with urllib.request.urlopen(req) as res:
    body = res.read()