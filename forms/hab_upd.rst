Habitat Status Update Form
==========================

**Form Code:** ``HAB-UPD`` | **Study Component:** Larval & Aquatic Habitat Ecology | **SOP Links:** SOP 3.1

The Habitat Status Update Form provides a fast update mechanism for registered aquatic habitats. Larval survey teams use this form between comprehensive dipping rounds to log hydrological transitions (such as seasonal desiccation, inundation, or removal) without repeating full physicochemical or dipping measurements.

Section 1: Habitat & Update Information
---------------------------------------

.. list-table::
   :widths: 25 20 20 35
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Description / Choice List
   * - ``node_code``
     - Text
     - Yes
     - Study Node Code
   * - ``village_id``
     - Text
     - Yes
     - Sentinel Site or Village Identifier
   * - ``habitat_id``
     - Text
     - Yes
     - Habitat Identifier (links to ``HAB-REG``)
   * - ``previous_status``
     - Select One
     - No
     - Prior recorded status code
   * - ``update_date``
     - Date
     - Yes
     - Date of status update visit
   * - ``collector_id``
     - Text
     - Yes
     - Field technician or team identifier

Section 2: Status Update
------------------------

.. list-table::
   :widths: 25 20 20 35
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Description / Choice List
   * - ``habitat_status``
     - Select One
     - Yes
     - 1=Active, 2=Inactive (temporarily dry), 3=Destroyed or removed, 4=Seasonal dry, 5=Flooded or inaccessible
   * - ``status_change_reason``
     - Select One
     - No
     - If not active: 1=Natural drying, 2=Drainage or filled, 3=Construction or development, 4=Agricultural activity, 5=Flooding, 6=Other
   * - ``status_notes``
     - Text
     - No
     - Narrative comments on habitat physical condition or modifications

Section 3: Verification
-----------------------

- **Technician Name:** Full name or digital signature of the inspecting technician.
- **Submission Timestamp:** Automated system time of status record.
