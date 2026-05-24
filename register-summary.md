# OGC Main

OGC Specification Elements packaged as FAIR Building Blocks.


The OGC Building Blocks register provides an overview of a series of [building blocks](https://ogcincubator.github.io/bblocks-docs/) managed by the OGC community through a variety of processes:

- formal standards publication processes the Standards Working Groups
- agreements with other standards bodies (eg. ISO)
- community hosted examples of re-use (profiles and extensions of OGC standards)
- informal "incubator" processes where more than one project needs a solution, and appropriate SWG scope is yet to be determined

![](https://lucid.app/publicSegments/view/9d075f82-8611-4f32-83eb-994143669cc8/image.png)


Notes:

1. Policies are in preparation for naming and governance of these sub-registers, and this is subject to change pending adoption of such policies.
1. Building Block identification will be designed to support transition between governance domains without change using symbolic references.
1. A formal definition of Building Blocks and the level of "granularity" they represent with respect to the OGC Modular Specification is TBD.


## Building Blocks

### `ogc.geo.common.data_types.bounding_box` — Bounding Box

**Type:** schema

The bounding box JSON object describes a simple spatial extent of a resource. For OGC API’s this could be a feature, a feature collection or a dataset, but it can be used in any JSON resource that wants to communicate its rough location. The extent is simple in that the bounding box does not describe the precise location and shape of the resource, but provides an axis-aligned approximation of the spatial extent that can be used as an initial test whether two resources are potentially intersecting each other.

### `ogc.geo.common.data_types.geojson` — GeoJSON

**Type:** schema

A GeoJSON object

### `ogc.geo.common.parameters.bbox` — bbox

**Type:** parameter

The bbox query parameter provides a simple mechanism for filtering resources based on their location. It selects all resources that intersect a rectangle (map view) or box (including height information).

### `ogc.geo.common.parameters.bbox-crs` — bbox-crs

**Type:** parameter

The bbox-crs query parameter can be used to assert the coordinate reference system that is used for the coordinate values of the bbox parameter.

### `ogc.ogc-utils.json-link` — JSON Link

**Type:** schema

Web linking is used to express relationships between resources. The JSON object representation of links described here is used consistently in OGC API’s.

### `ogc.geo.geopose.advanced` — GeoPose Advanced

**Type:** schema

Advanced GeoPose allowing flexible outer frame specification, quaternion orientation, and valid time.

### `ogc.geo.geopose.basic.quaternion` — GeoPose Basic-Quaternion

**Type:** schema

Basic GeoPose using quaternion to specify orientation

### `ogc.geo.geopose.basic.ypr` — GeoPose Basic-YPR

**Type:** schema

Basic GeoPose using yaw, pitch, and roll to specify orientation

### `ogc.geo.json-fg.time` — JSON-FG time member

**Type:** schema

### `ogc.ogc-utils.iri-or-curie` — IRI or CURIE

**Type:** datatype

This Building Block defines a data type allowing schemas and profiles to use string base type for a full IRI/URI or a CURIE (with or without a prefix). This common pattern is complex to implement, and this Building Block makes it easy to implement consistently where-ever need.

### `ogc.geo.features.feature` — Feature

**Type:** schema

A feature. Every feature is a sub-resource of an OGC Collection.

### `ogc.geo.json-fg.link-role` — Link with role and target conformance

**Type:** schema

A JSON-FG compliant web link with mandatory annotation of link role and optional conformance information to describe target resource. Compliant with profile resource descriptor model.

### `ogc.ogc-utils.topology` — Geometry using references

**Type:** schema

Demonstration of a schema using coordinates of points, withpout duplication

### `ogc.geo.features.featureCollection` — Feature Collection

**Type:** schema

A collection of features.

### `ogc.geo.json-fg.feature` — JSON-FG Feature

**Type:** schema

A OGC Features and Geometries JSON (JSON-FG) Feature, extending GeoJSON to support a limited set of additional capabilities that are out-of-scope for GeoJSON, but that are important for a variety of use cases involving feature data.

### `ogc.geo.json-fg.feature-lenient` — JSON-FG Feature - Lenient

**Type:** schema

A OGC Features and Geometries JSON (JSON-FG) Feature that does not require the "time" and "place" properties.

### `ogc.geo.json-fg.featureCollection` — JSON-FG Feature Collection

**Type:** schema

A collection of OGC Features and Geometries JSON (JSON-FG) Features, extending GeoJSON to support a limited set of additional capabilities that are out-of-scope for GeoJSON, but that are important for a variety of use cases involving feature data.

### `ogc.geo.json-fg.featureCollection-lenient` — JSON-FG Feature Collection - Lenient

**Type:** schema

A collection of lenient OGC Features and Geometries JSON (JSON-FG) Features, that do not require the "time" and "place" properties

