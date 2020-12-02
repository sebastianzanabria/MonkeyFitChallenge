from django.shortcuts import render
import requests
import re
from .models import Place

def home(request):
    TEMPLATE = "home.html"
    if not bool(request.GET):
        return render(request,TEMPLATE)
    params = request.GET.dict()
    #TODO: change response code if the performance is not desirable
    #TODO: input should be strip and downcase
    #TODO: if just one field is filled
    #TODO: if input have weird chars
    #TODO: if status is not OK
    URL_AUTOCOMPLETE = "https://maps.googleapis.com/maps/api/place/autocomplete/json"
    response_places = requests.get(URL_AUTOCOMPLETE, params=params)
    places = response_places.json().get('predictions')
    place_ids = list(map(lambda place: place.get('place_id'), places))
    #TODO: places limit to 5
    URL_DETAILS = "https://maps.googleapis.com/maps/api/place/details/json" 
    get_details = lambda place_id: requests.get(URL_DETAILS, params={'place_id': place_id, 'key':params.get('key')}).json().get('result')
    details = list(map(get_details, place_ids))
    FIELDS = ['place_id','name','formatted_address','business_status','rating','url','user_ratings_total','utc_offset']
    filter_details = lambda details: { k:v for (k, v) in details.items() if k in FIELDS } 
    filtered_details = list(map(filter_details, details ))
    #TODO: filter duplicates by place_id
    for detail in filtered_details:
        place = Place(**detail)
        place.save()
    #message = "You are searching: {} y {}".format(query, api_key)
    #context = {
        # 'message': message,
    # }
    return render(request, TEMPLATE)#, context)
