from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

import json
import serial
import requests
from django.shortcuts import render

URL = 'http://127.0.0.1:8000/'
arduino_port = 'COM6'


class MyRenderer(JSONRenderer):
    media_type = 'aapplication/json'



class Valueview(APIView):
    # renderer_classes = ()

    def get(self, request):
        ser = serial.Serial(
        port=arduino_port,
        baudrate=9600,
        )
        print("아두이노 통신")
        print(f'포트는 {arduino_port}입니다.')
        res = ser.readline()
        value = (res.decode()[:-1])
        json_data = json.loads(value)
        ser.close() 
        return render(request, 'place_stores.html',{ 'data' : json_data })