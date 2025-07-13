# BERT-score-tester

This script calculates the BERTScore (Precision, Recall, F1) to measure semantic similarity between an LLM-generated text and a reference text.

## Setup

1.  **Install:** `pip install torch transformers bert-score`
2.  **Activate Virtual Environment (if used):**
    * macOS/Linux: `source .venv/bin/activate`
    * Windows: `.venv\Scripts\activate`

## Usage

1.  **Edit `bert_tester.py`:** Paste your LLM's output into `llm_generated_text` and your reference text into `reference_text`.
2.  **Run:** `python bert_tester.py`

## Interpretation

* **F1 Score:** The main metric (0-1, higher is better), indicating overall semantic similarity.
* **Precision:** How much of the generated text is relevant to the reference.
* **Recall:** How much of the reference text is covered by the generated text.

*I used `rescale_with_baseline=False` to provide raw, direct similarity scores.*
