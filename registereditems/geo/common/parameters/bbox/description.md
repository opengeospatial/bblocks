`bbox` is a query parameter that may be applied in GET requests on a collection of resources.

The parameter, if provided, selects the resources with a spatial extent that intersects the specified bounding box.

The coordinates of the bounding box are in longitude, latitude and optionally ellipsoidal height unless a different coordinate reference system is specified in the query parameter `bbox-crs`.

The `bbox` parameter matches all resources in the collection that are not associated with a spatial geometry, too.

If a resource has multiple spatial geometry properties, it is the decision of the server whether only a single spatial geometry property is used to determine the spatial extent or all relevant geometries.
