Getting Started
===============

**VectorGrid-Africa** is an interconnected network of permanent vector observatories operating across multiple African partner countries (including Tanzania, Kenya, Mozambique, South Africa, and Madagascar). The network implements a standardized, harmonized surveillance framework to track mosquito vectors, species dynamics, and disease transmission risks.

Study Components
----------------

All participating nodes and observatory sites implement three core study components:

1. :doc:`components/household`
   Captures community census demographics, architectural vulnerability (roof, wall, floor, and open eaves), bed net ownership and condition, and domestic animal proximity.

2. :doc:`components/adult_vectors`
   Standardizes indoor and outdoor trapping regimes (CDC light traps, BG-Sentinel, resting buckets, Prokopack), morphological species identification, physiological staging, and ovarian tracheole dissections.

3. :doc:`components/larval_ecology`
   Tracks natural and artificial aquatic breeding habitats, *in situ* water physicochemical parameters, 10-dip sampling effort, predator guild audits, and voucher preservation.

Digital Data Collection Workflow
--------------------------------

VectorGrid defines harmonized data dictionaries, variable specifications, and categorical codebooks across all observatory sites.

To facilitate rapid field deployment, **ODK (Open Data Kit)** is provided as the primary reference implementation. Participating partner institutions and permanent observatories are free to adapt these standardized data models into other electronic data capture platforms (such as REDCap or institutional data systems) provided that core variable names, data types, and validation logic are preserved.

ODK Reference Implementation:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **Form Management (ODK Central):**
   Surveillance forms are maintained as standardized ODK XLSForms (``.xlsx``), downloadable from the :doc:`downloads` catalog and ready to upload directly to your node's ODK Central server.

2. **Mobile Data Collection (ODK Collect):**
   Field collectors and survey teams synchronize blank forms to Android devices using ODK Collect via project QR codes for offline field data entry.

3. **Demonstration Paper Templates:**
   Printable paper templates (``.docx``) are provided for demonstration, training, and visual reference of the questionnaire structure.

Field Quality Assurance & Operational Rules
-------------------------------------------

All field enumerators and laboratory technicians follow four core operational rules to maintain data integrity across the observatory network:

1. **Mandatory Zero Counts:**
   Never leave count fields blank or discard zero-catch nights or dry habitats. A catch of zero mosquitoes or an absence of larvae is critical surveillance data and must be entered explicitly as ``0``.

2. **GPS Accuracy Threshold (±5 Meters):**
   When capturing geolocations, enumerators must wait until mobile devices acquire sufficient satellite signals to achieve an accuracy of ±5 meters or better before confirming coordinates.

3. **Cold Chain Integrity During Sorting:**
   Adult mosquitoes retrieved from field traps must be kept cool on chilled stages or frozen gel packs during morphological examination to prevent enzymatic degradation of viral and parasite nucleic acids.

4. **Identifier Verification:**
   Before entering survey data, verify that Household IDs, Trap IDs, and Habitat IDs match the physical weather-resistant placards or tags affixed during baseline registration.

Reference Standards
-------------------
- **SOP Quick References:**
  - :doc:`sops/sop_1_1`: Site and household selection, cluster enumeration, and reserve cohort replacement.
  - :doc:`sops/sop_2_1`: Essential metadata hierarchy, ±5m GPS accuracy, and ambient logger placement.
  - :doc:`sops/sop_2_2`: CDC light trap, BG-Sentinel 24h, DN-Mini sampling, and rain contingency.
  - :doc:`sops/sop_2_4`: Specimen processing, morphological sorting, and 96-well biobank barcoding.
  - :doc:`sops/sop_3_1`: Larval dipping, *in situ* water analysis, and specimen voucher preservation.
- **Categorical Codebooks:** Consult :doc:`codebooks` for adult physiological staging, Detinova parity, Christophers egg stages, habitat typologies, predator codes, and larval classifications.
