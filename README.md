# Quantum Double-Slit Experiment Simulation ⚛️

This project provides a Python-based simulation of the renowned quantum double-slit experiment using the **Qiskit** library. It visually demonstrates one of the most fundamental principles of quantum mechanics: **wave-particle duality** and the **observer effect**.

The simulation generates a high-quality, stylized visualization of the two primary scenarios to clearly contrast the outcomes.

## Key Concepts Demonstrated
* **Superposition:** A quantum system's ability to be in multiple states at once, modeled here by a particle passing through both slits simultaneously.
* **Quantum Interference:** How the different paths of a quantum particle can interfere with each other, either constructively (amplifying) or destructively (canceling out).
* **Measurement (The Observer Effect):** The act of measuring a quantum system, which forces it to collapse from a superposition of states into a single, definite state, thereby altering the outcome.

***
## Simulation Results

The main output of the script is a visualization that directly compares the results of running the experiment with and without an "observer."

<img width="1440" height="864" alt="result" src="https://github.com/user-attachments/assets/10b0b295-e86e-453e-8ada-4dc82a7e2061" />


### Interpretation of the Diagram
* **Left Panel (Scenario 1: Interference):** This shows the outcome when the particle's path is not observed. It behaves like a wave, creating a predictable interference pattern. The result is consistently '0', representing constructive interference at a central point.
* **Right Panel (Scenario 2: Observer Effect):** This shows the outcome when we "measure" which slit the particle passes through. The act of observation forces the particle to behave like a classical particle, destroying the interference pattern. The result is a random 50/50 split between '0' and '1', indicating the loss of wave-like behavior.

**A common question is**: how does a bar chart show wave behavior? The diagram doesn't visualize the waves themselves, but rather their **statistical effect**, which is the key evidence.

* In a physical experiment, interfering waves create a pattern of bright and dark bands on a screen. The center band is the brightest due to **constructive interference**.
* In our simulation, we map this physical screen to our qubit's measurement outcomes:
    * **Outcome `0`** represents the central bright band.
    * **Outcome `1`** represents a dark band where waves should cancel out.
* Therefore, the fact that the left panel shows a 100% result of `0` means the particle is *always* found in the location of constructive interference. This perfectly predictable, non-random pattern is the "smoking gun" of wave behavior. The single bar *is* the interference pattern in its simplest statistical form.

***

## ⚙️ Setup and Installation

To run this simulation on your local machine, please follow these steps.

### Prerequisites
* Python 3.8 or later

### Instructions
1.  **Clone the repository (optional):**
    ```bash
    git clone https://github.com/NikaRamin/double-slit-experiment
    cd double-slit-experiment
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # For macOS/Linux
    python3 -m venv .venv
    source .venv/bin/activate

    # For Windows
    python -m venv .venv
    .\.venv\Scripts\activate
    ```

3.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

***

## ▶️ Usage

Once the setup is complete, run the main simulation script from your terminal:
```bash
python main.py
