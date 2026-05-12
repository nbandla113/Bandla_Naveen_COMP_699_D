def validate_email_domain(email):
    allowed_domains = ["gmail.com", "yahoo.com"]
    domain = email.split("@")[-1]
    if domain not in allowed_domains:
        return False
    return True