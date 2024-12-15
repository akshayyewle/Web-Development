from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from application01.models import Model01
from application01.serializer import Model01_Serializer

# Create your views here.
@csrf_exempt
def index(request):
    return render(request, 'index.html')

def Model01_View(request,id=0):
    
    # Read Data
    if request.method == 'GET':
        data = Model01.objects.all()
        data_serialized = Model01_Serializer(data, many=True).data 
        return JsonResponse(data_serialized, safe=False)
    
    # Create Data
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        data_serialized = Model01_Serializer(data=data)
        if data_serialized.is_valid():
            data_serialized.save()
            return JsonResponse('Added Successfully!', safe=False)
        else:
            return JsonResponse('Failed To Add!', safe=False)
    
    # Update Data
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        data_serialized = Model01_Serializer(Model01.objects.get(id=id), data=data)
        if data_serialized.is_valid():
            data_serialized.save()
            return JsonResponse('Updated Successfully!', safe=False)
        else:
            return JsonResponse('Failed To Update!', safe=False)
        
    # Delete Data
    elif request.method == 'DELETE':
        data = Model01.objects.get(id=id)
        data.delete()
        return JsonResponse('Deleted Successfully!', safe=False)