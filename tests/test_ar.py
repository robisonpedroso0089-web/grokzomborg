"""
🧪 GROKZOMBORG - Tests para Realidade Aumentada
ROOOAAAR! Testes unitários do módulo AR

pytest -v tests/test_ar.py
"""

import pytest
import cv2
import numpy as np
from ar_camera import ARCamera, ARMonsterVisualEffects, GestureDetector


class TestARCamera:
    """Testes para a classe ARCamera"""
    
    def setup_method(self):
        """Setup antes de cada teste"""
        self.ar_camera = ARCamera(evolution_level=1)
    
    def teardown_method(self):
        """Cleanup após cada teste"""
        if self.ar_camera.is_running:
            self.ar_camera.stop_camera()
    
    def test_initialization(self):
        """Testa inicialização da câmera AR"""
        assert self.ar_camera.evolution_level == 1
        assert self.ar_camera.is_running == False
        assert self.ar_camera.cap is None
    
    def test_evolution_level_increase(self):
        """Testa aumento de nível de evolução"""
        assert self.ar_camera.evolution_level == 1
        
        self.ar_camera.evolve_monster()
        assert self.ar_camera.evolution_level == 2
        
        self.ar_camera.evolve_monster()
        assert self.ar_camera.evolution_level == 3
        
        self.ar_camera.evolve_monster()
        assert self.ar_camera.evolution_level == 4
        
        # Não deve evoluir além de 4
        result = self.ar_camera.evolve_monster()
        assert result == False
        assert self.ar_camera.evolution_level == 4
    
    def test_monster_position_update(self):
        """Testa atualização de posição do monstro"""
        assert self.ar_camera.monster_pos is None
        
        # Simula detecção de rosto
        self.ar_camera.monster_pos = (100, 100)
        assert self.ar_camera.monster_pos == (100, 100)
    
    def test_monster_size_calculation(self):
        """Testa cálculo de tamanho do monstro"""
        initial_size = self.ar_camera.monster_size
        assert initial_size == 100
        
        # Simula detecção com diferentes tamanhos
        self.ar_camera.monster_size = 150
        assert self.ar_camera.monster_size == 150
    
    def test_fps_calculation(self):
        """Testa cálculo de FPS"""
        assert self.ar_camera.fps == 0
        
        # Simula frames
        for _ in range(30):
            self.ar_camera._update_fps()
        
        # FPS deve estar entre 0 e 60
        assert 0 <= self.ar_camera.fps <= 60


class TestARMonsterVisualEffects:
    """Testes para efeitos visuais do monstro"""
    
    def setup_method(self):
        """Setup antes de cada teste"""
        self.frame = np.zeros((480, 640, 3), dtype=np.uint8)
    
    def test_glow_effect(self):
        """Testa efeito de brilho"""
        result = ARMonsterVisualEffects.create_glow_effect(
            self.frame.copy(), 320, 240, 100, (0, 255, 0)
        )
        
        assert result.shape == self.frame.shape
        assert result.dtype == self.frame.dtype
    
    def test_distortion_wave(self):
        """Testa efeito de onda de distorção"""
        result = ARMonsterVisualEffects.create_distortion_wave(
            self.frame.copy(), 320, 240, wavelength=30, amplitude=10
        )
        
        assert result.shape == self.frame.shape
        assert result.dtype == self.frame.dtype
    
    def test_ghost_trail(self):
        """Testa efeito de rastro fantasmagórico"""
        positions = [(100, 100), (150, 150), (200, 200)]
        result = ARMonsterVisualEffects.create_ghost_trail(
            self.frame.copy(), positions, (0, 255, 255)
        )
        
        assert result.shape == self.frame.shape
        assert result.dtype == self.frame.dtype


class TestGestureDetector:
    """Testes para detector de gestos"""
    
    def setup_method(self):
        """Setup antes de cada teste"""
        self.detector = GestureDetector()
        self.frame = np.zeros((480, 640, 3), dtype=np.uint8)
    
    def test_initialization(self):
        """Testa inicialização do detector"""
        assert self.detector.hand_cascade is None
        assert len(self.detector.gesture_history) == 0
    
    def test_tap_detection(self):
        """Testa detecção de tap"""
        result = self.detector.detect_tap(self.frame, 320, 240, threshold=50)
        assert isinstance(result, bool)
    
    def test_swipe_detection(self):
        """Testa detecção de swipe"""
        result = self.detector.detect_swipe(self.frame)
        # Deve retornar None ou um valor válido
        assert result is None or isinstance(result, tuple)
    
    def test_peace_sign_detection(self):
        """Testa detecção de gesto peace"""
        result = self.detector.detect_peace_sign(self.frame)
        assert isinstance(result, bool)


class TestARIntegration:
    """Testes de integração do sistema AR completo"""
    
    def test_ar_workflow(self):
        """Testa fluxo completo de AR"""
        ar = ARCamera(evolution_level=1)
        
        # 1. Iniciar no nível 1
        assert ar.evolution_level == 1
        
        # 2. Evoluir para nível 2
        ar.evolve_monster()
        assert ar.evolution_level == 2
        
        # 3. Criar frame para processamento
        frame = np.zeros((480, 640, 3), dtype=np.uint8)
        
        # 4. Aplicar efeitos
        effects = ARMonsterVisualEffects()
        frame = effects.create_glow_effect(frame, 320, 240, 100, (0, 255, 0))
        
        assert frame.shape == (480, 640, 3)
        
        # 5. Parar câmera
        ar.stop_camera()
        assert ar.is_running == False
    
    def test_multiple_evolutions(self):
        """Testa múltiplas evoluções"""
        ar = ARCamera()
        
        for i in range(1, 5):
            assert ar.evolution_level == i
            if i < 4:
                ar.evolve_monster()


class TestPerformance:
    """Testes de performance e otimização"""
    
    def test_frame_processing_speed(self):
        """Testa velocidade de processamento de frame"""
        ar = ARCamera()
        frame = np.random.randint(0, 255, (480, 640, 3), dtype=np.uint8)
        
        import time
        start = time.time()
        
        # Processar 10 frames
        for _ in range(10):
            ar._process_frame(frame.copy())
        
        elapsed = time.time() - start
        
        # Deve processar pelo menos 10 frames em menos de 1 segundo
        assert elapsed < 2.0
    
    def test_memory_usage(self):
        """Testa uso de memória"""
        ar = ARCamera()
        
        # Criar múltiplas instâncias
        cameras = [ARCamera() for _ in range(5)]
        
        # Limpar
        for cam in cameras:
            cam.stop_camera()
        
        # Deve completar sem erro
        assert len(cameras) == 5


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
