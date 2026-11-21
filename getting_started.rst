Getting Started
===============

**VectorGrid-Africa** is an interconnected network of permanent vector observatories operating across multiple African partner countries (including Tanzania, Kenya, Mozambique, South Africa, and Madagascar). The network implements common surveillance methods across all nodes to monitor mosquito vectors, species dynamics, and disease transmission risks.

Study Components
----------------

All participating nodes and observatory sites implement three core study components:

1. :doc:`components/household`
   Captures household occupant demographics, housing characteristics (roof, wall, floor, and open eaves), bed net ownership and condition, and livestock proximity.

2. :doc:`components/adult_vectors`
   Standardises indoor and outdoor trapping methods (CDC light traps, BG-Sentinel, resting buckets, Prokopack), morphological species identification, physiological staging, and ovarian tracheole dissections.

3. :doc:`components/larval_ecology`
   Characterises and samples natural and artificial aquatic breeding habitats, recording *in situ* water quality parameters, dipping effort (scaled to habitat size), aquatic predator presence and counts, and specimen preservation.

Digital Data Collection Workflow
--------------------------------

VectorGrid defines harmonised data dictionaries, variable specifications, and categorical codebooks across all observatory sites.

To facilitate field deployment, **ODK (Open Data Kit)** is provided as the primary reference implementation. Participating partner institutions and permanent observatories are free to adapt these standardised data models into other electronic data capture platforms (such as REDCap or institutional data systems) provided that core variable names, data types, and validation logic are preserved.

ODK Reference Implementation:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **Form Management (ODK Central):**
   Surveillance forms are maintained as standardised ODK XLSForms (``.xlsx``), downloadable from the :doc:`downloads` catalogue and ready to upload directly to your node's ODK Central server.

2. **Mobile Data Collection (ODK Collect):**
   Field collectors and survey teams synchronise blank forms to Android devices using ODK Collect via project QR codes for offline field data entry.

3. **Reference Form Layouts:**
   Printable layout documents (``.docx``) are provided for training, visual review, and questionnaire reference alongside the ODK digital tools.

Reference Standards
-------------------
- **SOP Quick References:**

  - :doc:`sops/sop_1_1`: Site selection criteria, household sampling, and reserve household replacement.
  - :doc:`sops/sop_2_1`: Essential metadata hierarchy, ±5m GPS accuracy, and ambient logger placement.
  - :doc:`sops/sop_2_2`: CDC light trap, BG-Sentinel 24h, DN-Mini sampling, and rain contingency.
  - :doc:`sops/sop_2_4`: Specimen processing, morphological sorting, and storage plate barcoding.
  - :doc:`sops/sop_3_1`: Larval dipping, *in situ* water quality analysis, and specimen preservation.

- **Categorical Codebooks:** Consult :doc:`codebooks` for adult physiological staging, Detinova parity, Christophers egg stages, habitat types, predator codes, and larval classifications.
