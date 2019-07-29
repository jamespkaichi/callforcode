from __future__ import unicode_literals
from django.template.loader import get_template
from django.http import JsonResponse
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from datetime import datetime
from .models import Post
from django.shortcuts import redirect
import requests
import json
import base64

def index(request):
	template = get_template('index.html')
	now = datetime.now()
	posts = Post.objects.all()
	post_lists=list()
	position_list = getAllPosition()
	place_list = getAllplace()
	html = template.render(locals())
	return HttpResponse(html)

def showpost(request,slug):
	template = get_template('post.html')
	try:
		post = Post.objects.get(slug=slug)
		if post !=None:
			html = template.render(locals())
			return HttpResponse(html)
	except:
		return redirect("/")

def health(request):
    state = {"status": "UP"}
    return JsonResponse(state)


def handler404(request):
    return render(request, '404.html', status=404)

def handler500(request):
    return render(request, '500.html', status=500)


def listDevices(deviceType):
    
    #Get device list
    headers = {
    'accept': 'application/json',
    'authorization': 'Basic YS1rbWZjeTMtZXJrYjJ2aWJseDp1QDV6QUlsSWdHdihaSXplKHc=',}
    params = (
    ('_limit', '25'),)
    getUrl = 'https://kmfcy3.internetofthings.ibmcloud.com/api/v0002/device/types/%s/devices'%deviceType
    response = requests.get(getUrl, headers=headers, params=params)
    result=[]
    if 200 != response.status_code:
        print( response.status_code )
        print( response.reason )
    else:
        myresult=json.loads(response.text)
        for item in myresult['results']:
            #print(item['deviceId'])
            result.append(item['deviceId'])
    return result

def getDeviceLastPos(deviceType,deviceID):
    headers = {
    'accept': 'application/json',
    'authorization': 'Basic YS1rbWZjeTMtZXJrYjJ2aWJseDp1QDV6QUlsSWdHdihaSXplKHc=',}
    getUrl ='https://kmfcy3.internetofthings.ibmcloud.com/api/v0002/device/types/%s/devices/%s/events/event_1'%(deviceType,deviceID)
    response = requests.get(getUrl, headers=headers)
    position=""
    if 200 != response.status_code:
        print( response.status_code )
        print( response.reason )
    else:
        outresult=json.loads(response.text)
        payload = base64.b64decode(outresult['payload']).decode('utf-8')
        
    return payload

def getAllPosition():
    deviceList=listDevices('position')
    result=[]
    for item in deviceList:
        posData = json.loads(getDeviceLastPos('position',item))
        posStr="longitude:%s  latitude:%s"%(posData['longitude'],posData['latitude'])
        resultStr="carID:%s postion:%s"%(item,posStr)
        result.append(resultStr)
    return result

def getAllplace():
    deviceList=listDevices('temperature')
    result=[]
    for item in deviceList:
        tempData = json.loads(getDeviceLastPos('temperature',item))
        tempStr="PlaceID:%s  current degree: %s"%(item,tempData['currentDegree'])
        result.append(tempStr)
    return result