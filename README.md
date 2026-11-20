# VectorGrid Data Collection Tools Documentation

Technical documentation, standard operating procedures (SOPs), form reference specifications, and categorical codebooks for the multi-country **VectorGrid** vector observatory network.

---

## Overview

This repository contains the complete Sphinx documentation source for the VectorGrid data collection framework across three core study components:

1. **Household Surveillance:** Baseline household enrollment, dwelling characteristics, demographic rosters, and human behaviour observations.
2. **Adult Vector Surveillance:** Standardized trapping methods (CDC light traps, Prokopack, window exit traps, pyrethrum spray catches), morphotaxonomic identification, physiological scoring, and specimen preservation.
3. **Larval & Aquatic Habitat Ecology:** Aquatic breeding site registration, dipping surveys, water quality measurement, and aquatic predator presence and counts.

---

## Repository Structure

```text
sphinx_docs/
├── conf.py                   # Sphinx configuration and RTD theme styling
├── index.rst                 # Master index and documentation tree
├── getting_started.rst       # Field quality assurance and operational rules
├── codebooks.rst             # Categorical variables, taxa codes, and choices
├── downloads.rst             # Form packages and reference layout downloads
├── components/               # Study component overviews and protocols
│   ├── household.rst
│   ├── adult_vectors.rst
│   └── larval_ecology.rst
├── forms/                    # Form reference specifications (11 core forms)
│   ├── hh_reg.rst            # Household Registration (with nested status update)
│   ├── hh_beh.rst            # Human Behaviour Observation
│   ├── trap_reg.rst          # Trap Registration (with nested status update)
│   ├── spec_srt.rst          # Mosquito Collection & Sorting
│   ├── spec_dis.rst          # Mosquito Dissection & Parity
│   ├── env_obs.rst           # Environmental Observation
│   ├── env_ext.rst           # Extreme Weather Event
│   ├── hab_reg.rst           # Aquatic Habitat Registration (with nested status update)
│   └── hab_srv.rst           # Habitat Survey & Dipping
├── sops/                     # Standard Operating Procedures (SOP 1.1 to 3.1)
└── _static/                  # Static assets, custom CSS, JS, and downloadable forms
    ├── docx/                 # Reference Form Layouts (.docx)
    ├── odk/                  # ODK Central XLSForms (.xlsx)
    └── custom.css            # Responsive table and layout enhancements
```

---

## Local Development & Building Documentation

### Prerequisites

Install Python 3.10+ and the required Sphinx packages:

```bash
pip install sphinx sphinx-rtd-theme
```

### Build HTML Documentation

From the repository root:

```bash
# Clean build HTML pages
python -m sphinx -E -b html . _build/html
```

### Serve Locally

Start a local HTTP server to preview the built documentation:

```bash
python -m http.server 8000 --directory _build/html
```

Then open `http://127.0.0.1:8000/` in your browser.

---

## License & Citation

VectorGrid Africa Consortium. All rights reserved.
