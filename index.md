---
title: API Specification
layout: default
nav_order: 7
---

# API Specifications

{: .highlight }
**Work in progress**: The WG agreed with RDA a 6-month deadline extension (i.e., end of June 2025) in order to deliver full-fledged API specifications that go beyond the "vanilla" resolvers describe in the first iteration of the SKG-IF. We opted for **OpenAPI** to describe the endpoints and the format of the objects to exchange on the wire; the *ALPHA* specifications are shared below. For the sake of completeness, you can check our working document on API development [here](https://docs.google.com/document/d/1t7b7h28UTtM56Sda4NGJIp0hnQfGbcVVGn12fny9wfI/edit?tab=t.0#heading=h.hso3muyqtlhx).


The current (i.e., last) version of the SKG-IF OpenAPI specifications is available at [https://w3id.org/skg-if/api/skg-if-openapi.yaml](https://w3id.org/skg-if/api/skg-if-openapi.yaml).

One can access the OpenAPI specifications of all (current and previous) versions by using a version number in the `w3id.org` URL, before the name of the YAML file, following this pattern:

```
https://w3id.org/skg-if/api/<X.Y.Z>/skg-if-openapi.yaml
```

For instance:
* `https://w3id.org/skg-if/api/1.0.0/skg-if-openapi.yaml` allows to access to version 1.0.0 of the OpenAPI specifications;
* `https://w3id.org/skg-if/api/0.2.0/skg-if-openapi.yaml` allows to access to version 0.2.0 of the OpenAPI specifications;
* and so on.



