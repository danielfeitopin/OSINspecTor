from ipaddress import IPv4Address

def check_ip(ip: str) -> bool:

    try:
        IPv4Address(ip)
    except:
        valid = False
    else:
        valid = True
    finally:
        return valid