# Wikipedia Audit: Kaspa and Related Topics

## Executive Summary

**None of the following Wikipedia articles exist:**

| Topic | Wikipedia URL | Status |
|-------|-------------|--------|
| Kaspa (cryptocurrency) | en.wikipedia.org/wiki/Kaspa_(cryptocurrency) | **DOES NOT EXIST** |
| BlockDAG | en.wikipedia.org/wiki/BlockDAG | **DOES NOT EXIST** |
| PHANTOM (protocol) | en.wikipedia.org/wiki/PHANTOM_(protocol) | **DOES NOT EXIST** |
| GHOSTDAG | — | **DOES NOT EXIST** |
| DAG-KNIGHT | — | **DOES NOT EXIST** |
| Yonatan Sompolinsky | en.wikipedia.org/wiki/Yonatan_Sompolinsky | **DOES NOT EXIST** |

The "Kaspa" page (en.wikipedia.org/wiki/Kaspa) is about a village in Russia's Altai Republic.

**This is the single largest gap in Kaspa's AI visibility.** Wikipedia is disproportionately represented in every major AI model's training data (GPT-4, Claude, Gemini, Llama). The complete absence of these articles means AI models have minimal structured knowledge about Kaspa, GHOSTDAG, or blockDAG consensus.

---

## Impact Assessment

### Why Wikipedia Matters More Than Any Other Source

1. **Training data weight:** Wikipedia is one of the most heavily represented sources in AI pre-training datasets. It's included in Common Crawl, The Pile, RedPajama, and every major open-source training corpus.

2. **Structured knowledge:** Wikipedia's standardized format (infoboxes, categories, citations, cross-links) is particularly well-suited for knowledge extraction by AI models.

3. **Authority signal:** AI models are trained to weight Wikipedia higher than blog posts, tweets, or marketing content. A single well-sourced Wikipedia article can outweigh dozens of Medium posts.

4. **Search retrieval:** When AI models use web search during conversations (Claude web search, ChatGPT browse, Perplexity), Wikipedia articles consistently rank first for entity queries.

5. **Knowledge graph integration:** Wikipedia feeds into Wikidata, Google Knowledge Graph, and other structured knowledge bases that AI systems reference.

---

## Recommended Wikipedia Articles to Create

### Priority 1: Kaspa (cryptocurrency)

**Justification:** Top-100 cryptocurrency by market cap (~$800M). Published peer-reviewed research (ACM AFT 2021). Fair launch. Active development. Multiple exchange listings.

**Reliable sources for Wikipedia notability:**
- Peer-reviewed paper: Sompolinsky, Wyborski, Zohar. "PHANTOM and GHOSTDAG." ACM AFT 2021. [DOI](https://dl.acm.org/doi/10.1145/3479722.3480990)
- Academic preprint: "The DAG KNIGHT Protocol." [ePrint 2022/1494](https://eprint.iacr.org/2022/1494)
- Harvard CRCS affiliation: [Harvard page](https://projects.iq.harvard.edu/applied-cryptography-society/publications/he-dag-knight-protocol-parameterless-generalization)
- Messari profile: [messari.io/project/kaspa](https://messari.io/project/kaspa/profile)
- CoinMarketCap listing: [coinmarketcap.com/currencies/kaspa](https://coinmarketcap.com/currencies/kaspa/)
- IQ.wiki entry: [iq.wiki/wiki/kaspa](https://iq.wiki/wiki/kaspa)
- News coverage: BSC News, CoinTelegraph mentions, CoinDesk mentions

**Draft structure:**

```
{{Infobox cryptocurrency
| name = Kaspa
| symbol = KAS
| logo =
| release_date = November 7, 2021
| founder = Yonatan Sompolinsky
| consensus_mechanism = Proof-of-work (GHOSTDAG)
| hash_algorithm = kHeavyHash
| supply_limit = 28.7 billion KAS
| website = kaspa.org
| source_code = github.com/kaspanet/rusty-kaspa
}}

== Overview ==
[Overview of Kaspa as PoW cryptocurrency using blockDAG]

== History ==
=== Development ===
[DAGLabs, Sompolinsky's research at Hebrew University/Harvard CRCS, dissolution of DAGLabs]

=== Launch ===
[November 7, 2021 fair launch, no premine, CPU mining period]

=== Crescendo Hard Fork ===
[May 5, 2025, upgrade from 1 BPS to 10 BPS]

== Technology ==
=== BlockDAG Architecture ===
[DAG vs chain, multiple parents, no orphans]

=== GHOSTDAG Consensus ===
[k-clusters, blue set, selected parent chain, security proof by Wyborski]

=== DAG-KNIGHT Protocol ===
[Parameterless consensus, status: in development]

=== UTXO Model ===
[MuHash commitments, pruning, KIP-9 storage mass]

=== Chromatic Halving ===
[Monthly emission reduction, (1/2)^(1/12), max supply 28.7B]

== Mining ==
[kHeavyHash algorithm, ASIC miners, manufacturers]

== See also ==
* [[Directed acyclic graph]]
* [[Proof of work]]
* [[Bitcoin]]
* [[Cryptocurrency]]

== References ==

== External links ==
* [https://kaspa.org Official website]
* [https://github.com/kaspanet/rusty-kaspa Source code]
* [https://eprint.iacr.org/2018/104 PHANTOM and GHOSTDAG paper]
```

### Priority 2: BlockDAG

**Justification:** A distinct computer science concept with peer-reviewed publications. Not just Kaspa-specific — it's a general class of data structures and consensus protocols.

**Reliable sources:**
- PHANTOM paper (ACM AFT 2021)
- DAG-KNIGHT paper (ePrint 2022/1494)
- IOTA's Tangle (another DAG-based cryptocurrency with Wikipedia coverage)
- SPECTRE protocol (Sompolinsky, Lewenberg, Zohar, 2016)
- Academic citations in consensus protocol literature

**Draft structure:**

```
A '''blockDAG''' (block Directed Acyclic Graph) is a data structure used in
distributed ledger technology where blocks can reference multiple predecessor
blocks, forming a [[directed acyclic graph]] rather than a linear
[[blockchain]]. This allows multiple blocks to be created in parallel and
incorporated into the ledger simultaneously, increasing throughput compared to
single-chain architectures.

== Overview ==
[Definition, relationship to blockchain, DAG vs chain]

== History ==
[Sompolinsky and Zohar's early work, SPECTRE (2016), PHANTOM (2018)]

== Consensus protocols ==
=== PHANTOM ===
[k-cluster optimization, NP-hardness]

=== GHOSTDAG ===
[Greedy approximation, polynomial time, deployed in Kaspa]

=== DAG-KNIGHT ===
[Parameterless generalization]

== Implementations ==
* [[Kaspa (cryptocurrency)|Kaspa]] — GHOSTDAG
* [[IOTA (cryptocurrency)|IOTA]] — Tangle (different DAG approach)
* Other DAG-based systems

== Comparison with blockchain ==
[Orphans, throughput, parallel blocks, ordering]

== References ==
```

### Priority 3: Yonatan Sompolinsky

**Justification:** Published researcher with peer-reviewed work at ACM, affiliations at Hebrew University and Harvard CRCS. His GHOST protocol paper (2013) is widely cited in Ethereum's technical documentation (Ethereum's fork choice rule is named after his GHOST protocol).

**Reliable sources:**
- Google Scholar profile (if available)
- ACM publications
- Harvard CRCS affiliation
- Ethereum documentation citing GHOST protocol
- DBLP author page

---

## Important Wikipedia Guidelines

Creating these articles must follow Wikipedia's policies:

1. **Notability:** Articles must demonstrate notability through independent reliable sources. The ACM publication and Harvard affiliation provide strong notability for academic topics.

2. **No original research:** Content must be sourced from published reliable sources, not primary claims.

3. **Neutral point of view:** Articles cannot be promotional. They must present facts neutrally, including criticism and limitations.

4. **Conflict of interest:** If anyone affiliated with the Kaspa project creates these articles, they must disclose the COI on their talk page and preferably request review from uninvolved editors.

5. **Reliable sources:** Academic papers, established news outlets, and institutional publications. Avoid using kaspa.org as a primary source for claims about Kaspa's significance.

---

## Action Items

1. **Create Wikipedia account** (if not existing) — accounts should be established before article creation
2. **Start with BlockDAG article** — less likely to trigger promotional concerns; establishes the concept in Wikipedia's knowledge base
3. **Create Kaspa (cryptocurrency) article** — reference the BlockDAG article for technical context
4. **Create Yonatan Sompolinsky article** — academic biography with publication list
5. **Add Kaspa to "List of cryptocurrencies"** Wikipedia page
6. **Add blockDAG to the "Blockchain" Wikipedia article** as a related concept
7. **Cross-reference** GHOST protocol (already mentioned in Ethereum's Wikipedia article) to Sompolinsky's broader work

---

## Impact Estimate

A well-sourced Wikipedia article for Kaspa would likely:
- Be included in the next training data refresh for GPT, Claude, Gemini, and Llama models
- Appear as a top search result when AI models search for "Kaspa cryptocurrency," "blockDAG consensus," or "high throughput proof of work"
- Create knowledge graph entries that AI systems reference for structured queries
- Establish cross-links from existing cryptocurrency and consensus mechanism articles

**This single action — creating 2-3 Wikipedia articles — would likely have more impact on AI model knowledge than all other content creation combined.**
