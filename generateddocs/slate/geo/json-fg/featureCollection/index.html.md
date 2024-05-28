---
title: JSON-FG Feature Collection (Schema)

language_tabs:
  - json: JSON
  - jsonld: JSON-LD
  - turtle: RDF/Turtle

toc_footers:
  - Version 0.1
  - <a href='#'>JSON-FG Feature Collection</a>
  - <a href='https://blocks.ogc.org/register.html'>Building Blocks register</a>

search: true

code_clipboard: true

meta:
  - name: JSON-FG Feature Collection (Schema)
---


# JSON-FG Feature Collection `ogc.geo.json-fg.featureCollection`

A collection of OGC Features and Geometries JSON (JSON-FG) Features, extending GeoJSON to support a limited set of additional capabilities that are out-of-scope for GeoJSON, but that are important for a variety of use cases involving feature data.

<p class="status">
    <span data-rainbow-uri="http://www.opengis.net/def/status">Status</span>:
    <a href="http://www.opengis.net/def/status/stable" target="_blank" data-rainbow-uri>Stable</a>
</p>

<aside class="success">
This building block is <strong><a href="https://github.com/opengeospatial/bblocks/blob/master/tests/geo/json-fg/featureCollection/" target="_blank">valid</a></strong>
</aside>

# Description

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
# Examples

## Example



```json
{
  "@context": {
    "my": "http://my.org/featureTypes/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "name": "skos:prefLabel"
  },
  "id": "MyFeatureCollection",
  "name": "MyFeatureCollection",
  "type": "FeatureCollection",
  "features": [
    {
      "id": "f1",
      "type": "Feature",
      "featureType": "my:FeatureType",
      "geometry": null,
      "time": null,
      "coordRefSys": "EPSG",
      "place": {
        "type": "Point",
        "coordinates": [
          174.7501603083,
          -36.9307359096
        ]
      },
      "properties": {
        "comment": "An attribute value"
      }
    }
  ]
}
```

<blockquote class="lang-specific json">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/bblocks/tests/geo/json-fg/featureCollection/example_1_1.json">Open in new window</a>
    <a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=json&amp;dataUrl=https%3A%2F%2Fopengeospatial.github.io%2Fbblocks%2Ftests%2Fgeo%2Fjson-fg%2FfeatureCollection%2Fexample_1_1.json&amp;expand=2&amp;option=%7B%22showTable%22%3A+false%7D">View on JSON Viewer</a></p>
</blockquote>




```jsonld
{
  "@context": [
    "https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/featureCollection/context.jsonld",
    {
      "my": "http://my.org/featureTypes/",
      "skos": "http://www.w3.org/2004/02/skos/core#",
      "name": "skos:prefLabel"
    }
  ],
  "id": "MyFeatureCollection",
  "name": "MyFeatureCollection",
  "type": "FeatureCollection",
  "features": [
    {
      "id": "f1",
      "type": "Feature",
      "featureType": "my:FeatureType",
      "geometry": null,
      "time": null,
      "coordRefSys": "EPSG",
      "place": {
        "type": "Point",
        "coordinates": [
          174.7501603083,
          -36.9307359096
        ]
      },
      "properties": {
        "comment": "An attribute value"
      }
    }
  ]
}
```

<blockquote class="lang-specific jsonld">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/bblocks/tests/geo/json-fg/featureCollection/example_1_1.jsonld">Open in new window</a>
    <a target="_blank" href="https://json-ld.org/playground/#json-ld=https%3A%2F%2Fopengeospatial.github.io%2Fbblocks%2Ftests%2Fgeo%2Fjson-fg%2FfeatureCollection%2Fexample_1_1.jsonld">View on JSON-LD Playground</a>
</blockquote>




```turtle
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix my: <http://my.org/featureTypes/> .
@prefix ns1: <http://www.opengis.net/def/glossary/term/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<http://www.example.com/features/MyFeatureCollection> a geojson:FeatureCollection ;
    skos:prefLabel "MyFeatureCollection" ;
    geojson:features <http://www.example.com/features/f1> .

<http://www.example.com/features/f1> a my:FeatureType,
        geojson:Feature ;
    dcterms:spatial [ a geojson:Point ;
            geojson:coordinates ( 1.747502e+02 -3.693074e+01 ) ] ;
    ns1:CoordinateReferenceSystemCRS "EPSG" .


```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://opengeospatial.github.io/bblocks/tests/geo/json-fg/featureCollection/example_1_1.ttl">Open in new window</a>
</blockquote>


Minimal example of this schema.

NB. uses a local @context in the data example where application specialisations would apply such mappings.


# JSON Schema

```yaml--schema
$schema: https://json-schema.org/draft/2019-09/schema
title: a JSON-FG Feature Collection
description: This JSON Schema is part of JSON-FG version 0.1.1
type: object
required:
- type
- features
allOf:
- $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/geo/features/featureCollection/schema.yaml
- properties:
    type:
      type: string
      enum:
      - FeatureCollection
      x-jsonld-id: '@type'
    featureType:
      $ref: https://beta.schemas.opengis.net/json-fg/featuretype.json
      x-jsonld-id: https://purl.org/geojson/vocab#collectionFeatureType
    geometryDimension:
      type: integer
      minimum: 0
      maximum: 3
    coordRefSys:
      $ref: https://beta.schemas.opengis.net/json-fg/coordrefsys.json
    links:
      type: array
      items:
        allOf:
        - $ref: https://beta.schemas.opengis.net/json-fg/link.json
        - $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/json-link/schema.yaml
      x-jsonld-id: rdfs:seeAlso
    features:
      type: array
      items:
        $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/feature/schema.yaml
      x-jsonld-container: '@set'
      x-jsonld-id: https://purl.org/geojson/vocab#features
x-jsonld-prefixes:
  geojson: https://purl.org/geojson/vocab#

```

> <a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=yaml&amp;dataUrl=https%3A%2F%2Fopengeospatial.github.io%2Fbblocks%2Fannotated-schemas%2Fgeo%2Fjson-fg%2FfeatureCollection%2Fschema.yaml&amp;expand=2&amp;option=%7B%22showTable%22%3A+false%7D">View on YAML Viewer</a>

Links to the schema:

* YAML version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/featureCollection/schema.yaml" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/featureCollection/schema.yaml</a>
* JSON version: <a href="https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/featureCollection/schema.json" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/featureCollection/schema.json</a>


# JSON-LD Context

```json--ldContext
{
  "@context": {
    "links": {
      "@context": {
        "href": {
          "@type": "@id",
          "@id": "oa:hasTarget"
        },
        "rel": {
          "@context": {
            "@base": "http://www.iana.org/assignments/relation/"
          },
          "@id": "http://www.iana.org/assignments/relation",
          "@type": "@id"
        },
        "type": "dct:type",
        "hreflang": "dct:language",
        "title": "rdfs:label",
        "length": "dct:extent"
      },
      "@id": "rdfs:seeAlso"
    },
    "type": "@type",
    "id": "@id",
    "properties": "@nest",
    "geometry": {
      "@context": {},
      "@id": "geojson:geometry"
    },
    "bbox": {
      "@container": "@list",
      "@id": "geojson:bbox"
    },
    "Feature": "geojson:Feature",
    "FeatureCollection": "geojson:FeatureCollection",
    "GeometryCollection": "geojson:GeometryCollection",
    "LineString": "geojson:LineString",
    "MultiLineString": "geojson:MultiLineString",
    "MultiPoint": "geojson:MultiPoint",
    "MultiPolygon": "geojson:MultiPolygon",
    "Point": "geojson:Point",
    "Polygon": "geojson:Polygon",
    "features": {
      "@container": "@set",
      "@id": "geojson:features",
      "@context": {
        "links": {
          "@context": {
            "href": {
              "@type": "@id",
              "@id": "oa:hasTarget"
            },
            "rel": {
              "@context": {
                "@base": "http://www.iana.org/assignments/relation/"
              },
              "@id": "http://www.iana.org/assignments/relation",
              "@type": "@id"
            },
            "type": "dct:type",
            "hreflang": "dct:language",
            "title": "rdfs:label",
            "length": "dct:extent"
          },
          "@id": "rdfs:seeAlso"
        },
        "featureType": "@type",
        "time": {
          "@context": {
            "date": {
              "@id": "owlTime:hasTime",
              "@type": "http://www.w3.org/2001/XMLSchema#date"
            },
            "timestamp": {
              "@id": "owlTime:hasTime",
              "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
            },
            "interval": {
              "@id": "owlTime:hasTime",
              "@container": "@list"
            }
          },
          "@id": "dct:time"
        },
        "coordRefSys": "http://www.opengis.net/def/glossary/term/CoordinateReferenceSystemCRS",
        "place": {
          "@context": {
            "@base": "https://purl.org/geojson/vocab#"
          },
          "@id": "dct:spatial"
        }
      }
    },
    "featureType": "geojson:collectionFeatureType",
    "Polyhedron": "geojson:Polyhedron",
    "MultiPolyhedron": "geojson:MultiPolyhedron",
    "Prism": {
      "@id": "geojson:Prism",
      "@context": {
        "base": "geojson:prismBase",
        "lower": "geojson:prismLower",
        "upper": "geojson:prismUpper"
      }
    },
    "MultiPrism": {
      "@id": "geojson:MultiPrism",
      "@context": {
        "prisms": "geojson:prisms"
      }
    },
    "coordinates": {
      "@container": "@list",
      "@id": "geojson:coordinates"
    },
    "geometries": {
      "@id": "geojson:geometry",
      "@container": "@list"
    },
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "oa": "http://www.w3.org/ns/oa#",
    "dct": "http://purl.org/dc/terms/",
    "geojson": "https://purl.org/geojson/vocab#",
    "owlTime": "http://www.w3.org/2006/time#",
    "time": "http://www.w3.org/2006/time#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "@version": 1.1
  }
}
```

> <a target="_blank" href="https://json-ld.org/playground/#json-ld=https%3A%2F%2Fopengeospatial.github.io%2Fbblocks%2Fannotated-schemas%2Fgeo%2Fjson-fg%2FfeatureCollection%2Fcontext.jsonld">View on JSON-LD Playground</a>

You can find the full JSON-LD context here:
<a href="https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/featureCollection/context.jsonld" target="_blank">https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/featureCollection/context.jsonld</a>

# References

* [OGC Testbed-17: OGC Features and Geometries JSON Engineering Report](http://docs.ogc.org/per/21-017r1.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: <a href="https://github.com/opengeospatial/bblocks" target="_blank">https://github.com/opengeospatial/bblocks</a>
* Path:
<code><a href="https://github.com/opengeospatial/bblocks/blob/HEAD/registereditems/geo/json-fg/featureCollection" target="_blank">registereditems/geo/json-fg/featureCollection</a></code>

