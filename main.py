from core.agente import MiAgente
from tools.pruebas_tools import HERRAMIENTAS_DISPONIBLES
import google.generativeai as genai

def ejecutar_bucle():
    agente = MiAgente()
    print("🤖 Agente Local Activado. Escribe 'salir' para terminar.")

    while True:
        usuario = input("\n👤 Tú: ")
        if usuario.lower() == "salir": break

        # 1. Enviar mensaje a Gemini
        response = agente.enviar_mensaje(usuario)
        
        # 2. Revisar si Gemini quiere usar una herramienta
        # (Gemini puede pedir múltiples llamadas a funciones)
        for part in response.candidates[0].content.parts:
            if fn := part.function_call:
                nombre_fn = fn.name
                argumentos = fn.args
                
                print(f"\n⚠️  [SOLICITUD DE ACCIÓN]: El agente quiere ejecutar: {nombre_fn}")
                print(f"   Parámetros: {dict(argumentos)}")
                
                # --- SISTEMA DE PERMISOS ---
                confirmacion = input("   ¿Autorizas esta ejecución? (s/n): ")
                
                if confirmacion.lower() == 's':
                    # Ejecutar la función localmente
                    funcion_real = HERRAMIENTAS_DISPONIBLES[nombre_fn]
                    resultado = funcion_real(**argumentos)
                    
                    # Mostrar resultado en consola local (Privacidad)
                    print(f"✅ Resultado local: {resultado}")
                    
                    # 3. Enviar el resultado de vuelta a Gemini para que lo interprete
                    response = agente.chat.send_message(
                        genai.protos.Content(
                            parts=[genai.protos.Part(
                                function_response=genai.protos.FunctionResponse(
                                    name=nombre_fn,
                                    response={'result': resultado}
                                )
                            )]
                        )
                    )
                    print(f"\n🤖 Agente: {response.text}")
                else:
                    print("🚫 Acción cancelada por el usuario.")
            else:
                # Si no hay funciones, solo imprime la respuesta de texto
                if response.text:
                    print(f"\n🤖 Agente: {response.text}")

if __name__ == "__main__":
    ejecutar_bucle()