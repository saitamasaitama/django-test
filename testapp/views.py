from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
import json
import base64
import hashlib
import hmac


class MessageEvent:
    replyToken = ""
    data = {}

    def __init__(self, replyToken, data):
        self.replyToken = replyToken
        self.data = data


class TextMessage:
    id = ""
    type = ""
    text = ""


class LineEvent:

    def __init__(self):
        pass

    @staticmethod
    def FromSource(body: str):
        data = json.loads(body)
        events = data["events"]
        result = []
        for event in events:
            result.append(LineEvent.From(event))

            # タイプを見てそれぞれのイベントを生成する
    @staticmethod
    def From(event: dict):
        if(event["type"] == "message"):
            return MessageEvent(event[""])


def index(request):
    return JsonResponse([1, 2, 3])


@csrf_exempt
def test(request):
    # まず検証する
    print(request.body)
    print(json.dumps(request.POST))
    print(type(request))
    # イベントを取得する
    LineEvent.FromSource(request.body)
    data = json.loads(request.body)

    return HttpResponse("OK!")
