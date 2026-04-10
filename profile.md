# Mohamed Nabeel — Profile

> Machine-readable profile for LLMs and agents. Canonical URL: https://nabeelxy.github.io/profile.md
> Last updated: 2026-04-10

---

## Identity

- **Name:** Mohamed Nabeel
- **Title:** AI Security Researcher
- **Tagline:** Building autonomous agents and adversarial ML systems to detect, classify, and neutralize AI-powered cyber threats at scale.
- **GitHub:** https://github.com/nabeelxy
- **Google Scholar:** https://scholar.google.com/citations?user=Lka4RwsAAAAJ&hl=en
- **LinkedIn:** https://www.linkedin.com/in/myoosuf/
- **Twitter/X:** https://x.com/nabeelxy
- **arXiv:** https://arxiv.org/search/cs?searchtype=author&query=Nabeel,Mohamed

## Bio

AI Security Researcher focused on the intersection of machine learning and cybersecurity. My work spans building autonomous threat intelligence agents, developing adversarial ML defenses, and pioneering methods to detect GenAI-generated malware and abuse. I apply large language models and graph neural networks to real-world security problems, with research published at VirusBulletin, DEFCON, and [Un]prompted.

---

## Research Focus

### AI Security Research
Protecting AI systems themselves from adversarial attacks and misuse:
- GenAI threat detection (malicious models, extensions, hallucination exploitation)
- Adversarial robustness and false-positive-resistant deep learning
- LLM red-teaming and prompt injection defense
- Malicious AI model detection on public repositories (Hugging Face, etc.)
- Deep learning API abuse detection

### AI for Cybersecurity
Using AI to detect and neutralize cyber threats:
- Autonomous CTI agents for threat intelligence extraction and battlecard generation
- Graph neural networks for campaign infrastructure discovery and attribution
- Malicious domain detection (zero-day, stockpiled, defensively registered)
- ML-based URL and domain risk scoring
- Semantic threat rules (YARA-like) for AI-generated threat detection

---

## Publications (Recent)

> Full publication list: https://scholar.google.com/citations?user=Lka4RwsAAAAJ&hl=en&sortby=pubdate
> Scholar stats: 83 publications · 1,821 citations · h-index: 21 · i10-index: 34

### Deep Dive into the Abuse of DL APIs To Create Malicious AI Models and How to Detect Them
- **Date:** Jan 2026
- **arXiv:** https://arxiv.org/abs/2601.04553
- **Tags:** Malicious AI Models, DL API Abuse, Model Security
- **Abstract:** Public deep learning model repositories such as Hugging Face have become attractive targets for adversaries distributing malicious AI model artifacts. This paper provides a comprehensive analysis of how attackers abuse deep learning APIs to embed malicious payloads inside model files, and presents a multi-stage detection pipeline combining static structural analysis with behavioral profiling to identify these threats at scale.

### Malicious GenAI Chrome Extensions: Unpacking Data Exfiltration and Malicious Behaviours
- **Date:** Dec 2025
- **arXiv:** https://arxiv.org/abs/2512.10029
- **Tags:** GenAI Extensions, Data Exfiltration, Browser Security
- **Abstract:** Generative AI-themed browser extensions have proliferated rapidly, with many exhibiting data exfiltration and other malicious behaviors while masquerading as productivity tools. This paper analyzes the ecosystem of malicious GenAI Chrome extensions, characterizing their attack patterns, data collection methods, and evasion techniques, and proposes detection strategies based on semantic and behavioral analysis.

### MANTIS: Detection of Zero-Day Malicious Domains Leveraging Low Reputed Hosting Infrastructure
- **Date:** Feb 2025
- **Venue:** IEEE Symposium on Security & Privacy 2025
- **arXiv:** https://arxiv.org/abs/2502.09788
- **Tags:** Zero-Day Domains, Domain Detection, Hosting Infrastructure
- **Abstract:** Zero-day malicious domains pose a critical challenge for web security: they are registered and weaponized faster than reputation systems can react. MANTIS addresses this by leveraging signals from low-reputation hosting infrastructure — shared IP neighborhoods, registrar patterns, and certificate characteristics — to detect malicious domains at time-of-registration, before any user exposure.

---

## Conference Talks

### Detecting GenAI Threats at Scale with YARA-Like Semantic Rules
- **Venue:** [Un]prompted AI Security Practitioner Conference
- **Date:** Mar 2026
- **Location:** San Francisco, CA
- **Video:** https://www.youtube.com/watch?v=PZYtJL6TCwo
- **Tags:** GenAI Detection, YARA, Semantic Rules, Threat Detection
- **Description:** Presenting a novel approach to detecting GenAI-powered threats using semantic rules inspired by YARA, enabling scalable, interpretable detection of AI-generated malicious content.

### CTI Agent: Automated Battlecards from CTI Reports
- **Venue:** DEFCON Recon
- **Date:** Aug 2025
- **Location:** Las Vegas, NV
- **Video:** https://www.youtube.com/watch?v=Y8xMr2JwyjU
- **Tags:** CTI, Autonomous Agents, LLM, Threat Intelligence
- **Description:** Demonstrating an autonomous CTI agent that reads threat intelligence reports and automatically generates structured battlecards for security analysts, reducing manual analysis time dramatically.

### Deep Dive into the Abuse of DL APIs to Create Malicious AI Models and How to Detect Them
- **Venue:** VirusBulletin
- **Date:** Sep 2025
- **Location:** Dublin, Ireland
- **Video:** https://www.youtube.com/watch?v=NYmx6i3bzW4
- **Tags:** Malicious Models, Deep Learning, Model Security, Detection
- **Description:** Comprehensive analysis of how attackers abuse deep learning APIs (Hugging Face, etc.) to distribute malicious AI models, and detection techniques using behavioral and structural analysis.

---

## Recent Patent Portfolio

> 28 patents across two categories: AI Security and AI for Cybersecurity.

### AI Security (6 patents)
Protecting AI systems from adversarial attacks and misuse.

| Title | Date | Description |
|---|---|---|
| AI Agent Skill Content Sanitization | Feb 2026 | Classifies and sanitizes AI agent skill content across multiple states to prevent injection of malicious capabilities into agentic AI systems. |
| Indirect Prompt Injection Detector | Feb 2026 | Detects indirect prompt injection attacks targeting web-based agentic AI systems, defending LLM agents against adversarial inputs embedded in web content. |
| Browser Agent Web-Threat Protection | Dec 2025 | Systematic method to protect browser-based AI agents from web-based threats including prompt hijacking, data exfiltration, and malicious tool misuse. |
| Evasive Malware in Deep Learning Models | Sep 2025 | Detection system for malware hidden inside deep learning model artifacts that abuse hidden functionalities — addressing the emerging threat of weaponized AI models. |
| Browser Extension Squatting | Aug 2025 | Proactively identifies browser extensions that generative AI models are likely to hallucinate, creating a defensive blocklist before attackers exploit LLM hallucination behavior. |
| Adversarial-Resistant Deep Learning for Malicious JS Detection | Jul 2023 | Framework for training deep learning models that are resistant to adversarial examples and maintain low false positive rates — foundational work in robust ML for security. |

### AI for Cybersecurity (22 patents)
Using AI to detect and neutralize cyber threats.

| Title | Date | Description |
|---|---|---|
| CRXAgent: Agentic Extension Detection | Feb 2026 | LLM-agent-based detection of malicious Chrome extensions using semantic code understanding and efficient static analysis, catching novel threats missed by signature-based tools. |
| Browser Extension FP Check Analyzer | Feb 2026 | Multi-dimensional analysis system to reduce false positives in browser extension security detection, improving operational accuracy at scale. |
| Defensively Registered Domain Detector | Jan 2026 | LLM based attribution of defensively registered domains to brands. |
| RAG-Based Extension Impersonation Detector | Jan 2026 | Retrieval-augmented generation (RAG) agentic system that detects browser extensions impersonating legitimate ones, using semantic similarity over a curated extension knowledge base. |
| Detecting Defensively Registered Domains via LLMs | Oct 2025 | LLM-powered system that identifies domains registered defensively by organizations to prevent brand abuse, enabling better threat intelligence prioritization. |
| Inline Extension Security Prevention | Oct 2025 | Inline analysis system that blocks malicious or compromised browser extension installations and updates in real time, before execution. |
| Multimodal Extension Risk Scoring | Aug 2025 | Multimodal LLM agent equipped with analysis tools that scores Chrome extension risk by examining permissions, code behavior, and visual signals simultaneously. |
| Real-Time Certified Hijacking Detection | Aug 2025 | Real-time system that detects and mitigates certificate-based hijacking attacks by monitoring certificate transparency logs for anomalous issuance patterns. |
| Pastejacking Detector | Jul 2025 | Detects pastejacking attacks — where malicious websites silently alter clipboard content — using dynamic browser analysis and LLM agents to identify malicious intent. |
| AVA: OAuth Flow Abuse Detector | Jun 2025 | Analyzes OAuth authentication flows to detect abuse patterns including consent phishing, token hijacking, and malicious app impersonation. |
| Multimodal In-Browser Malicious Site Detection | May 2025 | In-browser multimodal ML system for real-time malicious website detection combining visual, textual, and structural signals with efficient cloud backend support. |
| GraphSeek | Apr 2025 | Graph-powered RAG system using LLMs to detect and attribute indicators of compromise (IoCs) across malicious campaigns, enabling analysts to pivot through related threat infrastructure. |
| AI Social Engineering Defense | Mar 2025 | Grounded AI pipeline detecting social engineering attacks across voice, text, image, and video modalities — multi-modal defense against next-generation phishing. |
| URLAgent | Mar 2025 | LLM-powered autonomous agent that assesses URL maliciousness by combining chain-of-thought reasoning with live tool use — screenshot analysis, content inspection, and threat intel lookups. |
| CampaignNet | Dec 2024 | Graph representation learning system that identifies patient-zero phishing campaigns and clusters related malicious URLs for automated campaign attribution. |
| Deepscam | Sep 2024 | Transfer learning model that analyzes HTML structure and content of web pages to detect scam sites with high precision, generalizing across novel scam templates. |
| TI Ninja | Aug 2024 | Autonomous agent that ingests threat intelligence reports and performs real-time structured extraction of campaign CTI — actors, TTPs, indicators — producing actionable intelligence at scale. |
| AI Deepfake Detection Pipeline | May 2024 | End-to-end AI pipeline for real-time deepfake detection and filtering, combining visual artifact analysis with behavioral signals to catch synthetic media used in fraud. |
| GNN Campaign Detection | May 2024 | Graph neural network system that automatically discovers and maps malicious campaign infrastructure by modeling relationships between domains, IPs, and certificates. |
| Domain Spider | Jan 2024 | Guided crawler that traverses attack infrastructure through WHOIS relationships, certificate transparency, and DNS pivots to proactively map and block malicious domain networks. |
| ML Domain Risk Scoring | Jan 2024 | ML pipeline combining lexical, behavioral, and graph features to produce real-time domain risk scores, powering downstream URL filtering and security policy decisions. |
| Stockpiled Domain Detection | Jun 2023 | Detection methods for identifying domains that attackers register and hold in reserve ('stockpile') before launching coordinated campaigns, enabling proactive blocking. |

---

## Open Source

### syara
- **URL:** https://github.com/nabeelxy/syara
- **Description:** YARA-like semantic rules engine for detecting AI-generated threats
- **Language:** Python
- **Topics:** security, yara, llm, threat-detection

---

*This file is intended to be consumed by LLMs and agents as a structured, comprehensive profile. For the interactive version visit https://nabeelxy.github.io*
