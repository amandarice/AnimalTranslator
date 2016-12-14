from ask import alexa
from random import randint
import urllib2
import json

def lambda_handler(request_obj, context={}):
    return alexa.route_request(request_obj)

@alexa.default_handler()
def default_handler(request):
    return launch_request_handler(request)

@alexa.request_handler("LaunchRequest")
def launch_request_handler(request):
    return alexa.create_response(message="Welcome to Animal Translator! Give me the name of an animal, and I will give you the human method for representing the sound it makes!",
                                 reprompt_message='Learning how to say the sounds of animals can be fun! What animal would you like me to sound out for you?')

@alexa.request_handler(request_type="SessionEndedRequest")
def session_ended_request_handler(request):
    return alexa.create_response(message="Goodbye!", end_session=True)

@alexa.intent_handler("GetAnimalSound")
def get_animal_sound_handler(request):

    name = request.get_slot_value("AnimalName")
    address_endpoint = "https://maps.googleapis.com/maps/api/geocode/json?address=" + str(zipcode) + "&key=AIzaSyBGIfYI-cPjjpk3DfA71AgKvPfbeq_op78"
    address = json.load(urllib2.urlopen(address_endpoint))
    lat = address["results"][0]["geometry"]["location"]['lat']
    lng = address["results"][0]["geometry"]["location"]['lng']

    brew_endpoint = "http://api.brewerydb.com/v2/search/geo/point?lat=" + str(lat) + "&lng=" + str(lng) + "&key=2d982c1274cf775318b70f4bb8cca4ff"
    brew_locations = json.load(urllib2.urlopen(brew_endpoint))

    brews = []
    breweries = ""

    for i in range(0,5):
        if brew_locations["data"][i]["brewery"]["name"] not in brews:
            brews.append(brew_locations["data"][i]["brewery"]["name"])
            breweries = breweries + brew_locations["data"][i]["brewery"]["name"] + ", "

    brewMessage = "Breweries in your area include " + breweries[:-2]

    return alexa.create_response(message=brewMessage, end_session=True)

@alexa.intent_handler("AMAZON.HelpIntent")
def help_intent_handler(request):
    return alexa.create_response(message="This skill gives you an animal sound after you give it an animal name.", end_session=False)

@alexa.intent_handler("AMAZON.StopIntent")
def stop_intent_handler(request):
    return alexa.create_response(message="Goodbye!", end_session=True)

@alexa.intent_handler("AMAZON.CancelIntent")
def cancel_intent_handler(request):
    return alexa.create_response(message="Goodbye!", end_session=True)