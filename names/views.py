import os
from rest_framework.views import APIView, Request, Response, status
from rest_framework.response import Response
from rest_framework import status
import requests
from names.models import Name
from moviepy.editor import concatenate_audioclips, AudioFileClip


class ReceberNome(APIView):
    def post(self, request):
        data = request.data
        nome_recebido = data.get("name")
        Name.objects.create(name=nome_recebido)

        print(nome_recebido)
        obter_audio_com_nome(nome_recebido)

        return Response(
            {"mensagem": "Nome recebido e áudio obtido com sucesso!"},
            status=status.HTTP_200_OK,
        )


def obter_audio_com_nome(nome):
    url = "https://api.elevenlabs.io/v1/text-to-speech/9taGhnBznbfOawuN2NPL"
    mensagem = f"Olá {nome}"
    payload = {"model_id": "eleven_multilingual_v2", "text": mensagem}

    headers = {
        "xi-api-key": "1d821b47d9b7a50ac7cfe9901ef87169",
        "Content-Type": "application/json",
    }
    response = requests.request("POST", url, json=payload, headers=headers)

    if response.status_code == 200:
        arquivo_saida = "audio.mp3"
        if os.path.exists(arquivo_saida):
            os.remove(arquivo_saida)

        with open("audio.mp3", "wb") as arquivo_audio:
            arquivo_audio.write(response.content)
        print("Arquivo de áudio salvo com sucesso!")
        concatAudio()
    else:
        print(
            "Erro ao obter o arquivo de áudio. Código de status:", response.status_code
        )


def concatAudio():
    input_audio1 = AudioFileClip("audio.mp3")
    input_audio2 = AudioFileClip("Recording_4.mp3")

    final_audio = concatenate_audioclips([input_audio1, input_audio2])

    final_audio.write_audiofile("combinado.mp3")
