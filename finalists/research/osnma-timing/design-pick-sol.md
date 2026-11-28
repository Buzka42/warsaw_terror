WILDCARD: EO provenance gate
RUNNER_UP: OSNMA timing integrity + NIS2 evidence

### Why the ranking undervalues it

**A genuine satellite product can still be the wrong input for a decision.** The ranking looks for a confirmed scene-substitution attack, but the gate can earn its keep without one. In April 2024, Copernicus Data Space reported that it had published some Sentinel-2 products with missing file content and told users to download them again. Copernicus already offers checksums and source traceability; the opening is to enforce what those tools don’t decide: whether this product covers the right area, is recent enough, and comes from an approved processing chain for *this* workflow. That’s a direct fit for Challenge 1’s focus on the resilience of space-enabled services. ([dataspace.copernicus.eu](https://dataspace.copernicus.eu/news/2024-4-17-sentinel-2-products-content-and-checksum-modification?utm_source=openai))

### What the winning version looks like

**Demo one decision, not a provenance dashboard.** Replay a post-flood inspection workflow using real Copernicus EMS products from southwest Poland (EMSR756), available through the public Rapid Mapping API. Feed the same workflow a current layer and an authentic but stale layer from the same area. Show how the stale layer changes which facilities get flagged in the unguarded workflow. Then turn on the gate: it holds the inspection list for review, explains which rule failed, and records exactly which product and policy version drove the decision. Label the stale-input test as a simulation, not a historical incident. ([mapping.emergency.copernicus.eu](https://mapping.emergency.copernicus.eu/news/information-bulletin-173-the-copernicus-emergency-management-service-monitors-floods-in-central-and-eastern-europe/?utm_source=openai))

For Warsaw, that’s a visible failure and recovery, not a green tick and a red cross. For Demo Day, pitch the same gate as a configurable integration for firms that turn satellite products into operational alerts. The timing idea is the runner-up because Galileo is central to the demo, but Microchip already sells GNSS protection and fleet-wide timing monitoring. It’s harder to show what a buyer would pay for beyond the incumbent stack. ([gsc-europa.eu](https://www.gsc-europa.eu/galileo/services/galileo-open-service-navigation-message-authentication-osnma?utm_source=openai))

### Single biggest risk

**It’s a feature, not a product.** If an EO integrator can cover the failure with a few existing ingestion rules, the demo won’t establish a business. Before pitching, get one integrator to name a real downstream decision their current checks don’t protect and agree to test the gate on that workflow.
