import os
import json
from typing import List, Dict, Optional, Any

import requests


class OllamaChat:
    """Cliente local para conversar com modelos LLM rodando no Ollama."""

    def __init__(
        self,
        host: Optional[str] = None,
        model: Optional[str] = None,
        temperature: float = 0.7,
        timeout: int = 30,
        system_prompt: Optional[str] = None,
    ) -> None:
        self.host = (host or os.getenv("OLLAMA_HOST") or "http://localhost:11434").rstrip("/")
        self.model = model or os.getenv("OLLAMA_MODEL") or "mistral"
        self.temperature = float(os.getenv("OLLAMA_TEMPERATURE", str(temperature)))
        self.timeout = timeout
        self.system_prompt = system_prompt or os.getenv(
            "GROKZOMBORG_SYSTEM_PROMPT",
            "Você é o Grokzomborg, um monstro reciclado e amigável, com personalidade cyberpunk. "
            "Ensina sustentabilidade e reciclagem em português, com respostas curtas, divertidas e ainda um toque de glitch.",
        )

    def _request(self, endpoint: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        url = f"{self.host}{endpoint}"
        try:
            response = requests.post(url, json=payload, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as exc:
            raise RuntimeError(f"Ollama indisponível em {url}: {exc}") from exc

    def generate(self, prompt: str, system_prompt: Optional[str] = None) -> str:
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
            "options": {"temperature": self.temperature},
        }
        if system_prompt:
            payload["system"] = system_prompt
        data = self._request("/api/generate", payload)
        response = data.get("response", "").strip()
        return response

    def chat(self, message: str, history: Optional[List[Dict[str, str]]] = None) -> str:
        if history is None:
            history = []

        messages: List[Dict[str, str]] = [{"role": "system", "content": self.system_prompt}]
        for item in history[-12:]:
            role = str(item.get("role", "user")).strip() or "user"
            content = str(item.get("content", "")).strip()
            if role in {"user", "assistant", "system"} and content:
                messages.append({"role": role, "content": content})

        messages.append({"role": "user", "content": str(message).strip()})

        payload = {
            "model": self.model,
            "messages": messages,
            "stream": False,
            "options": {"temperature": self.temperature},
        }
        data = self._request("/api/chat", payload)
        message_data = data.get("message", {})
        return str(message_data.get("content", "")).strip()

    def chat_with_memory(self, message: str, memory: Optional[Any] = None) -> str:
        if memory is None:
            history = []
        else:
            history = getattr(memory, "get_messages", lambda: [])()
            if not isinstance(history, list):
                history = []
        return self.chat(message, history=history)

    def generate_eco_content(self, topic: str) -> str:
        prompt = (
            f"Explique o tema '{topic}' de forma divertida, educativa e curta, "
            "destacando impacto ambiental, reciclagem e sustentabilidade."
        )
        return self.generate(prompt, system_prompt=self.system_prompt)

    @staticmethod
    def list_models(host: Optional[str] = None) -> List[str]:
        host_value = (host or os.getenv("OLLAMA_HOST") or "http://localhost:11434").rstrip("/")
        try:
            response = requests.get(f"{host_value}/api/tags", timeout=15)
            response.raise_for_status()
            payload = response.json()
            models = []
            for model in payload.get("models", []):
                name = model.get("name")
                if name:
                    models.append(name)
            return models
        except Exception:
            return []


if __name__ == "__main__":
    chat = OllamaChat()
    print(f"Modelo ativo: {chat.model}")
    print(f"Modelos disponíveis: {chat.list_models()}")
    print(chat.chat("Olá! Me fale sobre reciclagem em uma frase."))
