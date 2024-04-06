import base64
import numpy as np
np.set_printoptions(linewidth=110)

from qiskit_aer import AerSimulator
import LinearCode as LC

from bb84 import initiate_keygen, initialize_protocol, encode_qubits, array_to_string
# measure_qubits, filter_qubits, from bb84

NUM_QUBITS = 32
BACKEND = AerSimulator(method='stabilizer')

# Initilisation of the key
key = initiate_keygen()


