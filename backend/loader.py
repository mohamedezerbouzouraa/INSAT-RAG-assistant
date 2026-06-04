from langchain.schema import Document
def load_documents(path: str) -> list:
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    chunks = [c.strip() for c in text.split("\n\n") if c.strip()]
    return [Document(page_content=chunk) for chunk in chunks]
