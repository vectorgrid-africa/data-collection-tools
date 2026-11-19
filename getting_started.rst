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

Reference Standards
-------------------
- **SOP Quick References:** See :doc:`sops/sop_2_4` for specimen handling and 96-well biobank barcoding standards, and :doc:`sops/sop_3_1` for water quality analysis standards.
- **Categorical Codebooks:** Consult :doc:`codebooks` for harmonized habitat typologies, predator codes, and larval taxon classifications.
