# NilocasPatch — thesis analysis

Code behind *An exploratory framework for acoustic and vibrational detection of coronary
artery disease* (Silvia Valls Santafe, MSc Biomedical Engineering — AI & Digital Healthcare,
Queen Mary University of London).

One notebook per Results section. Shared plot style and helpers live in `src/style.py`.

```
notebooks/
  01_hardware_testing.ipynb        Figures 9-10   (Section 3.1)
  02_software_pipeline.ipynb       Figures 11-15  (Section 3.2)
  03_healthy_volunteers.ipynb      Table 3, Figures 16-20 (Section 3.3)
  04_supporting_information.ipynb  Figures SI-3, SI-4, SI-5
src/
  style.py                         Colours, matplotlib rcParams, finish_axis(), save_figure()
```

## Setup

```bash
pip install -r requirements.txt
```

Each notebook is self-contained and can be run independently (in order, top to bottom).
Run notebooks from inside the `notebooks/` folder — each one adds `../src` to `sys.path`
to import the shared style module.

## Data

Notebooks read from local folders (frequency-response CSVs, PhysioNet/CinC 2016 data,
volunteer recordings) referenced by absolute paths at the top of each notebook — update
these if your folder layout differs. All generated figures and tables are written to
`~/TFM QMUL/outputs`.
