import importlib


class DummyChat:
    def send_message(self, msg):
        return f"echo:{msg}"


class DummyModel:
    def __init__(self, model_name, tools):
        self.model_name = model_name
        self.tools = tools

    def start_chat(self, enable_automatic_function_calling=False):
        return DummyChat()


def test_enviar_mensaje(monkeypatch):
    # Evita dependencia de red y API real
    monkeypatch.setenv("GEMINI_API_KEY", "dummy")
    import core.agente as agente_mod
    importlib.reload(agente_mod)
    monkeypatch.setattr(agente_mod.genai, "GenerativeModel", DummyModel)

    agente = agente_mod.MiAgente()
    resp = agente.enviar_mensaje("hola")

    assert resp == "echo:hola"


def test_registro_de_tools(monkeypatch):
    monkeypatch.setenv("GEMINI_API_KEY", "dummy")
    import core.agente as agente_mod
    importlib.reload(agente_mod)

    captured = {}

    class CapturingModel(DummyModel):
        def __init__(self, model_name, tools):
            super().__init__(model_name, tools)
            captured["model_name"] = model_name
            captured["tools"] = tools

    monkeypatch.setattr(agente_mod.genai, "GenerativeModel", CapturingModel)
    _ = agente_mod.MiAgente()

    assert captured["model_name"] == "gemini-2.5-flash"
    assert agente_mod.obtener_hora in captured["tools"]
    assert agente_mod.escanear_red_local in captured["tools"]
