# Comunicareasy

An Augmentative and Alternative Communication (AAC) application developed in Python for stroke patients and their caregivers.

## Background
Individuals who suffer recurrent strokes often experience progressive loss of speech (aphasia). They are also frequently left with mobility in only one arm (hemiparesis). Consequently, a simple communication tool helps both patients and their caregivers communicate more easily.

## Project Purpose
To provide a clean, high-contrast, and easy-to-use "tap-to-talk" interface that helps patients with communication difficulties express basic needs, emotions, and everyday phrases quickly and without cognitive friction.

## Technologies Used
- **Language:** Python 3
- **Graphical Interface:** Flet
- **Version Control:** Git and GitHub

## Repository Structure
```text
comunicareasy/
├── models/
│   ├── __init__.py
│   ├── config.example.json
│   └── data_manager.py
├── tests/
│    ├── __init__.py
│    └── test_data_manager.py
├── .gitignore
├── LICENSE                     # Open-source license (MIT)
├── README.md                   # Main project documentation
├── app.py                      # Main application file
└── requirements.txt            # Python dependencies
```

## Local Installation and Execution

Follow these steps to clone and run the project on your machine (using WSL2 Ubuntu or a compatible terminal is recommended):
```bash
# 1. (Optional for Debian/Ubuntu) Ensure python venv support is installed
sudo apt update && sudo apt install python3-venv

# 2. Clone the repository
git clone https://github.com/alfonso-vasconez/comunicareasy.git
cd comunicareasy

# 3. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 4. Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# 5. Run the application
python3 app.py
```


## Roadmap Phases
- [x] Phase 1: Initial environment and repository setup.
- [ ] Phase 2: Base data model design (categories and phrases).
- [ ] Phase 3: Main patient interface (high contrast / tap-to-talk).
- [ ] Phase 4: Configuration panel for caregivers.
- [ ] Phase 5: Testing and usability refinement.

## License
This project is licensed under the MIT License. See the LICENSE file for details.