from ..models import Measurement
#retorna todos los measurements
def get_measurements():
    measurements = Measurement.objects.all()
    return measurements

#devuelve un measurement por id
def get_measurement(var_pk):
    measurement = Measurement.objects.get(pk=var_pk)
    return measurement

def create_measurement(var):
    measurement = Measurement(name=var["name"])
    measurement.save()
    return measurement

def update_measurement(var_pk, new_var):
    measurement = get_measurement(var_pk)
    measurement.name = new_var["name"]
    measurement.save()
    return measurement

def delete_measuement(var_pk):
    measurement = Measurement.objects.get(pk=var_pk)
    measurement.delete()
