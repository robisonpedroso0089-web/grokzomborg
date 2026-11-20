# Chat com Ollama e Node.js

Este guia mostra como executar um chat de terminal com o Ollama, usando um modelo local, histórico de conversa e respostas em streaming.

## 1. Prepare o Ollama

Instale o [Ollama](https://ollama.com/download) e baixe um modelo:

```bash
ollama pull llama3.1
```

Se o computador tiver pouca memória, use um modelo menor, por exemplo `llama3.2:1b`. Use o mesmo nome de modelo no comando `ollama pull` e no código abaixo.

O Ollama normalmente inicia o serviço automaticamente. Se não estiver em execução, abra outro terminal e rode:

```bash
ollama serve
```

O endereço local padrão é `http://127.0.0.1:11434`.

## 2. Configure o projeto Node.js

Na pasta do repositório, instale as dependências do chat:

```bash
npm init -y
npm pkg set type=module
npm install ollama
```

> Se o projeto já tiver `package.json`, não execute `npm init -y`; apenas ajuste `"type": "module"` se necessário e instale `ollama`.

## 3. Crie `chat-terminal.js`

```javascript
import { Ollama } from 'ollama'
import { createInterface } from 'node:readline/promises'
import { stdin, stdout } from 'node:process'

const client = new Ollama({
  host: process.env.OLLAMA_HOST || 'http://127.0.0.1:11434',
})
const model = process.env.OLLAMA_MODEL || 'llama3.1'
const terminal = createInterface({ input: stdin, output: stdout })
const messages = [
  {
    role: 'system',
    content:
      'Você é o Grokzomborg, um monstro reciclado prestativo. Responda em português com humor leve e dicas educativas sobre sustentabilidade.',
  },
]

async function main() {
  console.log(`🧟 Chat GROKZOMBORG (${model}) — digite "sair" para encerrar.\n`)

  try {
    while (true) {
      const input = (await terminal.question('Você: ')).trim()
      if (input.toLowerCase() === 'sair') break
      if (!input) continue

      messages.push({ role: 'user', content: input })
      let answer = ''

      try {
        const stream = await client.chat({ model, messages, stream: true })
        stdout.write('GROKZOMBORG: ')

        for await (const part of stream) {
          const token = part.message?.content || ''
          answer += token
          stdout.write(token)
        }

        messages.push({ role: 'assistant', content: answer })
        stdout.write('\n\n')
      } catch (error) {
        // Não deixa uma pergunta sem resposta no histórico da conversa.
        messages.pop()
        console.error('\nNão foi possível consultar o Ollama:', error.message, '\n')
      }
    }
  } finally {
    terminal.close()
  }
}

main().catch((error) => {
  console.error('Erro:', error.message)
  process.exitCode = 1
})
```

## 4. Inicie o chat

Certifique-se de que o Ollama está em execução e que o modelo foi baixado. Então rode:

```bash
node chat-terminal.js
```

Para escolher outro modelo instalado:

```bash
OLLAMA_MODEL=llama3.2:1b node chat-terminal.js
```

No PowerShell:

```powershell
$env:OLLAMA_MODEL="llama3.2:1b"
node chat-terminal.js
```

O histórico é mantido somente durante a execução atual do terminal.

## Ollama Cloud (opcional)

Para usar a API Cloud, crie uma chave no painel do Ollama e configure `OLLAMA_API_KEY` como variável de ambiente. Não salve a chave no código nem a envie ao navegador.

No Node.js, crie o cliente usando a chave do ambiente:

```javascript
const client = new Ollama({
  host: 'https://ollama.com',
  headers: {
    Authorization: `Bearer ${process.env.OLLAMA_API_KEY}`,
  },
})
```

Use um modelo Cloud disponível na sua conta, como `gpt-oss:120b`, na opção `model` da chamada `client.chat`.

## Diferença para o chat do site

Este exemplo é um chat de terminal independente. O site do GROKZOMBORG envia as mensagens para `/api/chat`, implementado em `api/chat.js`; essa rota precisa rodar num backend compatível, configurado com `OLLAMA_HOST`, `OLLAMA_MODEL` e `OLLAMA_TEMPERATURE`.

GitHub Pages e `python -m http.server 8000` servem arquivos estáticos e **não executam** `api/chat.js`. O servidor HTTP Python permite abrir a interface local em `http://localhost:8000`, mas para usar IA no chat do site é necessário iniciar também a API num ambiente de servidor com acesso ao Ollama.
