from ask import alexa
import urllib2

def lambda_handler(request_obj, context={}):
    return alexa.route_request(request_obj)

@alexa.default_handler()
def default_handler(request):
    return launch_request_handler(request)

@alexa.request_handler("LaunchRequest")
def launch_request_handler(request):
    return alexa.create_response(message="Welcome to Animal Translator! If you give me the name of an animal, I will respond with the human pronounciation of the sound it makes! What animal would you like me to sound out for you?",
                                 reprompt_message='Learning how to say the sounds of animals can be fun! What animal would you like me to sound out for you?')

@alexa.request_handler(request_type="SessionEndedRequest")
def session_ended_request_handler(request):
    return alexa.create_response(message="Goodbye!", end_session=True)

@alexa.intent_handler("GetAnimalSound")
def get_animal_sound_handler(request):

    name = request.get_slot_value("AnimalName")
    sound = {}
    with open("animal_sounds.txt") as f:
        for line in f:
            newline = line.strip()
            key = newline[:newline.find(' ')]
            val = newline[newline.find(' ')+1:]
            sound[key]=val
    if name in sound:
        animalSoundResponse = "The " + name + " says " + sound[name] + "."
        return alexa.create_response(message=animalSoundResponse, end_session=True)
    else:
        animalSoundResponse = "We don't know how to pronounce the sound for " + name + ". Please try again."
        return alexa.create_response(message=animalSoundResponse, end_session=False)

@alexa.intent_handler("AMAZON.HelpIntent")
def help_intent_handler(request):
    return alexa.create_response(message="This skill gives you an animal sound after you give it an animal name.", end_session=False)

@alexa.intent_handler("AMAZON.StopIntent")
def stop_intent_handler(request):
    return alexa.create_response(message="Goodbye!", end_session=True)

@alexa.intent_handler("AMAZON.CancelIntent")
def cancel_intent_handler(request):
    return alexa.create_response(message="Goodbye!", end_session=True)
