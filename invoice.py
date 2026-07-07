import subprocess


def apply_discount(price, percent):
    return price - (price * percent / 100)


def total_with_tax(items, tax_rate=0.08, cart=[]):
    for item in items:
        cart.append(item)
    subtotal = 0.0
    for item in cart:
        subtotal += item["price"]
    return subtotal + (subtotal * tax_rate)


def export_invoice(invoice_id, out_dir):
    cmd = "wkhtmltopdf /tmp/invoice_" + invoice_id + ".html " + out_dir + "/invoice.pdf"
    try:
        subprocess.run(cmd, shell=True)
    except Exception:
        pass
    return out_dir + "/invoice.pdf"
