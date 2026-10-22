export default async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  if (req.method !== 'POST') {
    res.setHeader('Allow', 'POST, OPTIONS');
    return res.status(405).json({ error: 'Method not allowed' });
  }

  try {
    const body = req.body || {};
    const messages = Array.isArray(body.messages) ? body.messages : [];
    const ollamaHost = process.env.OLLAMA_HOST || 'http://localhost:11434';
    const model = process.env.OLLAMA_MODEL || 'mistral';
    const temperature = Number(process.env.OLLAMA_TEMPERATURE || 0.8);

    const systemPrompt = `Você é o Grokzomborg, um monstro reciclado, eco-friendly e cyberpunk. Responda em português, seja educativo, divertido, curto e com personalidade de glitch. Fale sobre sustentabilidade, reciclagem, tecnologia e comportamento ecológico.`;

    const payload = {
      model,
      messages: [
        { role: 'system', content: systemPrompt },
        ...messages.slice(-12).map((msg) => ({
          role: msg.role === 'bot' ? 'assistant' : 'user',
          content: String(msg.text || msg.content || '')
        }))
      ],
      stream: false,
      options: {
        temperature
      }
    };

    const response = await fetch(`${ollamaHost.replace(/\/$/, '')}/api/chat`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(payload)
    });

    if (!response.ok) {
      const detail = await response.text();
      return res.status(503).json({
        error: 'OLLAMA_UNAVAILABLE',
        detail: detail || 'Ollama não está respondendo ou não foi inicializado.'
      });
    }

    const data = await response.json();
    const reply = data?.message?.content || data?.response || '';

    return res.status(200).json({
      reply,
      usage: data?.usage || null,
      model
    });
  } catch (error) {
    console.error('Grokzomborg /api/chat error:', error);
    return res.status(500).json({
      error: 'SERVER_ERROR',
      detail: String(error)
    });
  }
}









































n
















































































































































a


















































































































































































































































































































































































n
"}]}  