from engines import *

ENGINES = {
    "URL Structure Engine": url_structure,
    "Phishing Keyword Engine": phishing_keywords,
    "Entropy Engine": entropy_engine,
    "HTTPS Trust Engine": https_engine
}

def scan(url):
    print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(" BLACKHAT TOTAL :: URL ANALYSIS")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("Target:", url, "\n")

    flagged = 0

    for name, engine in ENGINES.items():
        result, reasons = engine(url)
        print(f"{name:<25} → {result}")
        if result != "CLEAN":
            flagged += 1
            for r in reasons:
                print("   -", r)

    print("\nDetection Ratio:", f"{flagged} / {len(ENGINES)}")
    print("Verdict:", "LIKELY PHISHING" if flagged >= 2 else "LOW RISK")

if __name__ == "__main__":
    u = input("Enter URL to scan: ")
    scan(u)
