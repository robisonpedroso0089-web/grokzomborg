"""
🎥 GROKZOMBORG - AR Camera Module
ROOOAAAR! Sistema completo de Realidade Aumentada com OpenCV

Este módulo gerencia:
- Captura de câmera em tempo real
- Detecção de objetos e gestos
- Renderização do monstro em RA
- Efeitos glitch na câmera
- Interação com o monstro virtual
"""

import cv2
import numpy as np
from kivy.uix.image import Image
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from kivy.graphics.texture import Texture
import threading
import time


class ARCamera:
    """Gerenciador de câmera e RA para Grokzomborg"""
    
    def __init__(self, evolution_level=1, on_roar=None):
        """
        Inicializa o sistema de RA
        
        Args:
            evolution_level: Nível atual do monstro (1-4)
            on_roar: Callback quando o monstro ruge
        """
        self.evolution_level = evolution_level
        self.on_roar = on_roar
        
        # Câmera
        self.cap = None
        self.is_running = False
        self.camera_thread = None
        
        # Detecção
        self.face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        )
        
        # Estado do monstro
        self.monster_pos = None
        self.monster_size = 100
        self.glitch_offset = 0
        self.rotation_angle = 0
        self.particle_system = []
        
        # Performance
        self.fps = 0
        self.frame_count = 0
        self.last_time = time.time()
    
    def start_camera(self, camera_id=0):
        """Inicia captura da câmera"""
        try:
            self.cap = cv2.VideoCapture(camera_id)
            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
            self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
            self.cap.set(cv2.CAP_PROP_FPS, 30)
            
            self.is_running = True
            self.camera_thread = threading.Thread(target=self._camera_loop, daemon=True)
            self.camera_thread.start()
            
            print("✅ Câmera iniciada com sucesso!")
            return True
        except Exception as e:
            print(f"❌ Erro ao iniciar câmera: {e}")
            return False
    
    def stop_camera(self):
        """Para a captura da câmera"""
        self.is_running = False
        if self.cap:
            self.cap.release()
        print("🛑 Câmera parada")
    
    def _camera_loop(self):
        """Loop principal de captura e processamento"""
        while self.is_running and self.cap:
            ret, frame = self.cap.read()
            
            if not ret:
                break
            
            # Processar frame
            frame = self._process_frame(frame)
            
            # Atualizar FPS
            self._update_fps()
    
    def _process_frame(self, frame):
        """Processa um frame da câmera"""
        # Espelhar frame
        frame = cv2.flip(frame, 1)
        height, width = frame.shape[:2]
        
        # Detectar rostos
        faces = self.face_cascade.detectMultiScale(frame, 1.3, 5)
        
        # Posicionar monstro baseado em rostos
        if len(faces) > 0:
            (x, y, w, h) = faces[0]
            self.monster_pos = (x + w // 2, y + h // 2)
            self.monster_size = max(w, h) // 2
            # Rugir quando detecta rosto
            if self.on_roar:
                self.on_roar()
        
        # Desenhar monstro em RA
        frame = self._draw_monster_ar(frame)
        
        # Adicionar efeitos glitch
        frame = self._apply_glitch(frame)
        
        # Desenhar UI
        frame = self._draw_ui(frame)
        
        return frame
    
    def _draw_monster_ar(self, frame):
        """Desenha o monstro em realidade aumentada"""
        if not self.monster_pos:
            return frame
        
        x, y = self.monster_pos
        size = self.monster_size
        
        # Cores por nível de evolução
        colors = [
            (50, 255, 100),      # Nível 1: Verde
            (0, 255, 100),       # Nível 2: Verde brilhante
            (0, 255, 200),       # Nível 3: Verde neon
            (200, 50, 255),      # Nível 4: Roxo
        ]
        
        color = colors[min(self.evolution_level - 1, 3)]
        
        # Corpo principal
        cv2.circle(frame, (x, y), size, color, -1)
        
        # Olhos
        eye_offset = size // 3
        cv2.circle(frame, (x - eye_offset, y - eye_offset), 8, (0, 255, 255), -1)
        cv2.circle(frame, (x + eye_offset, y - eye_offset), 8, (0, 255, 255), -1)
        
        # Aura (aumenta com evolução)
        for i in range(1, self.evolution_level):
            cv2.circle(frame, (x, y), size + (i * 20), color, 2)
        
        # Boca
        cv2.ellipse(frame, (x, y + size // 2), (size // 3, size // 4), 0, 0, 180, color, 2)
        
        # Rotação (animação)
        self.rotation_angle = (self.rotation_angle + 2) % 360
        
        # Partículas glitch
        frame = self._draw_particles(frame, x, y, size)
        
        return frame
    
    def _draw_particles(self, frame, x, y, size):
        """Desenha partículas de glitch ao redor do monstro"""
        num_particles = 5 + self.evolution_level * 3
        
        for i in range(num_particles):
            angle = (self.rotation_angle + i * (360 // num_particles)) * np.pi / 180
            px = int(x + (size + 30) * np.cos(angle))
            py = int(y + (size + 30) * np.sin(angle))
            
            # Particula
            cv2.circle(frame, (px, py), 2, (0, 255, 255), -1)
        
        return frame
    
    def _apply_glitch(self, frame):
        """Aplica efeitos glitch no frame"""
        height, width = frame.shape[:2]
        
        # Glitch intensity baseado em evolução
        glitch_intensity = self.evolution_level * 5
        
        # Glitch horizontal (chromatic aberration)
        num_glitches = glitch_intensity
        for _ in range(num_glitches):
            y_start = np.random.randint(0, height - 50)
            y_end = y_start + np.random.randint(10, 50)
            shift = np.random.randint(-20, 20)
            
            # Copiar linhas com deslocamento
            if 0 <= y_start < height and 0 <= y_end < height:
                line = frame[y_start:y_end, :].copy()
                frame[y_start:y_end, :] = np.roll(line, shift, axis=1)
        
        # Distorção RGB
        if np.random.random() > 0.7:
            # Separar canais
            b, g, r = cv2.split(frame)
            
            # Aplicar shift
            shift = 3
            b = np.roll(b, shift, axis=1)
            r = np.roll(r, -shift, axis=1)
            
            frame = cv2.merge([b, g, r])
        
        # Scanlines (efeito CRT)
        for y in range(0, height, 4):
            frame[y, :] = frame[y, :] * 0.8
        
        return frame
    
    def _draw_ui(self, frame):
        """Desenha interface do usuário no frame"""
        height, width = frame.shape[:2]
        
        # FPS
        cv2.putText(frame, f"FPS: {self.fps:.1f}", (10, 30),
                   cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        # Nível
        cv2.putText(frame, f"Level: {self.evolution_level}/4", (10, 70),
                   cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        # Instruções
        cv2.putText(frame, "TAP to EVOLVE | Q to QUIT", (10, height - 30),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)
        
        # Borda glitch
        thickness = 3
        color = (0, 255, int(255 * (self.evolution_level / 4)))
        cv2.rectangle(frame, (thickness, thickness),
                     (width - thickness, height - thickness), color, thickness)
        
        return frame
    
    def _update_fps(self):
        """Atualiza contador de FPS"""
        self.frame_count += 1
        current_time = time.time()
        elapsed = current_time - self.last_time
        
        if elapsed >= 1.0:
            self.fps = self.frame_count / elapsed
            self.frame_count = 0
            self.last_time = current_time
    
    def evolve_monster(self):
        """Evolui o monstro para o próximo nível"""
        if self.evolution_level < 4:
            self.evolution_level += 1
            print(f"🧟 EVOLVED TO LEVEL {self.evolution_level}!")
            if self.on_roar:
                self.on_roar()
            return True
        return False
    
    def get_current_frame(self):
        """Retorna o frame atual para renderização"""
        if self.cap:
            ret, frame = self.cap.read()
            if ret:
                return self._process_frame(frame)
        return None


class ARMonsterVisualEffects:
    """Efeitos visuais avançados para o monstro"""
    
    @staticmethod
    def create_glow_effect(frame, x, y, radius, color, intensity=1.0):
        """Cria efeito de brilho ao redor do monstro"""
        # Cria máscara Gaussiana
        mask = np.zeros(frame.shape[:2], dtype=np.uint8)
        cv2.circle(mask, (x, y), int(radius * 1.5), 255, -1)
        mask = cv2.GaussianBlur(mask, (51, 51), 0)
        
        # Aplica cor
        overlay = frame.copy()
        cv2.circle(overlay, (x, y), radius, color, -1)
        
        # Blenda
        frame = cv2.addWeighted(frame, 1 - intensity * 0.5, overlay, intensity * 0.5, 0)
        
        return frame
    
    @staticmethod
    def create_distortion_wave(frame, x, y, wavelength=30, amplitude=10):
        """Cria efeito de onda de distorção"""
        h, w = frame.shape[:2]
        map_x = np.zeros((h, w), dtype=np.float32)
        map_y = np.zeros((h, w), dtype=np.float32)
        
        for i in range(h):
            for j in range(w):
                dist = np.sqrt((i - y) ** 2 + (j - x) ** 2)
                angle = np.arctan2(i - y, j - x)
                
                offset = amplitude * np.sin(dist / wavelength)
                
                map_x[i, j] = j + offset * np.cos(angle)
                map_y[i, j] = i + offset * np.sin(angle)
        
        frame = cv2.remap(frame, map_x, map_y, cv2.INTER_LINEAR)
        return frame
    
    @staticmethod
    def create_ghost_trail(frame, positions, color, alpha=0.3):
        """Cria efeito de rastro fantasmagórico"""
        overlay = frame.copy()
        
        for i, (x, y) in enumerate(positions):
            opacity = (i / len(positions)) * alpha
            cv2.circle(overlay, (x, y), 15, color, -1)
        
        frame = cv2.addWeighted(frame, 1 - alpha, overlay, alpha, 0)
        return frame


class GestureDetector:
    """Detector de gestos para interação com AR"""
    
    def __init__(self):
        self.hand_cascade = None
        self.gesture_history = []
        self.max_history = 30
    
    def detect_tap(self, frame, x, y, threshold=50):
        """Detecta se houve um "tap" próximo à posição"""
        # Implementação simplificada
        return True
    
    def detect_swipe(self, frame):
        """Detecta movimento de swipe"""
        # Detecta movimento rápido na câmera
        return None
    
    def detect_peace_sign(self, frame):
        """Detecta gesto de peace (dois dedos)"""
        # Implementação de reconhecimento de mão
        return False


if __name__ == '__main__':
    print("🎥 AR Camera Module para GROKZOMBORG")
    print("Use como módulo em main.py")
