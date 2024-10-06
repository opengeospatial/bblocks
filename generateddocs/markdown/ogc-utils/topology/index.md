
# Geometry using references (Schema)

`ogc.ogc-utils.topology` *v0.1*

Demonstration of a schema using coordinates of points, withpout duplication

[*Status*](http://www.opengis.net/def/status): Under development

## Description

A datatype containing ordered list of references to other features. 

Other features may be either features with topology properties or GeoJSON (or FG-JSON) point objects.

This is a generalisation of the TopoJSON concept using inline data, and not limited to linestrings.


## Examples

### Example Topology object
See panel to right - note that a more user friendly "collapsable" version is in development. 
#### json
```json
{
  "type": "LineString",
  "references": [
    "P1",
    "P2"
  ]
}
```

#### jsonld
```jsonld
{
  "@context": "https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/topology/context.jsonld",
  "type": "LineString",
  "references": [
    "P1",
    "P2"
  ]
}
```

#### ttl
```ttl
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .

[] a geojson:LineString ;
    geojson:relatedFeatures ( <http://www.example.com/features/P1> <http://www.example.com/features/P2> ) .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: feature with geometry by reference
properties:
  type:
    $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/iri-or-curie/schema.yaml
    x-jsonld-id: '@type'
  references:
    type: array
    items:
      $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/iri-or-curie/schema.yaml
    x-jsonld-id: https://purl.org/geojson/vocab#relatedFeatures
    x-jsonld-type: '@id'
    x-jsonld-container: '@list'
required:
- references
- type
x-jsonld-extra-terms:
  LineString: https://purl.org/geojson/vocab#LineString
x-jsonld-prefixes:
  geojson: https://purl.org/geojson/vocab#
  csdm: https://linked.data.gov.au/def/csdm/
  dct: http://purl.org/dc/terms/

```

Links to the schema:

* YAML version: [schema.yaml](https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/topology/schema.json)
* JSON version: [schema.json](https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/topology/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "type": "@type",
    "references": {
      "@id": "geojson:relatedFeatures",
      "@type": "@id",
      "@container": "@list"
    },
    "LineString": "geojson:LineString",
    "geojson": "https://purl.org/geojson/vocab#",
    "csdm": "https://linked.data.gov.au/def/csdm/",
    "dct": "http://purl.org/dc/terms/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/topology/context.jsonld)


# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/opengeospatial/bblocks](https://github.com/opengeospatial/bblocks)
* Path: `registereditems/ogc-utils/topology`

