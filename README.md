🛠️ Installation
Prerequisites

Python 3.7 or higher

Step 1: Clone the Repository
bashgit clone https://github.com/yourusername/simple-rag-system.git
cd simple-rag-system
Step 2: Install Required Packages
bashpip install scikit-learn
Optional (for PDF support):
bashpip install PyPDF2
Optional (for Word document support):
bashpip install python-docx
Alternative: Install All at Once
bashpip install scikit-learn PyPDF2 python-docx
For Virtual Environment (Recommended)
bash# Create virtual environment
python3 -m venv venv

# Activate it
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install packages
pip install scikit-learn PyPDF2 python-docx
📁 Folder Structure
simple-rag-system/
├── complete_rag_system.py          # Main script
├── README.md                        # This file
└── documents/                       # Sample documents
    ├── space_exploration.txt
    ├── cooking_basics.txt
    ├── climate_change.txt
    ├── fitness_guide.txt
    ├── personal_finance.txt
    └── gardening_tips.txt
🚀 Usage
Run the System
bashpython3 complete_rag_system.py
Or if using virtual environment:
bashsource venv/bin/activate  # Activate venv first
python3 complete_rag_system.py
Ask Questions
Once running, you'll see:
❓ Your question:
Type your question and press Enter. The system will search all documents and show relevant results.
Type quit, exit, or q to stop.
💡 Example Questions to Ask
Space Exploration

"What is the International Space Station?"
"Tell me about Mars exploration"
"When was the moon landing?"
"What are space telescopes used for?"
"What is commercial spaceflight?"

Cooking

"How do I improve my knife skills?"
"What is heat control in cooking?"
"How do I cook pasta properly?"
"What are the mother sauces?"
"How do I season food?"

Climate Change

"What causes climate change?"
"What are greenhouse gases?"
"How does climate change affect oceans?"
"What are renewable energy solutions?"
"What can individuals do about climate change?"

Fitness & Exercise

"What are the best strength training exercises?"
"How much cardio should I do?"
"What should I eat for fitness?"
"Why is rest important in fitness?"
"How do I set fitness goals?"

Personal Finance

"How do I start investing?"
"What is an emergency fund?"
"How do I manage debt?"
"How do I plan for retirement?"
"What is a good budgeting strategy?"

Gardening

"How do I start composting?"
"What vegetables can I grow in containers?"
"How do I improve soil quality?"
"When should I water my plants?"
"How do I start seeds indoors?"

🎯 Sample Output
❓ Your question: How do I start investing?

======================================================================
🔍 Searching for: 'How do I start investing?'
======================================================================

📄 Result 1 | Score: 0.425 | Source: personal_finance.txt
----------------------------------------------------------------------
Investing Basics involve putting money to work for long-term growth. 
Diversification across different asset classes reduces risk. Index 
funds offer low-cost exposure to broad market returns. Start early 
to benefit from compound interest.

📄 Result 2 | Score: 0.312 | Source: personal_finance.txt
----------------------------------------------------------------------
Retirement Planning should begin as soon as you start earning. Take 
advantage of employer retirement plans, especially if they offer 
matching contributions. Individual Retirement Accounts (IRAs) provide 
tax advantages for long-term savings.
