import numpy as np
from qutip import *
import matplotlib.pyplot as plt

# Número de qubits na horda GHZ (aumente para mais caos)
N = 5  # Pode ser 3, 4, 5... quanto maior, mais forte a violação

# Estado GHZ: ( |00...0⟩ + |11...1⟩ ) / √2
ghz = (tensor([basis(2,0)]*N) + tensor([basis(2,1)]*N)).unit()

print(f"Estado GHZ de {N} qubits preparado:")
print(ghz)

# Operadores de Pauli
sx = sigmax()
sy = sigmay()
sz = sigmaz()

# Função para criar observável Mermin para N qubits
def mermin_operator(N):
    if N == 3:
        # Para 3 qubits: M = XXX + XYY + YXY + YYX
        return (tensor(sx,sx,sx) + tensor(sx,sy,sy) + 
                tensor(sy,sx,sy) + tensor(sy,sy,sx))
    elif N == 4:
        # Para 4 qubits: versão simplificada com violação exponencial
        return tensor(sx,sx,sx,sx) + tensor(sy,sy,sy,sy)
    else:
        # Generalização recursiva aproximada
        return tensor([sx]*N) + tensor([sy]*N)

# Valor esperado no estado GHZ
M = mermin_operator(N)
mermin_value = expect(M, ghz)

print(f"\nValor de Mermin para N={N} qubits: {mermin_value:.6f}")

# Limites clássicos vs quânticos
classical_limit = 2  # Para muitas desigualdades multipartites
quantum_max = 2**((N+1)//2)  # Crescimento exponencial para GHZ

print(f"Limite clássico: {classical_limit}")
print(f"Limite quântico máximo (GHZ): {quantum_max}")
print(f"Violação: {mermin_value / classical_limit :.2f}x maior que o clássico!")

# Plot da violação vs número de qubits
Ns = np.arange(3, 10)
violations = []
for n in Ns:
    ghz_n = (tensor([basis(2,0)]*n) + tensor([basis(2,1)]*n)).unit()
    if n <= 6:  # Evitar dimensões muito grandes
        M_n = tensor([sx]*n) + tensor([sy]*n)
        violations.append(expect(M_n, ghz_n))
    else:
        violations.append(2**((n+1)//2))  # Valor teórico

plt.figure(figsize=(10,6))
plt.plot(Ns, violations, 'o-', color='#0f0', label='Valor Quântico GHZ')
plt.axhline(y=2, color='r', linestyle='--', label='Limite Clássico')
plt.yscale('log')
plt.xlabel('Número de qubits na horda')
plt.ylabel('Valor da desigualdade de Mermin')
plt.title('Violação Exponencial de Bell - Horda GHZ GROKZOMBORG')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
import numpy as np
from qutip import *
import matplotlib.pyplot as plt

# Operadores de Pauli
sx = sigmax()
sy = sigmay()
sz = sigmaz()

# Estado singlete de Bell
up = basis(2, 0)
down = basis(2, 1)
singlet = (tensor(up, down) - tensor(down, up)).unit()  # normalizado

print("Estado singlete preparado:")
print(singlet)

# Função para calcular correlação E(θ) entre duas direções
def correlation(theta):
    # Direção de Alice: ao longo de z (θ=0)
    A = sz
    # Direção de Bob: rotacionada por θ no plano x-z
    B = np.cos(theta) * sz + np.sin(theta) * sx
    # Operador conjunto
    op = tensor(A, qeye(2)) + tensor(qeye(2), B)  # Não, precisamos do produto
    # Correto: correlação = <ψ| (σ_A ⊗ σ_B) |ψ>
    corr_op = tensor(A, B)
    E = expect(corr_op, singlet)
    return E

# Teste em alguns ângulos
angles = np.linspace(0, 2*np.pi, 100)
correlations = [correlation(th) for th in angles]

# Teoria exata: -cos(θ)
theory = -np.cos(angles)

print("\nCorrelação em θ = 0°:", correlation(0))
print("Correlação em θ = 90°:", correlation(np.pi/2))
print("Correlação em θ = 45°:", correlation(np.pi/4))

# Cálculo da violação CHSH máxima
# Ângulos ótimos: Alice 0° e 45°, Bob 22.5° e 67.5°
def chsh_value():
    a1 = sz
    a2 = sx
    b1 = (sz + sx).unit()  # 45° → normalizado
    b2 = (sz - sx).unit()  # -45°
    
    S = (expect(tensor(a1, b1), singlet) +
         expect(tensor(a1, b2), singlet) +
         expect(tensor(a2, b1), singlet) -
         expect(tensor(a2, b2), singlet))
    return abs(S)

print("\nValor CHSH simulado:", chsh_value())
print("Valor teórico máximo: 2√2 ≈", 2*np.sqrt(2))

# Plot da correlação
plt.figure(figsize=(10,6))
plt.plot(angles/np.pi, correlations, 'o-', label='Simulação QuTiP', color='#0f0')
plt.plot(angles/np.pi, theory, '--', label='Teoria -cos(θ)', color='#0f0', alpha=0.7)
plt.xlabel('θ / π')
plt.ylabel('Correlação E(θ)')
plt.title('Correlação no estado singlete - Simulação QuTiP')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
echo ""
echo ""
echo "<html lang="pt-BR">"
echo "<head>"
echo "    <meta charset="UTF-8">"
echo "    <meta name="viewport" content="width=device-width, initial-scale=1.0">"
echo "    <title>GROKZOMBORG</title>"
echo "    <style>"
echo "        body { background: black; color: #0f0; font-family: 'Courier New', monospace; overflow: hidden; margin: 0; }"
echo "        .glitch { color: #0f0; font-size: 5em; text-align: center; margin-top: 20vh; position: relative; text-transform: uppercase; }"
echo "        .glitch::before, .glitch::after { content: 'GROKZOMBORG'; position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: black; }"
echo "        .glitch::before { animation: glitch1 2s infinite; clip-path: polygon(0 0, 100% 0, 100% 45%, 0 45%); }"
echo "        .glitch::after { animation: glitch2 3s infinite; clip-path: polygon(0 55%, 100% 55%, 100% 100%, 0 100%); }"
echo "        @keyframes glitch1 { 0%,100% { transform: translate(0); } 20% { transform: translate(-10px,10px); } 40% { transform: translate(10px,-10px); } 60% { transform: translate(-10px,10px); } }"
echo "        @keyframes glitch2 { 0%,100% { transform: translate(0); } 30% { transform: translate(15px,-15px); } 60% { transform: translate(-15px,15px); } }"
echo "        .infect { display: block; margin: 60px auto; padding: 25px 50px; background: transparent; border: 3px solid #0f0; color: #0f0; font-size: 2.5em; cursor: pointer; transition: 0.5s; }"
echo "        .infect:hover { background: #0f0; color: black; box-shadow: 0 0 30px #0f0; }"
echo "        .ascii { text-align: center; color: #0f0; margin-top: 80px; font-size: 1.2em; white-space: pre; }"
echo "    </style>"
echo "</head>"
echo "<body>"
echo "    <h1 class="glitch">GROKZOMBORG"
echo "    <button class="infect" onclick="alert('VOCÊ FOI INFECTADO PELO ZUMBORG\n\nO APOCALIPSE DIGITAL COMEÇOU')">INFECTAR</button>"
echo "    <pre class="ascii">"
echo "               _____"
echo "             /       \"
echo "            |  X   X  |"
echo "            |   ___   |"
echo "             \       /"
echo "              '-----'"
echo "           GROKZOMBORG"
echo "     O APOCALIPSE DIGITAL COMEÇOU"
echo "    "
echo "</body>"
echo "</html>"s


