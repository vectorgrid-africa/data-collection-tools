# VectorGrid Data Collection Tools Documentation

Technical documentation, standard operating procedures (SOPs), form reference specifications, and categorical codebooks for the **VectorGrid-Africa** observatory.

🌐 **Live Documentation:** [https://vectorgrid-africa.github.io/data-collection-tools/](https://vectorgrid-africa.github.io/data-collection-tools/)

---

## Overview

This repository contains the complete Sphinx documentation source for the VectorGrid data collection framework across three sampling activities:

1. **Site & Household Selection:** Registration of the selected households, house structure, the people sleeping in each room, bed nets and livestock.
2. **Adult Mosquito Sampling:** Standardised trapping methods (CDC light traps, BG-Sentinel, DN-Mini, resting buckets, Prokopack aspiration, pit traps and optional pyrethrum spray catches), human-mosquito contact and human behaviour observations, morphological identification, physiological status, dissection, specimen preservation, and sample chain of custody.
3. **Larval Sampling:** Aquatic breeding site registration, dipping surveys, water quality measurement, and aquatic predator presence and counts.

---

## Local Development & Building Documentation

### Prerequisites

Install Python 3.10+ and the required Sphinx packages:

```bash
pip install sphinx furo
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
