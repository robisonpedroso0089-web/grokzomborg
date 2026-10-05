"use client"

import { useState } from "react";

export default function Joke() {
  const [joke, setJoke] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  async function fetchJoke() {
    setLoading(true);
    setError(null);
    try {
      const res = await fetch("https://icanhazdadjoke.com/", {
        headers: { Accept: "application/json" },
        cache: "no-store"
      });
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const data = await res.json();
      setJoke(data.joke || JSON.stringify(data));
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div style={{
      background: "rgba(0,0,0,0.6)",
      color: "#0f0",
      border: "2px solid #0f0",
      padding: 20,
      borderRadius: 8,
      maxWidth: 720,
      margin: "20px auto",
      fontFamily: "VT323, monospace",
      textAlign: "center"
    }}>
      <h2 style={{ margin: "0 0 8px", fontFamily: "Press Start 2P, cursive", fontSize: 18 }}>Gerador de Piadas</h2>

      <div style={{ minHeight: 48, marginBottom: 12 }}>
        {loading && <span>Carregando...</span>}
        {error && <span style={{ color: "#ff6666" }}>Erro: {error}</span>}
        {!loading && !error && !joke && <span>Clique em "Nova piada" para buscar uma piada aleatória.</span>}
        {!loading && !error && joke && <span style={{ fontSize: 18 }}>{joke}</span>}
      </div>

      <div>
        <button
          onClick={fetchJoke}
          disabled={loading}
          style={{
            background: "#0f0",
            color: "#000",
            border: "none",
            padding: "8px 14px",
            cursor: "pointer",
            fontWeight: "bold",
            borderRadius: 4
          }}
        >
          {loading ? "..." : "Nova piada"}
        </button>
        <button
          onClick={() => { setJoke(null); setError(null); }}
          style={{
            marginLeft: 12,
            background: "transparent",
            color: "#0f0",
            border: "1px solid #0f0",
            padding: "8px 12px",
            cursor: "pointer",
            borderRadius: 4
          }}
        >Limpar</button>
      </div>

      <p style={{ marginTop: 12, fontSize: 12, opacity: 0.9 }}>Fonte: https://icanhazdadjoke.com/ (Accept: application/json)</p>
    </div>
  );
}
