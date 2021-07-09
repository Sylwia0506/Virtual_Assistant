import speech_recognition as sr
import os
from gtts import gTTS
import datetime
import warnings
import calendar
import random
import wikipedia

warnings.filterwarnings('ignore')

def recordAudio():
    r =sr.Recognizer()
    with sr.Microphone() as source:
        print('Say something!')
        audio = r.listen(source)
    data=''
    try:
        data = r.recognize_google(audio)
        print ('You said:'  + data)
    except sr.UnknownValueError:
        print('Google Speech Recognition could not understand the audio, unknown error')
    except sr.RequestError as e:
        print('Request result from Google Speeach Recognition service error' + e)
    return data

def assistantResponse(text):
    print(text)
    myobj = gTTS(text=text, lang='en', slow=False)
    myobj.save('assistant_response.mp3')

    os.system('start assistant_response.mp3')

# text ='This is a test'
# assistantResponse(text)

def wakeWord(text):
    WAKE_WORDS = ['hey computer', 'ok computer']
    text =text.lower()

    for phrase in WAKE_WORDS:
        if phrase in text:
            return True

    return False

def getDate():

    now = datetime.datetime.now()
    my_date = datetime.datetime.today()
    weekday =calendar.day_name[my_date.weekday()]
    monthNum = now.month
    dayNum = now.day

    month_names =['January', 'February', 'March', 'April', 'May'
                  'June', 'July', 'August', 'September', 'October',
                  'November', 'December']

    ordinalNumbers = [ '1st','2nd', '3rd', '4th', '5th', '6th', '7th' , '8th', '9th', '10th',
                       '11st', '12nd', '13rd', '14th', '15th', '16th', '17th', '18th', '19th', '20th',
                       '21st', '22nd', '23rd', '24th', '25th', '26th', '27th', '28th', '29th', '30th', '31st']

#     return 'Today is '+ weekday + ' '+ month_names[monthNum -2] + ' the ' + ordinalNumbers[dayNum-1] + '.'
# print(getDate())

def greeting(text):
    GREETING_INPUTS = ['hi', 'hey', 'hola', 'greeting', 'wassup', 'hello']
    GREETING_RESPONSES = ['howdy', 'whats good', 'hello', 'hey there']

    for word in text.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES) + '.'

        return ''

def goodbye(text):
    GOODBYE_INPUTS = ['bye', 'goodbye', 'see you letter', 'goodnight', 'hello']
    GOODBYE_RESPONSES = ['bye bye', 'goodbye', 'hello']

    for word in text.split():
        if word.lower() in GOODBYE_INPUTS:
            return random.choice(GOODBYE_RESPONSES) + '.'

        return ''

def getPerson(text):
    wordList = text.split()

    for i in range (0, len(wordList)):
        if i+3 <= len(wordList) -1 and wordList[i].lower() == 'who' and wordList[i+1].lower() == 'is':
            return wordList[i+2] + ' ' + wordList[i+3]

def getDefinition(text):
    wordList = text.split()

    for i in range (0, len(wordList)):
      if i+3 <= len(wordList) -1 and wordList[i].lower() == 'what' and wordList[i+1].lower() == 'is':
            return wordList[i+2]

def color(text):
    QUESTION = ['What is your favorite color ?']
    ANSWER = ['blue', 'red', 'orange', 'yellow', 'black', 'brown', 'pink', 'gray', 'purple']

    for word in text.split():
        if word.lower() in QUESTION:
            return random.choice(ANSWER) + '.'

        return ''

while True:
    text = recordAudio()
    response = ''
    if(wakeWord(text) == True):
        response = response + greeting(text)

        if('data' in text):
            get_date = getDate()
            response = response + ' ' + get_date

        if ('who is' in text):
            person = getPerson(text)
            wiki = wikipedia.summary(person, sentences=2)
            response = response + ' ' + wiki

        if ('what is' in text):
            definition = getDefinition(text)
            wikip = wikipedia.summary(definition, sentences=2)
            response = response + ' ' + wikip


        if (color(text) == True):
            response = response + color(text)


        else:
            response = response + goodbye(text)

        assistantResponse(response)
