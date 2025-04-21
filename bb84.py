import numpy as np

def generate_quantum_key(length):
    bits = np.random.randint(2, size=length)
    bases = np.random.randint(2, size=length)
    return bits, bases

def bb84_simulation(key_length, eavesdropping=False):
    alice_bits, alice_bases = generate_quantum_key(key_length)
    bob_bases = np.random.randint(2, size=key_length)
    bob_bits = np.where(alice_bases == bob_bases, alice_bits, np.random.randint(2, size=key_length))
    
    if eavesdropping:
        eve_bits = simulate_eavesdropping(alice_bits, alice_bases, key_length)
        print(f"Eve's intercepted bits: {eve_bits}")
    
    shared_key = alice_bits[alice_bases == bob_bases]
    print(f"Chave compartilhada: {shared_key}")
    return shared_key
    
    shared_key = alice_bits[alice_bases == bob_bases]
    print(f"Shared Key: {shared_key}")
    return shared_key

def simulate_eavesdropping(alice_bits, alice_bases, key_length):
    eve_bases = np.random.randint(2, size=key_length)
    intercepted_bits = np.where(alice_bases == eve_bases, alice_bits, np.random.randint(2, size=key_length))
    return intercepted_bits

def check_for_eavesdropping(alice_key, bob_key, sample_size):
    sample_indices = np.random.choice(len(alice_key), sample_size, replace=False)
    errors = np.sum(alice_key[sample_indices] != bob_key[sample_indices])
    return errors > 0

if __name__ == "__main__":
    key_length = 10
    print("Protocol BB84 Simulation")
    bb84_simulation(key_length)
