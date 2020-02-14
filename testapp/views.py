from django.views.generic import TemplateView
from django.shortcuts import render
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

def index(request):
    return JsonResponse([1,2,3])
@csrf_exempt
def hello(request):
    print('hello')
    data = json.loads(request.body)
    sended = data["events"][0]["message"]["text"]
    token = data["events"][0]["replyToken"]
    print(request.body)
    reply_reversi=select_message(sended)
    reply_message(token , reply_reversi)
    '''push_message("元気？")'''
    return JsonResponse({"result":"hello"}) 




def select_message(sended):
    return_message = ""
    if sended == "オセロ":
        return_message = "モードを選んでください。0)プレイヤー同士 1)vsコンピューター "
        
    else:
        return_message += "オセロを終了します"
    
    return return_message

    
def reply_message(token , message,):

    import json
    import urllib.request

    url = 'https://api.line.me/v2/bot/message/reply'
    data = {
        'replyToken': token,
        'messages':[
            {
                'type': 'text',
                'text': message
            }
        ]
    }
    print(data)
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer vskFRXIrtpVwtBbBPUzf+Jw0kFQvboKzn5tKFlb6dApojbLBdsRTnnhA2uaDqgC0idK0Is8XcQX24N9nG/6b4GH8sqIWjtAvJBiIu4UgRUy7OIu0I7gVmECmD1KPvrRSVDs9jAEAzRZPOBeoAXtYVAdB04t89/1O/w1cDnyilFU='
    }

    req = urllib.request.Request(url, json.dumps(data).encode(), headers)
    with urllib.request.urlopen(req) as res:
        body = res.read()
    

def push_message(message):

    import json
    import urllib.request

    url = 'https://api.line.me/v2/bot/message/push '
    data = {
        'to':"U7250840ea54f17c72c63a58c74aefc14" ,
        'messages':[
            {
                'type': 'text',
                'text': message
            }
        ]
    }
    print(data)
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer vskFRXIrtpVwtBbBPUzf+Jw0kFQvboKzn5tKFlb6dApojbLBdsRTnnhA2uaDqgC0idK0Is8XcQX24N9nG/6b4GH8sqIWjtAvJBiIu4UgRUy7OIu0I7gVmECmD1KPvrRSVDs9jAEAzRZPOBeoAXtYVAdB04t89/1O/w1cDnyilFU='
    }

    req = urllib.request.Request(url, json.dumps(data).encode(), headers)
    with urllib.request.urlopen(req) as res:
        body = res.read()
    

       



