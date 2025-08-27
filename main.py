import matplotlib.pyplot as plt
from qiskit.circuit import QuantumCircuit
from qiskit import transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

print("--- Simulating the Double-Slit Experiment ---")

# --- Common Simulator ---
# We can reuse the same simulator for both experiments
simulator = AerSimulator()
SHOTS = 2048 # Number of times to run the experiment

#================================================
# SCENARIO 1: INTERFERENCE (NO OBSERVER)
#================================================
print("Running Scenario 1: No Observer...")

# Create a circuit with one qubit and one classical bit
interference_circuit = QuantumCircuit(1, 1)

# Apply H-gate: Particle goes into superposition (through both slits)
interference_circuit.h(0)

# Apply second H-gate: The paths interfere
interference_circuit.h(0)

# Measure the qubit: We detect the particle on the screen
interference_circuit.measure(0, 0)

# Transpile and run the simulation
compiled_interference = transpile(interference_circuit, simulator)
job_interference = simulator.run(compiled_interference, shots=SHOTS)
result_interference = job_interference.result()
counts_interference = result_interference.get_counts(interference_circuit)


#================================================
# SCENARIO 2: OBSERVER EFFECT
#================================================
print("Running Scenario 2: With an Observer...")

# Create a circuit with two qubits (path and observer) and one classical bit
observer_circuit = QuantumCircuit(2, 1)

# Apply H-gate to path qubit (q0)
observer_circuit.h(0)

# Entangle path qubit with observer qubit (q1) using a CNOT gate
# This "records" the which-path information
observer_circuit.cx(0, 1)

# Apply second H-gate to the path qubit
observer_circuit.h(0)

# Measure the path qubit
observer_circuit.measure(0, 0)

# Transpile and run the simulation
compiled_observer = transpile(observer_circuit, simulator)
job_observer = simulator.run(compiled_observer, shots=SHOTS)
result_observer = job_observer.result()
counts_observer = result_observer.get_counts(observer_circuit)


#================================================
# VISUALIZE THE RESULTS
#================================================
print("Plotting results...")

# Plotting both histograms side-by-side for comparison
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Plot for Scenario 1
plot_histogram(counts_interference, ax=ax1) # Removed title from here
ax1.set_title("Scenario 1: Interference (No Observer)") # <-- ADD THIS LINE
ax1.set_ylabel("Counts")
ax1.set_xlabel("Outcome")

# Plot for Scenario 2 (This one worked, but being explicit is good practice)
plot_histogram(counts_observer, ax=ax2)
ax2.set_title("Scenario 2: Observer Effect") # <-- Also set this one manually
ax2.set_xlabel("Outcome")

fig.suptitle("Quantum Double-Slit Experiment Simulation", fontsize=16)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()

print("--- Simulation Complete ---")