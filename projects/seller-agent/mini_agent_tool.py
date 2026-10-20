# =========================================================
# Example 6: eCOMMart Mini Agent Tool
# ALL Week 3 concepts: variables, strings, collections,
# conditions, loops, functions, is_nan, safe_eval, exceptions
# =========================================================

import math

# ──────────────────────────────────────────────────────────
# SECTION 1: Product Catalog (Dictionary + List)
# ──────────────────────────────────────────────────────────

CATALOG = {
    "WM-4021": {"name": "Wireless Mouse",  "category": "Electronics", "price": 499.00,  "stock": 120},
    "LS-7800": {"name": "Laptop Stand",    "category": "Accessories", "price": 850.00,  "stock": 0},
    "UH-1102": {"name": "USB Hub",         "category": "Electronics", "price": 350.00,  "stock": 45},
    "SW-9001": {"name": "Smart Watch",     "category": "Wearables",   "price": 2999.00, "stock": 30},
    "EB-3310": {"name": "Earbuds Pro",     "category": "Electronics", "price": 1299.00, "stock": 80},
    "PC-0055": {"name": "Phone Case",      "category": "Accessories", "price": 199.00,  "stock": 200},
}

DELIVERY_ZONES = {
    "40": ("Mumbai",    "Same-day delivery"),
    "56": ("Bangalore", "Next-day delivery"),
    "11": ("Delhi",     "2-day delivery"),
    "50": ("Pune",      "Next-day delivery"),
}


# ──────────────────────────────────────────────────────────
# SECTION 2: Helper Functions (Agent Tool Foundations)
# ──────────────────────────────────────────────────────────

def is_nan(value):
    """Returns True if value is missing, empty, or NaN."""
    if value is None:
        return True
    if isinstance(value, float) and math.isnan(value):
        return True
    if isinstance(value, str) and value.strip() == "":
        return True
    return False


def safe_eval_price(raw):
    """Safely converts a string to float. Returns None on failure."""
    try:
        return float(raw)
    except (ValueError, TypeError):
        return None


# ──────────────────────────────────────────────────────────
# SECTION 3: Business Logic Functions (Reusable Tools)
# ──────────────────────────────────────────────────────────

def get_product(sku):
    """
    Looks up a product by SKU in the eCOMMart catalog.

    Agent Tool Use:
        Call when customer asks 'Tell me about product WM-4021'
        or when checkout needs product details.

    Args:
        sku (str): Product SKU code.

    Returns:
        dict: {"found": bool, "product": dict or None, "message": str}
    """
    sku = sku.strip().upper()
    if sku in CATALOG:
        return {"found": True, "product": CATALOG[sku], "message": "Product found."}
    return {"found": False, "product": None, "message": f"SKU '{sku}' not found in catalog."}


def check_delivery(pin_code):
    """
    Returns delivery zone and estimated time for a PIN code.

    Agent Tool Use:
        Call when customer asks 'When will my order arrive?'

    Args:
        pin_code (str): 6-digit customer PIN code.

    Returns:
        dict: {"zone": str, "eta": str, "free_delivery_threshold": int}
    """
    if is_nan(pin_code) or len(str(pin_code)) < 6:
        return {"zone": "Unknown", "eta": "Cannot determine", "free_delivery_threshold": 500}

    prefix = str(pin_code)[:2]
    if prefix in DELIVERY_ZONES:
        zone, eta = DELIVERY_ZONES[prefix]
    else:
        zone, eta = "Other", "5-7 business days"

    return {"zone": zone, "eta": eta, "free_delivery_threshold": 500}


def get_discount_rate(cart_total):
    """
    Returns the applicable discount rate for a given cart total.

    Args:
        cart_total (float): Total value of the cart in INR.

    Returns:
        float: Discount rate as a decimal (e.g. 0.15 = 15%).
    """
    if cart_total >= 3000:
        return 0.20
    elif cart_total >= 2000:
        return 0.15
    elif cart_total >= 1000:
        return 0.10
    elif cart_total >= 500:
        return 0.05
    return 0.0


def process_order(sku_list, pin_code):
    """
    Processes a customer order end-to-end.

    This is the main agent tool — it combines all helper functions:
    lookup → stock check → discount → delivery → structured output.

    Agent Tool Use:
        Call when customer says 'I want to order WM-4021 x2 and UH-1102 x1'

    Args:
        sku_list (list of tuples): [(sku, qty), ...]
        pin_code (str): Customer's delivery PIN code.

    Returns:
        dict: Full order summary with items, pricing, and delivery info.
    """
    order_items = []
    subtotal    = 0.0
    issues      = []

    # Step 1: Validate and look up each product
    for sku, raw_qty in sku_list:
        qty = safe_eval_price(str(raw_qty))
        if is_nan(qty) or qty is None or qty <= 0:
            issues.append(f"Invalid quantity for SKU {sku}: '{raw_qty}'")
            continue

        qty = int(qty)
        result = get_product(sku)

        if not result["found"]:
            issues.append(result["message"])
            continue

        product = result["product"]

        # Check stock
        if product["stock"] == 0:
            issues.append(f"'{product['name']}' is out of stock.")
            continue
        if product["stock"] < qty:
            issues.append(f"Only {product['stock']} units of '{product['name']}' available.")
            qty = product["stock"]   # adjust to available stock

        line_total = product["price"] * qty
        subtotal  += line_total
        order_items.append({
            "name"      : product["name"],
            "sku"       : sku,
            "price"     : product["price"],
            "qty"       : qty,
            "line_total": line_total,
        })

    if not order_items:
        return {"success": False, "issues": issues, "summary": None}

    # Step 2: Calculate pricing
    discount_rate  = get_discount_rate(subtotal)
    discount_amt   = subtotal * discount_rate
    after_discount = subtotal - discount_amt
    gst_amt        = after_discount * 0.18
    grand_total    = after_discount + gst_amt

    # Step 3: Delivery info
    delivery      = check_delivery(pin_code)
    delivery_free = subtotal >= delivery["free_delivery_threshold"]

    # Step 4: Return structured output
    return {
        "success": True,
        "issues" : issues,
        "summary": {
            "items"        : order_items,
            "subtotal"     : round(subtotal, 2),
            "discount_rate": discount_rate,
            "discount_amt" : round(discount_amt, 2),
            "gst_amt"      : round(gst_amt, 2),
            "grand_total"  : round(grand_total, 2),
            "delivery"     : delivery,
            "delivery_free": delivery_free,
        }
    }


# ──────────────────────────────────────────────────────────
# SECTION 4: Output Formatter (Display Function)
# ──────────────────────────────────────────────────────────

def print_order_summary(order):
    """Prints a formatted order summary from the process_order result."""
    print("\n" + "=" * 60)
    print("         eCOMMart — Order Summary")
    print("=" * 60)

    if not order["success"]:
        print("  ❌ Order could not be processed.")
        for issue in order["issues"]:
            print(f"     ⚠  {issue}")
        return

    s = order["summary"]

    # Items
    for item in s["items"]:
        print(f"  {item['name']:<25} ₹{item['price']:>7.2f} x {item['qty']} = ₹{item['line_total']:.2f}")

    # Warnings / partial issues
    if order["issues"]:
        print("\n  ⚠  Notes:")
        for issue in order["issues"]:
            print(f"     - {issue}")

    # Pricing breakdown
    print("-" * 60)
    print(f"  {'Subtotal':<35} ₹{s['subtotal']:>8.2f}")
    print(f"  {'Discount (' + str(int(s['discount_rate']*100)) + '%)':<35} -₹{s['discount_amt']:>7.2f}")
    print(f"  {'GST (18%)':<35} +₹{s['gst_amt']:>7.2f}")
    print(f"  {'Delivery':<35} {'FREE ✓' if s['delivery_free'] else '₹60.00'}")
    print("=" * 60)
    grand = s['grand_total'] + (0 if s['delivery_free'] else 60)
    print(f"  {'GRAND TOTAL':<35} ₹{grand:>8.2f}")
    print("=" * 60)

    # Delivery info
    d = s["delivery"]
    print(f"\n  📦 Delivering to  : {d['zone']}")
    print(f"     Estimated time : {d['eta']}")
    print("=" * 60)


# ──────────────────────────────────────────────────────────
# SECTION 5: Run the Agent Tool
# ──────────────────────────────────────────────────────────

# Test Order 1 — valid order, Mumbai zone
order1 = process_order(
    sku_list=[("WM-4021", 2), ("UH-1102", 1), ("EB-3310", 1)],
    pin_code="400001"
)
print_order_summary(order1)

# Test Order 2 — out-of-stock item and invalid qty
order2 = process_order(
    sku_list=[("LS-7800", 1), ("SW-9001", "abc"), ("PC-0055", 3)],
    pin_code="560078"
)
print_order_summary(order2)

# Test Order 3 — unknown SKU and unknown PIN zone
order3 = process_order(
    sku_list=[("XX-9999", 1), ("PC-0055", 2)],
    pin_code="302001"
)
print_order_summary(order3)
