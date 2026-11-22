SOP 2.2: Adult Mosquito Sampling and Trap Placement
===================================================

This quick reference summarises trap placement, attractants, operating schedules and weather contingency procedures from **VectorGrid SOP 2.2, SOP 2.2.1 and SOP 2.3**.

Standard Trapping Deployments (SOP 2.2)
---------------------------------------
Peridomestic means the area within 10 m of the focal house walls. Record GPS coordinates (±5 m accuracy) for each focal house.

CDC Miniature Light Trap (Indoor)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* **Position:** Inside an occupied bedroom, about 1.5 m above the floor, near the foot end of an occupied bed. The trap hangs outside the net.
* **Occupancy Standard:** The bed is covered by an untreated mosquito net (provided by the research team if the household has none).
* **Operating Hours:** Connect the battery and switch on at sunset; at sunrise, switch off the trap and remove the collection bag (sunset and sunrise times set locally by site and season).
* **Power Source:** 6 V rechargeable battery or power bank.
* **Notes:** No CO\ :sub:`2` is used indoors. Record zero catches and any trap failure.

CDC Miniature Light Trap (Outdoor / CO\ :sub:`2`-baited)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* **Position:** Outdoors within 10 m of the focal house, in a shaded spot 1 to 1.5 m above the ground (1.5 m if possible), away from direct sunlight and strong wind.
* **Attractant:** Yeast and molasses fermentation (250 g molasses, 20 g dry yeast, 2 L water, prepared about 1 hour before), or 500 g to 1 kg of dry ice in a polystyrene box or CO\ :sub:`2` canister.
* **Operating Hours:** Switch on at sunset; switch off at sunrise.

BG-Sentinel Trap (24-Hour Surveillance)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* **Position:** Outdoors in a shaded area near vegetation, on a stand about 1 m high, avoiding direct rain.
* **Power Source:** 12 V battery.
* **Attractant:** BG-Lure cartridge with a CO\ :sub:`2` source (yeast and molasses mixture, or dry ice kept at least 1 m from the data logger).
* **Operating Schedule:** Switch on at sunset. After about 12 hours (morning), replace the collection bag ("Night" portion) and the CO\ :sub:`2` source, then restart. Continue until the next sunset (about 24 hours in total) and remove the second bag ("Day" portion). This tracks *Aedes* and other day-biting species.

Human-Mosquito Contact Sampling (SOP 2.2.1, DN-Mini)
----------------------------------------------------
* **Sampling Design:** Biannual (wet and dry seasons), 24 hours per household: day shift 06:00 to 18:00 and night shift 18:00 to 06:00. One DN-Mini indoors (main living room) and one outdoors (5 to 10 m from the house) per household, one volunteer per trap per shift, and 12 pre-labelled cups per shift (one per hour).
* **Trap Setup:** Double-Net Mini (DN-Mini) trap. The volunteer sits inside the inner net and never opens it during sampling.
* **Hourly Collection Routine:**

  * Every hour, the volunteer uses a mouth aspirator to collect mosquitoes from the outer net.
  * Mosquitoes go into the paper cup labelled for that hour, sealed with net and a rubber band.

* **Rain Contingency (Section 8.4):**

  * In light or moderate rain, cover the outdoor DN-Mini with plastic canvas.
  * In very heavy rain, the volunteer may leave the trap for a while; record the exit and return times.

* **Breaks (Section 8.5):** Food, water and toilet breaks are allowed; record exit and return times.
* **ODK recording:** Volunteer shifts, hourly cups (Cup ID made by the form), counts and each exit and return (as interruptions) are recorded on :doc:`../forms/hh_beh`.

Resting Mosquito Collections (SOP 2.3)
--------------------------------------
* **Indoor Resting (Prokopack or mouth aspirator):** First thing in the morning, between 06:00 and 09:00 as agreed with house owners, after the occupants leave the room. Close the room and aspirate walls and objects, starting low and moving upward.
* **Outdoor Resting (Prokopack):** Shaded, humid peridomestic sites within reach, such as vegetation, tree holes, crab holes, outer house walls near the roof and animal shelters; usually in the morning.
* **Resting Buckets:** Two 20 L black buckets lined with black cloth per focal house, at least 20 m apart, in shade not more than 10 m from the house, collected early in the morning with a Prokopack.
* **Muirhead-Thomson Pit Trap (MTPT):** A 1 m x 1 m x 1 m pit with horizontal cavities, sampled in the early morning about 30 minutes after sunrise; ideally 3 to 5 pits per site over 3 mornings.

Recording Traps in the ODK Forms
--------------------------------
* Register each trap on :doc:`../forms/trap_reg` with method ``CDC`` (with ``co2_bait`` = ``1`` for CO\ :sub:`2`-baited traps), ``BGS``, ``RB``, ``PKP`` or ``DN``. Methods not in the list, such as the MTPT, are recorded as ``other``.
* Record each collection on :doc:`../forms/spec_srt`, entering the morning (night catch) and evening (day catch) bags as separate records distinguished by their collection times.
