# WAPPAC Simulation Platform

Welcome to the official repository for the **WavePiston Passive Control (WAPPAC) Competition** developed by the **Centre for Ocean Energy Research (COER)** at Maynooth University.


## Documentation
Full competition rules, controller submission guidelines, and evaluation procedures are detailed on the official documentation site:

  [WAPPAC Documentation Portal](https://emg-mu.github.io/WAPPAC_docs/home.html)

---

## Repository Contents
The repository contains the **template files** and **model data** required for developing and testing control strategies for the WAPPAC benchmark problem.

| Folder / File | Description |
| :------------- | :----------- |
| `model_data/` | Contains hydrodynamic model data and parameters used by the simulator |
| `my_controller.py` | Example controller template file |
| `my_sim_input_file.json` | Example simulation input configuration |
| `control_helpers/` | *(Optional)* Folder for user-defined helper modules used by controllers |
| `external_packages/` | Local folder for installing third-party Python packages (empty by default) |
| `.gitignore` | Ensures large or local-only folders (e.g., `external_packages/`) are not tracked |

---

## Getting WAPPAC Simulation Platform

The simulator is distributed as **self-contained executables** for Windows and Linux, available under the [Releases](https://github.com/EMG-MU/WAPPAC_comp_pub/releases) section.

Each release ZIP contains:
- Precompiled binaries for both operating systems  
- Full source code snapshot  
- Example controller and model data  
- Usage instructions (`README_release.md`)

Download the latest release and extract it locally to start testing your controller.

---

## Contact

For competition or platform-related questions, please contact the COER team via the official channels listed in the documentation.

---

© 2025 COER – Maynooth University. All rights reserved.

```
