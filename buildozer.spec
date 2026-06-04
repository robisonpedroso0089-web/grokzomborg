[app]

# ROOOAAAR! Informações da Aplicação
title = Grokzomborg - O Monstro Ecológico
package.name = grokzomborg
package.domain = org.grokzomborg

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,wav,ogg

# Versão
version = 1.0.0

# Orientação
orientation = portrait
fullscreen = 0

# ROOOAAAR! Permissões Android
android.permissions = INTERNET,CAMERA,RECORD_AUDIO,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

# API levels
android.api = 33
android.minapi = 24
android.ndk = 26b
android.accept_sdk_license = True

# ROOOAAAR! Requisições (dependencies)
requirements = python3,kivy==2.3.0,requests,pillow,numpy,opencv-python,pyjnius,cython,pydub

# Arquitetura
android.archs = arm64-v8a,armeabi-v7a

# Assets
icon.filename = assets/icon.png
presplash.filename = assets/icon.png
presplash.loglevel = 2

# Gradle
android.gradle_dependencies = androidx.appcompat:appcompat:1.6.1

# Features
android.features = android.hardware.camera,android.hardware.microphone

# Metadata
android.meta_data = com.google.android.gms.version=@integer/google_play_services_version

[buildozer]

# ROOOAAAR! Configurações de build
log_level = 2
warn_on_root = 1
