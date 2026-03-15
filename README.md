# Agente Local con Gemini

Proyecto mínimo para probar un agente local que conversa con Gemini y puede solicitar ejecución de herramientas locales con confirmación del usuario.

**Características principales**
- Chat interactivo por consola.
- Llamadas a funciones locales controladas por permisos.
- Integración con `google-generativeai` y carga de variables desde `.env`.

## Requisitos
- Python 3.10+ (recomendado).
- Dependencias: `google-generativeai`, `python-dotenv`.

## Configuración
1. Crea un archivo `.env` en la raíz con:
```env
GEMINI_API_KEY=tu_api_key
```

2. Instala dependencias:
```bash
pip install google-generativeai python-dotenv
```

## Uso
Ejecuta:
```bash
python main.py
```

Comandos útiles dentro del chat:
- Escribe cualquier mensaje para conversar.
- `salir` para terminar.

Cuando el modelo solicite ejecutar una herramienta, el sistema pedirá confirmación explícita antes de ejecutar:
- `s` para autorizar.
- `n` para cancelar.

## Estructura del proyecto
- `main.py`: bucle principal de conversación y control de permisos.
- `core/agente.py`: configuración del modelo y envío de mensajes.
- `tools/pruebas_tools.py`: funciones locales disponibles (por ahora simuladas).

## Herramientas disponibles
Actualmente el agente puede ver y solicitar:
- `obtener_hora()`: devuelve la hora local del sistema.
- `escanear_red_local(rango)`: simula un escaneo de red en un rango.

Para agregar nuevas herramientas:
1. Define la función en `tools/pruebas_tools.py`.
2. Agrégala al diccionario `HERRAMIENTAS_DISPONIBLES`.
3. Regístrala en `core/agente.py` dentro de `tools=[...]`.

## Notas
- `escanear_red_local` es un mock; no realiza escaneo real.
- Las respuestas y resultados se imprimen en consola local para mantener privacidad.
