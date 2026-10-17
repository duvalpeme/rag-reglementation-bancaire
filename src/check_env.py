import time

def test(nom, module):
    debut = time.time()
    print(f"Import de {nom}...", flush=True)
    __import__(module)
    print(f"  OK en {time.time() - debut:.1f} s", flush=True)

test("PyMuPDF", "pymupdf")
test("chromadb", "chromadb")
test("rank_bm25", "rank_bm25")
test("anthropic", "anthropic")
test("streamlit", "streamlit")
test("torch (long la première fois)", "torch")
test("sentence_transformers", "sentence_transformers")
print("Tout est installé correctement.")