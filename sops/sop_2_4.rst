SOP 2.4: Mosquito Processing & Biobank Barcoding
================================================

This quick reference summarizes specimen reception, cold-chain sorting, dissection triage, microplate allocation, and biobank storage protocols from **VectorGrid SOP Task 2.4**.

1. Specimen Reception & Intake Verification
-------------------------------------------
* **Intake Match:** Field retrieval bags are cross-checked against the Deployment ID and Trap ID from ``SPEC-SRT``.
* **Cold-Chain Intake:** Mosquito bags must be transferred immediately to chilled sorting stages (0°C to 4°C) or placed over frozen ice packs to stop enzymatic degradation of viral and plasmodial nucleic acids.

2. Morphological Sorting & Triage Workflow
------------------------------------------
* **Microscopic Inspection:** Sort specimens under a stereomicroscope on a chilled surface.
* **Taxonomic Separation:**
  * Target Vectors: Separate *Anopheles gambiae s.l.* and *Anopheles funestus group*.
  * Secondary / Non-target: Separate other anophelines and culicines (*Culex*, *Aedes*, *Mansonia*).
  * Sex Determination: Separate males and females based on antennal plumosity.
* **Female Physiological Staging:**
  * Classify abdominal appearance into Unfed (UF), Partly Fed (PF), Fully Fed (FD), Semi-gravid, or Gravid (GV).
* **Fresh Dissection Allocation:**
  * Immediately transfer live, fresh fed or semi-gravid females designated for ovarian tracheole inspection to the dissection bench with ``SPEC-DIS``.
* **Non-Mosquito Bycatch:** Count and discard non-target insects (moths, beetles, flies).

3. Barcode Convention
---------------------
Every storage box, 96-well microplate, and vial rack must carry a machine-readable barcode adhering to the standard observatory syntax:

.. code-block:: text

   [Country Code][Node Code] [Box Number]

Format specification:

* **Country Code:** 2-letter ISO country code representing the partner country (such as ``TZ``, ``KE``, ``MZ``, ``ZA``, or ``MG``).
* **Node Code:** 2 to 4-letter unique observatory node identifier assigned to the field station (for example, ``01``, ``02``, or local node code).
* **Box Number:** 4-digit sequential box or rack number, zero-padded (such as ``0001``, ``0002``).

Generic Examples:

* ``TZ01 0001``: Participating observatory node in Tanzania, Box 0001
* ``KE01 0001``: Participating observatory node in Kenya, Box 0001
* ``MZ01 0002``: Participating observatory node in Mozambique, Box 0002

4. Plate Allocation & Well Mapping
----------------------------------
* **96-Well Microplate Layout:** Standard 8 × 12 grid (Rows A to H, Columns 1 to 12).
* **Progression Order:** Fill microplates column-by-column (A1 to H1, then A2 to H2) to maintain alignment with automated laboratory liquid handlers.
* **Specimen Storage Modes:**
  * **Individual Storage (1 specimen per well / tube):** Used for individual genotyping, target-site mutation assays, and whole-genome sequencing.
  * **Pool Storage (Up to 10 specimens per tube):** Mosquitoes of identical taxon, sex, collection event, and physiological status pooled for high-throughput pathogen screening.
* **Position Register:** Record starting and ending well coordinates (From: well to To: well) on ``SPEC-SRT`` Q12.

5. Temperature & Preservation Standards
---------------------------------------
* **Desiccant Management:** Microtubes and plates must contain color-indicating silica gel beads. Monitor indicator beads and replace saturated desiccant when beads shift color.
* **Storage Temperature Regimes:**
  * **Field Base Station:** Maintain specimens at -20°C in dedicated freezers.
  * **Central Biorepository:** Long-term preservation in -80°C ultra-low temperature freezers or vapor-phase liquid nitrogen.
* **Freeze-Thaw Prevention:** Prevent unnecessary temperature fluctuations; organize plates in labeled cryo-boxes before transfer.
