import re
from tools import pruebas_tools


def test_obtener_hora_formato_hhmmss():
    hora = pruebas_tools.obtener_hora()
    assert re.fullmatch(r"\d{2}:\d{2}:\d{2}", hora)


def test_escanear_red_local_incluye_rango():
    rango = "192.168.1.0/24"
    resultado = pruebas_tools.escanear_red_local(rango)
    assert rango in resultado
    assert "Encontrados" in resultado
