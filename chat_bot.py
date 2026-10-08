import os
from typing import List, Dict, Any


class MemoryManager:
    """Gerencia o histórico da conversa para manter contexto do Grokzomborg."""

    def __init__(self, max_history: int = 10, storage_path: str = "") -> None:
        self.max_history = max_history
        self.messages: List[Dict[str, str]] = []
        self.storage_path = storage_path or os.path.join(os.getcwd(), ".grokzomborg_memory.json")

    def add_message(self, role: str, content: Any) -> None:
        text = str(content).strip()
        if not text:
            return
        self.messages.append({"role": role, "content": text})
        if len(self.messages) > self.max_history:
            self.messages = self.messages[-self.max_history:]
        self.save()

    def get_messages(self) -> List[Dict[str, str]]:
        return list(self.messages)

    def clear(self) -> None:
        self.messages.clear()
        self.save()

    def save(self) -> None:
        try:
            with open(self.storage_path, "w", encoding="utf-8") as file:
                file.write("[\n")
                for index, message in enumerate(self.messages):
                    suffix = "," if index < len(self.messages) - 1 else ""
                    file.write(f"  {json.dumps(message)}{suffix}\n")
                file.write("]\n")
        except Exception:
            pass

    def load(self) -> None:
        try:
            if not os.path.exists(self.storage_path):
                self.messages = []
                return
            with open(self.storage_path, "r", encoding="utf-8") as file:
                raw = file.read().strip()
                if not raw:
                    self.messages = []
                    return
                self.messages = json.loads(raw)
        except Exception:
            self.messages = []


if __name__ == "__main__":
    memory = MemoryManager(max_history=5)
    memory.add_message("user", "Olá Grokzomborg!")
    memory.add_message("assistant", "ROOOAAAR! Bem-vindo ao caos reciclado!")
    print(memory.get_messages())
