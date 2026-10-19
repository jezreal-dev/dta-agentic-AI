# eComMART Agentic Commerce System (`projects/`)

This directory houses the source code for the **eComMART AI Engineering Squad's** two core agents and shared data layer, built progressively over the 24-week curriculum.

---

## Architecture Overview

```mermaid
flowchart LR
    subgraph BuyerSide["Buyer Experience (Epic E3)"]
        Buyer["Buyer"] --> BuyerAgent["Buyer Agent\n(Procurement Assistant)"]
    end

    subgraph SharedLayer["Shared Data & Memory (Weeks 3-5)"]
        Catalog[("ProductCatalog\n(JSON / SQLite)")]
        AuditLog[("Negotiation & Failure Logs\n(NFR-06)")]
    end

    subgraph SellerSide["Supplier Experience (Epics E1 & E2)"]
        SellerAgent["Seller Agent\n(Storefront Assistant)"] --> Supplier["Supplier\n(Human-in-the-Loop)"]
    end

    BuyerAgent <-->|"RFQ & Offer Negotiation"| SellerAgent
    SellerAgent -->|"check_stock(sku)"| Catalog
    SellerAgent -->|"Log Decisions & Flags"| AuditLog
```

---

## Components

| Directory | Agent / Component | Epics & Stories Covered | Current Modules |
| :--- | :--- | :--- | :--- |
| [`seller-agent/`](seller-agent/) | **Seller Agent** | `E1` (Story 1.1, 1.2) · `E2` (Story 2.1, 2.2, 2.3) | [`counter_offer.py`](seller-agent/counter_offer.py) |
| [`buyer-agent/`](buyer-agent/) | **Buyer Agent** | `E3` (Story 3.1, 3.2) | Planned for Sprint 3 |
| [`shared/`](shared/) | **Shared Data & Schemas** | Catalog, BANT, RFQ models | [`sample_catalog.json`](shared/sample_catalog.json) |
