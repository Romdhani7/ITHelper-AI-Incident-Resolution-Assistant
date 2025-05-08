import re
from docx import Document
import pandas as pd

# 1️⃣ Chemin vers ton .docx
doc_path = r"C:\Users\Amina\Downloads\les incidents.docx"

# 2️⃣ Lecture du document
doc = Document(doc_path)
full_text = "\n".join(para.text for para in doc.paragraphs)

# 3️⃣ Découpage en incidents (lookahead pour conserver le numéro)
segments = re.split(r'(?=\d+\.\s*Titre\s*:)', full_text)

data = []
for seg in segments:
    seg = seg.strip()
    if not seg:
        continue

    # 4️⃣ Extraction des champs avec regex
    titre_match = re.search(r'Titre\s*:\s*(.+)', seg)
    desc_match = re.search(r'Description\s*:\s*(.+)', seg)
    sol_match  = re.search(r'Solution\s*:\s*(.+)', seg)
    perte_match = re.search(r'Perte de vie matériel\s*:\s*(\d+)', seg)

    record = {
        "Titre": titre_match.group(1).strip() if titre_match else "",
        "Description": desc_match.group(1).strip() if desc_match else "",
        "Solution": sol_match.group(1).strip() if sol_match else "",
        "Perte de vie matériel (mois)": int(perte_match.group(1)) if perte_match else 0
    }
    data.append(record)

# 5️⃣ Création du DataFrame et sauvegarde
df = pd.DataFrame(data)
df.to_csv("incidents_materiels.csv", index=False, encoding='utf-8-sig')
df.to_excel("incidents_materiels.xlsx", index=False)

print("✅ Extraction terminée ! Fichiers créés :")
print("   • incidents_materiels.csv")
print("   • incidents_materiels.xlsx")
