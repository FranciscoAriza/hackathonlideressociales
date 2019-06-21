from django.shortcuts import render
from lideres.models import DenunciaLider
from lideres.forms import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_list_or_404, get_object_or_404
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, CategoriesOptions, ConceptsOptions, \
    EntitiesOptions, KeywordsOptions, MetadataOptions, RelationsOptions
from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource
from os.path import join, dirname
from pymongo import MongoClient


# Create your views here.
def index(request):
    user = request.user
    messages_pendientes = []
    lider_acreditado="dsadda"
    # lider_acreditado = Lider.objects.filter(usuario=user.id)
    if len(lider_acreditado) <= 0:
        messages_pendientes.append(
            "Recuerda que el cuídado de la vida inicia con la autoprotección.")
    context = {
        'messages_pendientes': messages_pendientes
    }
    return render(request, 'instituciones/index.html', context)


def denuncias(request):
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

    context = {
        'denuncia': denuncias
    }
    return render(request, 'instituciones/denuncias.html', context)


def about(request):
    return render(request, 'instituciones/about.html')