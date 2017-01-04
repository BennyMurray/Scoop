import json
from django.http import HttpResponse

def json_response(something):
    return HttpResponse(json.dumps(something))

