import pytest
import numpy as np
from bb84 import generate_quantum_key, simulate_eavesdropping, check_for_eavesdropping, bb84_simulation

@pytest.fixture
def key_length():
    return 10

def test_generate_quantum_key(key_length):
    bits, bases = generate_quantum_key(key_length)
    assert len(bits) == key_length, f"Expected {key_length} bits, got {len(bits)}"
    assert len(bases) == key_length, f"Expected {key_length} bases, got {len(bases)}"
    assert all(bit in [0, 1] for bit in bits), "Bits should be 0 or 1"
    assert all(base in [0, 1] for base in bases), "Bases should be 0 or 1"

def test_simulate_eavesdropping(key_length):
    alice_bits, alice_bases = generate_quantum_key(key_length)
    intercepted_bits, eve_bases = simulate_eavesdropping(alice_bits, alice_bases, key_length)
    assert len(intercepted_bits) == key_length, f"Expected {key_length} intercepted bits, got {len(intercepted_bits)}"
    matching_bases = alice_bases == eve_bases
    for i in range(key_length):
        if matching_bases[i]:
            assert intercepted_bits[i] == alice_bits[i], f"Intercepted bit {intercepted_bits[i]} should match Alice's bit {alice_bits[i]} at index {i}"

def test_check_for_eavesdropping_no_errors():
    alice_key = np.array([0, 1, 0, 1])
    bob_key = np.array([0, 1, 0, 1])
    sample_size = 2
    result = check_for_eavesdropping(alice_key, bob_key, sample_size)
    assert result == False, "Should not detect eavesdropping when keys match"

def test_check_for_eavesdropping_with_errors():
    alice_key = np.array([0, 1, 0, 1])
    bob_key = np.array([0, 1, 1, 1])
    sample_size = len(alice_key)  # Comparar toda a chave para garantir detecção
    result = check_for_eavesdropping(alice_key, bob_key, sample_size)
    assert result == True, "Should detect eavesdropping when keys differ"

def test_bb84_simulation_without_eavesdropping(key_length):
    shared_key = bb84_simulation(key_length, eavesdropping=False)
    assert len(shared_key) <= key_length, "Shared key length should not exceed original key length"
    assert all(bit in [0, 1] for bit in shared_key), "Shared key bits should be 0 or 1"

def test_bb84_simulation_with_eavesdropping(key_length):
    shared_key = bb84_simulation(key_length, eavesdropping=True)
    assert len(shared_key) <= key_length, "Shared key length should not exceed original key length"
    assert all(bit in [0, 1] for bit in shared_key), "Shared key bits should be 0 or 1"
