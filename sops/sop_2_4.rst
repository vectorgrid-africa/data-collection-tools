SOP 2.4: Field Mosquito Processing & Handling Workflow
======================================================

This quick reference summarises specimen intake, morphological sorting, downstream preservation pathways, standardised barcoding, and sample transfer protocols from **VectorGrid SOP Task 2.4**.

1. Specimen Intake & Morphological Sorting
------------------------------------------
These intake and sorting steps apply across all routine and biannual collections:

* **Intake Match:** Cross-check field retrieval bags against the Deployment ID and Trap ID from ``SPEC-SRT`` and transfer promptly for sorting under a stereomicroscope.
* **Taxonomic Separation:**

  * Target Vectors: Separate *Anopheles gambiae s.l.* and *Anopheles funestus group*.
  * Secondary / Non-target: Separate other anophelines and culicines (*Culex*, *Aedes*, *Mansonia*).
  * Sex Determination: Separate males and females based on antennal plumosity.

* **Female Physiological Staging:** Classify abdominal appearance into Unfed (UF), Partly Fed (PF), Fully Fed (FD), Semi-gravid (SG), or Gravid (GV).
* **Fresh Dissection Allocation:** Transfer live, fresh fed or semi-gravid females designated for ovarian tracheole inspection directly to the dissection bench with ``SPEC-DIS``.
* **Non-Target Insects:** Count and discard non-target insects (moths, beetles, flies).

2. Downstream Preservation Pathways
-----------------------------------
Not all collected specimens pass through every workflow. Following intake and morphological sorting, specimens are routed to the applicable handling pathway based on node equipment, target species, and downstream laboratory objectives:

* **Routine Archive / Dry Storage:** Store specimens in sealed microtubes or plates containing colour-indicating silica gel beads for general archiving or standard morphological and molecular follow-up.
* **MIRS Scanning (MIRS-equipped nodes):** Scan eligible specimens using Mid-Infrared Spectroscopy (MIRS) prior to downstream preservation for rapid species and age prediction.
* **Amplicon Sequencing (selected specimens):** Place individual specimens into 96-well skirted microplates pre-filled with 100 µL of 95% to 100% ethanol using a multichannel pipette, and seal tightly with 8-strip caps (and parafilm if shipped) for species identification, protozoan pathogen detection, and vertebrate blood-meal analysis.
* **Viral Pathogen Screening (selected specimens):** Use sterile tools between samples and maintain a cold chain on dry ice or a dry shipper (or preserve in RNA-stabilising reagents such as RNAlater, DNA-RNA Shield, or Trizol-LS) for RT-PCR screening.

3. Labelling, Barcoding & Plate Mapping
---------------------------------------
Every storage box, 96-well microplate, and vial rack carries a standardised barcode label in this format:

.. code-block:: text

   [Country Code][Node Code] [Plate / Box Number]

Format specification:

* **Country Code:** 2-letter ISO country code representing the partner country (such as ``TZ``, ``KE``, ``MZ``, ``ZA``, or ``MG``).
* **Node Code:** 2-letter node abbreviation assigned to the field station (for example, ``DS`` for Dar es Salaam).
* **Plate / Box Number:** 4-digit sequential plate or box number, zero-padded (such as ``0001``, ``0002``).

Example:

* ``TZDS 0001``: Country: Tanzania, Node: Dar es Salaam, Plate / Box: 0001.

Plate and well tracking:

* **96-Well Microplate Layout:** Standard 8 x 12 grid (Rows A to H, Columns 1 to 12).
* **Position Register:** Record well coordinates (From: well to To: well) on ``SPEC-SRT`` so each specimen links unambiguously to its field collection metadata.
* **Barcode Integration:** Where available, affix 1D/2D barcode labels next to the written ID on plates and trap sites to streamline digital scanning.

4. Packaging, Storage & Chain-of-Custody
----------------------------------------
* **Desiccant & Seal Checks:** Monitor colour-indicating silica gel beads and replace saturated desiccant when beads shift colour. Check ethanol plates for evaporation or loose caps before storage or dispatch.
* **Storage & Transport Conditions:**

  * Store completed plates in a freezer at the field base station where required by the downstream assay.
  * Specimens stored in RNAlater, DNA-RNA Shield, or Trizol-LS can travel at ambient temperature for weeks without immediate freezing.
  * When RNA preservation reagents are unavailable for viral screening, maintain an uninterrupted cold chain using dry ice or a dry shipper.

* **Chain-of-Custody Log:** Verify that every plate or tube is fully labelled and sealed, organise plates in labelled cryo-boxes before transfer, and complete a sample manifest or chain-of-custody handover log signed by transferring personnel.
