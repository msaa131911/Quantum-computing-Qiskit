from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit.circuit import Parameter, ParameterVector


theta = ParameterVector("theta", 2)

theta1 = Parameter("theta1")

qr = QuantumRegister(4, "q")


qc = QuantumCircuit(qr)

qc.h(qr[0])


qc.ccx(qr[0], qr[1], qr[2])



ss = qc.to_instruction(label="jk624")



print("Original Circuit:")
print(qc.draw())


qc1 = QuantumCircuit(4)



qc1.ry(theta1,0)


qc1.ry(theta[0],1)


qc1.ry(theta[1],2)


print("\nParameterized Circuit:")
print(qc1.draw())


qc2 = qc1.assign_parameters({
    theta1: 1.50,
    theta[0]: 0.75,
    theta[1]: 1.20
})

print("\nCircuit after assigning parameters:")
print(qc2.draw())


qc3 = QuantumCircuit(4, 4)

qc3.compose(qc2,inplace=True)

qc3.measure(range(4),range(4))


print("\nFinal Circuit:")
print(qc3.draw())



simulator = AerSimulator()
job = simulator.run(qc3,shots=1000)
result = job.result()
counts = result.get_counts()

print("\nMeasurement Results:")
print(counts)