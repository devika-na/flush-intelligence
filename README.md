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

Flush Intelligence is a smart acoustic toilet monitoring system that detects flush events, identifies the stall being used using acoustic/TDOA-based localization, records flush history, detects unusual usage patterns, and displays the data through a Streamlit dashboard.

The hardware prototype is simulated using Tinkercad Arduino, while Google Colab/Python is used for acoustic processing, event analysis, data storage, and dashboard generation.

## Technologies/Components Used

### For Software:

- **Python** — flush audio processing, detection, and stall localization
- **NumPy** — numerical and signal processing operations
- **SciPy** — cross-correlation and signal processing
- **Librosa** — audio loading and analysis
- **Matplotlib** — waveform and signal visualization
- **Streamlit** — interactive monitoring dashboard
- **Google Colab** — software prototyping and testing

### For Hardware:

- Arduino Uno — microcontroller for the hardware prototype
- Pushbuttons (4) — simulate flush events for four toilet stalls
- Piezo Buzzer — provides an audible indication of a detected flush
- Breadboard — circuit prototyping
- Jumper Wires— electrical connections
- Arduino INPUT_PULLUP— internal pull-up configuration for pushbuttons
- Tinkercad Circuits — hardware simulation and testing

### Implementation
For Software:
# Installation
pip install librosa soundfile numpy pandas scipy streamlit

# Run
jupyter notebook

Then run the project notebook cells.

To launch the dashboard:

streamlit run app.py

### Project Documentation
For Software:
https://drive.google.com/file/d/1yvzuEcwOqSCpPZ26XCOOslpef8Ys8vmx/view?usp=sharing

# Screenshots (Add at least 3)
<img width="1600" height="766" alt="1" src="https://github.com/user-attachments/assets/67b700f5-cc58-4b75-9bb1-0bca1e11750f" />
<img width="1600" height="711" alt="2" src="https://github.com/user-attachments/assets/9c6b3bc5-8f90-4b5b-b622-b634ab86db3c" />
<img width="1600" height="789" alt="3" src="https://github.com/user-attachments/assets/ed72ef7a-9c75-48e7-83dd-d743ce1f15c4" />
<img width="1600" height="696" alt="4" src="https://github.com/user-attachments/assets/d1bcc4d5-e1b1-4a5b-a4b2-834192b95df0" />




# Diagrams
FLUSH INTELLIGENCE – SOFTWARE WORKFLOW

                         FLUSH SOUND / EVENT
                                │
                                ▼
                     ┌─────────────────────┐
                     │   DATA ACQUISITION  │
                     │ Acoustic Audio +    │
                     │ Arduino Event       │
                     └──────────┬──────────┘
                                │
                                ▼
                     ┌─────────────────────┐
                     │   PRE-PROCESSING    │
                     │ RMS Energy + FFT    │
                     │ Audio Processing    │
                     └──────────┬──────────┘
                                │
                                ▼
                     ┌─────────────────────┐
                     │  FLUSH DETECTION    │
                     │ Energy Thresholding │
                     └──────────┬──────────┘
                                │
                                ▼
                     ┌─────────────────────┐
                     │ STALL LOCALIZATION  │
                     │ TDOA + Cross        │
                     │ Correlation         │
                     └──────────┬──────────┘
                                │
                                ▼
                     ┌─────────────────────┐
                     │   EVENT PROCESSING  │
                     │ Timestamp + Stall   │
                     │ ID + Flush Count    │
                     └──────────┬──────────┘
                                │
                    ┌───────────┴───────────┐
                    ▼                       ▼
          ┌──────────────────┐    ┌──────────────────┐
          │ ANOMALY          │    │ DATA STORAGE     │
          │ DETECTION        │    │ CSV / History    │
          └────────┬─────────┘    └────────┬─────────┘
                   └────────────┬───────────┘
                                ▼
                     ┌─────────────────────┐
                     │ STREAMLIT DASHBOARD │
                     │ • Flush Counts      │
                     │ • Stall Usage       │
                     │ • Alerts            │
                     │ • Bathroom of Day   │
                     │ • Flush Sound       │
                     └──────────┬──────────┘
                                │
                                ▼
                     ┌─────────────────────┐
                     │ REPORT / INSIGHTS   │
                     │ CSV Export & Usage  │
                     │ Analysis            │
                     └─────────────────────┘

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

#### Step 5 — Complete Hardware Prototype

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
FLUSH INTELLIGENCE – HARDWARE CIRCUIT

                         ┌─────────────────┐
                         │   ARDUINO UNO   │
                         └───────┬─────────┘
                                 │
             ┌───────────────────┼───────────────────┐
             │                   │                   │
             ▼                   ▼                   ▼
        ┌─────────┐         ┌─────────┐        ┌─────────┐
        │ STALL 1 │         │ STALL 2 │        │ STALL 3 │
        │ BUTTON  │         │ BUTTON  │        │ BUTTON  │
        │   D2    │         │   D3    │        │   D4    │
        └────┬────┘         └────┬────┘        └────┬────┘
             │                   │                   │
             └───────────────────┼───────────────────┘
                                 │
                           ┌─────▼─────┐
                           │  STALL 4  │
                           │  BUTTON   │
                           │    D5     │
                           └───────────┘

                         D8 ───────► (+) PIEZO
                                    BUZZER
                         GND ──────► (−)

        All pushbuttons use Arduino INPUT_PULLUP
        Button press → Arduino detects flush → Serial Event

        The hardware prototype uses an Arduino Uno with four pushbuttons representing four toilet stalls. Each button is connected to a digital input (D2–D5) using INPUT_PULLUP. When a flush is simulated, Arduino detects the corresponding stall and sends a serial event, while a piezo buzzer provides an audio indication.

# Build Photos
<img width="1915" height="928" alt="TINTIN" src="https://github.com/user-attachments/assets/59a3b243-a277-4a94-bd19-50858b97d34b" />
- Arduino Uno — microcontroller for the hardware prototype
- Pushbuttons (4) — simulate flush events for four toilet stalls
- Piezo Buzzer — provides an audible indication of a detected flush
- Breadboard — circuit prototyping
- Jumper Wires— electrical connections
- Arduino INPUT_PULLUP— internal pull-up configuration for pushbuttons
- Tinkercad Circuits — hardware simulation and testing

![Build](Add photos of build process here)
*Explain the build steps*

<img width="941" height="740" alt="Screenshot 2026-09-03 234759" src="https://github.com/user-attachments/assets/db3ac694-9d9b-4737-b054-baad7e28a6ad" />

The completed prototype contains four pushbuttons representing four toilet stalls, an Arduino Uno for processing the inputs, and a piezo buzzer for audible flush feedback. The system identifies the stall associated with each flush and maintains the corresponding flush count through the Serial Monitor.

### Project Demo
# Video
[Add your demo video link here]
*Explain what the video demonstrates*

# Additional Demos
[Add any extra demo materials/links]

## Team Contributions

Devika N A: Developed the Google Colab software prototype, including flush signal processing, detection, stall identification. Also managed the GitHub repository, README documentation, and project integration.

  Archana P U: Developed and tested the Tinkercad hardware prototype, including the Arduino, pushbuttons, piezo buzzer, stall inputs, and flush-counting logic. Also contributed to the GitHub repository and documentation,

Both Team Members: Worked together to integrate the software and hardware components, test the complete system, connect the different parts of the project, and prepare the final project documentation and demonstration.

---
Made with ❤️ at TinkerHub Useless Projects 

![Static Badge](https://img.shields.io/badge/TinkerHub-24?color=%23000000&link=https%3A%2F%2Fwww.tinkerhub.org%2F)
![Static Badge](https://img.shields.io/badge/UselessProjects--26-26?link=https%3A%2F%2Ftinkerhub.org%2Fevents%2F1M8ORET9A1%2Fuseless-projects-3.0)



