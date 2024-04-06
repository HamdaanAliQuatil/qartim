import base64
import numpy as np
np.set_printoptions(linewidth=110)

from qiskit_aer import AerSimulator
import LinearCode as LC

from bb84 import initiate_keygen, initialize_protocol, encode_qubits, array_to_string
# measure_qubits, filter_qubits, from bb84

NUM_QUBITS = 32
BACKEND = AerSimulator(method='stabilizer')

# Initilisation of the encoding basis and the sender states of the quibits
key = initiate_keygen()

# The bits to be sent
sent_bits = array_to_string(sender_states)

# Draw up a quantum circuit for encoding the qubit states
encoded_qubits = encode_qubits(NUM_QUBITS, sender_states, encoding_basis)
encoded_qubits.draw()


