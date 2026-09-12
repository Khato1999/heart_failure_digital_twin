# heart-failure-digital-twin


A research platform that combines:

- EchoNet-Dynamic echocardiography AI
- Left ventricular segmentation
- Ejection Fraction (EF) estimation
- End-Diastolic Volume (EDV) estimation
- End-Systolic Volume (ESV) estimation
- Patient-specific cardiovascular Digital Twin simulation
- Interactive Streamlit interface
- What-if physiological scenario analysis

---

## Project Overview

The application uses echocardiography imaging to estimate cardiac function and initialize a patient-specific cardiovascular Digital Twin.

### Workflow

```text
DICOM Echocardiography Study
                │
                ▼
      DICOM → AVI Conversion
                │
                ▼
        EchoNet-Dynamic
       (Segmentation AI)
                │
                ▼
           EDV / ESV
                │
                ▼
        EchoNet-Dynamic
        (EF Prediction AI)
                │
                ▼
         Patient Profile
                │
                ▼
    Cardiovascular Digital Twin
                │
                ▼
      What-If Scenario Analysis
```

---

# Disclaimer

This software is intended for:

- Research
- Education
- Method development
- Software engineering

This software is **NOT** a medical device and must **NOT** be used for:

- Clinical diagnosis
- Clinical decision support
- Treatment planning
- Patient management

---

# Repository Structure

```text
heart_failure_digital_twin/
│
├── app.py
├── setup.py
├── conftest.py
├── README.md
│
├── outputs/
│
├── scripts/
│   ├── build_cohort.py
│   ├── download_echonet.py
│   ├── inspect_echo_study.py
│   ├── train_volume_estimation.py
│   └── validate_echo_dataset.py
│
├── src/
│   └── heart_twin/
│       ├── __init__.py
│       ├── cohort.py
│       ├── echonet_integration.py
│       ├── imaging.py
│       ├── patient.py
│       ├── physiology.py
│       └── twin.py
│
├── tests/
│
├── reference/
│   └── original_echonet/
│       ├── InitializationNotebook.ipynb
│       ├── ConvertDICOMToAVI.ipynb
│       ├── beat_by_beat_analysis.R
│       └── ...
│
└── vendor/
    └── echonet_dynamic/
        ├── datasets/
        │   ├── __init__.py
        │   └── echo.py
        │
        ├── utils/
        │   ├── __init__.py
        │   ├── segmentation.py
        │   └── video.py
        │
        ├── __init__.py
        ├── __main__.py
        ├── __version__.py
        └── config.py
```

---

# Digital Twin Components

## Imaging Layer

Responsible for:

- DICOM processing
- AVI conversion
- Echo metadata extraction
- EchoNet integration
- Volume estimation

Files:

```text
src/heart_twin/imaging.py
src/heart_twin/echonet_integration.py
```

---

## Patient Layer

Responsible for:

- Input validation
- Volume handling
- EF consistency checks
- Teichholz volume estimation

Files:

```text
src/heart_twin/patient.py
```

---

## Physiology Layer

Responsible for:

- Closed-loop cardiovascular simulation
- Pressure-volume relationships
- Heart failure physiology
- Stroke volume calculation
- Cardiac output estimation

Files:

```text
src/heart_twin/physiology.py
```

---

## Twin Layer

Responsible for:

- Twin initialization
- Parameter calibration
- Emax estimation
- Scenario simulation

Files:

```text
src/heart_twin/twin.py
```

---

# EchoNet-Dynamic

The project uses:

**EchoNet-Dynamic: Interpretable AI for Beat-to-Beat Cardiac Function Assessment**

Official repository:

https://github.com/echonet/dynamic

Official project page:

https://echonet.github.io/dynamic/

Paper:

Ouyang D, He B, Ghorbani A, et al.
Video-based AI for beat-to-beat assessment of cardiac function.
Nature. 2020.

---

# Dataset Access

The EchoNet-Dynamic dataset is publicly available for research use.

Dataset portal:

https://echonet.github.io/dynamic/

Dataset request:

https://stanfordaimi.azurewebsites.net/datasets/echonet-dynamic

Project website:

https://echonet.github.io/dynamic/

---

# Downloading the Dataset

After receiving access, download:

```text
FileList.csv
VolumeTracings.csv
Videos/
```

Expected structure:

```text
EchoNet-Dynamic/

├── FileList.csv
├── VolumeTracings.csv
│
└── Videos/
    ├── XXXX.avi
    ├── YYYY.avi
    └── ...
```

---

# Environment Setup

Recommended:

```text
Python 3.10
```

The original EchoNet repository was created using older Python and PyTorch releases.

Python 3.13 may require dependency updates.

---

## Create Environment

### Windows

```powershell
python -m venv .venv
.venv\Scripts\activate
```

### Linux / macOS

```bash
python -m venv .venv
source .venv/bin/activate
```

---

# Install Dependencies

```bash
pip install torch torchvision

pip install numpy
pip install pandas
pip install scipy

pip install scikit-image
pip install scikit-learn

pip install matplotlib

pip install opencv-python

pip install pydicom

pip install imageio
pip install imageio-ffmpeg

pip install tqdm

pip install click

pip install pillow

pip install streamlit
```

---

# Install EchoNet

Clone the official repository:

```bash
git clone https://github.com/echonet/dynamic.git
```

Install:

```bash
cd dynamic

pip install -e .
```

Verify:

```bash
python -c "import echonet; print(echonet.__file__)"
```

---

# Download Pretrained Models

Required pretrained models:

## EF Prediction

```text
r2plus1d_18_32_2_pretrained.pt
```

## Segmentation

```text
deeplabv3_resnet50_random.pt
```

Store them in:

```text
weights/

├── r2plus1d_18_32_2_pretrained.pt
└── deeplabv3_resnet50_random.pt
```

---

# Running EchoNet

## Converting DICOM to AVI

Use:

```text
reference/original_echonet/ConvertDICOMToAVI.ipynb
```

Workflow:

```text
DICOM Study
      │
      ▼
ConvertDICOMToAVI.ipynb
      │
      ▼
     AVI
```

---

## Running Inference

Use:

```text
reference/original_echonet/InitializationNotebook.ipynb
```

Update:

```python
videosFolder = "path/to/avi/videos"
```

Run all notebook cells.

Outputs include:

```text
EF predictions
LV segmentation masks
size.csv
beat-level predictions
```

---

# Running the Digital Twin Application

Start Streamlit:

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

Workflow:

```text
Upload Echo Study
        │
        ▼
Run EchoNet
        │
        ▼
Extract
  - EF
  - EDV
  - ESV
        │
        ▼
Create Patient Twin
        │
        ▼
Run Simulations
```

---

# Validating an EchoNet Dataset

Run:

```bash
python scripts/validate_echo_dataset.py
```

The script validates:

- FileList.csv
- VolumeTracings.csv
- AVI files
- Dataset consistency

---

# Building a Cohort

Run:

```bash
python scripts/build_cohort.py
```

Generates:

```text
outputs/cohort/
```

for downstream analysis.

---

# Inspecting a Study

Run:

```bash
python scripts/inspect_echo_study.py
```

This verifies:

- video readability
- frame count
- dimensions
- metadata

before inference.

---

## Train Segmentation Model

```bash
python -m echonet.utils.segmentation \
    --data_dir path/to/EchoNet-Dynamic
```

Outputs:

```text
checkpoint.pt
best.pt
```

---

## Train EF Prediction Model

```bash
python -m echonet.utils.video \
    --data_dir path/to/EchoNet-Dynamic
```

Outputs:

```text
checkpoint.pt
best.pt
```

Training typically requires:

```text
NVIDIA GPU
CUDA
Several hours
```

---


# Data Sources

This project uses two primary research datasets.

## 1. EchoNet-Dynamic

Purpose:

- LV segmentation
- EF prediction
- Video-based cardiac assessment

Website:

https://echonet.github.io/dynamic/

Dataset:

https://stanfordaimi.azurewebsites.net/datasets/echonet-dynamic

Repository:

https://github.com/echonet/dynamic

---

## 2. Zigong Heart Failure Cohort

Purpose:

- Heart failure patient characteristics
- Clinical research
- Digital Twin population analysis

Dataset:

https://physionet.org/content/heart-failure-zigong/1.3/


---

# References

Ouyang D, He B, Ghorbani A, et al.

Video-based AI for beat-to-beat assessment of cardiac function.

Nature. 2020.

EchoNet-Dynamic Repository:

https://github.com/echonet/dynamic

EchoNet-Dynamic Dataset:

https://echonet.github.io/dynamic/

Stanford AIMI:

https://aimi.stanford.edu/



- EchoNet-Dynamic licensing requirements
- Dataset data-use agreements
- Local ethical and institutional regulations
