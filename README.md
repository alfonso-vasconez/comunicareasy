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
├── src/
│   ├── assets/              
│   ├── models/                     # Data management and user data template (data_manager.py, etc.)
│   │   ├── __init__.py
│   │   ├── config.example.json
│   │   └── data_manager.py
│   └── main.py                     # App
├── tests/
│   ├── __init__.py
│   └── test_data_manager.py
├── .gitignore
├── LICENSE
├── README.md
└── pyproject.toml
```

## Local Installation and Execution

Install Git and Python 3.10 or newer before starting. On Windows, install Python from
[python.org](https://www.python.org/downloads/) with the Python launcher enabled.
On macOS and Linux, use a Python 3.10+ installation.

Open a terminal in the folder where you want the project, then run:

```text
git clone https://github.com/alfonso-vasconez/comunicareasy.git
cd comunicareasy
```

Then follow **only** the instructions for your operating system and terminal.
Run each command from the `comunicareasy` folder.

### Windows (PowerShell)

These commands use the virtual environment's Python directly, so activation and
PowerShell execution-policy changes are not needed:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe app.py
```

### macOS or Linux (Bash or Zsh)

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python app.py
```

The final command starts Comunicareasy. Keep the terminal open while using the
application. If `python3 -m venv .venv` reports that `venv` is unavailable on
Debian or Ubuntu, install it with `sudo apt install python3-venv` and repeat the
setup commands.


## Roadmap Phases
- [x] Phase 1: Initial environment and repository setup.
- [ ] Phase 2: Base data model design (categories and phrases).
- [ ] Phase 3: Main patient interface (high contrast / tap-to-talk).
- [ ] Phase 4: Configuration panel for caregivers.
- [ ] Phase 5: Testing and usability refinement.

## License
This project is licensed under the MIT License. See the LICENSE file for details.