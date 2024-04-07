import numpy as np
from qiskit import QuantumCircuit, Aer, transpile
from qiskit.providers.aer import AerSimulator
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_histogram

# Function to create a random quantum state
def create_random_state():
    backend = Aer.get_backend('aer_simulator')
    qc = QuantumCircuit(1)
    qc.h(0)
    qc.s(0)
    qc.t(0)
    qc.measure_all()
    
    # Simulate the circuit to get the statevector
    transpiled_qc = transpile(qc, backend)
    result = backend.run(transpiled_qc).result()
    statevector = result.get_statevector()
    
    return statevector

# Function for Bob to measure qubits in a random basis
def measure_qubits(statevector, bases_used):
    backend = Aer.get_backend('aer_simulator')
    measurements = []
    
    for i in range(len(statevector)):
        basis = bases_used[i]
        qc = QuantumCircuit(1, 1)
        
        # Apply the appropriate measurement basis
        if basis == 0:
            qc.measure(0, 0)
        else:
            qc.h(0)
            qc.measure(0, 0)
        
        # Simulate the measurement
        transpiled_qc = transpile(qc, backend)
        result = backend.run(transpiled_qc, initial_state=statevector[i]).result()
        counts = result.get_counts()
        
        # Record the measurement outcome
        measurement = int(list(counts.keys())[0])
        measurements.append(measurement)
        
    return measurements

# Function to test Bob's functions
def test_bob_functions():
    # Step 1: Bob receives qubits from Alice
    alice_state = create_random_state()
    
    # Step 2: Bob randomly selects measurement bases
    bases_used = np.random.choice([0, 1], size=len(alice_state))
    
    # Step 3: Bob measures qubits
    bob_measurements = measure_qubits(alice_state, bases_used)
    
    # Step 4: Bob sends a bitvector of the bases used to measure to Alice
    print(f"Bob's bases used: {bases_used}")
    
    # Step 5: Alice responds with a bitvector of which bases were correct
    # Here we assume Alice knows the correct bases, for simplicity
    alice_correct_bases = bases_used  # In a real scenario, Alice would determine the correct bases
    
    print(f"Alice's correct bases: {alice_correct_bases}")
    
    # Step 6: Alice and Bob discard all qubits that were measured in the wrong basis
    correct_qubits = [bob_measurements[i] for i in range(len(bob_measurements)) if bases_used[i] == alice_correct_bases[i]]
    
    print(f"Correct qubits after discarding: {correct_qubits}")
    
    # Calculate the fidelity between the original state and the correct qubits
    correct_statevector = Statevector([0 if q == 0 else 1 for q in correct_qubits])
    fidelity = correct_statevector.fidelity(Statevector(alice_state))
    
    print(f"Fidelity between correct qubits and original state: {fidelity}")

# Run the test function
test_bob_functions()
