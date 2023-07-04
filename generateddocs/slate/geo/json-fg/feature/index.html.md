---
title: JSON-FG Feature (Schema)

toc_footers:
  - Version 0.1
  - <a href='#'>JSON-FG Feature</a>
  - <a href='https://blocks.ogc.org/register.html'>Building Blocks register</a>

search: true

code_clipboard: true

meta:
  - name: JSON-FG Feature (Schema)
---


# JSON-FG Feature `ogc.geo.json-fg.feature`

A OGC Features and Geometries JSON (JSON-FG) Feature, extending GeoJSON to support a limited set of additional capabilities that are out-of-scope for GeoJSON, but that are important for a variety of use cases involving feature data.

[Maturity](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity): Proposal

<aside class="success">
This building block is <strong>valid</strong>
</aside>

# Description

OGC Features and Geometries JSON (JSON-FG) extends GeoJSON to support a limited set of additional capabilities that are
out-of-scope for GeoJSON, but that are essential or important for a variety of use cases involving feature data.

Information that can be represented as GeoJSON is encoded as GeoJSON. Additional information is mainly encoded in
additional top-level members of GeoJSON objects. The members use keys that do not conflict with GeoJSON including the
obsolete version that pre-dates the IETF standard. GeoJSON clients will be able to parse and understand all aspects that
are specified by GeoJSON, JSON-FG clients will also parse and understand the additional capabilities.

This Standard specifies the following minimal extensions to the GeoJSON Standard:

* The ability to use Coordinate Reference Systems (CRSs) other than WGS 84;
* The ability to use non-Euclidean metrics, in particular ellipsoidal metrics;
* Support for solids and prisms as geometry types;
* The ability to encode temporal characteristics of a feature; and
* The ability to declare the type and the schema of a feature.

Information that can be represented as GeoJSON is encoded as GeoJSON. Additional information is mainly encoded in
additional members of the GeoJSON objects. The additional members use keys that do not conflict with GeoJSON. This is so
existing and future GeoJSON clients will continue to parse and understand GeoJSON content. JSON-FG enabled clients will
also be able to parse and understand the additional members.

JSON Schema is used to formally specify the JSON-FG syntax.

# JSON Schema

```yaml--schema
allOf:
- $ref: ../../features/feature/schema.yaml
- type: object
  required:
  - type
  - geometry
  - properties
  properties:
    type:
      type: string
      enum:
      - Feature
    id:
      oneOf:
      - type: number
      - type: string
    featureType:
      $ref: https://beta.schemas.opengis.net/json-fg/featuretype.json
    links:
      type: array
      items:
        $ref: https://beta.schemas.opengis.net/json-fg/link.json
    time:
      $ref: https://beta.schemas.opengis.net/json-fg/time.json
    coordRefSys:
      $ref: https://beta.schemas.opengis.net/json-fg/coordrefsys.json
    place:
      $ref: https://beta.schemas.opengis.net/json-fg/place.json
    geometry:
      $ref: https://beta.schemas.opengis.net/json-fg/geometry.json
    properties:
      oneOf:
      - type: 'null'
      - type: object

```

Links to the schema:

* YAML version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/feature/schema.yaml" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/feature/schema.yaml</a>
* JSON version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/feature/schema.json" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/feature/schema.json</a>


# JSON-LD Context

```json--ldContext
{
  "@context": {
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "geojson": "https://purl.org/geojson/vocab#",
    "type": "@type",
    "id": "@id",
    "properties": "https://purl.org/geojson/vocab#properties",
    "geometry": {
      "@context": {
        "type": "@type",
        "coordinates": {
          "@id": "https://purl.org/geojson/vocab#coordinates",
          "@container": "@list"
        }
      },
      "@id": "https://purl.org/geojson/vocab#geometry"
    },
    "bbox": {
      "@id": "https://purl.org/geojson/vocab#bbox",
      "@container": "@list"
    },
    "features": "geojson:features",
    "MultiLineString": "geojson:MultiLineString",
    "FeatureCollection": "geojson:FeatureCollection",
    "LineString": "geojson:LineString",
    "MultiPolygon": "geojson:MultiPolygon",
    "Feature": "geojson:Feature",
    "GeometryCollection": "geojson:GeometryCollection",
    "Point": "geojson:Point",
    "Polygon": "geojson:Polygon",
    "MultiPoint": "geojson:MultiPoint",
    "links": "http://www.w3.org/2000/01/rdf-schema#seeAlso"
  }
}
```

You can find the full JSON-LD context here:
<a href="https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/feature/context.jsonld" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/feature/context.jsonld</a>

# References

* [OGC Testbed-17: OGC Features and Geometries JSON Engineering Report](http://docs.ogc.org/per/21-017r1.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: <a href="https://github.com/opengeospatial/bblocks" target="_blank">https://github.com/opengeospatial/bblocks</a>
* Path: `registereditems/geo/json-fg/feature`

