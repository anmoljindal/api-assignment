from django.shortcuts import render
import json
from django.http import JsonResponse
import time
from django.views.decorators.csrf import csrf_exempt
from django.http import QueryDict

'''
dictionary to store which reqest 
is to be silienced and which is currently running
'''
error = {}
state = {}

#get request with connid and timeout as query parameters
@csrf_exempt
def request(req):
	#extracting query parameters
	conid = req.GET.get('connid', None)
	timeo = req.GET.get('timeout', None)

	#defualt response
	statusres = {'status':'ok'};

	#timeout 
	for i in range(int(timeo),0, -1):
		#if the request is in error list
		if conid in error:
			#then change response and exit timeout
			statusres = {'status':'killed'}
			break
		else:
			time.sleep(1) #sleep 1 sec
			#storing current timeout left
			state[conid] = str(i)

	if conid in state:
		del state[conid]

	if conid in error:
		del error[conid]


	#converting to json response
	return JsonResponse(statusres)
	

#get request to show all current running requests
@csrf_exempt
def serverStatus(req):
	return JsonResponse(state)


#put request to kill particular request
@csrf_exempt 
def kill(req):
	conid = req.POST.get("connid", None)
	#status response
	statusres = {}

	#if status is running
	if conid in state:
		error[conid] = 'true'
		statusres['status'] = 'ok'

	#alternate response
	else:
		statusres['status'] = 'invalid connection Id : '+ conid
	return JsonResponse(statusres)

