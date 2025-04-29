import numpy as np
import logging

logging.basicConfig(filename='bb84_simulation.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def generate_quantum_key(length):
    bits = np.random.randint(2, size=length)
    bases = np.random.randint(2, size=length)
    logging.info(f"Generated key: bits={bits.tolist()}, bases={bases.tolist()}")
    return bits, bases

def simulate_eavesdropping(alice_bits, alice_bases, key_length):
    eve_bases = np.random.randint(2, size=key_length)
    intercepted_bits = np.where(alice_bases == eve_bases, alice_bits, np.random.randint(2, size=key_length))
    logging.info(f"Eve intercepted: bases={eve_bases.tolist()}, bits={intercepted_bits.tolist()}")
    return intercepted_bits, eve_bases 

def check_for_eavesdropping(alice_key, bob_key, sample_size):
    sample_indices = np.random.choice(len(alice_key), sample_size, replace=False)
    errors = np.sum(alice_key[sample_indices] != bob_key[sample_indices])
    logging.info(f"Eavesdropping check: sample_size={sample_size}, errors={errors}")
    return errors > 0

def bb84_simulation(key_length, eavesdropping=False):
    logging.info(f"Starting BB84 simulation with key_length={key_length}, eavesdropping={eavesdropping}")
    alice_bits, alice_bases = generate_quantum_key(key_length)
    bob_bases = np.random.randint(2, size=key_length)
    bob_bits = np.where(alice_bases == bob_bases, alice_bits, np.random.randint(2, size=key_length))
    
    if eavesdropping:
        eve_bits = simulate_eavesdropping(alice_bits, alice_bases, key_length)
        logging.info(f"Eve's intercepted bits: {eve_bits.tolist()}")
    
    shared_key = alice_bits[alice_bases == bob_bases]
    logging.info(f"Shared key: {shared_key.tolist()}")
    
    if eavesdropping:
        bob_key = bob_bits[alice_bases == bob_bases]
        if check_for_eavesdropping(shared_key, bob_key, len(shared_key)//2):
            logging.warning("Eavesdropping detected!")
        else:
            logging.info("No eavesdropping detected.")
    
    print(f"Shared keys: {shared_key} (length: {len(shared_key)})")
    return shared_key

if __name__ == "__main__":
    key_length = 10
    print("Simulação do protocolo BB84")
    bb84_simulation(key_length, eavesdropping=True)
