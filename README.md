# Financial Misinformation Detection with LLM Hallucination Auditing + Market Impact Analysis

## Overview
A three-layer pipeline to detect financial misinformation in Indian and global markets using LLMs, audit hallucination risk statistically, and measure real market impact using Event Study Analysis.

## Architecture
- **Layer 1** — LLM Classification Engine: Headlines classified as FACTUAL/MISLEADING using LLaMA 3.1 8B via Groq
- **Layer 2** — Hallucination Risk Scoring Framework: Three-component statistical audit of LLM reliability (Consistency Score + Cross-Model Agreement + Confidence Calibration Flag)
- **Layer 3** — Event Study Market Impact Analysis: Abnormal returns and CAR calculated for each headline using SEBI-standard methodology *(in progress)*

## Dataset
87 verified financial headlines covering Indian equities (NSE), crypto, and indices spanning 2022-2023

## Tech Stack
Python, Groq API, LLaMA 3.1 8B, LLaMA 3.3 70B, pandas, yfinance, scipy, statsmodels

## Project Structure
```
data/               → raw and processed datasets
01_data_classification.ipynb    → Layer 1
02_hallucination_score.ipynb    → Layer 2
03_market_impact.ipynb          → Layer 3 (in progress)
utils.py            → shared utility functions
```

## Key Findings *(updated as project progresses)*
- 72 FACTUAL / 15 MISLEADING classifications across 87 headlines
- Hallucination risk scoring framework successfully identifies overconfident LLM classifications
