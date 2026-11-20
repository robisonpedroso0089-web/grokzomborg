# Ollama JavaScript no GROKZOMBORG

Este guia resume como usar o cliente JavaScript oficial do Ollama e como isso se relaciona com o chat deste projeto.

## Requisitos

- Node.js e npm para instalar e compilar o cliente JavaScript.
- Ollama instalado e em execução.
- Um modelo baixado localmente, por exemplo `mistral`.

```bash
ollama serve
```

Em outro terminal:

```bash
ollama pull mistral
ollama run mistral
```

O serviço local padrão do Ollama fica em `http://localhost:11434`.

## Instalar a biblioteca

Na raiz do seu projeto JavaScript:

```bash
npm install ollama
```

## Exemplo no Node.js

```javascript
import ollama from 'ollama'

const response = await ollama.chat({
  model: 'mistral',
  messages: [{ role: 'user', content: 'Como posso reciclar em casa?' }],
})

console.log(response.message.content)
```

Para usar outro host Ollama:

```javascript
import { Ollama } from 'ollama'

const client = new Ollama({ host: 'http://127.0.0.1:11434' })
const response = await client.chat({
  model: 'mistral',
  messages: [{ role: 'user', content: 'Olá, Grokzomborg!' }],
})

console.log(response.message.content)
```

## Streaming no Node.js

```javascript
import ollama from 'ollama'

const response = await ollama.chat({
  model: 'mistral',
  messages: [{ role: 'user', content: 'Explique compostagem.' }],
  stream: true,
})

for await (const part of response) {
  process.stdout.write(part.message.content)
}
```

## Uso no navegador

A biblioteca disponibiliza um módulo para navegador:

```javascript
import ollama from 'ollama/browser'
```

Esse import precisa ser processado por uma ferramenta de build JavaScript (por exemplo, Vite); não funciona diretamente como script clássico sem bundler. O navegador também precisa conseguir acessar o servidor Ollama local e suas regras de CORS/rede precisam permitir essa conexão.

**Não coloque chaves de API no JavaScript enviado ao navegador.** Para Ollama Cloud, faça as requisições em um backend e mantenha `OLLAMA_API_KEY` somente como variável de ambiente do servidor.

## Como o chat deste repositório se conecta

A página `index.html` envia as mensagens para `/api/chat`. O arquivo `api/chat.js` é uma função de servidor que encaminha a conversa para Ollama, usando estas variáveis de ambiente:

```env
OLLAMA_HOST=http://localhost:11434
OLLAMA_MODEL=mistral
OLLAMA_TEMPERATURE=0.8
```

A rota `/api/chat` precisa ser executada em um ambiente que ofereça suporte a funções de servidor e tenha acesso ao Ollama. **GitHub Pages e `python -m http.server` servem arquivos estáticos; não executam `api/chat.js`.** Portanto, abrir `http://localhost:8000` disponibiliza a página, mas não inicia nem a API nem o Ollama.

Para servir apenas a página localmente:

```bash
python -m http.server 8000
```

Acesse `http://localhost:8000`. Para conversas com IA, inicie também o Ollama e execute a função `/api/chat` por meio de um backend compatível, configurando as variáveis de ambiente acima.

## Mais recursos da biblioteca

O cliente oficial também oferece geração de texto, listagem e gerenciamento de modelos, embeddings, chamadas de ferramentas e respostas em streaming. Consulte a documentação do pacote `ollama` e a referência da API Ollama para detalhes e compatibilidade de cada modelo.
