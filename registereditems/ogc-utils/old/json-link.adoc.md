Version: 1.0.1

# Overview

Web linking according to
[RFC 8288](http://tools.ietf.org/rfc/rfc8288.txt) is used to express
relationships between resources. The JSON object representation of links
described here is used consistently in OGC API’s.

[**Maturity**](https://github.com/cportele/ogcapi-building-blocks#building-block-maturity):
Mature

# Pre-defined properties

<table>
<caption>Properties</caption>
<colgroup>
<col style="width: 20%" />
<col style="width: 10%" />
<col style="width: 70%" />
</colgroup>
<thead>
<tr class="header">
<th>Property</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>href</p></td>
<td><p>URI</p></td>
<td><p><strong>REQUIRED</strong>. The link target URI, specified as an absolute or relative URI-Reference.</p></td>
</tr>
<tr class="even">
<td><p>rel</p></td>
<td><p>String</p></td>
<td><p><strong>REQUIRED</strong>. The link relation type(s). It identifies the semantics of the link, or it indicates that the target resource has particular attributes, or exhibits particular behaviors. All link relation types discussed in OGC API standards are either specified in the <a href="https://www.iana.org/assignments/link-relations">IANA link relation type register</a> or the <a href="http://www.opengis.net/def/rel">OGC link relation type register</a>. Link relation types that are URIs may also be encoded as a <a href="https://www.w3.org/TR/curie/">Safe CURIE</a> where the prefix has to be registered in the <a href="http://www.opengis.net/def/prefix">OGC prefix register</a> (which does not exist yet). The default prefix expands to <code>http://www.opengis.net/def/rel/ogc/1.0/</code>. An example of a Safe CURIE is <code>[conformance]</code> for <code>http://www.opengis.net/def/rel/ogc/1.0/conformance</code>.</p></td>
</tr>
<tr class="odd">
<td><p>anchor</p></td>
<td><p>String</p></td>
<td><p>The anchor of the link. The default anchor is the JSON object that contains the JSON member that contains the Link object. For example, in a document that is a JSON object with a "links" member the anchor of each link in the "links" array is the document URI. In a Link object that is embedded deeper inside a JSON document, the anchor is the document URI with a URI fragment that is the JSON Pointer of the JSON member that contains the Link object.</p>
<p>The <code>anchor</code> attribute is currently not mentioned in OGC API Features.</p></td>
</tr>
<tr class="even">
<td><p>type</p></td>
<td><p>String</p></td>
<td><p>The <code>type</code> attribute, when present, is a hint indicating what the media type of the result of dereferencing the link should be. Note that this is only a hint; for example, it does not override the <code>Content-Type</code> header field of a HTTP response obtained by actually following the link.</p></td>
</tr>
<tr class="odd">
<td><p>title</p></td>
<td><p>String</p></td>
<td><p>The <code>title</code> attribute, when present, is used to label the destination of a link such that it can be used as a human-readable identifier in the language indicated by the <code>Content-Language</code> header field (if present).</p></td>
</tr>
<tr class="even">
<td><p>hreflang</p></td>
<td><p>String</p></td>
<td><p>The <code>hreflang</code> attribute, when present, is a hint indicating what the language of the result of dereferencing the link should be. Note that this is only a hint; for example, it does not override the <code>Content-Language</code> header field of a HTTP response obtained by actually following the link.</p></td>
</tr>
<tr class="odd">
<td><p>length</p></td>
<td><p>Integer</p></td>
<td><p>The <code>length</code> attribute, when present, indicates an advisory length in octets of the representation returned when the target URI in the <code>href</code> attribute is dereferenced. Note that this is only a hint; for example, it does not override the <code>Content-Length</code> header field of a HTTP response obtained by actually following the link.</p></td>
</tr>
</tbody>
</table>

Additional link attributes may be added to the Link object.

## Example

``` JSON
{
   "href": "http://data.example.org/api.html",
   "rel": "service-doc",
   "type": "text/html",
   "title": "the API documentation",
   "hreflang": "en"
}
```

## Schema

``` YAML
Unresolved directive in json-link.adoc - include::link.yaml[]
```

# Representation: HTTP Header

Links should be included in HTTP headers of requests or responses, too.

``` TEXT
Link: <http://data.example.org/api.html>"; rel="service-doc"; type="text/html"; title="the API documentation"; hreflang="en"
```
