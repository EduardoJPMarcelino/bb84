import numpy as np

def generate_quantum_key(length):
    bits = np.random.randint(2, size=length)
    bases = np.random.randint(2, size=length)
    return bits, bases

def bb84_simulation(key_length):
    alice_bits, alice_bases = generate_quantum_key(key_length)
    bob_bases = np.random.randint(2, size=key_length)
    bob_bits = np.where(alice_bases == bob_bases, alice_bits, np.random.randint(2, size=key_length))
    
    shared_key = alice_bits[alice_bases == bob_bases]
    print(f"Shared Key: {shared_key}")
    return shared_key

if __name__ == "__main__":
    key_length = 10
    print("Protocol BB84 Simulation")
    bb84_simulation(key_length)
