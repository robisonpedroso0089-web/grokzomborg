Adiciona um gerador de piadas aleatórias usando a API externa icanhazdadjoke.com.

Como usar:

1. Certifique-se de que seu projeto Next.js está configurado (Next 13+ com App Router).
2. Rode:
   npm install
   npm run dev
3. Abra /joke (ex: http://localhost:3000/joke) e clique em "Nova piada".

Observações:
- O componente faz uma requisição client-side para https://icanhazdadjoke.com/ usando o header Accept: application/json.
- Se desejar outra API de piadas (ou um fetch no servidor), eu posso ajustar.
