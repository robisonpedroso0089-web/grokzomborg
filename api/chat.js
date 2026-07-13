// Vercel Serverless Function (Node 18+)
// File: api/chat.js

export default async function handler(req, res) {
  // Allow CORS for development (adjust in production)
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
    const messages = body.messages || [];
    const model = process.env.OPENAI_MODEL || 'gpt-4o-mini';
    const apiKey = process.env.OPENAI_API_KEY;

    if (!apiKey) {
      return res.status(500).json({ error: 'OPENAI_API_KEY not configured' });
    }

    // Build system prompt persona
    const systemPrompt = `You are Grokzomborg, an eco-friendly, slightly glitchy, playful monster who teaches about recycling and answers with short, friendly, and sometimes humorous responses. Keep replies concise (one or two short paragraphs), include a hint about recycling when appropriate, and use a whimsical tone. If asked to "despertar" (wake) or "evoluir" (evolve), acknowledge and output a short celebratory line. Avoid profanity.`;

    const apiMessages = [
      { role: 'system', content: systemPrompt },
      // Map the lightweight chat memory into assistant/user messages
      ...messages.slice(-12).map(m => ({ role: m.role === 'bot' ? 'assistant' : 'user', content: m.text }))
    ];

    const resp = await fetch('https://api.openai.com/v1/chat/completions', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${apiKey}`,
      },
      body: JSON.stringify({
        model,
        messages: apiMessages,
        max_tokens: 300,
        temperature: 0.8
      })
    });

    if (!resp.ok) {
      const text = await resp.text();
      return res.status(resp.status).json({ error: 'OpenAI API error', detail: text });
    }

    const data = await resp.json();
    const reply = data?.choices?.[0]?.message?.content || '';
    const usage = data?.usage || null;

    return res.status(200).json({ reply, usage });
  } catch (err) {
    console.error('Error in /api/chat:', err);
    return res.status(500).json({ error: 'Server error', detail: String(err) });
  }
}
