# utils.py
# Palīgfunkcijas iepirkumu saraksta aprēķiniem

def calc_line_total(item):
    """Aprēķina vienas līnijas summu: price * quantity.
    Prasa, lai item satur 'price' un 'quantity' atslēgas."""
    price = item.get('price', 0) or 0
    quantity = item.get('quantity', 0) or 0
    try:
        return float(price) * int(quantity)
    except (ValueError, TypeError):
        return 0.0

def calc_grand_total(items):
    """Kopējā summa visām līnijām."""
    return sum(calc_line_total(it) for it in items)

def count_units(items):
    """Kopējais vienību skaits (subtotal)."""
    return sum(int(it.get('quantity', 0) or 0) for it in items)
