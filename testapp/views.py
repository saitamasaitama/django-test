from django.views.generic import TemplateView
from django.shortcuts import render
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import urllib.request
from pythonreversi import reversi

# Create your views here.


import base64
import hashlib
import hmac

def index(request):
    return JsonResponse([1,2,3])




@csrf_exempt
def hello(request):
    json_open = open('setting.json', 'r')
    json_load = json.load(json_open)
    channel_secret = json_load['LINE']['channel_secret']
    print(f"LINE_secret:{channel_secret}")
    request_body = request.body
    data = confirm_json_loads(request_body)
    body = request.body.decode('utf-8')
    print(f"body:{body}")
    hash = hmac.new(channel_secret.encode('utf-8'),
        body.encode('utf-8'), hashlib.sha256).digest()
    signature = base64.b64encode(hash)
    print(f"calculated:{signature}")
    Line_Signature = request.META.get('HTTP_X_LINE_SIGNATURE').encode()
    print(f"received_line:{Line_Signature}")
    confirm_message = verify_signature(signature,Line_Signature)#signatureが一致するかの確認
    print(confirm_message)
    received = data["events"][0]["message"]["text"]
    reply_token = data["events"][0]["replyToken"]
    user_id = data["events"][0]["source"]["userId"]
    user_information = get_user_infromation(user_id)
    user_name = json.loads(user_information)
    user_name = user_name['displayName']
    selected_message = select_message(received,user_id,user_name)
    reply_message(reply_token , selected_message, user_id)


    return confirm_message 

def confirm_json_loads(body):
    try:
        return json.loads(body)
    except Exception as e:

        print("error")
        message = JsonResponse({'message': 'Login failure.'}, status=403)

        return message
def verify_signature(signature_1,signature_2):
    print(f"signature_1:{signature_1}")
    print(f"signature_2:{signature_2}")
    if signature_1 != signature_2:
        return JsonResponse({'message': 'Login failure.'}, status=403)

    else :
        return JsonResponse({'message': 'Success.'}, status=200)


def select_message(sended,user_id,user_name):

    return_message = ""
    if sended == "オセロ":
        user_name = user_name + "さん"
        print(user_id)
        reversi.othello_instance.play()
        reversi.othello_instance.board.put_board_image(user_id)
        sum_stone = reversi.othello_instance.board.count_stone()
        print(sum_stone)
        white_stone = sum_stone[0]
        black_stone = sum_stone[1]
        return_message += f"白{white_stone}枚、黒{black_stone}枚です\n"
        return_message += "どこに置きますか？\n"
        return_message +=user_name

        
    elif int(sended) == int:

        sended = list(sended)
        reversi.othello_instance.board.put(int(sended[0]),int(sended[1]),1)
        reversi.othello_instance.board.put_board_image(user_id)
        
    else:
        return_message += "オセロを終了します"
    
    return return_message

    
def reply_message(token , message, user_id):

    url = 'https://api.line.me/v2/bot/message/reply'
    print(url)
    data = {
        'replyToken': token,
        'messages':[
            {
                'type': 'text',
                'text': message
            },
            {   'type' : 'image',
                'originalContentUrl' : f'https://test.python-bot.saitamasaitama.com/static/testapp/{user_id}.png',
                'previewImageUrl'    : f'https://test.python-bot.saitamasaitama.com/static/testapp/{user_id}.png'
            }
        ]
    }
    print(data)
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer vskFRXIrtpVwtBbBPUzf+Jw0kFQvboKzn5tKFlb6dApojbLBdsRTnnhA2uaDqgC0idK0Is8XcQX24N9nG/6b4GH8sqIWjtAvJBiIu4UgRUy7OIu0I7gVmECmD1KPvrRSVDs9jAEAzRZPOBeoAXtYVAdB04t89/1O/w1cDnyilFU='
    }
    print(headers)
    req = urllib.request.Request(url, json.dumps(data).encode(), headers)
    print(req)
    with urllib.request.urlopen(req) as res:
        body = res.read()
    

def push_message(message):

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
    

def get_user_infromation(user_id):

    url = f"https://api.line.me/v2/bot/profile/{user_id}"
    print(url)
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer vskFRXIrtpVwtBbBPUzf+Jw0kFQvboKzn5tKFlb6dApojbLBdsRTnnhA2uaDqgC0idK0Is8XcQX24N9nG/6b4GH8sqIWjtAvJBiIu4UgRUy7OIu0I7gVmECmD1KPvrRSVDs9jAEAzRZPOBeoAXtYVAdB04t89/1O/w1cDnyilFU='
    }

    
    req = urllib.request.Request(url,None,headers)
    with urllib.request.urlopen(req) as res:
        body = res.read()
    return body

