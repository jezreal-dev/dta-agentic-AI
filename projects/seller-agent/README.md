# eComMART Seller Agent (`projects/seller-agent/`)

The **Seller Agent** acts as a virtual storefront assistant for independent suppliers on eComMART.

## Responsibilities & Epics
- **Epic E1 (`FR-01`, `FR-02`, `NFR-02`):** Verify true inventory availability in `ProductCatalog` before quoting; never invent stock (`0/20` hallucinated stock cases).
- **Epic E2 (`FR-03`–`FR-06`, `NFR-03`, `NFR-04`, `NFR-06`):**
  - Qualify incoming leads using the **BANT** framework (Story 2.1).
  - Automatically counter low offers using `counter_offer()` while enforcing the supplier's minimum floor price (`NFR-03`) (Story 2.2).
  - Escalate unusual or out-of-policy requests to the supplier for human review (`FR-05`) (Story 2.3).

## Running Tests
```bash
python3 projects/seller-agent/counter_offer.py
```
