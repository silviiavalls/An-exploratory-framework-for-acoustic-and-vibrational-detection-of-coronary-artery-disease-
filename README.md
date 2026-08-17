# NilocasPatch — thesis analysis

[![Python](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/)

Analysis code accompanying the MSc thesis:

> **An exploratory framework for acoustic and vibrational detection of coronary artery disease**
> Silvia Valls Santafe · MSc Biomedical Engineering — Artificial Intelligence & Digital Healthcare
> Queen Mary University of London, 2026

The NilocasPatch is a wearable multi-sensor chest patch (microphones + accelerometers) developed
to support non-invasive pre-screening of coronary artery disease. This repository contains the
complete signal-processing, statistical and machine-learning pipeline used to produce every
figure and table in the Results section of the thesis.

## Repository structure

One notebook per Results section, plus a shared style module:

| File | Contents | Thesis section |
|---|---|---|
| `notebooks/01_hardware_testing.ipynb` | Figures 9–10 | Section 3.1 |
| `notebooks/02_software_pipeline.ipynb` | Figures 11–15 | Section 3.2 |
| `notebooks/03_healthy_volunteers.ipynb` | Table 3, Figures 16–20 | Section 3.3 |
| `notebooks/04_supporting_information.ipynb` | Figures SI-3, SI-4, SI-5 | Supporting Information |
| `src/style.py` | Shared colours, `matplotlib` settings, `finish_axis()`, `save_figure()` | — |

## Setup

```bash
pip install -r requirements.txt
```

Each notebook is self-contained and can be run independently, top to bottom. Run them from
inside the `notebooks/` folder — each one adds `../src` to `sys.path` to import the shared
style module.

## Data availability

This repository contains **analysis code only**. Raw data are not included:

- **Frequency-response and hardware characterisation data** are available from the corresponding
  author on reasonable request.
- **Healthy-volunteer recordings** were collected under Queen Mary Ethics of Research Committee
  approval (QMERC25.1523) and are not publicly shared, in line with the participant consent
  obtained for this study.
- **PhysioNet/CinC 2016 data** are third-party data and should be obtained directly from
  [PhysioNet](https://physionet.org/content/challenge-2016/).

To reproduce the figures, place your own copies of these datasets in the folders referenced at
the top of each notebook (or edit those paths to match your local setup). Generated figures and
tables are written to `~/TFM QMUL/outputs`.

## Citation

If you use this code, please cite:

> Valls Santafe, S. (2026). *An exploratory framework for acoustic and vibrational detection of
> coronary artery disease* [MSc thesis, Queen Mary University of London].

## Author

Silvia Valls Santafe — MSc Biomedical Engineering (AI & Digital Healthcare), Queen Mary University of London
Supervised by Prof. Zion Tse, Prof. Steve Greenwald, Prof. Simon Shaw, and Fangze Peng.
