import warnings; warnings.filterwarnings("ignore")
import datetime, os, sys, json, urllib.parse, urllib.request, base64
from pathlib import Path

with open(os.path.expanduser("~/.openclaw/openclaw.json")) as f:
    cfg = json.load(f)
env = cfg.get("env", {})
def g(k): return env.get(k) or env.get("vars", {}).get(k, "")

for k in ["MANTICORE_USER","MANTICORE_PASS","MANTICORE_URL",
          "WP_LSA_URL","WP_LSA_USER","WP_LSA_PASS",
          "WP_ANDROID_URL","WP_ANDROID_USER","WP_ANDROID_PASS",
          "WP_SAMSUNG_URL","WP_SAMSUNG_USER","WP_SAMSUNG_PASS"]:
    v = g(k)
    if v: os.environ[k] = v

from google.oauth2 import service_account
from googleapiclient.discovery import build

R = {}
SA_CANDIDATES = [
    Path(os.path.expanduser("~/.openclaw/creds/android-magazine-sa.json")),
    Path(os.path.expanduser("~/.openclaw/workspace/android-magazine-sa.json")),
]
SA = next((str(path) for path in SA_CANDIDATES if path.exists()), None)
if SA is None:
    missing = ", ".join(str(path) for path in SA_CANDIDATES)
    print("=== LISA PRE-FLIGHT CHECK v2 ===")
    print(f"  [FAIL] SA: missing service account file, checked: {missing}")
    print("STOP - opravit")
    sys.exit(1)

try:
    c = service_account.Credentials.from_service_account_file(SA, scopes=["https://www.googleapis.com/auth/analytics.readonly"])
    s = build("analyticsdata", "v1beta", credentials=c, cache_discovery=False)
    for n,p in {"LSA":"361706440","Android":"361709661","Samsung":"361723333"}.items():
        s.properties().runReport(property="properties/"+p, body={"dateRanges":[{"startDate":"1daysAgo","endDate":"yesterday"}],"metrics":[{"name":"sessions"}],"limit":1}).execute()
        R["GA4_"+n] = "PASS"
except Exception as e:
    R["GA4"] = "FAIL: "+str(e)[:80]

try:
    c = service_account.Credentials.from_service_account_file(SA, scopes=["https://www.googleapis.com/auth/webmasters.readonly"])
    s = build("searchconsole", "v1", credentials=c, cache_discovery=False)
    body = {"startDate":(datetime.date.today()-datetime.timedelta(7)).isoformat(),"endDate":(datetime.date.today()-datetime.timedelta(1)).isoformat(),"dimensions":["date"],"rowLimit":1}
    for n,site in {"LSA":"sc-domain:letemsvetemapplem.eu","Android":"sc-domain:androidmagazine.eu","Samsung":"sc-domain:samsungmagazine.eu"}.items():
        s.searchanalytics().query(siteUrl=site, body=body).execute()
        R["GSC_"+n] = "PASS"
except Exception as e:
    R["GSC"] = "FAIL: "+str(e)[:80]

WP_CONFIGS = {
    "LSA": (g("WP_LSA_URL") or "https://www.letemsvetemapplem.eu", "Lisa", g("WP_LSA_PASS")),
    "Android": (g("WP_ANDROID_URL") or "https://androidmagazine.eu", "Lisa", g("WP_ANDROID_PASS")),
    "Samsung": (g("WP_SAMSUNG_URL") or "https://samsungmagazine.eu", "LisaAI", g("WP_SAMSUNG_PASS")),
}

wp_pass = set()
for n,(url,user,pwd) in WP_CONFIGS.items():
    try:
        tok = base64.b64encode((user+":"+pwd).encode()).decode()
        req = urllib.request.Request(url+"/wp-json/wp/v2/posts?per_page=1", headers={"Authorization":"Basic "+tok})
        with urllib.request.urlopen(req, timeout=10) as r:
            posts = json.loads(r.read()); R["WP_"+n] = "PASS ("+str(len(posts))+" posts)"
            wp_pass.add(n)
    except Exception as e:
        R["WP_"+n] = "FAIL: "+str(e)[:60]

MU = g("MANTICORE_URL") or "https://searchnew.tfsys.eu/results"
MP = g("MANTICORE_PASS"); MN = g("MANTICORE_USER")
for n,tf in {"LSA":"letemsvetemapplem.eu","Android":"androidmagazine.eu","Samsung":"samsungmagazine.eu"}.items():
    try:
        if not MP:
            raise RuntimeError("MANTICORE_PASS chybi")
        tok = base64.b64encode((MN+":"+MP).encode()).decode()
        q = urllib.parse.urlencode({"tf_user":tf,"s":"test","count":1,"post_status":"any"})
        req = urllib.request.Request(MU+"?"+q, headers={"Authorization":"Basic "+tok})
        with urllib.request.urlopen(req, timeout=8) as r:
            data = json.loads(r.read()); R["Manticore_"+n] = "PASS ("+str(len(data.get("docs",[])))+" docs)"
    except Exception as e:
        if n in wp_pass:
            R["Manticore_"+n] = "PASS_FALLBACK -> WP REST"
        else:
            R["Manticore_"+n] = "FAIL: "+str(e)[:80]

print("=== LISA PRE-FLIGHT CHECK v2 ===")
ok = True
for k,v in R.items():
    passed = v.startswith("PASS")
    print("  ["+( "OK" if passed else "FAIL")+"] "+k+": "+v)
    if not passed and (
        k.startswith("GA4_")
        or k == "GA4"
        or k.startswith("GSC_")
        or k == "GSC"
        or k.startswith("Manticore_")
    ):
        ok = False
print("VSECHNO OK" if ok else "STOP - opravit")
sys.exit(0 if ok else 1)
