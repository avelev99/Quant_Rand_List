#!/usr/bin/env python3
"""
Simplified Quantum Animal Selector
Single-shot quantum randomness demonstration using IBM Quantum
"""

from qiskit import QuantumCircuit, transpile
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler

def quantum_animal_selector():
    # IBM Quantum API Configuration
    API_KEY = "cfab6b2248c2ead8d6223f0506e17b8c2826fb79e7154f31c19dc3af6ed16e77bb7b8570c5f2a7222e4fd91ac81b99e9a7c5ff293da9ad0939c0c4baccef322c"
    
    # Complete list of 64 animals and insects (2^6 = 64 possibilities)
    ANIMALS = [
        "Lion", "Tiger", "Elephant", "Giraffe", "Zebra", "Hippo", "Rhino", "Cheetah",
        "Leopard", "Jaguar", "Puma", "Lynx", "Ocelot", "Serval", "Caracal", "Bobcat",
        "Wolf", "Fox", "Bear", "Panda", "Koala", "Kangaroo", "Wallaby", "Wombat",
        "Platypus", "Echidna", "Sloth", "Armadillo", "Anteater", "Pangolin", "Aardvark", "Meerkat",
        "Mongoose", "Ferret", "Otter", "Seal", "Walrus", "Dolphin", "Whale", "Shark",
        "Octopus", "Squid", "Jellyfish", "Starfish", "Crab", "Lobster", "Shrimp", "Seahorse",
        "Butterfly", "Dragonfly", "Bee", "Ant", "Beetle", "Ladybug", "Grasshopper", "Cricket",
        "Spider", "Scorpion", "Centipede", "Millipede", "Snail", "Slug", "Earthworm", "Firefly"
    ]
    
    print("🔬 Quantum Animal Selector - Single Shot Demo")
    print("=" * 50)
    
    try:
        # Initialize IBM Quantum service
        print("🔌 Connecting to IBM Quantum...")
        service = QiskitRuntimeService(
            channel="ibm_quantum",
            token=API_KEY
        )
        
        # Get available quantum backend (QPU only)
        backend = service.least_busy(operational=True, simulator=False)
        print(f"🖥️  Selected quantum backend: {backend.name}")
        
        # Create quantum circuit with 6 qubits (2^6 = 64 possibilities)
        print("⚛️  Creating quantum circuit...")
        qc = QuantumCircuit(6, 6)
        
        # Apply Hadamard gates to create superposition
        for i in range(6):
            qc.h(i)
        
        # Measure all qubits
        qc.measure_all()
        
        print("📊 Circuit created with 6 qubits in superposition")
        
        # Transpile circuit for the backend
        print("🔄 Transpiling circuit for quantum hardware...")
        transpiled_qc = transpile(qc, backend=backend, optimization_level=3)
        
        # Execute single shot on quantum hardware
        print("🚀 Executing single quantum shot...")
        print("⏳ Waiting for quantum result...")
        
        sampler = Sampler(backend)
        job = sampler.run([transpiled_qc], shots=1)
        result = job.result()
        
        # Extract the single measurement result
        counts = result[0].data.meas.get_counts()
        binary_result = list(counts.keys())[0]  # Get the single result
        
        # Convert binary to decimal for animal selection
        decimal_result = int(binary_result, 2)
        selected_animal = ANIMALS[decimal_result]
        
        # Display results
        print("\n" + "=" * 50)
        print("🎯 QUANTUM RESULT")
        print("=" * 50)
        print(f"📊 Binary measurement: {binary_result}")
        print(f"🔢 Decimal value: {decimal_result}")
        print(f"🦁 Selected animal: {selected_animal}")
        print(f"🎲 Quantum backend: {backend.name}")
        print("=" * 50)
        
        # Verification
        print(f"\n✅ Single shot executed successfully!")
        print(f"📈 Total possible outcomes: {len(ANIMALS)}")
        print(f"🎯 Quantum randomness achieved with 1 shot")
        
        return {
            'binary': binary_result,
            'decimal': decimal_result,
            'animal': selected_animal,
            'backend': backend.name
        }
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("🔧 Please check your IBM Quantum account and API key")
        return None

# Execute the quantum animal selector
if __name__ == "__main__":
    result = quantum_animal_selector()
    
    if result:
        print(f"\n🎉 Quantum selection complete: {result['animal']}")
    else:
        print("\n💥 Quantum execution failed")
