<img width="1280" height="640" alt="git (1)" src="https://github.com/user-attachments/assets/8920b256-2ba8-4988-b824-5351134eb4bd" />



# Flush Intelligence 🚽


## Basic Details
### Team Name: The Overengineers

### Team Members
DEVIKA N A - [LBSITW]
ARCHANA P U- [LBSITW]


### Project Description
Flush Intelligence is a smart bathroom monitoring system that detects toilet flushes and identifies which stall was used. It tracks flush counts and bathroom usage, detects unusual activity, and visualizes the data through an interactive dashboard. It even features “Bathroom of the Day”, showing which bathroom was loved the most based on its usage!

### The Problem (that doesn't exist)
People use bathrooms every day, but nobody knows which bathroom is loved the most, how many times the toilets were flushed, or which stall is secretly the most popular. There is absolutely no reason to know any of this — so naturally, we decided to build a system that does.

### The Solution (that nobody asked for)

We built Flush Intelligence to solve this extremely unnecessary problem. Our system detects flush events, identifies the stall being used, counts flushes, analyzes bathroom usage, and displays everything on a dashboard. It can even detect unusual usage patterns and crown a “Bathroom of the Day”based on which bathroom gets the most love. 

The system is designed to work with real hardware sensors, but due to limited access to hardware resources and budget constraints, we use Tinkercad to simulate and prototype the hardware setup. This allows us to test our circuit and sensor logic virtually while developing the system toward a real-world hardware implementation.


## Technical Details
### Technologies/Components Used

### Technologies/Components Used

For Software:

* Python — flush signal processing and detection
* Streamlit — interactive dashboard
* NumPy — numerical and signal processing operations
* SciPy — audio and signal processing
* Matplotlib — waveform and data visualization
* Google Colab — software prototyping and testing

For Hardware:

* Arduino Uno — microcontroller for the hardware prototype
* Pushbuttons — simulate flush/sensor inputs
* Breadboard — circuit prototyping
* Jumper wires — electrical connections
* 10 kΩ resistors — pull-down configuration
* Tinkercad Circuits — hardware simulation and testing


### Implementation
For Software:
# Installation
[commands]

# Run
[commands]

### Project Documentation
For Software:

# Screenshots (Add at least 3)
![Screenshot1](Add screenshot 1 here with proper name)
*Add caption explaining what this shows*

![Screenshot2](Add screenshot 2 here with proper name)
*Add caption explaining what this shows*

![Screenshot3](Add screenshot 3 here with proper name)
*Add caption explaining what this shows*

# Diagrams
![Workflow](Add your workflow/architecture diagram here)
*Add caption explaining your workflow*

For Hardware:
### Hardware Prototype Progress

#### Step 1 — Pushbutton 1

We started building the hardware prototype in Tinkercad.

 Pushbutton 1 → Arduino Digital Pin 2
 Proof: [Tinkercad Simulation Video](https://drive.google.com/drive/folders/1CWhYKMVx7-yNj94Xo5vewKT76Qgc5y60?usp=drive_link)
 [stimulation 2](https://drive.google.com/file/d/18HerJWOePKBejCe66i9InhfR-iMavVDB/view?usp=sharing)
#### Step 2 — Pushbutton 2

We continued building the hardware prototype in Tinkercad.
Connection completed:
* Pushbutton 2 → Arduino Digital Pin 3
* Pushbutton 2 triggers a sound to simulate a toilet flush event 🔊🚽

Proof: [Tinkercad Simulation Video](https://drive.google.com/file/d/14jBvCwAIZIHi0gdns5zaElzmxRb5-gZq/view?usp=sharing)
#### Step 3 — Pushbutton 3 & 4

We completed the third and fourth stall sensor connections in Tinkercad.

Connection completed:

* Pushbutton 3 → Arduino Digital Pin 4
* Pushbutton 4 → Arduino Digital Pin 5
* Both pushbuttons produce a sound to simulate toilet flush events 🔊🚽
Proof: [Tinkercad Simulation Video](https://drive.google.com/file/d/15fw68esqFwyvlWp0djq-_-EKHXgFFyCQ/view?usp=sharing)
#### Step 4 — Pushbutton Testing

We tested the completed Tinkercad circuit by pressing each pushbutton individually. Each pushbutton successfully responds to the press and produces the corresponding sound, simulating a toilet flush event.

Proof: [Tinkercad Simulation Video](https://drive.google.com/file/d/1XltzRQgSeol6pA4y5ujIOkkRmNsDZdIa/view?usp=sharing)

#### Step 4 — Pushbutton Testing

We tested the completed Tinkercad hardware prototype by pressing each pushbutton individually. Each pushbutton successfully detected a flush event and produced a corresponding buzzer sound.

The Arduino also identifies the specific stall and records the number of flushes through the Serial Monitor.

Testing completed:

* Pushbutton 1 → Stall 1 → Arduino Digital Pin 2
* Pushbutton 2 → Stall 2 → Arduino Digital Pin 3
* Pushbutton 3 → Stall 3 → Arduino Digital Pin 4
* Pushbutton 4 → Stall 4 → Arduino Digital Pin 5
* Piezo buzzer → Arduino Digital Pin 8
* Buttons use Arduino `INPUT_PULLUP`
* Each detected flush increases the corresponding stall's flush count
* Serial Monitor displays the stall number and flush count
* Piezo buzzer provides an audible indication of the flush event 🔊🚽
[full simulation video](https://drive.google.com/file/d/1hyJCwk_XhaXgOq9hyY4OLtAyCjNtCKi3/view?usp=sharing)

[Tinkercad](https://www.tinkercad.com/things/7oXE79eQFHA-flush-inntelligence-hardware-prototype?sharecode=Jtvme0ySVaiBGOZ6NoaRBKA5bJR-Nzc0kUlBXu_JcpE)


# Schematic & Circuit
![Circuit](Add your circuit diagram here)
*Add caption explaining connections*

![Schematic](Add your schematic diagram here)
*Add caption explaining the schematic*

# Build Photos
![Components](Add photo of your components here)
*List out all components shown*

![Build](Add photos of build process here)
*Explain the build steps*

![Final](Add photo of final product here)
*Explain the final build*

### Project Demo
# Video
[Add your demo video link here]
*Explain what the video demonstrates*

# Additional Demos
[Add any extra demo materials/links]

## Team Contributions
- [Name 1]: [Specific contributions]
- [Name 2]: [Specific contributions]
- [Name 3]: [Specific contributions]

---
Made with ❤️ at TinkerHub Useless Projects 

![Static Badge](https://img.shields.io/badge/TinkerHub-24?color=%23000000&link=https%3A%2F%2Fwww.tinkerhub.org%2F)
![Static Badge](https://img.shields.io/badge/UselessProjects--26-26?link=https%3A%2F%2Ftinkerhub.org%2Fevents%2F1M8ORET9A1%2Fuseless-projects-3.0)



