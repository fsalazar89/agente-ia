import datetime

def obtener_hora():
    """Devuelve la hora actual del sistema. Útil para saludos o logs."""
    return datetime.datetime.now().strftime("%H:%M:%S")

def escanear_red_local(rango: str):
    """
    Simula un escaneo de red en un rango específico (ej: 192.168.1.0/24).
    Devuelve una lista de dispositivos encontrados.
    """
    # Aquí luego pondrás tu código de nmap
    return f"Escaneando {rango}... Encontrados: 192.168.1.1 (Router), 192.168.1.15 (PC-Local)"

# Diccionario para que el agente sepa qué funciones tiene disponibles
HERRAMIENTAS_DISPONIBLES = {
    "obtener_hora": obtener_hora,
    "escanear_red_local": escanear_red_local
}