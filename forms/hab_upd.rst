Habitat Status Update Form
==========================

**Form Code:** ``HAB-UPD`` | **Form ID:** ``vg_hab_upd`` | **Version:** ``2026112201`` | **Component:** Larval Sampling | **SOP Links:** :doc:`SOP 3.1 <../sops/sop_3_1>`

The Habitat Status Update Form changes the status of a registered habitat between surveys (for example seasonal drying, flooding or destruction) and records the reason, without repeating the survey measurements.

How This Form Works
-------------------

* **Entity:** Updates the selected record in the ``habitats`` entity list. Properties written: ``last_update_date``, ``status``, ``status_reason``, ``status_notes``.
* Select the district, then the habitat from the ``habitats`` entity list. The Habitat ID, location, type and current status are shown.
* Status values: ``active``, ``inactive``, ``destroyed``, ``seasonal_dry`` and ``flooded``. A reason is required for any status other than ``active``.
* Changes overwrite the habitat record. HAB-SRV lists only ``active`` habitats.

Section 1: Survey Information
-----------------------------

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``district``
     - Select one
     - Yes
     - Select district

       District list (set for each node)

       *Hint:* Filter habitats by district
   * - ``collector_id``
     - Text
     - Yes
     - Field Worker Name
   * - ``update_date``
     - Date
     - Yes
     - Update Date

       *Check:* ``value <= today()``

       *Default:* today

       *Saved to entity property* ``last_update_date``

Section 2: Habitat Selection
----------------------------

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``habitat``
     - Select record
     - Yes
     - Select Habitat

       Pick a record from the ``habitats`` entity list (filtered by district)
   * - ``auto_habitat_id``
     - Calculated
     - Auto
     - Taken from the selected ``habitats`` record (property ``habitat_id``)
   * - ``auto_node``
     - Calculated
     - Auto
     - Taken from the selected ``habitats`` record (property ``node_code``)
   * - ``auto_village``
     - Calculated
     - Auto
     - Taken from the selected ``habitats`` record (property ``village``)
   * - ``auto_district``
     - Calculated
     - Auto
     - Taken from the selected ``habitats`` record (property ``district``)
   * - ``auto_habitat_type``
     - Calculated
     - Auto
     - Taken from the selected ``habitats`` record (property ``habitat_type_name``)
   * - ``auto_water_type``
     - Calculated
     - Auto
     - Taken from the selected ``habitats`` record (property ``water_type_name``)
   * - ``current_status``
     - Calculated
     - Auto
     - Taken from the selected ``habitats`` record (property ``status``)

Section 3: Status Update
------------------------

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``new_status``
     - Select one
     - Yes
     - New Status

       ``active`` = Active; ``inactive`` = Inactive (temporarily dry); ``destroyed`` = Destroyed / Removed; ``seasonal_dry`` = Seasonal Dry; ``flooded`` = Flooded / Inaccessible

       *Saved to entity property* ``status``
   * - ``status_reason``
     - Select one
     - Yes
     - Reason for Change

       ``natural_drying`` = Natural drying; ``drainage`` = Drainage / Filled; ``construction`` = Construction / Development; ``agriculture`` = Agricultural activity; ``flooding`` = Flooding; ``other`` = Other

       *Shown if* ``new_status != active``

       *Saved to entity property* ``status_reason``
   * - ``status_reason_other``
     - Text
     - Yes
     - Specify other reason

       *Shown if* ``status_reason = other``
   * - ``status_notes``
     - Text
     - No
     - Additional Notes

       *Saved to entity property* ``status_notes``

Section 4: Signature
--------------------

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``full_name_signature``
     - Text
     - Yes
     - Full name (as signature)
