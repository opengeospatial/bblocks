
# JSON-FG Feature Collection (Schema)

`ogc.geo.json-fg.featureCollection` *v0.1*

A collection of OGC Features and Geometries JSON (JSON-FG) Features, extending GeoJSON to support a limited set of additional capabilities that are out-of-scope for GeoJSON, but that are important for a variety of use cases involving feature data.

[*Maturity*](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity): Proposal

## Description

OGC Features and Geometries JSON (JSON-FG) extends GeoJSON to support a limited set of additional capabilities that are
out-of-scope for GeoJSON, but that are essential or important for a variety of use cases involving feature data.
A **feature collection** contains a set of features from a dataset.

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
## Schema

```yaml
allOf:
- $schema: https://json-schema.org/draft/2019-09/schema
  title: a JSON-FG Feature Collection
  description: This JSON Schema is part of JSON-FG version 0.1.1
  type: object
  required:
  - type
  - features
  properties:
    type:
      type: string
      enum:
      - FeatureCollection
    featureType:
      $ref: https://beta.schemas.opengis.net/json-fg/featuretype.json
    geometryDimension:
      type: integer
      minimum: 0
      maximum: 3
    coordRefSys:
      $ref: https://beta.schemas.opengis.net/json-fg/coordrefsys.json
- $ref: ../../features/featureCollection/schema.yaml

```

Links to the schema:

* YAML version: [schema.yaml](https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/featureCollection/schema.json)
* JSON version: [schema.json](https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/featureCollection/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "links": {
      "@id": "http://www.w3.org/2000/01/rdf-schema#seeAlso",
      "@context": {
        "href": "@id",
        "title": "rdfs:label"
      }
    },
    "features": {
      "@id": "https://purl.org/geojson/vocab#features",
      "@context": {
        "type": "@type",
        "id": "@id",
        "properties": "geojson:properties",
        "geometry": {
          "@id": "https://purl.org/geojson/vocab#geometry",
          "@context": {
            "type": "@type",
            "coordinates": {
              "@id": "https://purl.org/geojson/vocab#coordinates",
              "@container": "@list"
            }
          }
        },
        "bbox": {
          "@id": "https://purl.org/geojson/vocab#bbox",
          "@container": "@list"
        },
        "GeometryCollection": "geojson:GeometryCollection",
        "LineString": "geojson:LineString",
        "Feature": "geojson:Feature",
        "MultiLineString": "geojson:MultiLineString",
        "MultiPoint": "geojson:MultiPoint",
        "features": "geojson:features",
        "FeatureCollection": "geojson:FeatureCollection",
        "Polygon": "geojson:Polygon",
        "MultiPolygon": "geojson:MultiPolygon",
        "Point": "geojson:Point",
        "links": {
          "@id": "http://www.w3.org/2000/01/rdf-schema#seeAlso",
          "@context": {
            "href": "@id",
            "title": "rdfs:label"
          }
        }
      }
    }
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/featureCollection/context.jsonld)

## Sources

* [OGC Testbed-17: OGC Features and Geometries JSON Engineering Report](http://docs.ogc.org/per/21-017r1.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/opengeospatial/bblocks](https://github.com/opengeospatial/bblocks)
* Path: `registereditems/geo/json-fg/featureCollection`

