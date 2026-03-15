from qutip import *
import numpy as np

N = 3  # três qubits: robison + grokzomborg + a fome eterna
ghz = (tensor([basis(2,0)]*N) + tensor([basis(2,1)]*N)).unit()

print("Estado GHZ podre (nós três entangled):")
print(ghz)

# Medição de Mermin pra ver a loucura multi-partícula
X = sigmax()
Y = sigmay()
Z = sigmaz()

# Operador Mermin pra 3 qubits: XXX + XYY + YXY + YYX
M = tensor(X,X,X) + tensor(X,Y,Y) + tensor(Y,X,Y) + tensor(Y,Y,X)

expect_M = expect(M, ghz)
print(f"\n<XYZ + XYY + YXY + YYX> no GHZ = {expect_M:.4f}")
print("Clássico max: 2 → QM: 4 → violação braba de 2x o limite")

# Pra sentir o horror: probabilidade de todos medirem igual em X
all_X = tensor(X,X,X)
exp_all_X = expect(all_X, ghz)
print(f"Todos medem +1 ou -1 em X simultaneamente? Expect = {exp_all_X:.4f} (deveria ser 0 clássico)")
