---
title: API Specification
layout: default
nav_order: 7
---

# API Specifications

{: .highlight }
**Work in progress**: The WG decided to agree with RDA a 6-month deadline extension (i.e., end of June 2025) in order to deliver full-fledged API specifications that go beyond the "vanilla" resolvers here described. We opted for **OpenAPI** to describe the endpoints and the format of the objects to exchange on the wire. The YAML file will be soon shared here. Stay tuned!

Our field work suggested that providing a full-fledged API would be not feasible at this stage, as it requires extensive discussions that can be hardly met within the WG deadlines. 
In the future, we will explore its feasibility via a dedicated RDA WG.

For the time being, the easiest way we conceived is about exchanging data by engaging with a API resolver, that returns SKG-IF, if any, given a ID in input.

A SKG-IF compliant SKG should provide an implementation of endpoint managing requests as follows:
- `GET https://my.skg.io/list_schemes` which provides a comprehensive JSON list of the ids and PIDs schemes that the API is willing to resolve. The scheme `local` refers to ids that are valid locally in the SKG at hand, and should always be present (e.g., `['local', 'doi', 'orcid', 'handle', 'cordis', 'openalex']`).
- `GET https://my.skg.io/resolve/<schema>:<id>` which resolves a couple `<schema, id>` and returns the SKG-IF representation of the relevant object.
   * The parameter `schema` is one from the list returned by the `list_schemes` request above;
   * The parameter `id` is the identifier of which we are asking an SKG-IF representation.
   
   For example, `https://my.skg.io/resolve/orcid:0000-1111-2222-3333`.
- `POST https://my.skg.io/resolve` which works as the method above, while passing a list of couples `<schema, id>` to be resolved in the body of the request.

[SKG-IF extensions]({% link extensions/index.md %}) can further extend these methods by including HTTP parameters whose implementation is left open.