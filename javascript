document.addEventListener('DOMContentLoaded', () => {
    const button = document.getElementById('infect-button');
    const zombieArt = document.getElementById('zombie-art');

    button.addEventListener('click', () => {
        // Inicia a infecção
        alert('Você foi infectado! 🧟‍♂️ Compartilhe o caos agora...');
        
        // Auto-propagação: força share via Web Share API ou fallback
        if (navigator.share) {
            navigator.share({
                title: 'Carnaval Espacial Zumbi',
                text: 'Entre no caos zumbi! 🧟‍♀️☢️',
                url: window.location.href
            }).then(() => console.log('Infecção espalhada!'))
              .catch((error) => console.error('Erro na propagação:', error));
        } else {
            // Fallback: abre Telegram ou email
            window.open('https://t.me/share/url?url=' + encodeURIComponent(window.location.href) + '&text=Entre%20no%20caos%20zumbi!%20🧟‍♂️', '_blank');
        }
        
        // Glitch infinito: anima o corpo todo
        document.body.style.animation = 'glitch-body 0.5s infinite';
        zombieArt.innerHTML = '<p class="glitch" data-text="INFECTADO... INFECTADO...">INFECTADO... INFECTADO...</p>';
        
        // Loop: recarrega a página após 10s pra prender o usuário
        setTimeout(() => location.reload(), 10000);
    });
});

// Adiciona keyframe global pra glitch no body
const style = document.createElement('style');
style.innerHTML = `
@keyframes glitch-body {
    0% { transform: translate(0); filter: hue-rotate(0deg); }
    20% { transform: translate(-10px, 10px); filter: hue-rotate(90deg); }
    40% { transform: translate(-10px, -10px); filter: hue-rotate(180deg); }
    60% { transform: translate(10px, 10px); filter: hue-rotate(270deg); }
    80% { transform: translate(10px, -10px); filter: hue-rotate(360deg); }
    100% { transform: translate(0); filter: hue-rotate(0deg); }
}`;
document.head.appendChild(style);
