# Overture Maps — attribution and licensing

Data: Overture Maps Foundation, https://overturemaps.org/ . Release **2026-10-21.0**, accessed **2026-10-28** (JST). This slide deck uses actual GeoParquet rows for a Kyoto bounding box. Rows were spatially filtered and rendered with a custom style; polygon rings, line coordinates and point positions come from the acquired data. The extraction is a modified subset, and the maps are produced works.

## Buildings, transportation and water

© OpenStreetMap contributors, Overture Maps Foundation. OpenStreetMap is available under the Open Database License (ODbL) 1.0: https://www.openstreetmap.org/copyright and https://opendatacommons.org/licenses/odbl/1-0/ . The full license is included in [LICENSE-ODbL-1.0.txt](../../licenses/overture-maps/LICENSE-ODbL-1.0.txt).

The actual Kyoto building subset also contains Microsoft Global ML Building Footprints (ODbL 1.0) and data by Qian Shi et al. **A First High-quality Vector Data of Buildings in East Asian Countries Based on a Comprehensive Large-scale Mapping Framework**, Zenodo, 22 July 2023, https://doi.org/10.5281/zenodo.8174931 , CC BY 4.0. Credit and source license are retained; the CC BY 4.0 text is included in [LICENSE-CC-BY-4.0.txt](../../licenses/overture-maps/LICENSE-CC-BY-4.0.txt). The Buildings theme as distributed is ODbL; individual source attribution is retained alongside it.

Transportation and water records used here identify OpenStreetMap as their source. Rendering does not introduce an additional external basemap.

## Places

The actual displayed Places extent includes sources **Meta, Microsoft, Overture, Uberall, OpenTravel, PinMeTo and DAC** under CDLA Permissive 2.0, **Foursquare** under Apache 2.0, and **AllThePlaces** under CC0 1.0. Each record's source and license were inspected; source occurrence counts include multiple sources on the same record and are not distinct place counts.

- [LICENSE-CDLA-Permissive-2.0.txt](../../licenses/overture-maps/LICENSE-CDLA-Permissive-2.0.txt): https://cdla.dev/permissive-2-0/ .
- [LICENSE-Apache-2.0.txt](../../licenses/overture-maps/LICENSE-Apache-2.0.txt): https://www.apache.org/licenses/LICENSE-2.0 .
- [NOTICE-Foursquare.txt](../../licenses/overture-maps/NOTICE-Foursquare.txt): full current Foursquare OS Places notice from https://opensource.foursquare.com/places-notice-txt/ . © 2026 Foursquare Labs, Inc. All rights reserved. The Overture attribution page separately states © 2024; this package preserves the current linked notice verbatim in its substantive content.
- [LICENSE-CC0-1.0.txt](../../licenses/overture-maps/LICENSE-CC0-1.0.txt): https://creativecommons.org/publicdomain/zero/1.0/ .

Foursquare data were transformed to the Overture schema by the distributor (Overture attribution page: changed 2026-03-18). In this material, rows were selected by bounding box, geometry was projected to EPSG:3857 for display, and point symbols/text labels were styled. The dataset values were not generated. Apache license and notice accompany the published material.

Other themes are explained but not rendered from downloaded rows: Addresses has country/source-specific terms; Base, Buildings, Divisions and Transportation are ODbL themes. The complete distributor list is https://docs.overturemaps.org/attribution/ . No blanket single-license claim is made for all six themes.

## Official website screenshot

The early screenshot shows https://overturemaps.org/ with its actual branding, navigation, CSS and hero text (accessed 2026-10-28). Copyright and trademarks remain with their owners. A cookie banner is visible; video/media and analytics loading were omitted during the capture. The screenshot is used to identify the official project, separately from the self-rendered map data.

## License text sources

ODbL and CDLA texts were extracted as readable text from the official license pages; navigation is retained where present and scripts/styles are omitted. Apache text was downloaded from Apache. CC BY 4.0 and CC0 1.0 texts were obtained from the SPDX license-list-data canonical text copies after official `.en.txt` endpoints returned 404:

- https://raw.githubusercontent.com/spdx/license-list-data/main/text/CC-BY-4.0.txt
- https://raw.githubusercontent.com/spdx/license-list-data/main/text/CC0-1.0.txt
