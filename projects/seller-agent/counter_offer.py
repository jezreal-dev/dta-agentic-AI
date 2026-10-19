# counter_offer.py
# Story 2.2 - Counter low offers automatically
# Author: Jezreal Momoh (eComMART AI Engineering Squad)


def counter_offer(listed_price, buyer_offer, floor_price, stock=None):
    """
    Returns a counter-offer or flags the request for review.

    listed_price : the original price on the catalog
    buyer_offer  : the price the buyer is proposing
    floor_price  : the minimum price the supplier accepts
    stock        : number of units available (None means unknown)
    """
    # AC-3 / NFR-02: do not invent availability when out of stock
    if stock is not None and stock <= 0:
        return {"action": "unavailable", "reason": "out of stock"}

    if buyer_offer >= listed_price:
        # Buyer paid full price - accept immediately
        return {"action": "accept", "price": buyer_offer}

    if buyer_offer < floor_price:
        # Below the minimum - counter at the floor (enforces NFR-03)
        return {"action": "counter", "price": floor_price}

    # Between floor and listed price - counter at the midpoint
    mid = (listed_price + buyer_offer) / 2
    return {"action": "counter", "price": round(mid, 2)}


# Quick test suite
if __name__ == "__main__":
    # Test 1: offer between floor and listed price -> midpoint counter
    result = counter_offer(100, 85, 80)
    print(f"Test 1: {result}")   # expect counter at 92.5

    # Test 2: offer below floor price -> floor protection (NFR-03)
    result = counter_offer(100, 70, 80)
    print(f"Test 2: {result}")   # expect counter at 80

    # Test 3: offer at or above listed price -> immediate accept
    result = counter_offer(100, 100, 80)
    print(f"Test 3: {result}")   # expect accept at 100

    # Test 4: out of stock -> never invent availability (AC-3 / NFR-02)
    result = counter_offer(100, 85, 80, stock=0)
    print(f"Test 4: {result}")   # expect unavailable
