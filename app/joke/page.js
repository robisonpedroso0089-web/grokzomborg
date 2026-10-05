import Joke from '../../components/Joke';

export default function Page() {
  return (
    <main style={{
      minHeight: '100vh',
      background: '#000',
      color: '#0f0',
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      paddingTop: 48,
      fontFamily: 'VT323, monospace'
    }}>
      <h1 style={{ fontFamily: 'Press Start 2P, cursive', fontSize: 20 }}>GROKZOMBORG — JOKES</h1>
      <p style={{ maxWidth: 720, textAlign: 'center' }}>Clique no botão para buscar uma piada aleatória usando a API externa <code>icanhazdadjoke.com</code>.</p>
      <Joke />
    </main>
  );
}
