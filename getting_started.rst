Getting Started
===============

**VectorGrid-Africa** is a coordinated network of mosquito-monitoring sites in East and Southern Africa, with nodes in Tanzania, Kenya, Mozambique, South Africa and Madagascar. All nodes follow the same harmonised field and laboratory protocols (the VectorGrid SOPs), so that data on mosquito vectors, vector-borne pathogens and their environmental drivers can be compared across countries, surveillance types and time.

Components
----------

The forms are structured into three components:

1. :doc:`components/household`
   Captures the selected households' housing characteristics (roof, wall, floor, and open eaves), the people sleeping in each room, bed nets in use (treated, untreated and unidentified), and livestock proximity.

2. :doc:`components/adult_vectors`
   Standardises indoor and outdoor trapping methods (CDC light traps, BG-Sentinel, DN-Mini, resting buckets, Prokopack), morphological identification, physiological status, and ovarian tracheole dissections.

3. :doc:`components/larval_ecology`
   Characterises and samples natural and artificial aquatic breeding habitats in the Supplementary Sites, recording *in situ* water quality parameters, dipping effort (scaled to habitat size), aquatic predator presence and counts, and specimen preservation.

Digital Data Collection Workflow
--------------------------------

VectorGrid-Africa defines harmonised variables and categorical codebooks across all nodes.

To facilitate field deployment, **ODK (Open Data Kit)** is provided as the primary reference implementation. Partner institutions may adapt these forms into other tools (such as REDCap or institutional databases) provided that core variable names and validation logic are preserved.

ODK Reference Implementation:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **Form Management (ODK Central):**
   Surveillance forms are maintained as standardised ODK XLSForms (``.xlsx``), downloadable from the :doc:`downloads` catalogue and ready to upload directly to your node's ODK Central server.

2. **Mobile Data Collection (ODK Collect):**
   Field collectors and survey teams synchronise blank forms to Android devices using ODK Collect via project QR codes for offline field data entry.

SOP Summaries & Codebooks
-------------------------

- **SOP Quick References:**

  - :doc:`sops/sop_1_1`: Site selection criteria, household sampling, and household replacement.
  - :doc:`sops/sop_2_1`: Essential metadata, weather and extreme weather events, and data logger placement.
  - :doc:`sops/sop_2_2`: CDC light trap, BG-Sentinel 24h, DN-Mini sampling, resting collections, and rain contingency.
  - :doc:`sops/sop_2_4`: Specimen processing, morphological sorting, and storage plate barcoding.
  - :doc:`sops/sop_3_1`: Larval dipping, *in situ* water quality analysis, and specimen preservation.

- **Categorical Codebooks:** Consult :doc:`codebooks` for adult physiological status, Detinova parity, Christophers egg stages, habitat types, predator codes, and larval classifications.
