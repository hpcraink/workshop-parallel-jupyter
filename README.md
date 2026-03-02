<img src="https://www.bwhpc.de/assets/img/Logo_KIT_en.png" alt="KIT" width="150"> <img src="https://github.com/hpcraink/workshop-parallel-jupyter/blob/main/images/HochschuleEsslingen_Logo_RGB_DE.png" alt="Hochschule Esslingen" width="200"> <img src="images/Konstanz_Logo.svg" alt="Universität Konstanz" width="200">

# Workshop Parallel Jupyter
Additional documentation can be found in the bwHPC Wiki: [Python](https://wiki.bwhpc.de/e/Python)

## Prerequisites

Participants must have already completed these basics:
* Being [registered](https://wiki.bwhpc.de/e/Registration) on a bwHPC cluster. 
* For later practice, X11 access is needed. To enable this, please follow the login instructions of your respective cluster.
* If you are not using the bwUniCluster, you can skip the "1_Start" notebook where the JupyterLab job is set up. You can use [instructions of your specific cluster](https://wiki.bwhpc.de/e/Python) instead.

## Quick Start
This workshop uses a modern Python environment managed with `uv`. To get started:

1. **Install uv** (if not already installed):
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Set up the environment**:
   ```bash
   uv sync
   ```

3. **Test the environment**:
   ```bash
   uv run python scripts/test_environment.py
   ```

4. **Start Jupyter**:
   ```bash
   uv run jupyter lab
   ```

## Environment Testing

The environment is automatically tested via GitHub Actions whenever dependencies change. You can also test locally:

- Test all imports: `uv run python scripts/test_environment.py`
- Verify notebooks: All notebooks are automatically validated for syntax
