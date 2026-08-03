#!/usr/bin/env python3
"""
📖 GROKZOMBORG - Guia de Desenvolvimento
ROOOAAAR! Documentação técnica completa

Como contribuir, compilar e customizar o Grokzomborg
"""

# ============================================================================
# 🚀 GUIA RÁPIDO DE INÍCIO
# ============================================================================

## 1. Instalação de Dependências

```bash
# Clone o repositório
git clone https://github.com/robisonpedroso0089-web/grokzomborg.git
cd grokzomborg

# Crie um ambiente virtual
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Instale tudo
pip install -r requirements.txt

# (Opcional) Para desenvolvimento
pip install -r requirements-dev.txt
```

## 2. Executar a Aplicação

```bash
# Desktop (com RA)
python main.py

# Website
open index.html
```

## 3. Testar

```bash
pytest tests/test_ar.py -v
```

# ============================================================================
# 📁 ESTRUTURA DE PASTAS
# ============================================================================

```
grokzomborg/
├── main.py                 # Aplicação principal (Kivy + RA)
├── ar_camera.py            # Módulo de Realidade Aumentada
├── game_systems.py         # Sistemas de jogo (som, estado, etc)
├── index.html              # Website com RA web
├── requirements.txt        # Dependências Python
├── buildozer.spec          # Config para build Android
├── README.md               # Documentação principal
├── DEVELOPMENT.md          # Este arquivo
│
├── assets/
│   ├── sounds/
│   │   ├── roar1.wav       # Rugido nível 1
│   │   ├── roar2.wav       # Rugido nível 2
│   │   ├── roar3.wav       # Rugido nível 3
│   │   └── roar4.wav       # Rugido nível 4
│   ├── images/
│   │   └── icon.png        # Ícone da app
│   └── models/             # Modelos 3D (futuro)
│
├── tests/
│   ├── __init__.py
│   ├── test_ar.py          # Testes de RA
│   ├── test_game.py        # Testes de gameplay
│   └── test_performance.py # Testes de performance
│
└── .github/
    └── workflows/
        ├── tests.yml       # CI/CD - Testes
        └── build.yml       # CI/CD - Build
```

# ============================================================================
# 🎮 DESENVOLVIMENTO FEATURES
# ============================================================================

## Feature: Adicionar Novo Nível de Evolução

### 1. Atualizar `main.py`

```python
# Na classe Grokzomborg, atualizar cores:
colors = [
    (0.2, 0.8, 0.3),   # Nível 1
    (0.1, 0.9, 0.4),   # Nível 2
    (0.0, 1.0, 0.5),   # Nível 3
    (0.8, 0.2, 0.9),   # Nível 4
    (1.0, 0.0, 1.0),   # NOVO: Nível 5
]
```

### 2. Atualizar `ar_camera.py`

```python
# Na classe ARCamera:
colors = [
    (50, 255, 100),      # Verde
    (0, 255, 100),       # Verde brilhante
    (0, 255, 200),       # Verde neon
    (200, 50, 255),      # Roxo
    (255, 0, 255),       # NOVO: Magenta
]
```

### 3. Adicionar Sons

- Gravar novo áudio: `roar5.wav`
- Salvar em: `assets/sounds/roar5.wav`

### 4. Atualizar Progression

```python
# Em game_systems.py, LevelProgression.LEVELS:
5: {
    'name': 'Ascenção Final',
    'color': (1.0, 0.0, 1.0),
    'taps_required': 100,
    'size_multiplier': 2.5,
    'speed_multiplier': 2.0,
    'description': 'O monstro transcende a realidade!'
}
```

# ============================================================================
# 🧪 TESTES
# ============================================================================

## Rodar todos os testes

```bash
pytest -v
```

## Rodar testes específicos

```bash
# Apenas testes de RA
pytest tests/test_ar.py -v

# Apenas um teste
pytest tests/test_ar.py::TestARCamera::test_evolution_level_increase -v

# Com cobertura
pytest --cov=. tests/
```

# ============================================================================
# 📦 BUILD & DEPLOY
# ============================================================================

## Build para Desktop

```bash
# Windows
pyinstaller --onefile main.py

# macOS
pyinstaller --onefile main.py

# Linux
pyinstaller --onefile main.py
```

## Build para Android

```bash
# Setup (primeira vez)
buildozer android debug

# Compilar
buildozer android debug

# Instalar no dispositivo
adb install -r bin/grokzomborg-1.1.0-debug.apk

# Ver logs
buildozer android debug deploy run logcat
```

# ============================================================================
# 🔧 DEBUG & TROUBLESHOOTING
# ============================================================================

## Câmera não funciona

```python
# Verificar disponibilidade
import cv2
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Câmera não encontrada!")
    
# Tentar outro índice
cap = cv2.VideoCapture(1)
```

## OpenCV não carrega

```bash
# Reinstalar
pip uninstall opencv-python
pip install opencv-python==4.8.1.78
```

## Kivy dá erro em mobile

```bash
# Limpar build
rm -rf .buildozer bin dist

# Recompilar
buildozer android debug
```

---

**ROOOAAAR-ZIIIMB!!!** 🧟‍♂️⚡🌍
