"""
🎵 GROKZOMBORG - Sound Manager
ROOOAAAR! Sistema de gerenciamento de áudio

Gerencia sons, efeitos sonoros e rugidos do monstro
"""

import os
from kivy.core.audio import SoundLoader
from pydub import AudioSegment
from pydub.generators import Sine
import random


class SoundManager:
    """Gerenciador de áudio para Grokzomborg"""
    
    def __init__(self, sounds_dir='assets/sounds'):
        """Inicializa o gerenciador de som"""
        self.sounds_dir = sounds_dir
        self.roar_sounds = {}
        self.sfx_sounds = {}
        self.current_bgm = None
        self.volume = 1.0
        self._load_sounds()
    
    def _load_sounds(self):
        """Carrega todos os sons disponíveis"""
        # Rugidos
        for i in range(1, 5):
            sound_file = os.path.join(self.sounds_dir, f'roar{i}.wav')
            if os.path.exists(sound_file):
                try:
                    self.roar_sounds[i] = SoundLoader.load(sound_file)
                    print(f"✅ Rugido {i} carregado")
                except Exception as e:
                    print(f"⚠️ Erro ao carregar roar{i}.wav: {e}")
    
    def play_roar(self, level=1):
        """Toca rugido baseado no nível de evolução"""
        sound_index = min(level, 4)
        if sound_index in self.roar_sounds:
            try:
                self.roar_sounds[sound_index].play()
                print(f"🔊 ROOOAAAR (Nível {level})!")
            except Exception as e:
                print(f"❌ Erro ao tocar rugido: {e}")
    
    def play_evolve_sound(self):
        """Toca som de evolução"""
        # Gerar som sintetizado
        print("✨ Som de evolução!")
    
    def play_glitch_sound(self):
        """Toca som de glitch"""
        print("🔲 Som de glitch!")
    
    def set_volume(self, volume):
        """Define volume (0.0 a 1.0)"""
        self.volume = max(0.0, min(1.0, volume))
        print(f"🔊 Volume: {self.volume * 100:.0f}%")


class VisualsManager:
    """Gerenciador de efeitos visuais e renderização"""
    
    def __init__(self):
        """Inicializa o gerenciador de visuais"""
        self.glitch_intensity = 0
        self.particle_systems = {}
    
    @staticmethod
    def create_glitch_animation(duration=0.5, intensity=1.0):
        """Cria animação de glitch"""
        return {
            'duration': duration,
            'intensity': intensity,
            'type': 'glitch'
        }
    
    @staticmethod
    def create_evolution_animation(duration=1.0):
        """Cria animação de evolução"""
        return {
            'duration': duration,
            'type': 'evolution'
        }


class GameState:
    """Gerenciador de estado do jogo"""
    
    def __init__(self):
        """Inicializa o estado do jogo"""
        self.evolution_level = 1
        self.tap_count = 0
        self.total_taps = 0
        self.session_time = 0
        self.energy = 100
        self.achievements = []
    
    def add_tap(self):
        """Adiciona um toque"""
        self.tap_count += 1
        self.total_taps += 1
        self.energy = max(0, self.energy - 1)
        return self.tap_count
    
    def evolve(self):
        """Evolui o monstro"""
        if self.evolution_level < 4:
            self.evolution_level += 1
            self.energy = max(50, self.energy - 20)
            return True
        return False
    
    def save_state(self, filename='grokzomborg_save.json'):
        """Salva o estado do jogo"""
        import json
        state = {
            'evolution_level': self.evolution_level,
            'tap_count': self.tap_count,
            'total_taps': self.total_taps,
            'energy': self.energy,
            'achievements': self.achievements
        }
        with open(filename, 'w') as f:
            json.dump(state, f, indent=2)
        print(f"💾 Estado salvo em {filename}")
    
    def load_state(self, filename='grokzomborg_save.json'):
        """Carrega o estado do jogo"""
        import json
        try:
            with open(filename, 'r') as f:
                state = json.load(f)
            self.evolution_level = state.get('evolution_level', 1)
            self.tap_count = state.get('tap_count', 0)
            self.total_taps = state.get('total_taps', 0)
            self.energy = state.get('energy', 100)
            self.achievements = state.get('achievements', [])
            print(f"📂 Estado carregado de {filename}")
        except FileNotFoundError:
            print(f"⚠️ Arquivo de save não encontrado: {filename}")


class AchievementSystem:
    """Sistema de conquistas/achievements"""
    
    ACHIEVEMENTS = {
        'first_tap': {'name': 'Primeiro Toque', 'description': 'Toque no monstro pela primeira vez'},
        'evolution_1': {'name': 'Despertar', 'description': 'Alcance nível 2'},
        'evolution_2': {'name': 'Evoluído', 'description': 'Alcance nível 3'},
        'evolution_3': {'name': 'Potencializado', 'description': 'Alcance nível 4'},
        'evolution_4': {'name': 'Caos Total', 'description': 'Alcance nível máximo'},
        'speed_tapper': {'name': 'Tapper Rápido', 'description': 'Faça 50 toques'},
        'eco_warrior': {'name': 'Guerreiro Ecológico', 'description': 'Junte 100 toques'},
        'ar_explorer': {'name': 'Explorador RA', 'description': 'Use RA por 5 minutos'},
        'glitch_master': {'name': 'Mestre do Glitch', 'description': 'Ative glitch 20 vezes'},
        'sound_seeker': {'name': 'Buscador de Sons', 'description': 'Ouça todos os rugidos'},
    }
    
    def __init__(self):
        """Inicializa o sistema de achievements"""
        self.unlocked = []
    
    def unlock(self, achievement_id):
        """Desbloqueia um achievement"""
        if achievement_id not in self.unlocked:
            self.unlocked.append(achievement_id)
            if achievement_id in self.ACHIEVEMENTS:
                achievement = self.ACHIEVEMENTS[achievement_id]
                print(f"🏆 Desbloqueado: {achievement['name']}!")
                print(f"   {achievement['description']}")
            return True
        return False
    
    def get_progress(self):
        """Retorna progresso dos achievements"""
        total = len(self.ACHIEVEMENTS)
        unlocked = len(self.unlocked)
        percentage = (unlocked / total) * 100
        return {
            'unlocked': unlocked,
            'total': total,
            'percentage': percentage
        }


class LevelProgression:
    """Sistema de progressão de níveis"""
    
    LEVELS = {
        1: {
            'name': 'Despertado',
            'color': (0.2, 0.8, 0.3),
            'taps_required': 0,
            'size_multiplier': 1.0,
            'speed_multiplier': 1.0,
            'description': 'O monstro acaba de acordar do lixão'
        },
        2: {
            'name': 'Evoluído',
            'color': (0.1, 0.9, 0.4),
            'taps_required': 10,
            'size_multiplier': 1.3,
            'speed_multiplier': 1.2,
            'description': 'Absorveu energia ecológica'
        },
        3: {
            'name': 'Potencializado',
            'color': (0.0, 1.0, 0.5),
            'taps_required': 25,
            'size_multiplier': 1.6,
            'speed_multiplier': 1.4,
            'description': 'Transformação cósmica em andamento'
        },
        4: {
            'name': 'Caos Total',
            'color': (0.8, 0.2, 0.9),
            'taps_required': 50,
            'size_multiplier': 2.0,
            'speed_multiplier': 1.6,
            'description': 'Forma final: Puro glitch e fúria ecológica'
        }
    }
    
    @staticmethod
    def get_level_info(level):
        """Retorna informações do nível"""
        return LevelProgression.LEVELS.get(level, {})
    
    @staticmethod
    def get_taps_for_level(level):
        """Retorna toques necessários para alcançar um nível"""
        return LevelProgression.LEVELS.get(level, {}).get('taps_required', 0)


class ARSettings:
    """Configurações de Realidade Aumentada"""
    
    def __init__(self):
        """Inicializa as configurações de RA"""
        self.ar_enabled = True
        self.camera_index = 0
        self.resolution = (640, 480)
        self.fps_target = 30
        self.monster_scale = 1.0
        self.glitch_intensity = 1.0
        self.particle_enabled = True
        self.gesture_detection = True
    
    def set_resolution(self, width, height):
        """Define resolução da câmera"""
        self.resolution = (width, height)
        print(f"📷 Resolução definida: {width}x{height}")
    
    def set_glitch_intensity(self, intensity):
        """Define intensidade de glitch (0.0 a 1.0)"""
        self.glitch_intensity = max(0.0, min(1.0, intensity))
        print(f"✨ Intensidade de glitch: {self.glitch_intensity * 100:.0f}%")


if __name__ == '__main__':
    print("🎮 Game Systems para GROKZOMBORG")
    
    # Teste do gerenciador de som
    sound_manager = SoundManager()
    sound_manager.play_roar(1)
    sound_manager.set_volume(0.8)
    
    # Teste do estado do jogo
    game_state = GameState()
    game_state.add_tap()
    print(f"Toques: {game_state.tap_count}")
    
    # Teste do sistema de achievements
    achievements = AchievementSystem()
    achievements.unlock('first_tap')
    progress = achievements.get_progress()
    print(f"Achievements: {progress['unlocked']}/{progress['total']}")
    
    # Teste da progressão
    level_info = LevelProgression.get_level_info(2)
    print(f"Nível 2: {level_info.get('name')}")
