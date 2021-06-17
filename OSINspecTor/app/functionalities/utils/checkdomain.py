from ipaddress import ip_address

def check_domain(domain: str) -> bool:

    try:
        ip_address(domain)
    except:
        valid = domain.isprintable()
    else:
        valid = False
    finally:
        return valid