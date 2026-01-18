import pickle
import os
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class SimpleRAG:    
    def __init__(self):
        self.texts = []
        self.sources = []
        self.vectorizer = None
        self.vectors = None
    
    def load_file(self, file_path):
        path = Path(file_path)
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                text = f.read()
            paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
            for para in paragraphs:
                if len(para) > 50:
                    self.texts.append(para)
                    self.sources.append(path.name)
            
            print(f"✅ Loaded {len(paragraphs)} chunks from {path.name}")
        except Exception as e:
            print(f"❌ Error loading {path.name}: {e}")
    
    def load_files(self, file_paths):
        """Load multiple files"""
        for file_path in file_paths:
            self.load_file(file_path)
        if self.texts:
            print(f"\n📊 Total chunks: {len(self.texts)}")
            print("🔢 Creating embeddings...")
            self.vectorizer = TfidfVectorizer()
            self.vectors = self.vectorizer.fit_transform(self.texts)
            print("✅ Ready to search!\n")
    
    def search(self, query, top_k=1):
        if not self.texts:
            print("❌ No documents loaded!")
            return []
        
        query_vector = self.vectorizer.transform([query])
        similarities = cosine_similarity(query_vector, self.vectors)[0]
        top_indices = similarities.argsort()[-top_k:][::-1]
        
        results = []
        for idx in top_indices:
            results.append({
                'text': self.texts[idx],
                'score': similarities[idx],
                'source': self.sources[idx]
            })
        
        return results

if __name__ == "__main__":
    print("="*70)
    print("🎯 INTERACTIVE RAG SYSTEM")
    print("="*70)
    rag = SimpleRAG()
    script_dir = Path(__file__).parent
    docs_folder = script_dir / "documents"
    
    print("\n📚 Loading documents from 'documents' folder...")
    print("-"*70)
    document_files = [
        docs_folder / "space_exploration.txt",
        docs_folder / "cooking_basics.txt",
        docs_folder / "climate_change.txt",
        docs_folder / "fitness_guide.txt",
        docs_folder / "personal_finance.txt",
        docs_folder / "gardening_tips.txt"
    ]
    if not docs_folder.exists():
        print(f"❌ ERROR: 'documents' folder not found!")
        print(f"Expected location: {docs_folder}")
        print("\nPlease make sure you have the 'documents' folder in the same")
        print("location as this script with all the sample files inside.")
        exit()
    rag.load_files(document_files)
    print("="*70)
    print("📖 KNOWLEDGE BASE LOADED")
    print("="*70)
    print("\nTopics available:")
    print("  • Space Exploration (Moon, Mars, ISS, telescopes)")
    print("  • Cooking Basics (Knife skills, heat control, techniques)")
    print("  • Climate Change (Causes, effects, solutions)")
    print("  • Fitness & Exercise (Cardio, strength, nutrition)")
    print("  • Personal Finance (Budgeting, investing, retirement)")
    print("  • Gardening (Soil, plants, composting, containers)")

    print("\n" + "="*70)
    print("🔍 ASK YOUR QUESTIONS")
    print("="*70)
    print("Type your question and press Enter")
    print("Type 'quit' or 'exit' to stop")
    print("="*70)
    
    while True:
        print()
        query = input("❓ Your question: ").strip()

        if query.lower() in ['quit', 'exit', 'q', '']:
            print("\n👋 Goodbye!")
            break
        print(f"\n{'='*70}")
        print(f"🔍 Searching for: '{query}'")
        print('='*70)
        
        results = rag.search(query, top_k=1)

        for i, r in enumerate(results, 1):
            print(f"\n📄 Result {i} | Score: {r['score']:.3f} | Source: {r['source']}")
            print("-"*70)
            print(r['text'])
            print()
