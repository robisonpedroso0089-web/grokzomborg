# main.py - GROKZOMBORG: WEBSITE OFICIAL ATIVADO!
# ROOOAAAR-ZIIIMB!!! O monstro evoluiu para versão web-kivy híbrida!

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line, Rectangle
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import random
import os

class GrokzomborgWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.evolucao = 0
        self.energia = 100

        self.rugidos = [
            "🟢 WEBSITE GROKZOMBORG ATIVADO!",
            "🟡 *bip bip* GLITCH CÓSMICO!",
            "🔵 01010111 01000101 01000010 01010011!",
            "🔴 EU SOU O MONSTRO QUE TEM SITE PRÓPRIO!"
        ]

        # Carrega sons apenas se existirem
        self.sons = []
        sound_files = ['data/sounds/roar1.wav', 'data/sounds/roar2.wav', 
                       'data/sounds/roar3.wav', 'data/sounds/roar4.wav']
        for sound_file in sound_files:
            som = SoundLoader.load(sound_file) if os.path.exists(sound_file) else None
            self.sons.append(som)

        # Fundo cósmico
        with self.canvas.before:
            Color(0.005, 0.005, 0.02, 1)
            self.bg = Rectangle(pos=self.pos, size=self.size)

        self.bind(size=self.atualizar_fundo, pos=self.atualizar_fundo)

        # Posição e velocidade
        self.x = self.width / 2
        self.y = self.height / 2
        self.vx = random.choice([-6, 6])
        self.vy = random.choice([-6, 6])

        self.desenhar()
        Clock.schedule_interval(self.update, 1/60.0)

        # Website overlay
        self.site = Label(
            text="🌌 GROKZOMBORG\n\n"
                 "DESPERTE O CAOS RECICLADO\n\n"
                 "Bem-vindo ao mundo do glitch\n\n"
                 "Clique para evoluir • Toque para mover\n\n"
                 "Evolução: " + str(self.evolucao) + "/4 | Energia: " + str(self.energia) + "%\n\n"
                 "🎵 O monstro reciclado que zumbi o planeta de volta à vida!",
            font_size='32sp',
            color=(0, 1, 0.6, 1),
            size_hint=(0.9, 0.8),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            halign='center',
            valign='center'
        )
        self.add_widget(self.site)

    def atualizar_fundo(self, *args):
        self.bg.pos = self.pos
        self.bg.size = self.size

    def atualizar_site(self):
        """Atualiza informações do website overlay"""
        self.site.text = (
            "🌌 GROKZOMBORG\n\n"
            "DESPERTE O CAOS RECICLADO\n\n"
            "Bem-vindo ao mundo do glitch\n\n"
            f"Clique para evoluir • Toque para mover\n\n"
            f"Evolução: {self.evolucao + 1}/4 | Energia: {self.energia}%\n\n"
            f"{self.rugidos[self.evolucao]}"
        )

    def desenhar(self):
        """Desenha o Grokzomborg com evolução visual"""
        self.canvas.clear()
        with self.canvas:
            # Cores por estágio de evolução
            cores = [(1, 0.2, 0.2), (0.2, 1, 0.2), (0.2, 0.6, 1), (1, 1, 0.1)]
            Color(*cores[self.evolucao])

            # Corpo principal (aumenta com evolução)
            tam = 120 + self.evolucao * 50
            Ellipse(pos=(self.x - tam/2, self.y - tam/2), size=(tam, tam))

            # Olhos demoníacos
            Color(1, 0, 0, 1)
            olho = 35 + self.evolucao * 15
            Ellipse(pos=(self.x - olho - 35, self.y + 50), size=(olho, olho * 1.8))
            Ellipse(pos=(self.x + 35, self.y + 50), size=(olho, olho * 1.8))

            # Garra cibernética
            Color(0.7, 0.7, 0.9, 1)
            Line(points=[self.x + 60, self.y - 50, self.x + 160, self.y - 180],
                 width=12 + self.evolucao * 6, cap='round')

            # Efeito glitch no nível máximo
            if self.evolucao == 3:
                Color(1, 0, 1, random.uniform(0.5, 1.0))
                for _ in range(40):
                    x1 = self.x + random.randint(-200, 200)
                    y1 = self.y + random.randint(-200, 200)
                    x2 = self.x + random.randint(-200, 200)
                    y2 = self.y + random.randint(-200, 200)
                    Line(points=[x1, y1, x2, y2],
                         width=random.randint(2, 8))

    def update(self, dt):
        """Atualiza posição e redraw"""
        self.x += self.vx
        self.y += self.vy

        # Rebote nas bordas
        if self.x < 150 or self.x > self.width - 150:
            self.vx *= -1
        if self.y < 150 or self.y > self.height - 250:
            self.vy *= -1

        self.desenhar()

    def tocar_som(self):
        """Toca som de rugido se disponível"""
        som = self.sons[self.evolucao]
        if som:
            try:
                som.stop()
                som.play()
            except Exception as e:
                print(f"⚠️ Erro ao tocar som: {e}")

    def exibir_mensagem(self):
        """Mostra mensagem de rugido na tela"""
        msg = Label(
            text=self.rugidos[self.evolucao],
            font_size='42sp',
            color=(0, 1, 0.7, 1),
            size_hint=(0.95, None),
            height=120,
            pos_hint={'center_x': 0.5, 'top': 0.95}
        )
        self.add_widget(msg)
        Clock.schedule_once(lambda dt: self.remove_widget(msg), 3.0)

    def on_touch_down(self, touch):
        """Touch handler - move o monstro e evolui"""
        self.x = touch.x
        self.y = touch.y

        # Evolui
        self.evolucao = (self.evolucao + 1) % 4
        self.energia = max(0, self.energia - 15)

        # Efeitos
        self.tocar_som()
        self.exibir_mensagem()
        self.atualizar_site()

        # Reinicia energia ao atingir máxima evolução
        if self.evolucao == 0:
            self.energia = 100

        print(f"█ Evolução {self.evolucao + 1}/4 - Energia: {self.energia}% █")

        return True


class GrokzomborgApp(App):
    def build(self):
        self.title = "🧟‍♂️ Grokzomborg - Website Oficial"
        # Tenta carregar ícone, se não existir continua
        try:
            self.icon = "data/icon.png"
        except:
            pass

        return GrokzomborgWidget()


if __name__ == '__main__':
    print("🌌 INICIANDO GROKZOMBORG...")
    print("█" * 60)
    print("ROOOAAAR-ZIIIMB!!! O monstro reciclado acordou!")
    print("█" * 60)
    GrokzomborgApp().run()
