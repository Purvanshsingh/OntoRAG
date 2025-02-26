# OntoRAG

**Ontology-Grounded Retrieval-Augmented Generation for Large Language Models**

OntoRAG is an open-source Python module that implements the OG-RAG framework described in our research paper. By integrating domain-specific ontologies with large language model (LLM) pipelines through a hypergraph-based retrieval system, OntoRAG enhances factual accuracy, reduces hallucinations, and improves context attribution in generated responses.

---

![image](https://github.com/user-attachments/assets/18bb95b8-bcac-4e7d-bf30-c2c335dbe367)

---

## Overview

Modern LLMs often struggle with domain-specific accuracy and context verification. OntoRAG addresses these challenges by:
- **Ontology Integration:** Leveraging structured domain knowledge to guide the retrieval process.
- **Hypergraph-Based Retrieval:** Transforming ontology-mapped data into hyperedges to efficiently extract relevant context.
- **Enhanced Reliability:** Boosting factual recall and interpretability, making it ideal for applications in agriculture, healthcare, legal research, and more.

This repository provides a complete, end-to-end implementation of the OG-RAG framework, enabling researchers and developers to quickly integrate robust retrieval-augmented generation into their projects.

---

## Features

- **Seamless Ontology Mapping:** Automatically map domain-specific documents to an ontology.
- **Efficient Hypergraph Construction:** Flatten complex relationships into hyperedges for optimized retrieval.
- **Improved LLM Outputs:** Enhance factual accuracy and reduce hallucinations in generated responses.
- **Easy Integration:** Pip-installable module with a user-friendly API.
- **Comprehensive Documentation & Examples:** Step-by-step guides, tutorials, and test cases to help you get started.

---

## Installation

Install OntoRAG via pip:

```bash
pip install ontorag
```

## Contributing

Contributions are welcome! If you’d like to help improve OntoRAG, please check out our [Contributing Guidelines](CONTRIBUTING.md) for more details on how to get started.


## Citation

If you use OntoRAG in your research or projects, please cite the original paper:

**Kartik Sharma, Peeyush Kumar, and Yunqing Li**  
*OG-RAG: Ontology-Grounded Retrieval-Augmented Generation For Large Language Models*  
Microsoft Research, 2024.
