import matplotlib.pyplot as plt
from qiskit.circuit import QuantumCircuit
from qiskit import transpile
from qiskit_aer import AerSimulator

# --- Simulation Logic (to get the data) ---
simulator = AerSimulator()
SHOTS = 2048 # Number of times to run the experiment

# Scenario 1: Interference (No Observer)
qc_interference = QuantumCircuit(1, 1)
qc_interference.h(0)
qc_interference.h(0)
qc_interference.measure(0, 0)
counts_interference = simulator.run(transpile(qc_interference, simulator), shots=SHOTS).result().get_counts()

# Scenario 2: Observer Effect
qc_observer = QuantumCircuit(2, 1)
qc_observer.h(0)
qc_observer.cx(0, 1)
qc_observer.h(0)
qc_observer.measure(0, 0)
counts_observer = simulator.run(transpile(qc_observer, simulator), shots=SHOTS).result().get_counts()

# --- Infographic Plotting ---
BG_COLOR = '#1A233B'
TEXT_COLOR = '#EAEAF2'
BAR_BLUE = '#00BFFF'
BAR_ORANGE = '#FF8C00'
BAR_GREEN = '#32CD32'
GRID_COLOR = '#4A5568'
plt.style.use('dark_background')
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Helvetica', 'Arial']
plt.rcParams['text.color'] = TEXT_COLOR
plt.rcParams['axes.labelcolor'] = TEXT_COLOR
plt.rcParams['xtick.color'] = TEXT_COLOR
plt.rcParams['ytick.color'] = TEXT_COLOR
plt.rcParams['axes.facecolor'] = BG_COLOR
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 10))
fig.set_facecolor(BG_COLOR)

# --- Panel 1: Interference (No Observer) ---
x_keys_interference = ['0']
y_values_interference = [counts_interference.get('0', 0)]
bars1 = ax1.bar(x_keys_interference, y_values_interference, color=BAR_BLUE, width=0.6)
ax1.set_title("SCENARIO 1: INTERFERENCE (NO OBSERVER)", fontsize=16, fontweight='bold', pad=30)
ax1.set_ylim(0, SHOTS * 1.2)
ax1.set_ylabel("Counts", fontsize=12, labelpad=15)
ax1.set_xlabel("MEASURED OUTCOME", fontsize=12, labelpad=15)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['left'].set_color(GRID_COLOR)
ax1.spines['bottom'].set_color(GRID_COLOR)
ax1.grid(axis='y', color=GRID_COLOR, linestyle='-', linewidth=0.4, alpha=0.7)
ax1.text(0, -SHOTS * 0.2, "WAVE-LIKE BEHAVIOR", ha='center',
         bbox=dict(boxstyle="round,pad=0.5", fc='white', ec="none", alpha=0.9), color=BG_COLOR, fontweight='bold', fontsize=12)
ax1.text(0, SHOTS * 0.95, "CONSTRUCTIVE\nINTERFERENCE", ha='center', va='top',
         bbox=dict(boxstyle="round,pad=0.5", fc='white', ec="none", alpha=0.9), color=BG_COLOR, fontweight='bold', fontsize=12)
for bar in bars1:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2.0, yval + (SHOTS * 0.03), int(yval), ha='center', va='bottom', color=TEXT_COLOR, fontsize=12)

# --- Panel 2: Observer Effect ---
labels2 = ['0', '1']
values2 = [counts_observer.get('0', 0), counts_observer.get('1', 0)]
colors2 = [BAR_ORANGE, BAR_GREEN]
bars2 = ax2.bar(labels2, values2, color=colors2, width=0.6)
ax2.set_title("SCENARIO 2: OBSERVER EFFECT", fontsize=16, fontweight='bold', pad=30)
ax2.set_ylim(0, SHOTS * 1.2)
ax2.set_xlabel("MEASURED OUTCOME", fontsize=12, labelpad=15)
ax2.set_ylabel("Counts", fontsize=12, labelpad=15)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.spines['left'].set_color(GRID_COLOR)
ax2.spines['bottom'].set_color(GRID_COLOR)
ax2.grid(axis='y', color=GRID_COLOR, linestyle='-', linewidth=0.4, alpha=0.7)
ax2.text(0.5, -SHOTS * 0.2, "PARTICLE-LIKE BEHAVIOR", ha='center',
         bbox=dict(boxstyle="round,pad=0.5", fc='white', ec="none", alpha=0.9), color=BG_COLOR, fontweight='bold', fontsize=12)
ax2.text(0.5, SHOTS * 0.95, "RANDOM OUTCOME", ha='center', va='top',
         bbox=dict(boxstyle="round,pad=0.5", fc='white', ec="none", alpha=0.9), color=BG_COLOR, fontweight='bold', fontsize=12)
for bar in bars2:
    yval = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2.0, yval + (SHOTS * 0.03), int(yval), ha='center', va='bottom', color=TEXT_COLOR, fontsize=12)


# --- Main Titles & Final Layout Adjustment ---
fig.text(0.5, 0.95, "QUANTUM DOUBLE-SLIT EXPERIMENT: WAVE VS. PARTICLE",
         ha='center', va='bottom', fontsize=24, fontweight='bold', color=TEXT_COLOR)
fig.text(0.5, 0.85, "Visualizing how observation collapses the quantum wave function",
         ha='center', va='bottom', fontsize=16, style='italic', color='#B0C4DE')
plt.subplots_adjust(top=0.85, bottom=0.15, left=0.08, right=0.95, wspace=0.3)

plt.show()