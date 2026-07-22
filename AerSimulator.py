from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()

sim = AerSimulator()     
tqc = transpile(qc, sim)
result = sim.run(tqc, shots=1024).result()

print(result.get_counts())


