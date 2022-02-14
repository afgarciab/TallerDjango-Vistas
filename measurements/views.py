from django.shortcuts import render

from .logic import logic_measurements as vl
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def measurements_view(request):
    if request.method == 'GET':
        id = request.GET.get("id", None)
        if id:
            measurement = vl.get_measurement(pk)
            measurement_dto = serializers.serialize('json', measurement)
            return HttpResponse(measurement_dto, 'application/json')
        else:
            measurement = vl.get_measurements()
            measurement_dto = serializers.serialize('json', measurement)
            return HttpResponse(measurement_dto, 'application/json')

    if request.method == 'POST':
        measurement = vl.create_measurement(json.loads(request.body))
        measurement_dto = serializers.serialize('json', measurement)
        return HttpResponse(measurement_dto, 'application/json')

@csrf_exempt
def measurement_view(request, pk):
    if request.method == 'GET':
        measurement_dto = vl.get_measurement(pk)
        measurement = serializers.serialize('json', [measurement_dto,])
        return HttpResponse(measurement, 'application/json')

    if request.method == 'PUT':
        measurement_dto = vl.update_measurement(pk, json.loads(request.body))
        measurement = serializers.serialize('json', [measurement_dto,])
        return HttpResponse(measurement, 'application/json')


# Create your views here.
