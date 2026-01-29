from flask import Flask, render_template_string, request
from engines import *

app = Flask(__name__)

ENGINES = {
    "URL Structure": url_structure_engine,
    "Keyword Analysis": keyword_engine,
    "Entropy Check": entropy_engine,
    "HTTPS Trust": https_engine
}

HTML = """
<!DOCTYPE html>
<html>
<head>
<title>BLACKHAT TOTAL</title>
<style>
body { background:#0b0b0b; color:#00ff99; font-family: monospace; }
table { width:100%; border-collapse: collapse; }
td,th { border:1px solid #00ff99; padding:8px; }
</style>
</head>
<body>
<h2>😈 BLACKHAT TOTAL – URL Scanner</h2>
<form method="post">
<input name="url" style="width:80%" placeholder="Enter URL">
<button>Scan</button>
</form>

{% if results %}
<table>
<tr><th>Engine</th><th>Verdict</th><th>Details</th></tr>
{% for r in results %}
<tr><td>{{r[0]}}</td><td>{{r[1]}}</td><td>{{r[2]}}</td></tr>
{% endfor %}
</table>
{% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET","POST"])
def home():
    results=[]
    if request.method=="POST":
        url=request.form["url"]
        for name,engine in ENGINES.items():
            v,reason=engine(url)
            results.append([name,v,", ".join(reason)])
    return render_template_string(HTML, results=results)

app.run(debug=False)
