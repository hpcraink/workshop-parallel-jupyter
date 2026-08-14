<img src="https://www.bwhpc.de/assets/img/Logo_KIT_en.png" alt="KIT" width="150"> <img src="https://github.com/hpcraink/workshop-parallel-jupyter/blob/main/images/HochschuleEsslingen_Logo_RGB_DE.png" alt="Hochschule Esslingen" width="200"> <img src="images/Konstanz_Logo.svg" alt="Universität Konstanz" width="200">

# Workshop Parallel Jupyter

An applied introduction to scientific computing with Python on high performance
computing systems, delivered entirely through Jupyter notebooks.

The material begins with the fundamentals of the language and progresses to
machine learning, deep learning on GPU hardware, and distributed computation across
multiple compute nodes using Dask. Each chapter is a directory of notebooks intended
to be executed by the participant on real datasets, within a JupyterLab session
running on the cluster.

## Contents

| Chapter | Subject |
|---|---|
| **01_Getting_Started** | Launching a JupyterLab job |
| **02_Python_Fundamentals** | Data types, control structures, functions, classes, exceptions and virtual environments, across six notebooks |
| **03_NumPy** | Arrays and vectorised operations, and the reasons to prefer them over explicit iteration |
| **04_Pandas** | DataFrames and Series, followed by an exploratory analysis of the Titanic dataset |
| **05_Data_Visualization** | A single dataset presented through three libraries: hvPlot, Matplotlib and Plotly |
| **06_Machine_Learning** | Supervised learning (regression, cross-validation, grid search) and unsupervised learning (k-means clustering, principal component analysis) |
| **07_Natural_Language_Processing** | Sentiment classification of Amazon product reviews |
| **08_Deep_Learning** | Neural networks in **TensorFlow** (classification, regression, convolutional networks, autoencoders), and the equivalent concepts in **PyTorch**, implemented from first principles and then refactored step by step |
| **09_Dask** | Scaling beyond a single machine: parallel dataframes and a Dask cluster distributed over several compute nodes |

The chapters are cumulative and are best followed in sequence, although each
individual notebook is self-contained and may be executed independently.

## Prerequisites

1. **An account on a bwHPC system.** Participants must be
   [registered](https://wiki.bwhpc.de/e/Registration) on a bwHPC cluster prior to the
   workshop.

2. **An active JupyterLab job.** The notebooks are intended to be opened in
   JupyterLab *on the cluster*. On the bwUniCluster,
   the [`01_Getting_Started`](01_Getting_Started) notebook documents how this job is
   submitted. On other systems, the
   [site-specific instructions](https://wiki.bwhpc.de/e/Python) should be followed
   instead.

**Python 3.11 or later is recommended.** The deep learning chapters depend on recent
releases of TensorFlow and PyTorch, neither of which supports earlier versions of the
interpreter.

## Quick Start

The environment is managed with [`uv`](https://docs.astral.sh/uv/). Exact package
versions are recorded in `uv.lock`, which ensures that every participant obtains an
identical environment — on the cluster, on a local machine, or in continuous
integration — and which `uv` resolves and installs in seconds rather than minutes.

**1. Clone the repository and enter it**

```bash
git clone https://github.com/hpcraink/workshop-parallel-jupyter.git
cd workshop-parallel-jupyter
```

**2. Install uv**, if it is not already available

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**3. Create the environment**

```bash
uv sync
```

This reads `pyproject.toml` and `uv.lock` and constructs a `.venv` directory
containing every package required by the notebooks.

**4. Register the environment as a Jupyter kernel**

```bash
uv run python -m ipykernel install --user \
    --name workshop --display-name "Workshop"
```

**5. Select the kernel.** Open any notebook in JupyterLab and choose **Workshop**
from the kernel selector in the upper right. Should the entry not appear
immediately, reload the page.

**6. Verify the environment (optional)**

```bash
uv run python scripts/test_environment.py
```

This collects every import statement occurring in the notebooks and confirms that
the environment satisfies each one. The same verification is performed automatically
by GitHub Actions whenever the notebooks or the declared dependencies are modified.

## Further documentation

The [bwHPC Wiki](https://wiki.bwhpc.de/) documents the clusters themselves,
including registration, job submission, available software modules and
site-specific guidance.
