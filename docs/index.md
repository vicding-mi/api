# API specifications


Our field work suggested that providing a full-fledged API would be not feasible at this stage, as it requires extensive discussions that can be hardly met within the WG deadlines. 
In the future, we will explore its feasibility via a dedicated RDA WG.

For the time being, the easiest way we conceived is about exchanging data by engaging with a API resolver, that returns SKG-IF, if any, given a ID in input.

A SKG-IF compliant SKG should provide an implementation of endpoint managing requests as follows

- `https://my.skg.io/list_schemes` which provides a comprehensive JSON list of the ids and PIDs schemes that the API is willing to resolve. The scheme `local` refers to ids that are valid locally in the SKG at hand, and should always be present (e.g., `['local', 'doi', 'orcid', 'handle', 'cordis', 'openalex']`).
- `https://my.skg.io/resolve/<schema>:<id>` which resolves a couple `<schema, id>` and returns its SKG-IF representation.
   
   * The parameter `schema` is one from the list returned by the `list_schemes` request above.
   * The parameter `id` is the identifier that we are asking a SKG-IF representation.

For example, `https://my.skg.io/search/orcid:0000-1111-2222-3333`.