# WAPPAC Simulation Platform

Welcome to the official repository for the **WavePiston Passive Control (WAPPAC) Competition** developed by the **Centre for Ocean Energy Research (COER)** at Maynooth University.


## Documentation
Full competition rules, controller submission guidelines, and evaluation procedures are detailed on the official documentation site:

  [WAPPAC Documentation Portal](https://emg-mu.github.io/WAPPAC_docs/home.html)

---

## Getting WAPPAC Simulation Platform

The simulator is distributed as **self-contained executables** for Windows and Linux, available after registering via the following [form](https://docs.google.com/forms/d/e/1FAIpQLScfgXSWWg5eI0pRg2_jd_cX82W4DifeaOzrqx5pv14d5TWwPQ/viewform).

Each release ZIP contains:
- Precompiled binaries for both operating systems  
- Full source code snapshot  
- Example controller and model data  

Download the latest release and extract it locally to start testing your controller.

---

## Repository Contents
The repository contains the **template files** and **model data** required for developing and testing control strategies for the WAPPAC benchmark problem. Note that the WAPPAC binaries are not included in the repository due to their size; they are available as a GitHub release as specified above.

| Folder / File | Description |
| :------------- | :----------- |
| `model_data/` | Contains hydrodynamic model data and parameters used by the simulator |
| `my_controller.py` | Example controller template file |
| `my_sim_input_file.json` | Example simulation input configuration |
| `control_helpers/` | *(Optional)* Folder for user-defined helper modules used by controllers |
| `external_packages/` | Local folder for installing third-party Python packages (empty by default) |
| `.gitignore` | Ensures large or local-only folders (e.g., `external_packages/`) are not tracked |

---

## Contact

For competition or platform-related questions, or if having any issues while registering and obtaining the WAPPAC simulation platform, please contact the COER team via the following official channels:

  Email: eugenio.gelos@mu.ie - colm.fitzgerald@mu.ie

Use this address for technical assistance, bug or security reports, and formal competition-related inquiries.

---

© 2025 COER – Maynooth University.
```
