# VectorGrid Data Collection Tools Documentation

Technical documentation, standard operating procedures (SOPs), form reference specifications, and categorical codebooks for the multi-country **VectorGrid** vector observatory network.

🌐 **Live Documentation:** [https://vectorgrid-africa.github.io/data-collection-tools/](https://vectorgrid-africa.github.io/data-collection-tools/)

---

## Overview

This repository contains the complete Sphinx documentation source for the VectorGrid data collection framework across three core study components:

1. **Household Surveillance:** Baseline household enrolment, dwelling characteristics, demographic rosters, and human behaviour observations.
2. **Adult Vector Surveillance:** Standardised trapping methods (CDC light traps, Prokopack, window exit traps, pyrethrum spray catches), morphotaxonomic identification, physiological scoring, and specimen preservation.
3. **Larval & Aquatic Habitat Ecology:** Aquatic breeding site registration, dipping surveys, water quality measurement, and aquatic predator presence and counts.

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
