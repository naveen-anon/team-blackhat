import re
import math
from urllib.parse import urlparse

def _result(reasons):
    if len(reasons) >= 2:
        return "MALICIOUS", reasons
    elif len(reasons) == 1:
        return "SUSPICIOUS", reasons
    else:
        return "CLEAN", []

# 1️⃣ URL STRUCTURE ENGINE
def url_structure_engine(url):
    reasons = []
    p = urlparse(url)

    if p.netloc.count('.') >= 4:
        reasons.append("Excessive subdomains (fake trust layering)")

    if "-" in p.netloc:
        reasons.append("Hyphenated domain (brand impersonation)")

    if re.search(r"https?://\d+\.\d+\.\d+\.\d+", url):
        reasons.append("IP-based URL")

    return _result(reasons)

# 2️⃣ KEYWORD ENGINE
def keyword_engine(url):
    reasons = []
    keywords = ["login", "verify", "secure", "update", "account", "bank", "confirm"]

    for k in keywords:
        if k in url.lower():
            reasons.append(f"Social-engineering keyword: {k}")

    return _result(reasons)

# 3️⃣ ENTROPY ENGINE
def entropy_engine(url):
    reasons = []

    def entropy(s):
        probs = [s.count(c)/len(s) for c in set(s)]
        return -sum(p * math.log2(p) for p in probs)

    e = entropy(url)
    if e > 4.2:
        reasons.append(f"High entropy / obfuscation ({round(e,2)})")

    return _result(reasons)

# 4️⃣ HTTPS TRUST ENGINE
def https_engine(url):
    reasons = []
    if not url.startswith("https://"):
        reasons.append("No HTTPS")
    return _result(reasons)
