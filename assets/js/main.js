/* ========================================
   MAIN JAVASCRIPT - INTERACTIVITY
   ======================================== */

document.addEventListener('DOMContentLoaded', function() {
    initSmoothScroll();
    initButtonAnimations();
    initGlitchEffects();
    initNavbarEffect();
    initRandomGlitch();
});

/* ========================================
   SMOOTH SCROLL BEHAVIOR
   ======================================== */

function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

/* ========================================
   BUTTON ANIMATIONS
   ======================================== */

function initButtonAnimations() {
    const buttons = document.querySelectorAll('.btn-primary, .btn-secondary');
    
    buttons.forEach(button => {
        button.addEventListener('mouseenter', function() {
            this.style.animation = 'button-pulse 0.5s ease-out';
        });

        button.addEventListener('click', function(event) {
            createClickEffect(event);
        });
    });
}

/* ========================================
   CLICK EFFECT - RIPPLE ON BUTTON CLICK
   ======================================== */

function createClickEffect(event) {
    const button = event.target;
    const ripple = document.createElement('span');
    
    const rect = button.getBoundingClientRect();
    const size = Math.max(rect.width, rect.height);
    const x = event.clientX - rect.left - size / 2;
    const y = event.clientY - rect.top - size / 2;

    ripple.style.width = ripple.style.height = size + 'px';
    ripple.style.left = x + 'px';
    ripple.style.top = y + 'px';
    ripple.classList.add('ripple');

    button.appendChild(ripple);

    setTimeout(() => ripple.remove(), 600);
}

/* ========================================
   GLITCH EFFECTS ENHANCEMENT
   ======================================== */

function initGlitchEffects() {
    const glitchElements = document.querySelectorAll('.glitch, .glitch-rgb, .glitch-text');
    
    glitchElements.forEach(element => {
        element.addEventListener('mouseenter', function() {
            this.style.animationPlayState = 'running';
            this.style.animationDuration = '0.5s';
        });

        element.addEventListener('mouseleave', function() {
            this.style.animationDuration = '2s';
        });
    });
}

/* ========================================
   NAVBAR EFFECT ON SCROLL
   ======================================== */

function initNavbarEffect() {
    const navbar = document.querySelector('.navbar');
    let lastScrollY = 0;

    window.addEventListener('scroll', function() {
        const currentScrollY = window.scrollY;

        if (currentScrollY > 50) {
            navbar.style.boxShadow = '0 0 20px rgba(15, 255, 0, 0.4)';
            navbar.style.backgroundColor = 'rgba(5, 5, 5, 0.98)';
        } else {
            navbar.style.boxShadow = '0 0 10px rgba(15, 255, 0, 0.2)';
            navbar.style.backgroundColor = 'rgba(10, 10, 10, 0.95)';
        }

        lastScrollY = currentScrollY;
    });
}

/* ========================================
   RANDOM GLITCH EFFECT ON ELEMENTS
   ======================================== */

function initRandomGlitch() {
    const cards = document.querySelectorAll('.card');

    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            triggerGlitch(this);
        });
    });
}

function triggerGlitch(element) {
    const glitchDuration = 0.3;
    element.style.animation = `glitch-card-random ${glitchDuration}s`;

    setTimeout(() => {
        element.style.animation = 'none';
    }, glitchDuration * 1000);
}

/* ========================================
   DYNAMIC GLOW EFFECT
   ======================================== */

function addGlowEffect() {
    document.addEventListener('mousemove', function(e) {
        const glitchElements = document.querySelectorAll('.glitch, .glitch-rgb');
        
        glitchElements.forEach(element => {
            const rect = element.getBoundingClientRect();
            const elementCenterX = rect.left + rect.width / 2;
            const elementCenterY = rect.top + rect.height / 2;

            const distance = Math.hypot(e.clientX - elementCenterX, e.clientY - elementCenterY);
            const maxDistance = 300;

            if (distance < maxDistance) {
                const intensity = 1 - (distance / maxDistance);
                element.style.textShadow = `
                    0 0 ${20 * intensity}px rgba(15, 255, 0, 0.8),
                    0 0 ${30 * intensity}px rgba(0, 255, 255, 0.6),
                    0.05em 0 0 #ff00ff,
                    -0.05em -0.025em 0 #00ffff,
                    0.025em 0.05em 0 #ffff00
                `;
            }
        });
    });
}

// Initialize glow effect
addGlowEffect();

/* ========================================
   CONSOLE EASTER EGG
   ======================================== */

console.log(`
╔═══════════════════════════════════════╗
║        🎵 GROKZOMBORG AWAKENS 🎵      ║
╠═══════════════════════════════════════╣
║ Bem-vindo ao caos harmônico cósmico   ║
║ The glitch is alive... can you hear?  ║
║ Acordes ecoam através das dimensões   ║
╚═══════════════════════════════════════╝
`);

console.log('%cGROKZOMBORG', 'color: #0f0; font-size: 20px; font-weight: bold; text-shadow: 0 0 10px #00ffff;');
console.log('%cDESPERTE', 'color: #ff00ff; font-size: 16px; font-weight: bold;');