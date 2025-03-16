import requests
import os

endpoint = "https://maestriayachay.cognitiveservices.azure.com/"
key = "2F54M87YQt6vNtfBKP1EUTIqByV71csVGSlb2mVQ37SZEapPwOu9JQQJ99BCACYeBjFXJ3w3AAAFACOG6XhS"
analyze_url = f"{endpoint}/vision/v3.1/analyze?visualFeatures=Description"

headers = {
    'Ocp-Apim-Subscription-Key': key,
    'Content-Type': 'application/octet-stream'
}

def read_image(filepath):
    try:
        with open(filepath, 'rb') as image_file:
            response = requests.post(analyze_url, headers=headers, data=image_file)
        response.raise_for_status()
        analysis = response.json()

        # Obtiene la descripción de la respuesta
        description = analysis['description']['captions'][0]['text'] if analysis['description']['captions'] else 'No description available'
        print(f"Description: {description}")  # Print the description to the console
        return description
    except Exception as e:
        # Imprimir el error en la consola
        print(e)
        return 'Descripción no disponible'
