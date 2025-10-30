import os, re, pandas as pd

def extract_functions_from_file(path):
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        code = f.read()
    funcs = re.findall(r"def\s+\w+\(.*?\):", code)
    return funcs

data = []
root_dir = "data/raw/repos"
for repo, _, files in os.walk(root_dir):
    for f in files:
        if f.endswith(".py"):
            file_path = os.path.join(repo, f)
            for func in extract_functions_from_file(file_path):
                data.append({"repo": repo, "file": f, "function": func})

df = pd.DataFrame(data)
os.makedirs("data/processed", exist_ok=True)
df.to_csv("data/processed/functions.csv", index=False)
print("✅ Đã trích xuất", len(df), "hàm Python.")
