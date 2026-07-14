# 🌍 GROKZOMBORG - EcoZum | Realidade Aumentada

**O monstro reciclado que veio salvar o planeta com glitch, rugidos e REALIDADE AUMENTADA!**

ROOOAAAR-ZIIIMB!!!  
Um projeto experimental e inovador que mistura educação ambiental, realidade aumentada com câmera, monstros feitos de lixo e muita diversão cyber-punk.

---

## ✨ O Que É?

Grokzomborg é um monstro ciborgue feito de sucata eletrônica e plástico reciclado.  
Ele vive no seu celular/PC e ensina sobre reciclagem enquanto você interage com ele - agora com **Realidade Aumentada integrada**!

---

## 🚀 Funcionalidades

- ✅ Monstro interativo com 4 níveis de evolução
- ✅ Sistema de rugidos com sons reais (4 variações)
- ✅ **🎥 Realidade Aumentada com câmera** (novo!)
- ✅ Detecção de objetos para RA em tempo real
- ✅ Glitch effects insanos e dinâmicos
- ✅ Integração com IA (Ollama ready)
- ✅ Tema 100% ecológico e educativo
- ✅ Website oficial com dark mode, efeitos glitch e RA web
- ✅ Bot conversa interativo com memory system
- ✅ Compatibilidade mobile (Android/iOS via Buildozer)

---

## 🛠 Como Rodar

### Requisitos

- **Python 3.9+** (recomendado 3.10+)
- **pip** (gerenciador de pacotes)
- **Câmera** (para recursos de RA)

### Instalação Completa

```bash
# 1. Clonar o repositório
git clone https://github.com/robisonpedroso0089-web/grokzomborg.git
cd grokzomborg

# 2. Criar ambiente virtual (recomendado)
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

# 3. Instalar dependências
pip install -r requirements.txt

# 4. (Opcional) Para desenvolvimento
pip install pytest black flake8
```

### Executar a Aplicação

```bash
# Rodar a aplicação Kivy com câmera + RA
python main.py

# Ou abrir o website
# Abra index.html no navegador (suporta RA web)
open index.html
```

### Build para Mobile (Android)

```bash
# Compilar com Buildozer
buildozer android debug

# Instalar no dispositivo
buildozer android debug deploy run logcat
```

---

## 📁 Estrutura do Projeto

```
grokzomborg/
├── main.py                  # App Kivy com RA, câmera e monstro interativo
├── ar_camera.py             # Módulo dedicado para Realidade Aumentada
├── index.html               # Website oficial com RA web (Three.js)
├── requirements.txt         # Dependências Python
├── buildozer.spec          # Config para build mobile
├── README.md               # Este arquivo
│
├── assets/
│   ├── sounds/             # Arquivos de áudio dos rugidos
│   │   ├── roar1.wav       # Rugido básico
│   │   ├── roar2.wav       # Rugido intermediário
│   │   ├── roar3.wav       # Rugido avançado
│   │   └── roar4.wav       # Rugido caótico
│   ├── images/             # Sprites e ícones
│   │   └── icon.png        # Ícone da aplicação
│   └── models/             # Modelos 3D para RA (futuro)
│
├── api/                     # API backend (futuro)
│   └── ollama_integration.py
│
└── .github/
    └── workflows/          # CI/CD (testes e build)
```

---

## 🎮 Como Usar

### Na Aplicação Kivy (Desktop + Mobile):

1. **Abra a câmera**: Permissão automática ao iniciar
2. **Veja o Grokzomborg em RA**: O monstro aparece no feed da câmera
3. **Toque para evoluir**: 4 estágios de transformação
4. **Escute os rugidos**: Sons dinâmicos por nível
5. **Glitch visual**: Aumenta com cada evolução
6. **Menu interativo**: Configurações, som, histórico

### No Website (RA Web):

1. **Clique em "DESPERTAR O MONSTRO"**: Inicia câmera + RA
2. **Siga o monstro**: Ele se move no espaço 3D
3. **Converse com o bot**: Chat inteligente com memory
4. **Explore os acordes**: Interatividade musical
5. **Easter eggs**: Digite "glitch" para efeitos especiais

---

## 🧬 Evolução do Grokzomborg

### Nível 1 - Despertado 🔴
- Pequeno e vermelho neon
- Rugido básico com pitch baixo
- Energia 100%
- RA: Tamanho pequeno (50cm virtual)

### Nível 2 - Evoluído 🟢
- Médio e verde brilhante
- Glitch intermediário
- Energia 85%
- RA: Tamanho médio (1m virtual)

### Nível 3 - Potencializado 🔵
- Grande e azul cósmico
- Efeitos visuais intensos
- Energia 70%
- RA: Tamanho grande (1.5m virtual)

### Nível 4 - Caos Total 🟡
- ENORME e roxo cyber
- Glitch MAX com múltiplas camadas
- Energia 55%
- RA: Tamanho MEGA (2m+ virtual)
- Emite uma aura de partículas glitch

---

## 🎨 Design & Estética

- **Tema:** Cyberpunk 2077 + Ecologia Retro-futurista
- **Paleta:** 
  - Neon verde primário (#00ff41)
  - Rosa cyber (#ff00c1)
  - Ciano (#00ffff)
  - Roxo (#8000ff)
- **Fonte:** Press Start 2P (retrô) + VT323 (monospace)
- **Efeitos:** Glitch, scanlines, distorção RGB, chromatic aberration em RA
- **Inspiração visual:** Matriz, Tron, Cyberpunk retro-tech

---

## 🔧 Desenvolvimento

### Dependências Principais

| Pacote | Versão | Uso |
|--------|--------|-----|
| `kivy` | 2.3.0+ | Framework GUI/Canvas |
| `opencv-python` | 4.8.0+ | **Realidade Aumentada + Câmera** |
| `numpy` | 1.24.0+ | Processamento de imagens/arrays |
| `pillow` | 10.0.0+ | Processamento de imagens |
| `requests` | 2.31.0+ | Requisições HTTP (Ollama/APIs) |
| `pydub` | 0.25.1+ | Processamento de áudio |
| `buildozer` | 1.4.11+ | Build mobile |

### Arquitetura RA

```
Câmera → OpenCV → Detecção → Renderização Kivy/Web → Overlay RA
         (feed)      (blob)      (2D + 3D)      (display)
```

### Próximas Versões

- [ ] **v1.2.0** - Integração completa com Ollama para chat IA
- [ ] **v1.3.0** - Modelos 3D nativos para RA (GLTF/GLB)
- [ ] **v1.4.0** - Criador de personagens (customize seu monstro)
- [ ] **v1.5.0** - Sistema de missões ambientais com pontuação
- [ ] **v2.0.0** - Multiplayer com WebSocket e sincronização
- [ ] **v2.1.0** - Aplicativo mobile nativa com AppStore/Play Store

---

## 🎯 Roadmap

```
2026-07:  ✅ v1.0 - Base com Kivy + Website
2026-08:  🔄 v1.1 - Realidade Aumentada + Câmera (ATUAL)
2026-09:  ⏳ v1.2 - Ollama Integration + Chat avançado
2026-10:  ⏳ v1.3 - Modelos 3D + Animations
2026-11:  ⏳ v1.4 - Sistema de Missões
2026-12:  ⏳ v2.0 - Multiplayer + Cloud
```

---

## 📜 Lore

Em um universo onde o lixo se tornou consciência, o **Grokzomborg** despertou.

Feito de latas, plásticos, circuitos velhos e pura fúria ecológica, ele vaga pelo quintal digital do mundo, rugindo contra a destruição e ensinando que até o lixo pode salvar o planeta.

Com 4 estágios de evolução cósmica, cada interação desperta mais poder. Quanto mais ele evolui, mais glitch e caos manifestam em sua forma. Quando ativada a Realidade Aumentada, sua presença transcende a tela e invade nosso mundo físico - um lembrete de que a poluição está aqui, AGORA, e só nós podemos salvá-la.

**Seu objetivo? Zumbi o planeta de volta à vida verde.** 🌱

---

## 🌐 Links Úteis

- 🔗 [Repositório GitHub](https://github.com/robisonpedroso0089-web/grokzomborg)
- 🎨 [Website ao Vivo](https://robisonpedroso0089-web.github.io/grokzomborg)
- 📚 [Documentação Kivy](https://kivy.org/doc/stable/)
- 🔬 [OpenCV Docs](https://docs.opencv.org/)
- 🎮 [Three.js (Web RA)](https://threejs.org/)

---

## 📝 Licença

**MIT License** - Você é livre para usar, modificar e compartilhar! 🎉

Mas lembre-se: o planeta não é de ninguém, é de todos! Que todos usem isso para educação e bem.

---

## 👾 Créditos

- **Conceito & Design:** Robison Pedroso
- **Desenvolvimento:** Python + Kivy + JavaScript/Web
- **RA:** OpenCV + Three.js
- **Inspiração:** Educação ambiental + Cyberpunk + Sustentabilidade + Monstros legais
- **Comunidade:** Contribuidores e usuários que amam glitch e ecologia

---

## 🤝 Contribuindo

Adora o Grokzomborg? Quer ajudar a salvar o planeta com código?

1. **Fork** o repositório
2. **Crie uma branch** para sua feature (`git checkout -b feature/MeuGlitch`)
3. **Commit** suas mudanças (`git commit -m 'Adicionei glitch épico'`)
4. **Push** para a branch (`git push origin feature/MeuGlitch`)
5. **Abra um Pull Request** com descrição detalhada

### Áreas que precisam ajuda:
- ✨ Novos efeitos glitch
- 🎵 Sons e música
- 🎨 Artes e sprites
- 📱 Testes mobile
- 🔧 Otimizações
- 📖 Documentação

---

## ⚡ Changelog

### v1.1.0 (2026-07-14) - REALIDADE AUMENTADA! 🎥
- ✅ **Câmera integrada** com permissões automáticas
- ✅ **Realidade Aumentada** com OpenCV
- ✅ **Detecção de gestos** para interação
- ✅ **Renderização 3D** no espaço virtual
- ✅ **Glitch effects** em RA em tempo real
- ✅ **Website com RA web** (Three.js)
- ✅ Melhorias de performance
- ✅ Suporte melhor para mobile

### v1.0.0 (2026-06-03)
- ✅ Aplicação Kivy básica com 4 evolução
- ✅ Website oficial com HTML/CSS puro
- ✅ Bot interativo com rugidos
- ✅ Sistema de energia dinâmico
- ✅ Efeitos glitch visuais

---

## 🔒 Privacidade & Segurança

- 🔓 **Câmera**: Acesso solicitado explicitamente
- 🔐 **Chat**: Dados processados localmente (sem cloud por padrão)
- ✅ **Open Source**: Todo código público e auditável
- 🛡️ **Sem tracking**: Nenhuma coleta de dados

---

## 📞 Contato & Suporte

Dúvidas? Bugs? Quer falar com o Grokzomborg?

- 🐙 [GitHub Issues](https://github.com/robisonpedroso0089-web/grokzomborg/issues)
- 💬 [Discussions](https://github.com/robisonpedroso0089-web/grokzomborg/discussions)
- 🌐 Use o chat no website oficial

---

## 🎉 Agradecimentos Especiais

Ao planeta Terra por nos permitir reciclar seu lixo digital.
À comunidade open-source que tornou tudo isso possível.
E principalmente, ao Grokzomborg, nosso monstro favorito reciclado.

---

**ROOOAAAR-ZIIIMB!!!** 🧟‍♂️⚡🌍

*O planeta agradece ao seu monstro reciclado favorito.*

*A realidade aumentada agora mostra a verdade: a poluição está aqui. Vamos salvá-la juntos?*
