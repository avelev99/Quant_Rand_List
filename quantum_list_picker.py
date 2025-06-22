import math
from qiskit_ibm_provider import IBMProvider  # type: ignore
from qiskit import transpile
from qiskit.circuit import QuantumCircuit


def pick_random_element(items, backend_name="ibm_lima"):
    """Pick a random element from items using a quantum backend.

    Args:
        items (list): List of items to choose from.
        backend_name (str): IBM Quantum backend name. Defaults to 'ibm_lima'.

    Returns:
        object: Randomly chosen element from items.
    """
    if not items:
        raise ValueError("The list of items cannot be empty")

    num_qubits = math.ceil(math.log2(len(items))) or 1
    qc = QuantumCircuit(num_qubits, num_qubits)
    qc.h(range(num_qubits))
    qc.measure(range(num_qubits), range(num_qubits))

    try:
        provider = IBMProvider()
        backend = provider.get_backend(backend_name)
    except Exception as exc:
        raise RuntimeError(
            "IBM Quantum account is not configured or backend unavailable"
        ) from exc

    compiled = transpile(qc, backend)
    job = backend.run(compiled, shots=1)
    result = job.result()
    bitstring = list(result.get_counts(qc).keys())[0]

    index = int(bitstring, 2) % len(items)
    return items[index]


if __name__ == "__main__":
    items = [
        "Ant", "Bear", "Cat", "Dog", "Elephant", "Frog", "Giraffe", "Horse",
        "Iguana", "Jaguar", "Koala", "Lion", "Monkey", "Newt", "Owl",
        "Penguin", "Quail", "Rabbit", "Snake", "Tiger", "Urchin", "Vulture",
        "Wolf", "Xerus", "Yak", "Zebra", "Aardvark", "Butterfly", "Cheetah",
        "Dolphin", "Eagle", "Falcon", "Goat", "Hamster", "Impala", "Jellyfish",
        "Kangaroo", "Lemur", "Moth", "Nightingale", "Opossum", "Parrot",
        "Quokka", "Raccoon", "Shark", "Turtle", "Uakari", "Viper", "Walrus",
        "Xantus", "Yakutian Horse", "Zebu", "Alpaca", "Bison", "Crab",
        "Donkey", "Emu", "Firefly", "Gazelle", "Heron", "Insect", "Jackal",
        "Kookaburra", "Llama"
    ]

    element = pick_random_element(items)
    print(f"Random element: {element}")
