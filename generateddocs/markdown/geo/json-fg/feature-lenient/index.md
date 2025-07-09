
# JSON-FG Feature - Lenient (Schema)

`ogc.geo.json-fg.feature-lenient` *v0.1*

A OGC Features and Geometries JSON (JSON-FG) Feature that does not require the "time" and "place" properties.

[*Status*](http://www.opengis.net/def/status): Stable

## Description

OGC Features and Geometries JSON (JSON-FG) extends GeoJSON to support a limited set of additional capabilities that are
out-of-scope for GeoJSON, but that are essential or important for a variety of use cases involving feature data.

This Building Block extends the standard JSON-FG one by removing the requirement to provide values for the 
"time" and "place" properties.

## Examples

### Example feature for a fence without time or place
#### json
```json
{
    "type": "Feature",
    "id": "fence.1",
    "conformsTo" : [ "[ogc-json-fg-1-0.2:core]", "[ogc-json-fg-1-0.2:3d]" ],
    "featureType": "fence",
    "geometry": null,
    "coordRefSys": "http://www.opengis.net/def/crs/EPSG/0/7415",
    "properties": null
}
```

#### jsonld
```jsonld
{
  "@context": "https://blocks.ogc.org/annotated-schemas/geo/json-fg/feature-lenient/context.jsonld",
  "type": "Feature",
  "id": "fence.1",
  "conformsTo": [
    "[ogc-json-fg-1-0.2:core]",
    "[ogc-json-fg-1-0.2:3d]"
  ],
  "featureType": "fence",
  "geometry": null,
  "coordRefSys": "http://www.opengis.net/def/crs/EPSG/0/7415",
  "properties": null
}
```

#### ttl
```ttl
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix ns1: <http://www.opengis.net/def/glossary/term/> .

<https://example.com/json-fg/fence.1> a <https://example.com/json-fg/fence>,
        geojson:Feature ;
    ns1:CoordinateReferenceSystemCRS "http://www.opengis.net/def/crs/EPSG/0/7415" .


```


### Example feature for a fence (full)
#### json
```json
{
    "type": "Feature",
    "id": "fence.1",
    "conformsTo" : [ "http://www.opengis.net/spec/json-fg-1/0.3/conf/core", "http://www.opengis.net/spec/json-fg-1/0.3/conf/prisms" ],
    "featureType": "fence",
    "time": {
        "interval": [
            "2022-07-12T16:55:18Z",
            ".."
        ]
    },
    "geometry": null,
    "coordRefSys": "http://www.opengis.net/def/crs/EPSG/0/7415",
    "place": {
        "type": "Prism",
        "base": {
            "type": "LineString",
            "coordinates": [
                [
                    81220.15,
                    455113.71
                ],
                [
                    81223.15,
                    455116.71
                ]
            ]
        },
        "lower": 2.02,
        "upper": 3.22
    },
    "properties": null
}
```

#### jsonld
```jsonld
{
  "@context": "https://blocks.ogc.org/annotated-schemas/geo/json-fg/feature-lenient/context.jsonld",
  "type": "Feature",
  "id": "fence.1",
  "conformsTo": [
    "http://www.opengis.net/spec/json-fg-1/0.3/conf/core",
    "http://www.opengis.net/spec/json-fg-1/0.3/conf/prisms"
  ],
  "featureType": "fence",
  "time": {
    "interval": [
      "2022-07-12T16:55:18Z",
      ".."
    ]
  },
  "geometry": null,
  "coordRefSys": "http://www.opengis.net/def/crs/EPSG/0/7415",
  "place": {
    "type": "Prism",
    "base": {
      "type": "LineString",
      "coordinates": [
        [
          81220.15,
          455113.71
        ],
        [
          81223.15,
          455116.71
        ]
      ]
    },
    "lower": 2.02,
    "upper": 3.22
  },
  "properties": null
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix ns1: <http://www.opengis.net/def/glossary/term/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix time: <http://www.w3.org/2006/time#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.com/json-fg/fence.1> a <https://example.com/json-fg/fence>,
        geojson:Feature ;
    dcterms:spatial [ a geojson:Prism ;
            geojson:prismBase [ a geojson:LineString ;
                    geojson:coordinates ( ( 8.122015e+04 4.551137e+05 ) ( 8.122315e+04 4.551167e+05 ) ) ] ;
            geojson:prismLower 2.02e+00 ;
            geojson:prismUpper 3.22e+00 ] ;
    dcterms:time [ time:hasTime ( "2022-07-12T16:55:18Z" ".." ) ] ;
    ns1:CoordinateReferenceSystemCRS "http://www.opengis.net/def/crs/EPSG/0/7415" .


```


### Example feature for a building without time or place
#### json
```json
{
   "type": "Feature",
   "id": "DENW19AL0000giv5BL",
   "conformsTo": [
      "[ogc-json-fg-1-0.2:core]"         ,
      "[ogc-json-fg-1-0.2:types-schemas]",
      "[ogc-json-fg-1-0.2:3d]"
   ],
   "featureType": "app:building",
   "featureSchema": "https://example.org/data/v1/collections/buildings/schema",
   "coordRefSys": "http://www.opengis.net/def/crs/EPSG/0/5555",
   "geometry": {
      "type": "Polygon",
      "coordinates": [
         [
            [8.7092045, 51.5035285, 100],
            [8.7093128, 51.5034570, 100],
            [8.7093919, 51.5035030, 100],
            [8.7092837, 51.5035747, 100],
            [8.7092045, 51.5035285, 100]
         ]
      ]
   },
   "links": [
      {
         "href": "https://example.org/data/v1/collections/cadastralparcel/items/05297001600313______",
         "rel": "http://www.opengis.net/def/rel/ogc/1.0/within",
         "title": "Cadastral parcel 313 in district Wünnenberg (016)"
      },
      {
         "href" : "https://inspire.ec.europa.eu/featureconcept/Building",
         "rel"  : "type"                                                ,
         "title": "This feature is of type 'building'"
      }
   ],
   "properties": {
      "lastChange": "2014-04-24T10:50:18Z",
      "built": "2012-03",
      "function": "Agricultural building",
      "height_m": 20.0,
      "owners": [
         {"href": "https://example.org/john-doe", "title": "John Doe"},
         {"href": "https://example.org/jane-doe", "title": "Jane Doe"}
      ]
   }
}

```

#### jsonld
```jsonld
{
  "@context": "https://blocks.ogc.org/annotated-schemas/geo/json-fg/feature-lenient/context.jsonld",
  "type": "Feature",
  "id": "DENW19AL0000giv5BL",
  "conformsTo": [
    "[ogc-json-fg-1-0.2:core]",
    "[ogc-json-fg-1-0.2:types-schemas]",
    "[ogc-json-fg-1-0.2:3d]"
  ],
  "featureType": "app:building",
  "featureSchema": "https://example.org/data/v1/collections/buildings/schema",
  "coordRefSys": "http://www.opengis.net/def/crs/EPSG/0/5555",
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          8.7092045,
          51.5035285,
          100
        ],
        [
          8.7093128,
          51.503457,
          100
        ],
        [
          8.7093919,
          51.503503,
          100
        ],
        [
          8.7092837,
          51.5035747,
          100
        ],
        [
          8.7092045,
          51.5035285,
          100
        ]
      ]
    ]
  },
  "links": [
    {
      "href": "https://example.org/data/v1/collections/cadastralparcel/items/05297001600313______",
      "rel": "http://www.opengis.net/def/rel/ogc/1.0/within",
      "title": "Cadastral parcel 313 in district W\u00fcnnenberg (016)"
    },
    {
      "href": "https://inspire.ec.europa.eu/featureconcept/Building",
      "rel": "type",
      "title": "This feature is of type 'building'"
    }
  ],
  "properties": {
    "lastChange": "2014-04-24T10:50:18Z",
    "built": "2012-03",
    "function": "Agricultural building",
    "height_m": 20.0,
    "owners": [
      {
        "href": "https://example.org/john-doe",
        "title": "John Doe"
      },
      {
        "href": "https://example.org/jane-doe",
        "title": "Jane Doe"
      }
    ]
  }
}
```

#### ttl
```ttl
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix ns1: <http://www.iana.org/assignments/> .
@prefix ns2: <http://www.opengis.net/def/glossary/term/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.com/json-fg/DENW19AL0000giv5BL> a <app:building>,
        geojson:Feature ;
    ns2:CoordinateReferenceSystemCRS "http://www.opengis.net/def/crs/EPSG/0/5555" ;
    rdfs:seeAlso [ rdfs:label "Cadastral parcel 313 in district Wünnenberg (016)" ;
            ns1:relation <http://www.opengis.net/def/rel/ogc/1.0/within> ;
            oa:hasTarget <https://example.org/data/v1/collections/cadastralparcel/items/05297001600313______> ],
        [ rdfs:label "This feature is of type 'building'" ;
            ns1:relation <http://www.iana.org/assignments/relation/type> ;
            oa:hasTarget <https://inspire.ec.europa.eu/featureconcept/Building> ] ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( 8.709205e+00 5.150353e+01 100 ) ( 8.709313e+00 5.150346e+01 100 ) ( 8.709392e+00 5.15035e+01 100 ) ( 8.709284e+00 5.150357e+01 100 ) ( 8.709205e+00 5.150353e+01 100 ) ) ) ] .


```


### Example feature for a building (full)
#### json
```json
{
   "type": "Feature",
   "id": "DENW19AL0000giv5BL",
   "conformsTo": [
      "http://www.opengis.net/spec/json-fg-1/0.3/conf/core"         ,
      "http://www.opengis.net/spec/json-fg-1/0.3/conf/types-schemas",
      "http://www.opengis.net/spec/json-fg-1/0.3/conf/polyhedra"
   ],
   "featureType": "app:building",
   "featureSchema": "https://example.org/data/v1/collections/buildings/schema",
   "time": { "interval": ["2014-04-24T10:50:18Z", ".."] },
   "coordRefSys": "http://www.opengis.net/def/crs/EPSG/0/5555",
   "place": {
      "type": "Polyhedron",
      "coordinates": [
         [
            [
               [
                  [479816.670, 5705861.672, 100],
                  [479822.187, 5705866.783, 100],
                  [479829.666, 5705858.785, 100],
                  [479824.155, 5705853.684, 100],
                  [479816.670, 5705861.672, 100]
               ]
            ],
            [
               [
                  [479816.670, 5705861.672, 110],
                  [479824.155, 5705853.684, 110],
                  [479829.666, 5705858.785, 120],
                  [479822.187, 5705866.783, 120],
                  [479816.670, 5705861.672, 110]
               ]
            ],
            [
               [
                  [479816.670, 5705861.672, 110],
                  [479816.670, 5705861.672, 100],
                  [479824.155, 5705853.684, 100],
                  [479824.155, 5705853.684, 110],
                  [479816.670, 5705861.672, 110]
               ]
            ],
            [
               [
                  [479824.155, 5705853.684, 110],
                  [479824.155, 5705853.684, 100],
                  [479829.666, 5705858.785, 100],
                  [479829.666, 5705858.785, 120],
                  [479824.155, 5705853.684, 110]
               ]
            ],
            [
               [
                  [479829.666, 5705858.785, 120],
                  [479829.666, 5705858.785, 100],
                  [479822.187, 5705866.783, 100],
                  [479822.187, 5705866.783, 120],
                  [479829.666, 5705858.785, 120]
               ]
            ],
            [
               [
                  [479822.187, 5705866.783, 120],
                  [479822.187, 5705866.783, 100],
                  [479816.670, 5705861.672, 100],
                  [479816.670, 5705861.672, 110],
                  [479822.187, 5705866.783, 120]
               ]
            ]
         ]
      ]
   },
   "geometry": {
      "type": "Polygon",
      "coordinates": [
         [
            [8.7092045, 51.5035285, 100],
            [8.7093128, 51.5034570, 100],
            [8.7093919, 51.5035030, 100],
            [8.7092837, 51.5035747, 100],
            [8.7092045, 51.5035285, 100]
         ]
      ]
   },
   "links": [
      {
         "href": "https://example.org/data/v1/collections/cadastralparcel/items/05297001600313______",
         "rel": "http://www.opengis.net/def/rel/ogc/1.0/within",
         "title": "Cadastral parcel 313 in district Wünnenberg (016)"
      },
      {
         "href" : "https://inspire.ec.europa.eu/featureconcept/Building",
         "rel"  : "type"                                                ,
         "title": "This feature is of type 'building'"
      }
   ],
   "properties": {
      "lastChange": "2014-04-24T10:50:18Z",
      "built": "2012-03",
      "function": "Agricultural building",
      "height_m": 20.0,
      "owners": [
         {"href": "https://example.org/john-doe", "title": "John Doe"},
         {"href": "https://example.org/jane-doe", "title": "Jane Doe"}
      ]
   }
}

```

#### jsonld
```jsonld
{
  "@context": "https://blocks.ogc.org/annotated-schemas/geo/json-fg/feature-lenient/context.jsonld",
  "type": "Feature",
  "id": "DENW19AL0000giv5BL",
  "conformsTo": [
    "http://www.opengis.net/spec/json-fg-1/0.3/conf/core",
    "http://www.opengis.net/spec/json-fg-1/0.3/conf/types-schemas",
    "http://www.opengis.net/spec/json-fg-1/0.3/conf/polyhedra"
  ],
  "featureType": "app:building",
  "featureSchema": "https://example.org/data/v1/collections/buildings/schema",
  "time": {
    "interval": [
      "2014-04-24T10:50:18Z",
      ".."
    ]
  },
  "coordRefSys": "http://www.opengis.net/def/crs/EPSG/0/5555",
  "place": {
    "type": "Polyhedron",
    "coordinates": [
      [
        [
          [
            [
              479816.67,
              5705861.672,
              100
            ],
            [
              479822.187,
              5705866.783,
              100
            ],
            [
              479829.666,
              5705858.785,
              100
            ],
            [
              479824.155,
              5705853.684,
              100
            ],
            [
              479816.67,
              5705861.672,
              100
            ]
          ]
        ],
        [
          [
            [
              479816.67,
              5705861.672,
              110
            ],
            [
              479824.155,
              5705853.684,
              110
            ],
            [
              479829.666,
              5705858.785,
              120
            ],
            [
              479822.187,
              5705866.783,
              120
            ],
            [
              479816.67,
              5705861.672,
              110
            ]
          ]
        ],
        [
          [
            [
              479816.67,
              5705861.672,
              110
            ],
            [
              479816.67,
              5705861.672,
              100
            ],
            [
              479824.155,
              5705853.684,
              100
            ],
            [
              479824.155,
              5705853.684,
              110
            ],
            [
              479816.67,
              5705861.672,
              110
            ]
          ]
        ],
        [
          [
            [
              479824.155,
              5705853.684,
              110
            ],
            [
              479824.155,
              5705853.684,
              100
            ],
            [
              479829.666,
              5705858.785,
              100
            ],
            [
              479829.666,
              5705858.785,
              120
            ],
            [
              479824.155,
              5705853.684,
              110
            ]
          ]
        ],
        [
          [
            [
              479829.666,
              5705858.785,
              120
            ],
            [
              479829.666,
              5705858.785,
              100
            ],
            [
              479822.187,
              5705866.783,
              100
            ],
            [
              479822.187,
              5705866.783,
              120
            ],
            [
              479829.666,
              5705858.785,
              120
            ]
          ]
        ],
        [
          [
            [
              479822.187,
              5705866.783,
              120
            ],
            [
              479822.187,
              5705866.783,
              100
            ],
            [
              479816.67,
              5705861.672,
              100
            ],
            [
              479816.67,
              5705861.672,
              110
            ],
            [
              479822.187,
              5705866.783,
              120
            ]
          ]
        ]
      ]
    ]
  },
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          8.7092045,
          51.5035285,
          100
        ],
        [
          8.7093128,
          51.503457,
          100
        ],
        [
          8.7093919,
          51.503503,
          100
        ],
        [
          8.7092837,
          51.5035747,
          100
        ],
        [
          8.7092045,
          51.5035285,
          100
        ]
      ]
    ]
  },
  "links": [
    {
      "href": "https://example.org/data/v1/collections/cadastralparcel/items/05297001600313______",
      "rel": "http://www.opengis.net/def/rel/ogc/1.0/within",
      "title": "Cadastral parcel 313 in district W\u00fcnnenberg (016)"
    },
    {
      "href": "https://inspire.ec.europa.eu/featureconcept/Building",
      "rel": "type",
      "title": "This feature is of type 'building'"
    }
  ],
  "properties": {
    "lastChange": "2014-04-24T10:50:18Z",
    "built": "2012-03",
    "function": "Agricultural building",
    "height_m": 20.0,
    "owners": [
      {
        "href": "https://example.org/john-doe",
        "title": "John Doe"
      },
      {
        "href": "https://example.org/jane-doe",
        "title": "Jane Doe"
      }
    ]
  }
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix ns1: <http://www.iana.org/assignments/> .
@prefix ns2: <http://www.opengis.net/def/glossary/term/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix time: <http://www.w3.org/2006/time#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.com/json-fg/DENW19AL0000giv5BL> a <app:building>,
        geojson:Feature ;
    dcterms:spatial [ a geojson:Polyhedron ;
            geojson:coordinates ( ( ( ( ( 4.798167e+05 5.705862e+06 100 ) ( 4.798222e+05 5.705867e+06 100 ) ( 4.798297e+05 5.705859e+06 100 ) ( 4.798242e+05 5.705854e+06 100 ) ( 4.798167e+05 5.705862e+06 100 ) ) ) ( ( ( 4.798167e+05 5.705862e+06 110 ) ( 4.798242e+05 5.705854e+06 110 ) ( 4.798297e+05 5.705859e+06 120 ) ( 4.798222e+05 5.705867e+06 120 ) ( 4.798167e+05 5.705862e+06 110 ) ) ) ( ( ( 4.798167e+05 5.705862e+06 110 ) ( 4.798167e+05 5.705862e+06 100 ) ( 4.798242e+05 5.705854e+06 100 ) ( 4.798242e+05 5.705854e+06 110 ) ( 4.798167e+05 5.705862e+06 110 ) ) ) ( ( ( 4.798242e+05 5.705854e+06 110 ) ( 4.798242e+05 5.705854e+06 100 ) ( 4.798297e+05 5.705859e+06 100 ) ( 4.798297e+05 5.705859e+06 120 ) ( 4.798242e+05 5.705854e+06 110 ) ) ) ( ( ( 4.798297e+05 5.705859e+06 120 ) ( 4.798297e+05 5.705859e+06 100 ) ( 4.798222e+05 5.705867e+06 100 ) ( 4.798222e+05 5.705867e+06 120 ) ( 4.798297e+05 5.705859e+06 120 ) ) ) ( ( ( 4.798222e+05 5.705867e+06 120 ) ( 4.798222e+05 5.705867e+06 100 ) ( 4.798167e+05 5.705862e+06 100 ) ( 4.798167e+05 5.705862e+06 110 ) ( 4.798222e+05 5.705867e+06 120 ) ) ) ) ) ] ;
    dcterms:time [ time:hasTime ( "2014-04-24T10:50:18Z" ".." ) ] ;
    ns2:CoordinateReferenceSystemCRS "http://www.opengis.net/def/crs/EPSG/0/5555" ;
    rdfs:seeAlso [ rdfs:label "Cadastral parcel 313 in district Wünnenberg (016)" ;
            ns1:relation <http://www.opengis.net/def/rel/ogc/1.0/within> ;
            oa:hasTarget <https://example.org/data/v1/collections/cadastralparcel/items/05297001600313______> ],
        [ rdfs:label "This feature is of type 'building'" ;
            ns1:relation <http://www.iana.org/assignments/relation/type> ;
            oa:hasTarget <https://inspire.ec.europa.eu/featureconcept/Building> ] ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( 8.709205e+00 5.150353e+01 100 ) ( 8.709313e+00 5.150346e+01 100 ) ( 8.709392e+00 5.15035e+01 100 ) ( 8.709284e+00 5.150357e+01 100 ) ( 8.709205e+00 5.150353e+01 100 ) ) ) ] .


```


### Feature with a custom geometry (Arc) without time
This feature follows
[the Arc extension](https://github.com/opengeospatial/ogc-feat-geo-json/blob/main/core/examples/extensions/arc.json)
for the `place` property.

#### json
```json
{
  "type": "Feature",
  "id": "my-space-station",
  "conformsTo": [
    "[ogc-json-fg-1-0.2:core]",
    "[ogc-json-fg-1-0.2:3d]"
  ],
  "featureType": "space-station",
  "geometry": null,
  "coordRefSys": "http://www.opengis.net/def/crs/EPSG/0/7415",
  "place": {
    "type": "Arc",
    "coordinates": [
      81220.15,
      455113.71,
      44143.21
    ]
  },
  "properties": {}
}

```

#### jsonld
```jsonld
{
  "@context": "https://blocks.ogc.org/annotated-schemas/geo/json-fg/feature-lenient/context.jsonld",
  "type": "Feature",
  "id": "my-space-station",
  "conformsTo": [
    "[ogc-json-fg-1-0.2:core]",
    "[ogc-json-fg-1-0.2:3d]"
  ],
  "featureType": "space-station",
  "geometry": null,
  "coordRefSys": "http://www.opengis.net/def/crs/EPSG/0/7415",
  "place": {
    "type": "Arc",
    "coordinates": [
      81220.15,
      455113.71,
      44143.21
    ]
  },
  "properties": {}
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix ns1: <http://www.opengis.net/def/glossary/term/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.com/json-fg/my-space-station> a <https://example.com/json-fg/space-station>,
        geojson:Feature ;
    dcterms:spatial [ a <https://example.com/json-fg/Arc> ;
            geojson:coordinates ( 8.122015e+04 4.551137e+05 4.414321e+04 ) ] ;
    ns1:CoordinateReferenceSystemCRS "http://www.opengis.net/def/crs/EPSG/0/7415" .


```

## Schema

```yaml
allOf:
- $ref: https://blocks.ogc.org/annotated-schemas/geo/features/feature/schema.yaml
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
      x-jsonld-id: '@type'
    id:
      oneOf:
      - type: number
      - type: string
      x-jsonld-id: '@id'
    featureType:
      $ref: https://beta.schemas.opengis.net/json-fg/featuretype.json
      x-jsonld-id: '@type'
    links:
      type: array
      items:
        allOf:
        - $ref: https://beta.schemas.opengis.net/json-fg/link.json
        - $ref: https://blocks.ogc.org/annotated-schemas/ogc-utils/json-link/schema.yaml
      x-jsonld-id: http://www.w3.org/2000/01/rdf-schema#seeAlso
    time:
      $ref: https://blocks.ogc.org/annotated-schemas/geo/json-fg/time/schema.yaml
      x-jsonld-id: http://purl.org/dc/terms/time
    coordRefSys:
      $ref: https://beta.schemas.opengis.net/json-fg/coordrefsys.json
      x-jsonld-id: http://www.opengis.net/def/glossary/term/CoordinateReferenceSystemCRS
    place:
      $ref: https://beta.schemas.opengis.net/json-fg/place.json
      x-jsonld-id: http://purl.org/dc/terms/spatial
    geometry:
      $ref: https://beta.schemas.opengis.net/json-fg/geometry.json
      x-jsonld-id: https://purl.org/geojson/vocab#geometry
    properties:
      oneOf:
      - type: 'null'
      - type: object
      x-jsonld-id: '@nest'
x-jsonld-extra-terms:
  Feature: https://purl.org/geojson/vocab#Feature
  FeatureCollection: https://purl.org/geojson/vocab#FeatureCollection
  GeometryCollection: https://purl.org/geojson/vocab#GeometryCollection
  LineString: https://purl.org/geojson/vocab#LineString
  MultiLineString: https://purl.org/geojson/vocab#MultiLineString
  MultiPoint: https://purl.org/geojson/vocab#MultiPoint
  MultiPolygon: https://purl.org/geojson/vocab#MultiPolygon
  Point: https://purl.org/geojson/vocab#Point
  Polygon: https://purl.org/geojson/vocab#Polygon
  Polyhedron: https://purl.org/geojson/vocab#Polyhedron
  MultiPolyhedron: https://purl.org/geojson/vocab#MultiPolyhedron
  Prism:
    x-jsonld-id: https://purl.org/geojson/vocab#Prism
    x-jsonld-context:
      base: https://purl.org/geojson/vocab#prismBase
      lower: https://purl.org/geojson/vocab#prismLower
      upper: https://purl.org/geojson/vocab#prismUpper
  MultiPrism:
    x-jsonld-id: https://purl.org/geojson/vocab#MultiPrism
    x-jsonld-context:
      prisms: https://purl.org/geojson/vocab#prisms
  bbox:
    x-jsonld-container: '@list'
    x-jsonld-id: https://purl.org/geojson/vocab#bbox
  coordinates:
    x-jsonld-container: '@list'
    x-jsonld-id: https://purl.org/geojson/vocab#coordinates
  features:
    x-jsonld-container: '@set'
    x-jsonld-id: https://purl.org/geojson/vocab#features
  geometries:
    x-jsonld-id: https://purl.org/geojson/vocab#geometry
    x-jsonld-container: '@list'
x-jsonld-prefixes:
  geojson: https://purl.org/geojson/vocab#
  rdfs: http://www.w3.org/2000/01/rdf-schema#
  dct: http://purl.org/dc/terms/
  owlTime: http://www.w3.org/2006/time#

```

Links to the schema:

* YAML version: [schema.yaml](https://blocks.ogc.org/annotated-schemas/geo/json-fg/feature-lenient/schema.json)
* JSON version: [schema.json](https://blocks.ogc.org/annotated-schemas/geo/json-fg/feature-lenient/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "type": "@type",
    "id": "@id",
    "properties": "@nest",
    "geometry": "geojson:geometry",
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
      "@id": "geojson:features"
    },
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
          "@type": "xsd:date"
        },
        "timestamp": {
          "@id": "owlTime:hasTime",
          "@type": "xsd:dateTime"
        },
        "interval": {
          "@id": "owlTime:hasTime",
          "@container": "@list"
        }
      },
      "@id": "dct:time"
    },
    "coordRefSys": "http://www.opengis.net/def/glossary/term/CoordinateReferenceSystemCRS",
    "place": "dct:spatial",
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
    "geojson": "https://purl.org/geojson/vocab#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "oa": "http://www.w3.org/ns/oa#",
    "dct": "http://purl.org/dc/terms/",
    "owlTime": "http://www.w3.org/2006/time#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://blocks.ogc.org/annotated-schemas/geo/json-fg/feature-lenient/context.jsonld)

## Sources

* [OGC Testbed-17: OGC Features and Geometries JSON Engineering Report](http://docs.ogc.org/per/21-017r1.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/opengeospatial/bblocks](https://github.com/opengeospatial/bblocks)
* Path: `registereditems/geo/json-fg/feature-lenient`

