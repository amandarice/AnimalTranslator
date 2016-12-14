# AnimalTranslator

AnimalTranslator is an Alexa skill that provides the human pronunciation for the sound of an animal you name.

Sample Interaction:

* Your Question: "Alexa, ask Animal Translator what does the cow say?"
* Alexa's Response: "The cow says moo."

This skill is primarily intended for young children learning how to identify different animals. You must use the singular form of the animal's name (e.g. use "dog" instead of "dogs") and can only use one-worded names. There are currently 23 animal names available.

### Project Format

The speech_assets folder contains the files which comprise the Voice User Interface:
* intent schema in intent_schema.json
* sample utterances in utterances.txt
* custom slot values in LIST_OF_NAMES.txt, which contains a list of animal names

The ask folder is based on the ask-alexa-pykit and is used to help develop an Alexa skill in Python.

The lambda function in lambda_function.py is used to run the Alexa skill using AWS Lambda.

### To Upload to Lambda

Right click all of the following, then compress:
* ask folder
* lambda_function.py
* animal_sounds.txt

Upload the compressed zip to Lambda.

### Testing

Text/JSON calls and responses - https://developer.amazon.com/edw/home.html

Vocal calls and responses - https://echosim.io/

**Written by Amanda Rice**
