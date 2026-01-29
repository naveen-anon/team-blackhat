import re
import math

def url_structure(url):
    reasons = []
    if len(url) > 75:
        reasons.append("URL too long")
    if "-" in url:
        reasons.append("Possible typosquatting")
    return verdict(reasons), reasons

def phishing_keywords(url):
    keywords = ["login", "verify", "update", "secure"]
    reasons = [k for k in keywords if k in url.lower()]
    return verdict(reasons), reasons

def entropy_engine(url):
    prob = [url.count(c)/len(url) for c in set(url)]
    ent = -sum(p * math.log2(p) for p in prob)
    if ent > 4.2:
        return "SUSPICIOUS", [f"High entropy ({round(ent,2)})"]
    return "CLEAN", []

def https_engine(url):
    if url.startswith("https"):
        return "MISLEADING", ["HTTPS does not mean trusted"]
    return "SUSPICIOUS", ["No HTTPS"]

def verdict(reasons):
    return "CLEAN" if not reasons else "SUSPICIOUS"
