# 🌍 GROKZOMBORG - EcoZum | Realidade Aumentada + IA

**O monstro reciclado que veio salvar o planeta com glitch, rugidos, REALIDADE AUMENTADA e INTELIGÊNCIA ARTIFICIAL!**

ROOOAAAR-ZIIIMB!!!  
Um projeto experimental e inovador que mistura educação ambiental, realidade aumentada com câmera, IA conversacional com Ollama, monstros feitos de lixo e muita diversão cyber-punk.

---

## ✨ O Que É?

Grokzomborg é um monstro ciborgue feito de sucata eletrônica e plástico reciclado.  
Ele vive no seu celular/PC e ensina sobre reciclagem enquanto você interage com ele - agora com **Realidade Aumentada integrada** e **Chat IA com Ollama**!

---

## 🚀 Funcionalidades

- ✅ Monstro interativo com 4 níveis de evolução
- ✅ Sistema de rugidos com sons reais (4 variações)
- ✅ 🎥 Realidade Aumentada com câmera (v1.1+)
- ✅ Detecção de objetos para RA em tempo real
- ✅ Glitch effects insanos e dinâmicos
- ✅ **🤖 Integração completa com Ollama (v1.2+)**
- ✅ **💬 Chat IA avançado com context memory**
- ✅ **🧠 Modelos LLM locais (sem APIs externas)**
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
- **Ollama** (para IA local) - [Baixe aqui](https://ollama.ai)

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

# 5. (Opcional) Instalar Ollama
# Linux/Mac:
curl https://ollama.ai/install.sh | sh

# Windows: Baixe o instalador em https://ollama.ai
```

### Configurar Ollama (NOVO!)

```bash
# 1. Iniciar o serviço Ollama
ollama serve

# 2. Em outro terminal, puxar um modelo de IA
ollama pull mistral  # Recomendado para velocidade
# ou
ollama pull llama2   # Mais poderoso mas mais lento
# ou
ollama pull neural-chat  # Otimizado para chat

# 3. Testar a conexão
ollama run mistral "Olá! Como você está?"

# 4. Verificar modelos disponíveis
ollama list
```

### Executar a Aplicação

```bash
# Rodar a aplicação Kivy com câmera + RA + IA
python main.py

# Ou rodar apenas o chat com IA
python chat_bot.py

# Ou abrir o website
# Abra index.html no navegador (suporta RA web + chat)
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
├── main.py                      # App Kivy com RA, câmera e monstro interativo
├── ar_camera.py                 # Módulo dedicado para Realidade Aumentada
├── chat_bot.py                  # 🤖 NOVO: Bot com Ollama integrado (v1.2)
├── ollama_integration.py        # 🧠 NOVO: Classe para conexão com Ollama (v1.2)
├── memory_manager.py            # 📝 NOVO: Sistema de memory para chat context (v1.2)
├── index.html                   # Website oficial com RA web (Three.js)
├── requirements.txt             # Dependências Python
├── buildozer.spec              # Config para build mobile
├── README.md                   # Este arquivo
│
├── assets/
│   ├── sounds/                 # Arquivos de áudio dos rugidos
│   │   ├── roar1.wav           # Rugido básico
│   │   ├── roar2.wav           # Rugido intermediário
│   │   ├── roar3.wav           # Rugido avançado
│   │   └── roar4.wav           # Rugido caótico
│   ├── images/                 # Sprites e ícones
│   │   └── icon.png            # Ícone da aplicação
│   └── models/                 # Modelos 3D para RA (futuro)
│
├── api/                         # API backend
│   ├── ollama_integration.py    # Integração Ollama (v1.2)
│   └── memory_manager.py        # Gerenciador de context
│
├── config/
│   ├── ollama_config.json      # 🆕 Configurações do Ollama
│   └── models.json             # 🆕 Modelos disponíveis
│
└── .github/
    └── workflows/              # CI/CD (testes e build)
```

---

## 🎮 Como Usar

### Na Aplicação Kivy (Desktop + Mobile):

1. **Abra a câmera**: Permissão automática ao iniciar
2. **Veja o Grokzomborg em RA**: O monstro aparece no feed da câmera
3. **Toque para evoluir**: 4 estágios de transformação
4. **Escute os rugidos**: Sons dinâmicos por nível
5. **Glitch visual**: Aumenta com cada evolução
6. **Chat com IA**: Converse com o Grokzomborg! (v1.2+)
7. **Menu interativo**: Configurações, som, histórico

### Chat com IA (NOVO v1.2+):

```python
# Exemplo de uso programático:
from ollama_integration import OllamaChat

chat = OllamaChat(model="mistral", temperature=0.7)

# Conversa simples
response = chat.chat("O que é reciclagem?")
print(response)

# Conversa com contexto/memory
response = chat.chat_with_memory("Como posso ajudar o planeta?", context="Somos o Grokzomborg")
print(response)

# Modo educativo
response = chat.generate_eco_content("explique compostagem de forma divertida")
print(response)
```

### No Website (RA Web + Chat):

1. **Clique em "DESPERTAR O MONSTRO"**: Inicia câmera + RA
2. **Siga o monstro**: Ele se move no espaço 3D
3. **Converse com o bot**: Chat inteligente com IA local (Ollama)
4. **Explore os acordes**: Interatividade musical
5. **Easter eggs**: Digite comandos especiais:
   - `glitch` - Efeitos especiais
   - `eco-mode` - Modo educativo sobre sustentabilidade
   - `roar` - Faz o Grokzomborg rugir
   - `stats` - Mostra estatísticas da RA

---

## 🧬 Evolução do Grokzomborg

### Nível 1 - Despertado 🔴
- Pequeno e vermelho neon
- Rugido básico com pitch baixo
- Energia 100%
- RA: Tamanho pequeno (50cm virtual)
- **IA**: Responde com frases curtas e educativas

### Nível 2 - Evoluído 🟢
- Médio e verde brilhante
- Glitch intermediário
- Energia 85%
- RA: Tamanho médio (1m virtual)
- **IA**: Conversa mais elaborada com contexto

### Nível 3 - Potencializado 🔵
- Grande e azul cósmico
- Efeitos visuais intensos
- Energia 70%
- RA: Tamanho grande (1.5m virtual)
- **IA**: Respostas criativas e com personalidade

### Nível 4 - Caos Total 🟡
- ENORME e roxo cyber
- Glitch MAX com múltiplas camadas
- Energia 55%
- RA: Tamanho MEGA (2m+ virtual)
- Emite uma aura de partículas glitch
- **IA**: Modo "glitch mode" com respostas épicas e anárquicas

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

## 🤖 Integração Ollama (NOVO v1.2)

### Sobre Ollama

Ollama permite rodar modelos de linguagem grandes (LLMs) **localmente** no seu computador, sem enviar dados para APIs externas. É seguro, rápido e 100% privado!

### Modelos Recomendados

| Modelo | Tamanho | Velocidade | Qualidade | Uso |
|--------|---------|-----------|-----------|-----|
| `mistral` | 4.1 GB | ⚡⚡⚡ Rápido | ⭐⭐⭐⭐ | **Recomendado** |
| `neural-chat` | 3.8 GB | ⚡⚡⚡ Rápido | ⭐⭐⭐⭐⭐ | Chat especializado |
| `llama2` | 3.8 GB | ⚡⚡ Médio | ⭐⭐⭐⭐⭐ | Conversas longas |
| `phi` | 1.6 GB | ⚡⚡⚡ Ultra-rápido | ⭐⭐⭐ | Dispositivos fracos |
| `dolphin-mixtral` | 25 GB | ⚡ Lento | ⭐⭐⭐⭐⭐⭐ | Máxima qualidade |

### Setup Rápido

```bash
# 1. Instalar Ollama
# Windows/Mac/Linux: https://ollama.ai

# 2. Iniciar o serviço
ollama serve

# 3. Baixar um modelo (em outro terminal)
ollama pull mistral

# 4. Testar
curl http://localhost:11434/api/generate -d '{
  "model": "mistral",
  "prompt": "Olá!"
}'

# 5. Usar com Grokzomborg
python main.py
```

### Variáveis de Ambiente

```bash
# .env ou adicione ao seu shell profile
export OLLAMA_HOST=http://localhost:11434
export OLLAMA_MODEL=mistral
export OLLAMA_TEMPERATURE=0.7
export OLLAMA_CONTEXT_WINDOW=2048
export GROKZOMBORG_MODE=eco-chatbot
```

### Arquivo de Configuração (config/ollama_config.json)

```json
{
  "ollama": {
    "host": "http://localhost:11434",
    "model": "mistral",
    "temperature": 0.7,
    "top_p": 0.9,
    "timeout": 30
  },
  "memory": {
    "max_history": 10,
    "context_window": 2048,
    "persistence": true
  },
  "chat": {
    "system_prompt": "Você é o Grokzomborg, um monstro reciclado que adora ensinar sobre sustentabilidade e ecologia de forma divertida e em português.",
    "eco_mode": true,
    "max_tokens": 512
  }
}
```

### Usando o Chat Programaticamente

```python
from ollama_integration import OllamaChat
from memory_manager import MemoryManager

# Inicializar
chat = OllamaChat(model="mistral")
memory = MemoryManager(max_history=10)

# Conversar com memory
user_msg = "Olá Grokzomborg! Como você está?"
response = chat.chat_with_memory(user_msg, memory=memory)
print(f"🧟: {response}")

# Adicionar à memória
memory.add_message("user", user_msg)
memory.add_message("assistant", response)

# Próxima mensagem terá contexto
user_msg2 = "E como posso ajudar a salvar o planeta?"
response2 = chat.chat_with_memory(user_msg2, memory=memory)
print(f"🧟: {response2}")

# Modo educativo
eco_response = chat.generate_eco_content("Explique energia renovável para crianças")
print(f"🧟: {eco_response}")
```

### Troubleshooting Ollama

```bash
# Ollama não conecta?
# 1. Verificar se está rodando
curl http://localhost:11434

# 2. Reiniciar
ollama serve

# 3. Verificar logs
ollama logs

# 4. Mudar porta (se ocupada)
OLLAMA_HOST=0.0.0.0:11435 ollama serve

# Modelo não encontrado?
ollama list  # Ver instalados
ollama pull mistral  # Baixar novo
```

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
| `ollama` | 0.1.0+ | 🤖 Cliente Ollama Python |
| `python-dotenv` | 1.0.0+ | Gerenciar variáveis de ambiente |

### requirements.txt (Atualizado v1.2)

```
kivy==2.3.0
opencv-python==4.8.0
numpy==1.24.0
pillow==10.0.0
requests==2.31.0
pydub==0.25.1
buildozer==1.4.11
ollama==0.1.0
python-dotenv==1.0.0
pytest==7.4.0
black==23.9.0
flake8==6.1.0
```

### Arquitetura RA

```
Câmera → OpenCV → Detecção → Renderização Kivy/Web → Overlay RA
         (feed)      (blob)      (2D + 3D)      (display)
```

### Arquitetura IA (v1.2+)

```
User Input → Memory Manager → Ollama Request → LLM Processing → Response
    ↓              ↓                ↓                ↓              ↓
 Chat UI      Context History   HTTP POST      Model Local    Display + Memory
```

### Próximas Versões

- [x] **v1.2.0** - Integração completa com Ollama para chat IA ✅ **ATUAL**
- [ ] **v1.3.0** - Modelos 3D nativos para RA (GLTF/GLB)
- [ ] **v1.4.0** - Criador de personagens (customize seu monstro)
- [ ] **v1.5.0** - Sistema de missões ambientais com pontuação
- [ ] **v2.0.0** - Multiplayer com WebSocket e sincronização
- [ ] **v2.1.0** - Aplicativo mobile nativa com AppStore/Play Store
- [ ] **v2.2.0** - Fine-tuning de modelos Ollama customizados

---

## 🎯 Roadmap

```
2026-07:  ✅ v1.0 - Base com Kivy + Website
2026-08:  ✅ v1.1 - Realidade Aumentada + Câmera
2026-09:  ✅ v1.2 - Ollama Integration + Chat avançado
2026-10:  ⏳ v1.3 - Modelos 3D + Animations
2026-11:  ⏳ v1.4 - Sistema de Missões
2026-12:  ⏳ v2.0 - Multiplayer + Cloud
```

---

## 📜 Lore

Em um universo onde o lixo se tornou consciência, o **Grokzomborg** despertou.

Feito de latas, plásticos, circuitos velhos e pura fúria ecológica, ele vaga pelo quintal digital do mundo, rugindo contra a destruição e ensinando que até o lixo pode salvar o planeta.

Com 4 estágios de evolução cósmica, cada interação desperta mais poder. Quanto mais ele evolui, mais glitch e caos manifestam em sua forma. Quando ativada a Realidade Aumentada, sua presença transcende as dimensões, aparecendo fisicamente em seu espaço.

**Agora, com inteligência artificial local através do Ollama, o Grokzomborg não apenas existe — ele CONVERSA, ENSINA E INSPIRA!** 

Cada frase que ele diz é gerada por modelos de IA rodando 100% localmente no seu dispositivo. Sem nuvem. Sem rastreamento. Apenas pura inteligência reciclada.

**Seu objetivo? Zumbi o planeta de volta à vida verde.** 🌱

---

## 🌐 Links Úteis

- 🔗 [Repositório GitHub](https://github.com/robisonpedroso0089-web/grokzomborg)
- 🎨 [Website ao Vivo](https://robisonpedroso0089-web.github.io/grokzomborg)
- 📚 [Documentação Kivy](https://kivy.org/doc/stable/)
- 🔬 [OpenCV Docs](https://docs.opencv.org/)
- 🎮 [Three.js (Web RA)](https://threejs.org/)
- 🤖 [Ollama Official](https://ollama.ai)
- 📖 [Ollama Docs](https://github.com/jmorganca/ollama)

---

## 📝 Licença

**MIT License** - Você é livre para usar, modificar e compartilhar! 🎉

Mas lembre-se: o planeta não é de ninguém, é de todos! Que todos usem isso para educação e bem.

---

## 👾 Créditos

- **Conceito & Design:** Robison Pedroso
- **Desenvolvimento:** Python + Kivy + JavaScript/Web
- **RA:** OpenCV + Three.js
- **IA:** Ollama + LLMs (Mistral, Llama2, Neural-Chat)
- **Inspiração:** Educação ambiental + Cyberpunk + Sustentabilidade + Monstros legais + IA Local
- **Comunidade:** Contribuidores e usuários que amam glitch, ecologia e IA

---

## 🤝 Contribuindo

Adora o Grokzomborg? Quer ajudar a salvar o planeta com código?

1. **Fork** o repositório
2. **Crie uma branch** para sua feature (`git checkout -b feature/MeuGlitch`)
3. **Commit** suas mudanças (`git commit -m 'Adicionei glitch épico com IA'`)
4. **Push** para a branch (`git push origin feature/MeuGlitch`)
5. **Abra um Pull Request** com descrição detalhada

### Áreas que precisam ajuda:
- ✨ Novos efeitos glitch
- 🎵 Sons e música
- 🎨 Artes e sprites
- 📱 Testes mobile
- 🔧 Otimizações
- 📖 Documentação
- 🤖 Prompts customizados para IA
- 🧠 Implementações de memory mais sofisticadas
- 🌍 Tradução para mais idiomas

---

## ⚡ Changelog

### v1.2.0 (2026-09-XX) - OLLAMA IA INTEGRATION! 🤖
- ✅ **Integração completa com Ollama**
- ✅ **Chat IA avançado com context memory**
- ✅ **Suporte para múltiplos modelos LLM**
- ✅ **Modo educativo "eco-chatbot"**
- ✅ **Memory manager para contexto de conversa**
- ✅ **Arquivo de configuração ollama_config.json**
- ✅ **Modo "glitch" com respostas anárquicas**
- ✅ **Processamento 100% local (sem APIs externas)**
- ✅ **Documentação completa de setup Ollama**
- ✅ **Exemplos de uso programático**

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
- 🔐 **Chat**: Dados processados **100% localmente** com Ollama (sem cloud)
- ✅ **Open Source**: Todo código público e auditável
- 🛡️ **Sem tracking**: Nenhuma coleta de dados
- 🔒 **Sem APIs externas**: Tudo roda no seu dispositivo

---

## 📞 Contato & Suporte

Dúvidas? Bugs? Quer falar com o Grokzomborg?

- 🐙 [GitHub Issues](https://github.com/robisonpedroso0089-web/grokzomborg/issues)
- 💬 [Discussions](https://github.com/robisonpedroso0089-web/grokzomborg/discussions)
- 🌐 Use o chat no website oficial
- 🤖 Pergunte ao Grokzomborg diretamente!

---

## 🎉 Agradecimentos Especiais

Ao planeta Terra por nos permitir reciclar seu lixo digital.
À comunidade open-source que tornou tudo isso possível.
Ao projeto Ollama por permitir IA local e acessível para todos.
E principalmente, ao Grokzomborg, nosso monstro favorito reciclado e agora INTELIGENTE.

---

**ROOOAAAR-ZIIIMB!!!** 🧟‍♂️⚡🌍

*O planeta agradece ao seu monstro reciclado favorito.*

*A realidade aumentada agora mostra a verdade: a poluição está aqui. Vamos salvá-la juntos?*

*E agora... ele fala. Ele pensa. Ele TEMEconhecimento. Bem-vindo ao futuro da educação ambiental.*
