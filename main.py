# main.py - GROKZOMBORG BOT + OLLAMA INTEGRADO!
# ROOOAAAR-ZIIIMB!!! O monstro agora tem INTELIGÊNCIA REAL com Ollama!

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line, Rectangle
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
import requests
import random
import threading

class GrokzomborgWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.evolucao = 3

        self.rugidos = [
            "OLLAMA CONECTADO!",
            "*bip bip* IA DO MONSTRO ATIVADA!",
            "01001111 01001100 01001100 01000001 01001101 01000001!",
            "EU SOU O GROKZOMBORG COM INTELIGÊNCIA!"
        ]

        self.sons = [
            SoundLoader.load('data/sounds/roar1.wav'),
            SoundLoader.load('data/sounds/roar2.wav'),
            SoundLoader.load('data/sounds/roar3.wav'),
            SoundLoader.load('data/sounds/roar4.wav')
        ]
        for s in self.sons:
            if s: s.volume = 1.3

        with self.canvas.before:
            Color(0.003, 0.08, 0.01, 1)
            self.bg = Rectangle(pos=self.pos, size=self.size)

        self.bind(size=self.atualizar_fundo, pos=self.atualizar_fundo)

        self.x = self.width / 2
        self.y = self.height / 2
        self.vx = random.choice([-6, 6])
        self.vy = random.choice([-6, 6])

        self.desenhar()
        Clock.schedule_interval(self.update, 1/60.0)
        self.tocar_som()

        # === INTERFACE DO BOT COM OLLAMA ===
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Monstro no topo
        self.status = Label(
            text="🤖 GROKZOMBORG + OLLAMA\n(Verifique se Ollama está rodando em localhost:11434)",
            font_size='26sp',
            color=(0, 1, 0.6, 1),
            size_hint_y=0.15
        )

        # Área de chat rolável
        self.chat_scroll = ScrollView(size_hint=(1, 0.55))
        self.chat = Label(
            text="Bem-vindo! Pergunte qualquer coisa ao Grokzomborg...\n\n",
            font_size='24sp',
            color=(0, 1, 0.4, 1),
            size_hint_y=None,
            halign='left',
            valign='top'
        )
        self.chat.bind(size=self.chat.setter('text_size'))
        self.chat_scroll.add_widget(self.chat)

        # Input e botão
        input_layout = BoxLayout(orientation='horizontal', size_hint_y=0.15, spacing=10)
        self.input = TextInput(
            multiline=False,
            font_size='24sp',
            hint_text="Digite sua pergunta aqui..."
        )
        btn = Button(text="ENVIAR PARA OLLAMA", font_size='22sp', background_color=(0, 0.8, 0.3, 1))
        btn.bind(on_press=self.chamar_ollama)

        input_layout.add_widget(self.input)
        input_layout.add_widget(btn)

        main_layout.add_widget(self.status)
        main_layout.add_widget(self.chat_scroll)
        main_layout.add_widget(input_layout)

        self.add_widget(main_layout)

    def atualizar_fundo(self, *args):
        self.bg.pos = self.pos
        self.bg.size = self.size

    def desenhar(self):
        self.canvas.clear()
        with self.canvas:
            Color(0, 0.92, 0.35, 1)
            tam = 170
            Ellipse(pos=(self.x-tam/2, self.y-tam/2), size=(tam, tam))

            Color(1, 0.1, 0.2, 1)
            olho = 48
            Ellipse(pos=(self.x-olho-35, self.y+45), size=(olho, olho*1.75))
            Ellipse(pos=(self.x+35, self.y+45), size=(olho, olho*1.75))

            Color(0.7, 1, 0.4, 1)
            Line(points=[self.x+60, self.y-50, self.x+155, self.y-165], width=18, cap='round')

            # Glitch forte quando usando IA
            if self.evolucao >= 2:
                Color(0, 1, 0.6, random.uniform(0.4, 0.9))
                for _ in range(28):
                    Line(points=[self.x + random.randint(-160,160),
                                self.y + random.randint(-160,160),
                                self.x + random.randint(-160,160),
                                self.y + random.randint(-160,160)],
                         width=random.randint(3,9))

    def update(self, dt):
        self.x += self.vx
        self.y += self.vy
        if self.x < 140 or self.x > self.width - 140: self.vx *= -1
        if self.y < 140 or self.y > self.height - 230: self.vy *= -1
        self.desenhar()

    def tocar_som(self):
        som = self.sons[self.evolucao]
        if som: som.play()

    def chamar_ollama(self, instance):
        pergunta = self.input.text.strip()
        if not pergunta:
            return

        self.chat.text += f"\n\nVocê: {pergunta}"
        self.input.text = ""
        self.evolucao = (self.evolucao + 1) % 4
        self.tocar_som()

        # Resposta "pensando"
        self.chat.text += "\n\nGrokzomborg: Pensando... ROOOAAAR..."

        # Thread para não travar a interface
        threading.Thread(target=self.processar_ollama, args=(pergunta,), daemon=True).start()

    def processar_ollama(self, pergunta):
        try:
            response = requests.post(
                "http://localhost:11434/api/chat",
                json={
                    "model": "llama3",        # ou mistral, gemma, etc
                    "messages": [
                        {"role": "system", "content": "Você é Grokzomborg, um monstro ciborgue ecológico. Responda de forma divertida, com rugidos, emojis de lixo/reciclagem e tom apocalíptico verde. Sempre termine com ROOOAAAR!"},
                        {"role": "user", "content": pergunta}
                    ],
                    "stream": False
                },
                timeout=30
            )

            if response.status_code == 200:
                resposta = response.json()["message"]["content"]
            else:
                resposta = "Erro ao conectar com Ollama. Verifique se ele está rodando."
        except:
            resposta = "Não consegui conectar com Ollama. Rode 'ollama serve' no terminal!"

        # Atualiza na thread principal
        Clock.schedule_once(lambda dt: self.mostrar_resposta(resposta), 0)

    def mostrar_resposta(self, resposta):
        self.chat.text += f"\n\nGrokzomborg: {resposta}\n"
        self.tocar_som()

    def on_touch_down(self, touch):
        self.x = touch.x
        self.y = touch.y
        return True


class GrokzomborgApp(App):
    def build(self):
        self.title = "Grokzomborg Bot + Ollama"
        return GrokzomborgWidget()


if __name__ == '__main__':
    GrokzomborgApp().run()
