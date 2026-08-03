#!/usr/bin/env python3
"""
⚙️ GROKZOMBORG - Setup Script
ROOOAAAR! Script de configuração automática

Executa: python setup.py
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path


def create_directory_structure():
    """Cria estrutura de pastas"""
    print("📁 Criando estrutura de diretórios...")
    
    directories = [
        'assets/sounds',
        'assets/images',
        'assets/models',
        'api',
        'tests',
        'outputs',
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"  ✅ {directory}")


def create_sample_files():
    """Cria arquivos de exemplo"""
    print("\n📄 Criando arquivos de exemplo...")
    
    # Arquivo .env
    env_content = """# GROKZOMBORG Environment
DEBUG=True
AR_ENABLED=True
CAMERA_INDEX=0
RESOLUTION_WIDTH=640
RESOLUTION_HEIGHT=480
FPS_TARGET=30
VOLUME=0.8
GLITCH_INTENSITY=1.0
"""
    
    with open('.env.example', 'w') as f:
        f.write(env_content)
    print("  ✅ .env.example")
    
    # Arquivo de configuração
    config_content = """# GROKZOMBORG Configuration
[app]
title = GROKZOMBORG - O Monstro Ecológico
author = Robison Pedroso
version = 1.1.0

[window]
width = 540
height = 960
fullscreen = False

[ar]
enabled = True
camera_index = 0
resolution = 640x480
fps_target = 30

[audio]
volume = 0.8
sound_enabled = True
bgm_enabled = False

[gameplay]
glitch_intensity = 1.0
particle_enabled = True
gesture_detection = True
"""
    
    with open('config.ini', 'w') as f:
        f.write(config_content)
    print("  ✅ config.ini")


def check_dependencies():
    """Verifica dependências instaladas"""
    print("\n🔍 Verificando dependências...")
    
    required_packages = [
        'kivy',
        'opencv-python',
        'numpy',
        'pillow',
        'pydub',
        'requests',
    ]
    
    for package in required_packages:
        try:
            __import__(package.replace('-', '_'))
            print(f"  ✅ {package}")
        except ImportError:
            print(f"  ❌ {package} - NÃO INSTALADO")
            print(f"     Execute: pip install {package}")


def initialize_git():
    """Inicializa repositório Git"""
    print("\n🔧 Configurando Git...")
    
    if not os.path.exists('.git'):
        subprocess.run(['git', 'init'], capture_output=True)
        print("  ✅ Repositório Git inicializado")
    else:
        print("  ℹ️  Repositório Git já existe")


def create_requirements_dev():
    """Cria requirements para desenvolvimento"""
    print("\n📦 Criando requirements-dev.txt...")
    
    dev_requirements = """# Development Dependencies
-r requirements.txt

# Testing
pytest>=7.4.0
pytest-cov>=4.1.0
pytest-xdist>=3.3.0

# Code Quality
black>=23.7.0
flake8>=6.0.0
pylint>=2.17.5
mypy>=1.4.1
isort>=5.12.0

# Debugging
ipdb>=0.13.13
debugpy>=1.6.7

# Documentation
sphinx>=7.1.0
sphinx-rtd-theme>=1.3.0
"""
    
    with open('requirements-dev.txt', 'w') as f:
        f.write(dev_requirements)
    print("  ✅ requirements-dev.txt")


def print_next_steps():
    """Mostra próximas etapas"""
    print("\n" + "="*60)
    print("🚀 SETUP CONCLUÍDO COM SUCESSO!")
    print("="*60)
    print("\n📝 Próximos passos:\n")
    print("1. Instale as dependências:")
    print("   pip install -r requirements.txt\n")
    print("2. (Opcional) Instale ferramentas de desenvolvimento:")
    print("   pip install -r requirements-dev.txt\n")
    print("3. Execute a aplicação:")
    print("   python main.py\n")
    print("4. Ou abra o website:")
    print("   open index.html\n")
    print("5. Execute os testes:")
    print("   pytest tests/test_ar.py -v\n")
    print("="*60)
    print("\n🔗 Links úteis:")
    print("  - Documentação: README.md")
    print("  - Guia de Dev: DEVELOPMENT.md")
    print("  - GitHub: https://github.com/robisonpedroso0089-web/grokzomborg")
    print("\n🧟 ROOOAAAR-ZIIIMB!!!")


def main():
    """Função principal"""
    print("\n" + "="*60)
    print("🌍 GROKZOMBORG - Setup Script v1.1.0")
    print("="*60 + "\n")
    
    try:
        create_directory_structure()
        create_sample_files()
        create_requirements_dev()
        check_dependencies()
        initialize_git()
        print_next_steps()
        
        return 0
    
    except Exception as e:
        print(f"\n❌ Erro durante setup: {e}")
        return 1


if __name__ == '__main__':
    sys.exit(main())
