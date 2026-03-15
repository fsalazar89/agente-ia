import google.generativeai as genai
import os
from dotenv import load_dotenv
from tools.pruebas_tools import obtener_hora, escanear_red_local

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class MiAgente:
    def __init__(self):
        # Registramos las funciones que el modelo puede "ver"
        self.model = genai.GenerativeModel(
            model_name='gemini-2.5-flash',
            tools=[obtener_hora, escanear_red_local]
        )
        # Iniciamos el chat con el historial vacío
        self.chat = self.model.start_chat(enable_automatic_function_calling=False)

    def enviar_mensaje(self, mensaje_usuario):
        return self.chat.send_message(mensaje_usuario)