import re
import dns.resolver

def isValidPlate(plate: str)-> bool:
    pattern = r'^[A-Z]{3}\d{3}$'
    return bool(re.match(pattern, plate))

def isValidEmail(email: str)-> bool:
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, email):
        return False
    
    _, domain = email.split('@')
    
    # Verify domain exists
    try:
        dns.resolver.resolve(domain, 'MX')
    except dns.resolver.NXDOMAIN:
        return False
    except dns.resolver.NoAnswer:
        return False
    except dns.resolver.NoNameservers:
        return False
    
    return True

def isValidDate(date: str)-> bool:
    pattern = re.compile(r'^\d{4}-\d{2}-\d{2}$')
    return bool(pattern.match(date))