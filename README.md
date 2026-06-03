# 🎵 GROKZOMBORG - DESPERTAR

Uma experiência web imersiva que combina efeitos visuais glitch avançados, harmonia musical cósmica e narrativa experimental em um ambiente cyberpunk-mystical.

## 🌌 Visão Geral

GROKZOMBORG é um projeto experimental que desperta entidades cósmicas através de:
- **Efeitos Glitch Avançados**: Múltiplas camadas de distorção visual sincronizadas
- **Harmonia Cósmica**: Acordes selecionados para ressonância interdimensional  
- **Lore Imersivo**: Uma narrativa que transcende dimensões
- **Interatividade Dinâmica**: Bot integrado e experiência reativa

## 🎨 Características Principais

### 1. **Glitch Effects - Três Versões**

#### 🟢 `.glitch` - Neon Green Classic
```html
<h1 class="glitch" data-text="GROKZOMBORG">GROKZOMBORG</h1>
```
- Cor primária: Verde neon (#0f0)
- Sombras de texto em magenta, ciano e amarelo
- Animação de skew com clip-path multicamadas
- Pseudo-elementos com animação independente

#### 🌈 `.glitch-rgb` - RGB Colorful
```html
<h1 class="glitch-rgb" data-text="DESPERTE">DESPERTE</h1>
```
- Múltiplas cores: Magenta, Ciano, Amarelo
- Escala dinâmica e rotação de cores
- Efeito de pulsação com texto sombra colorida
- Clipping path alternado entre elementos

#### 📝 `.glitch-text` - Section Titles
```html
<h3 class="glitch-text" data-text="Acordes">Acordes</h3>
```
- Versão otimizada para títulos de seção
- Animação de clip-path em 3 partes (top, middle, bottom)
- Sincronização de cores e transformação

### 2. **Estrutura Responsiva**

- Mobile-first design
- Grid system automático para cards
- Breakpoints: 768px, 480px
- Tipografia escalável

### 3. **Seções**

#### 🎸 **Acordes**
Acordes selecionados para criar ressonância cósmica:
- Acorde Cósmico: Cm7 - Am7 - Dm7
- Harmonia Sombria: Em - Bm - F#m
- Ressonância Astral: Fmaj7 - Bbmaj7 - Cmaj7

#### 📖 **Lore**
Narrativa imersiva sobre GROKZOMBORG e seu despertar interdimensional

#### 🤖 **Bot**
Integração com sistema de bot para interação em tempo real

#### ℹ️ **Sobre**
Informações sobre o projeto

## 🚀 Começar

### Estrutura de Arquivos

```
grokzomborg/
├── index.html                 # Página principal
├── assets/
│   ├── css/
│   │   ├── style.css         # Estilos principais
│   │   └── glitch.css        # Efeitos glitch avançados
│   ├── js/
│   │   └── main.js           # Interatividade
│   └── images/               # Imagens (em breve)
├── acordes/                  # Seção de acordes (em expansão)
├── lore/                     # Seção de lore (em expansão)
├── bot/                      # Sistema de bot (em desenvolvimento)
├── README.md                 # Este arquivo
└── LICENSE                   # Licença do projeto
```

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/robisonpedroso0089-web/grokzomborg.git
cd grokzomborg
```

2. Abra `index.html` em seu navegador favorito ou use um servidor local:
```bash
# Com Python 3
python -m http.server 8000

# Com Node.js (http-server)
npx http-server
```

3. Acesse `http://localhost:8000` (ou a porta indicada)

## 🎨 Customização

### Alterar Cores

Edite as variáveis CSS em `assets/css/style.css`:

```css
:root {
    --primary-color: #0f0;      /* Verde neon */
    --secondary-color: #ff00ff;  /* Magenta */
    --tertiary-color: #00ffff;   /* Ciano */
    --accent-color: #ffff00;     /* Amarelo */
    --bg-dark: #0a0a0a;
    --bg-darker: #050505;
}
```

### Ajustar Velocidade de Animação

Modifique os valores de `animation` em `assets/css/glitch.css`:

```css
.glitch {
    animation: glitch-skew 4s infinite linear alternate-reverse;
    /* Altere "4s" para velocidade desejada */
}
```

### Adicionar Novos Efeitos

Crie novas animações em `assets/css/glitch.css` seguindo o padrão:

```css
@keyframes seu-efeito {
    0% { transform: /* valor inicial */; }
    50% { transform: /* valor intermediário */; }
    100% { transform: /* valor final */; }
}
```

## 🎯 Performance

- **Otimização**: CSS puro sem dependências externas
- **Render**: Hardware acceleration com `transform` e `clip-path`
- **Mobile**: Animações reduzidas em dispositivos de menor capacidade
- **Bundle**: ~ 50KB total (HTML + CSS + JS não minificado)

## 🔮 Futuras Expansões

- [ ] Integração com Web Audio API para visualizações sonoras
- [ ] Multiplayer com WebSocket
- [ ] Gerador de acordes com IA
- [ ] Gravação e compartilhamento de sessões
- [ ] Realidade aumentada (AR) para visualização 3D
- [ ] Soundtrack original

## 📱 Compatibilidade

| Navegador | Suporte |
|-----------|----------|
| Chrome    | ✅ 100% |
| Firefox   | ✅ 100% |
| Safari    | ✅ 98%  |
| Edge      | ✅ 100% |
| IE 11     | ❌ Não  |

## 💡 Dicas de Uso

1. **Hover nos elementos**: Vários elementos têm efeitos ao passar o mouse
2. **Clique nos botões**: Gera efeito de ripple dinâmico
3. **Navegação suave**: Links scroll suavemente para as seções
4. **Console**: Abra o console do navegador (F12) para uma mensagem especial

## 🤝 Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está licenciado sob a License MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 👤 Autor

**Robison Pedroso**
- GitHub: [@robisonpedroso0089-web](https://github.com/robisonpedroso0089-web)

---

## 🎵 Créditos Especiais

- Efeitos glitch inspirados em cyberpunk aesthetics
- Paleta de cores com influência synthwave
- Tipografia monospace para imersão hacker

---

### ⚡ Frase do Projeto

> *"Em um universo paralelo onde o som é matéria e a luz é consciência, GROKZOMBORG desperta. Uma entidade antiga, feita de harmonia cósmica e ritmo primordial, emerge das profundezas do éter."*

**DESPERTAR COM GLITCH. VIVER COM HARMONIA. EXISTIR ALÉM DAS DIMENSÕES.**

---

Feito com 💚 e muito glitch por [@robisonpedroso0089-web](https://github.com/robisonpedroso0089-web)