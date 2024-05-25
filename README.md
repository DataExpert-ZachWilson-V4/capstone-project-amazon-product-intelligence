[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/1lXY_Wlg)


# E-commerce Product Intelligence

Goal: Create an extensible ETL pipeline for an E-commerce Product Intelligence Pipeline with an LLM-based RAG in the mix. 

### Datasets
- [Amazon Product Data by Stanford SNAP](https://huggingface.co/datasets/McAuley-Lab/Amazon-Reviews-2023) - 48.19M products - will random sample by category and partial load ~2-3M (LLM costs mostly) for demo
- Amazon Product Taxonomy - in repo
- Amazon Top N and Bottom N Scraper - I'll build this
- [Knowledge Graph](https://towardsdatascience.com/how-to-convert-any-text-into-a-graph-of-concepts-110844f22a1a)

### Components
**Primary Tables**
  - Stores
  - Products
  - Product Taxonomies
  - Reviews - will load a few not all

**Knowledge graph**
 - Product Text Embeddings SCD - SCD since we won't upgrade our AI models often
 - Product Text Embeddings Cumulative - Needed for Hiearchial RAG 
 - Product Text Knowledge Graph Nodes
 - Product Text Knowledge Graph Vertices
 - Reviews Embeddings - Won't build but possible expansion
 - Review Embeddings Cumulative - Won't build but possible expansion
 - Product Image Embeddings - Won't build but possible expansion

**Live API**
  - Amazon Top and Bottom N Stores by Category - N depending on what my scraper can manage

**Pipelines**
- Top/Bottom N Products -> Primary Tables
- Top/Bottom N Products -> Knowledge Graph
- Historical Backfill of Product Data from SNAP dataset (S3) -> Primary Tables
- Products -> LLM -> Knowledge Graph Nodes

**EDA**

**Data Quality**
- Normalize Knowledge Graph Nodes
- Clean up SNAP Dataset for Product duplicates/ultra-similars for better RAG

**RAG Bot Use Cases**

NOTE: I'll probably build out one of these but I imagine these are a few possible use cases.

Write a product description for me that would work well for X product in Y category
1. Find the most similar successful/worst N products + keywords/concepts in the category, i.e.>4.5 stars etc.
2. Use as part of Langchain to write a description

Categorize my Product Properly
1. Cosine Similarity Match the input description with existing products and get N similar products
2. Get their knowledge graphs and use conceptual context similarity strength (weight of the edges) to get even more associated products
3. Summarize key findings from product descriptions about categories
4. Produce an augmented prompt of the description which mentions 
5. Lang Chain to classify in categories hierarchically
   
What can I do to make my store more SEO-friendly today?
1. Find the most similar successful N products in the past N days
2. Summarize findings


**Potential Stack Decisions**
- Duck DB for quick local work
- Open AI GPT4Omni or Ollama for LLM
- Streamlit for LLM interface + Knowledge Graph
- Playwright or Pypetteer for Scraping
- Airflow for Orchestration
- S3 for Datalake
