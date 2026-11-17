"""Extrahera text ur lärarens egna prov/uppgifter (docx) till en korpus.
Utesluter arkiv, förlagsmaterial, AI-gjorda och nyligen genererade filer."""
import os, re, json, sys, datetime
import docx

ROT = r"C:\Users\Hedav\OneDrive - Jönköpings kommun"
KURSER = [r"Fysik\Fysik 1", r"Fysik\Fysik 2", r"Fysik\Fysik 3",
          r"Matematik\Matematik 1a", r"Matematik\Matematik 1b", r"Matematik\Matematik 1c",
          r"Matematik\Matematik 2a", r"Matematik\Matematik 2b", r"Matematik\Matematik 2c",
          r"Matematik\Matematik 3b", r"Matematik\Matematik 3c", r"Matematik\Matematik 4",
          r"Matematik\Matematik 5"]
UNDER = ["Prov", "Extrauppgifter", "Diagnoser", "Repetition inför NP", "Repetition inför Kursprov",
         "Inlämningsuppgifter", "Läxförhör", "Stöd och komplettering"]
UT = re.compile(r"arkiv|förlag|lösningsförslag|bedömning|impuls|origo|övningsprov ai|\bai\b|utkast|"
                r"gamla nationella|lösningar|facit|kollega|nationellt|np ", re.I)
GRANS = datetime.datetime(2026, 9, 1)

ut = []
for k in KURSER:
    for u in UNDER:
        bas = os.path.join(ROT, k, u)
        if not os.path.isdir(bas):
            continue
        for dp, dn, fn in os.walk(bas):
            for f in fn:
                if not f.lower().endswith(".docx") or f.startswith("~$"):
                    continue
                p = os.path.join(dp, f)
                rel = os.path.relpath(p, ROT)
                if UT.search(rel):
                    continue
                try:
                    d = docx.Document(p)
                except Exception as e:
                    continue
                cp = d.core_properties
                skapad = cp.created
                if skapad and skapad.replace(tzinfo=None) >= GRANS:
                    continue
                if (cp.author or "").lower() in ("python-docx", "claude"):
                    continue
                stycken = [x.text.strip() for x in d.paragraphs if x.text.strip()]
                for t in d.tables:
                    for r in t.rows:
                        for c in r.cells:
                            s = c.text.strip()
                            if s:
                                stycken.append(s)
                ut.append({"fil": rel, "kurs": k.split("\\")[-1], "skapad": str(skapad)[:10],
                           "forf": cp.author, "text": stycken})
json.dump(ut, open(sys.argv[1], "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(ut), "filer", sum(len(x["text"]) for x in ut), "stycken")
