Aquatic Habitat Registration Form
=================================

**Form Code:** ``HAB-REG`` | **Form ID:** ``vg_hab_reg`` | **Version:** ``2026112201`` | **Component:** Larval Sampling | **SOP Links:** :doc:`SOP 3.1 <../sops/sop_3_1>`

The Aquatic Habitat Registration Form registers an aquatic habitat once: its location, GPS point, Habitat ID, natural or artificial origin, permanence and habitat type. Water, vegetation and size measurements are taken at each survey on :doc:`hab_srv`, not at registration.

How This Form Works
-------------------

* **Entity:** Creates a new record in the ``habitats`` entity list. Properties written: ``node_code``, ``collector_id``, ``registration_date``, ``country``, ``district``, ``ward``, ``village``, ``subvillage``, ``habitat_id``, ``geometry``, ``natural_artificial``, ``permanence``, ``habitat_type``, ``habitat_type_name``, ``water_type_name``, ``status``.
* The full location and GPS point are asked only on this form. HAB-UPD and HAB-SRV pick the habitat by district.
* Habitat ID is typed (no format check), for example ``HAB-001``. Entity label shown on other forms: Habitat ID - Village - Habitat type.
* Habitat types use codes 1 to 22 (see :doc:`../codebooks`).

Section 1: Survey Information
-----------------------------

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``node_code``
     - Text
     - Yes
     - Node Code

       *Saved to entity property* ``node_code``
   * - ``collector_id``
     - Text
     - Yes
     - Field Worker Name

       *Saved to entity property* ``collector_id``
   * - ``registration_date``
     - Date
     - Yes
     - Survey Date

       *Check:* ``value <= today()``

       *Default:* today

       *Saved to entity property* ``registration_date``
   * - ``registration_time``
     - Time
     - Yes
     - Survey Time

Section 2: Location
-------------------

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``country``
     - Calculated
     - Auto
     - Preset in the form to the node's country

       *Saved to entity property* ``country``
   * - ``district``
     - Select one
     - Yes
     - District

       District list (set for each node)

       *Saved to entity property* ``district``
   * - ``ward``
     - Select one
     - Yes
     - Ward

       Ward list (set for each node)

       *Saved to entity property* ``ward``
   * - ``village``
     - Select one
     - Yes
     - Village

       Village list (set for each node)

       *Saved to entity property* ``village``
   * - ``subvillage``
     - Text
     - No
     - Sub-village Name

       *Saved to entity property* ``subvillage``

Section 3: Habitat Identification
---------------------------------

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``habitat_id``
     - Text
     - Yes
     - Habitat ID

       *Hint:* e.g., HAB-001

       *Saved to entity property* ``habitat_id``

Section 4: GPS Location
-----------------------

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``gps_location``
     - GPS point
     - Yes
     - Capture GPS Location

       *Hint:* Wait for accuracy < 5 m

       *Saved to entity property* ``geometry``

Section 5: Habitat Characteristics
----------------------------------

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``natural_artificial``
     - Select one
     - Yes
     - Natural / Artificial

       ``1`` = Natural; ``2`` = Artificial

       *Saved to entity property* ``natural_artificial``
   * - ``permanence``
     - Select one
     - Yes
     - Water type (permanence)

       ``1`` = Temporary; ``2`` = Semi-permanent; ``3`` = Permanent

       *Saved to entity property* ``permanence``
   * - ``habitat_type``
     - Select one
     - Yes
     - Habitat Type

       22 options, see :doc:`../codebooks`

       *Saved to entity property* ``habitat_type``
   * - ``habitat_type_other``
     - Text
     - Yes
     - Specify other habitat type

       *Shown if* ``habitat_type = 22``
   * - ``habitat_type_name``
     - Calculated
     - Auto
     - Habitat type name, or the typed other type

       *Saved to entity property* ``habitat_type_name``
   * - ``water_type_name``
     - Calculated
     - Auto
     - Permanence name: Temporary, Semi-permanent or Permanent

       *Saved to entity property* ``water_type_name``

Section 6: System Fields
------------------------

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``status``
     - Calculated
     - Auto
     - Fixed value: ``active``

       *Saved to entity property* ``status``

Section 7: Signature
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

Habitat Status Update
---------------------

Between surveys, habitat status changes (seasonal drying, drainage, destruction, flooding) are recorded with the update form:

.. toctree::
   :maxdepth: 2

   hab_upd
