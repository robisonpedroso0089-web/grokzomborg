"""
🌍 GROKZOMBORG - Main Application with Augmented Reality
ROOOAAAR-ZIIIMB!!!

O monstro reciclado que veio salvar o planeta com glitch e rugidos!

Este arquivo foi atualizado em v1.1.0 para incluir:
- 🎥 Realidade Aumentada com câmera
- 🎮 Interatividade melhorada
- 🔊 Sistema de som completo
- ✨ Efeitos glitch dinâmicos
"""

import os
import random
import threading
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.properties import NumericProperty, StringProperty, BooleanProperty
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.core.audio import SoundLoader
from kivy.graphics import Color, Ellipse, Line, Rectangle
from kivy.animation import Animation
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg

# Importar módulo de RA
try:
    from ar_camera import ARCamera
    AR_AVAILABLE = True
except ImportError:
    AR_AVAILABLE = False
    print("⚠️ OpenCV não disponível - RA desabilitada")

# ROOOAAAR! Configurações da Janela
Window.size = (540, 960)
Window.clearcolor = (0.05, 0.15, 0.08, 1)  # Verde escuro cyber-punk
Window.allow_fullscreen = True

# ROOOAAAR! Diretórios de Assets
ASSETS_DIR = os.path.join(os.path.dirname(__file__), 'assets')
SOUNDS_DIR = os.path.join(ASSETS_DIR, 'sounds')
IMAGES_DIR = os.path.join(ASSETS_DIR, 'images')


class Grokzomborg(Widget):
    """
    ROOOAAAR! O monstro ciborgue principal!
    Evolui através de 4 níveis ao ser tocado.
    Possui movimento automático com colisão.
    Agora com Realidade Aumentada!
    """
    
    evolution_level = NumericProperty(1)
    tap_count = NumericProperty(0)
    roar_text = StringProperty("ROOOAAAR-ZIIIMB!!!")
    ar_enabled = BooleanProperty(False)
    
    # Configurações de movimento
    velocity_x = 3
    velocity_y = 2
    
    def __init__(self, ar_enabled=False, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (1, 1)
        self.pos_hint = {'x': 0, 'y': 0}
        
        # ROOOAAAR! Efeitos glitch
        self.glitch_intensity = 0
        self.glitch_offset_x = 0
        self.glitch_offset_y = 0
        
        # Sons (ROOOAAAR!)
        self.roar_sounds = {}
        self._load_sounds()
        
        # Variáveis de movimento
        self.monster_x = 200
        self.monster_y = 400
        self.monster_size = 150
        
        # RA
        self.ar_enabled = ar_enabled
        self.ar_camera = None
        if self.ar_enabled and AR_AVAILABLE:
            self.ar_camera = ARCamera(
                evolution_level=self.evolution_level,
                on_roar=self.roar
            )
        
        # Bind ao toque
        self.bind(size=self._update_canvas)
        
        # Clock para movimento automático
        Clock.schedule_interval(self._update_movement, 1/60)  # 60fps
        Clock.schedule_interval(self._update_glitch, 0.05)  # Efeito glitch
        
        self._draw_canvas()
    
    def _load_sounds(self):
        """ROOOAAAR! Carrega os sons de rugido"""
        for i in range(1, 5):
            sound_file = os.path.join(SOUNDS_DIR, f'roar{i}.wav')
            if os.path.exists(sound_file):
                try:
                    self.roar_sounds[i] = SoundLoader.load(sound_file)
                except Exception as e:
                    print(f"⚠️ Erro ao carregar roar{i}.wav: {e}")
            else:
                print(f"⚠️ Som não encontrado: {sound_file}")
    
    def _draw_canvas(self):
        """ROOOAAAR! Desenha o monstro e efeitos glitch na tela"""
        self.canvas.clear()
        
        with self.canvas:
            # Fundo glitch (efeito cyber-punk)
            Color(0.1, 0.3, 0.15, 0.3)
            Ellipse(pos=(self.monster_x + self.glitch_offset_x - 30,
                        self.monster_y + self.glitch_offset_y - 30),
                   size=(self.monster_size + 60, self.monster_size + 60))
            
            # Corpo do monstro (cor muda por nível)
            colors = [
                (0.2, 0.8, 0.3),   # Nível 1: Verde claro
                (0.1, 0.9, 0.4),   # Nível 2: Verde brilhante
                (0.0, 1.0, 0.5),   # Nível 3: Verde neon
                (0.8, 0.2, 0.9),   # Nível 4: Roxo cyber
            ]
            
            color = colors[min(self.evolution_level - 1, 3)]
            Color(*color, 0.9)
            
            # Corpo principal
            Ellipse(pos=(self.monster_x + self.glitch_offset_x,
                        self.monster_y + self.glitch_offset_y),
                   size=(self.monster_size, self.monster_size))
            
            # Olhos glitch (ROOOAAAR!)
            Color(1, 1, 0, 0.8)  # Amarelo neon
            eye_offset = self.monster_size * 0.25
            Ellipse(pos=(self.monster_x + eye_offset + self.glitch_offset_x,
                        self.monster_y + eye_offset + self.glitch_offset_y),
                   size=(20, 20))
            Ellipse(pos=(self.monster_x + self.monster_size - eye_offset - 20 + self.glitch_offset_x,
                        self.monster_y + eye_offset + self.glitch_offset_y),
                   size=(20, 20))
            
            # Aura glitch intensifica com evolution (ROOOAAAR!)
            if self.evolution_level > 1:
                Color(*color, 0.3)
                Line(circle=(self.monster_x + self.monster_size/2 + self.glitch_offset_x,
                            self.monster_y + self.monster_size/2 + self.glitch_offset_y,
                            self.monster_size * 0.6), width=2)
            
            if self.evolution_level > 2:
                Line(circle=(self.monster_x + self.monster_size/2 + self.glitch_offset_x,
                            self.monster_y + self.monster_size/2 + self.glitch_offset_y,
                            self.monster_size * 0.8), width=1)
            
            if self.evolution_level > 3:
                Color(0.8, 0.2, 0.9, 0.5)
                Line(circle=(self.monster_x + self.monster_size/2 + self.glitch_offset_x,
                            self.monster_y + self.monster_size/2 + self.glitch_offset_y,
                            self.monster_size), width=3)
    
    def _update_canvas(self, instance, value):
        """ROOOAAAR! Atualiza canvas quando tamanho muda"""
        self._draw_canvas()
    
    def _update_movement(self, dt):
        """ROOOAAAR! Atualiza movimento automático com colisão"""
        self.monster_x += self.velocity_x
        self.monster_y += self.velocity_y
        
        # Colisão com bordas
        if self.monster_x <= 0 or self.monster_x + self.monster_size >= self.width:
            self.velocity_x *= -1
            self.roar()
        
        if self.monster_y <= 0 or self.monster_y + self.monster_size >= self.height:
            self.velocity_y *= -1
            self.roar()
        
        self._draw_canvas()
    
    def _update_glitch(self, dt):
        """ROOOAAAR! Atualiza efeito glitch visual"""
        if self.glitch_intensity > 0:
            self.glitch_offset_x = random.randint(-5, 5) * self.glitch_intensity
            self.glitch_offset_y = random.randint(-5, 5) * self.glitch_intensity
            self.glitch_intensity *= 0.95
        else:
            self.glitch_offset_x = 0
            self.glitch_offset_y = 0
    
    def on_touch_down(self, touch):
        """ROOOAAAR! Toque na tela evolui o monstro!"""
        monster_rect = (self.monster_x, self.monster_y,
                       self.monster_size, self.monster_size)
        
        if (monster_rect[0] <= touch.x <= monster_rect[0] + monster_rect[2] and
            monster_rect[1] <= touch.y <= monster_rect[1] + monster_rect[3]):
            
            self.tap_count += 1
            self.glitch_intensity = 2
            self.roar()
            
            # Evolui a cada 10 toques
            if self.evolution_level < 4:
                new_level = min(4, 1 + self.tap_count // 10)
                if new_level > self.evolution_level:
                    self.evolution_level = new_level
                    self._evolution_animation()
                    
                    # Atualizar RA
                    if self.ar_camera:
                        self.ar_camera.evolution_level = new_level
            
            # Aumenta velocidade com evolução
            self.velocity_x *= (1 + self.evolution_level * 0.1)
            self.velocity_y *= (1 + self.evolution_level * 0.1)
            
            return True
        
        return super().on_touch_down(touch)
    
    def _evolution_animation(self):
        """ROOOAAAR! Animação de evolução"""
        anim = Animation(monster_size=self.monster_size * 1.2, duration=0.3)
        anim += Animation(monster_size=self.monster_size * 0.9, duration=0.2)
        anim.start(self)
    
    def roar(self):
        """ROOOAAAR! Toca som de rugido"""
        sound_index = min(self.evolution_level, 4)
        if sound_index in self.roar_sounds:
            try:
                self.roar_sounds[sound_index].play()
            except Exception as e:
                print(f"⚠️ Erro ao tocar som: {e}")
        
        roar_messages = [
            "ROOOAAAR-ZIIIMB!!!",
            "RECICLEEEE!!!",
            "EEEEVOLVIIII!!!",
            "CYBER-PUUUNK!!!",
            "🌍 SALVA O PLANETA! 🌍"
        ]
        self.roar_text = roar_messages[min(self.evolution_level - 1, 4)]


class GrokzomborgApp(App):
    """ROOOAAAR! Aplicação principal do Grokzomborg com RA"""
    
    def build(self):
        """ROOOAAAR! Constrói a interface"""
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Header
        header = BoxLayout(size_hint_y=0.1, spacing=10)
        
        level_label = Label(
            text=f"Nível: [color=00ff00]{1}[/color]",
            markup=True,
            size_hint_x=0.5,
            font_size='18sp'
        )
        
        tap_label = Label(
            text=f"Toques: [color=ffff00]{0}[/color]",
            markup=True,
            size_hint_x=0.5,
            font_size='18sp'
        )
        
        header.add_widget(level_label)
        header.add_widget(tap_label)
        
        # Game area
        game_area = FloatLayout(size_hint_y=0.85)
        monster = Grokzomborg(ar_enabled=True)
        game_area.add_widget(monster)
        
        # Atualizar labels
        def update_labels(instance, value):
            level_label.text = f"Nível: [color=00ff00]{monster.evolution_level}[/color]"
            tap_label.text = f"Toques: [color=ffff00]{monster.tap_count}[/color]"
        
        monster.bind(evolution_level=update_labels, tap_count=update_labels)
        
        # Footer
        footer = Label(
            text=monster.roar_text,
            size_hint_y=0.05,
            font_size='16sp',
            color=(0, 1, 0.5, 1)
        )
        monster.bind(roar_text=lambda inst, val: setattr(footer, 'text', val))
        
        main_layout.add_widget(header)
        main_layout.add_widget(game_area)
        main_layout.add_widget(footer)
        
        self.title = "🌍 GROKZOMBORG - O Monstro Ecológico! 🌍"
        
        return main_layout


if __name__ == '__main__':
    GrokzomborgApp().run()
