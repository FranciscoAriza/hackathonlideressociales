from django.shortcuts import render
import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, CategoriesOptions, ConceptsOptions, \
    EntitiesOptions, KeywordsOptions, MetadataOptions, RelationsOptions
from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource
from os.path import join, dirname
from pymongo import MongoClient
from eventregistry import *
from bson.objectid import ObjectId

client = MongoClient('localhost', 27017)



def landing(request):
    return render(request, 'home/landing.html')


# Create your views here.
def landing_audio(request):
    speech_to_text = SpeechToTextV1(
        iam_apikey='',
        url='https://stream.watsonplatform.net/speech-to-text/api'
    )

    class MyRecognizeCallback(RecognizeCallback):
        def __init__(self):
            RecognizeCallback.__init__(self)

        def on_data(self, data):
            print(json.dumps(data, indent=2))

        def on_error(self, error):
            print('Error received: {}'.format(error))

        def on_inactivity_timeout(self, error):
            print('Inactivity timeout: {}'.format(error))

    myRecognizeCallback = MyRecognizeCallback()

    with open(join(dirname(__file__), '01_denunciante.ogg'),
              'rb') as audio_file:
        audio_source = AudioSource(audio_file)
        speech_to_text.recognize_using_websocket(
            audio=audio_source,
            content_type='audio/ogg;codecs=vorbis',
            recognize_callback=myRecognizeCallback,
            model='es-ES_NarrowbandModel',
            max_alternatives=1)

    context = {
        'data': "Hello"
    }
    return render(request, 'home/landing.html', context)


# Create your views here.
def nlp_watson(url):
    print(url)
    natural_language_understanding = NaturalLanguageUnderstandingV1(
        version='2018-11-16',
        iam_apikey='',
        url='https://gateway.watsonplatform.net/natural-language-understanding/api'
    )
    try:
        response = natural_language_understanding.analyze(
            url=url,
            features=Features(categories=CategoriesOptions(limit=15),
                              concepts=ConceptsOptions(limit=10),
                              entities=EntitiesOptions(sentiment=True, limit=20),
                              keywords=KeywordsOptions(sentiment=True, emotion=True, limit=5),
                              metadata=MetadataOptions())
                              #relations=RelationsOptions()),
            ).get_result()

        data = json.dumps(response, indent=2)
        # new = json.loads(response)
        # print(data)
        db = client.asalvo
        news = db.news
        new_id = news.insert_one(response).inserted_id
        # print(new_id)
    except:
        print('Error ocurred')

    return 0

def landing_text(request):
    # recolectar_noticias()
    # nlp_news()
    context = {
        'data': ""
    }
    return render(request, 'home/landing.html', context)

def recolectar_noticias():
    API_KEY=""

    er = EventRegistry(apiKey=API_KEY)
    # q = QueryArticles(keywords=QueryItems.OR(["líder social", "líderes sociales", "lideresas", "líder comunitario",
    #                                           "lider social", "lideres sociales", "lider comunitario"]))

    q = QueryArticles(keywords=QueryItems.AND(["Colombia", "indigenas", "indigena"]))

    q.setRequestedResult(RequestArticlesInfo(count=100,
                                             returnInfo=ReturnInfo(
                                                 articleInfo=ArticleInfoFlags(duplicateList=False, concepts=False,
                                                                              categories=False, location=True,
                                                                              image=True))))
    res = er.execQuery(q)
    # q = QueryArticlesIter(conceptUri=er.getConceptUri("George Clooney"))
    # print(res)
    db = client.asalvo
    news = db.group_news
    new_id = news.insert_one(res).inserted_id
    print(new_id)
    return 0

def nlp_news():
    db = client.asalvo
    # news = db.group_news.find_one({'_id': ObjectId('5d0c95f19bf070fa48666e13')})
    news = db.group_news.find({})

    # print(news)
    acum = 0
    for y in news:
        for x in y['articles']['results']:
            nlp_watson(x['url'])
            acum += 1

    print(acum)


    return 0