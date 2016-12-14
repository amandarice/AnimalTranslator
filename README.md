# AnimalTranslator
Alexa skill that translates animal names to human sounds

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
