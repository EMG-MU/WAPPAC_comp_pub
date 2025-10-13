# external_packages/

This folder is reserved for local installation of **custom** or **third-party** Python packages that participants may want to use when developing controllers locally.

**Key points**

- The folder is **empty by default** in the official distribution.
- At runtime, the WAPPAC simulator will make packages placed here importable (the folder name **must** remain exactly `external_packages/`).
- **Do not upload** this folder when submitting to the competition. Instead, provide a `requirements.txt` listing package names and versions (see submission guidelines). The competition organizers will re-create the environment from `requirements.txt` when reproducing your results.
- Install packages locally into this folder during development using:

```bash
python -m pip install --target ./external_packages <package_name>
```
Examples:

```{bash}
python -m pip install --target ./external_packages control
python -m pip install --target ./external_packages cvxpy
```
This keeps your system Python untouched and makes imports available to my_controller.py during local testing.