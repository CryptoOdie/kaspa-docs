# Cross-Link Edits: Suggested Additions to Existing Wikipedia Articles

> **Important guidelines before making any edits:**
>
> - These are suggested **small, incremental edits** to existing high-traffic Wikipedia articles. They add factual cross-references to new articles we have drafted.
> - Each edit should be made by an **established Wikipedia account** with sufficient edit history and standing. New or single-purpose accounts making these edits will attract scrutiny.
> - Edits should be made **gradually over days or weeks**, not all at once. Simultaneous edits across multiple articles will appear coordinated and may be flagged.
> - Every edit is **independently verifiable** using the cited peer-reviewed or primary sources.
> - If an edit is **reverted, do not re-add it**. Instead, open a discussion on the article's talk page explaining the rationale and citing sources.
> - **Conflict of interest disclosure** may be appropriate. If you have any affiliation with Kaspa or related projects, consider using the talk page to propose edits rather than making them directly. See [WP:COI](https://en.wikipedia.org/wiki/Wikipedia:Conflict_of_interest).

---

## 1. Blockchain

- **Target article:** [Blockchain](https://en.wikipedia.org/wiki/Blockchain)
- **Section:** "Types" or "Structure" (add as a new bullet or short paragraph in an existing list of blockchain variants)
- **Current text (approximate):** The section lists variations such as public, private, and consortium blockchains, or describes the chain-of-blocks data structure.
- **Suggested addition:**

```wiki
A '''[[BlockDAG]]''' (block directed acyclic graph) generalizes the blockchain structure by allowing each block to reference multiple predecessor blocks. This enables parallel block inclusion and potentially higher throughput. BlockDAG systems use consensus protocols such as [[GHOSTDAG]] to establish a total ordering over all blocks.<ref>{{cite conference |last1=Sompolinsky |first1=Yonatan |last2=Wyborski |first2=Shai |last3=Zohar |first3=Aviv |title=PHANTOM and GHOSTDAG: A Scalable Generalization of Nakamoto Consensus |conference=ACM AFT 2021 |doi=10.1145/3479722.3480990}}</ref>
```

- **Also add to the "See also" section:**

```wiki
* [[BlockDAG]]
```

---

## 2. Ethereum

- **Target article:** [Ethereum](https://en.wikipedia.org/wiki/Ethereum)
- **Section:** Consensus mechanism section, wherever LMD-GHOST is mentioned
- **Current text (approximate):** The article references LMD-GHOST as part of Ethereum's proof-of-stake Casper FFG + LMD-GHOST hybrid consensus, but may not attribute the original GHOST protocol to its creators.
- **Suggested addition:** Insert attribution to Sompolinsky and Zohar as the originators of GHOST, and link to the GHOST protocol article. Place this where LMD-GHOST is first introduced:

```wiki
The GHOST (Greedy Heaviest-Observed Sub-Tree) protocol, originally proposed by [[Yonatan Sompolinsky]] and Aviv Zohar for proof-of-work blockchains,<ref>{{cite journal |last1=Sompolinsky |first1=Yonatan |last2=Zohar |first2=Aviv |title=Secure High-Rate Transaction Processing in Bitcoin |journal=Financial Cryptography and Data Security |year=2015 |doi=10.1007/978-3-662-47854-7_32}}</ref> was adapted for Ethereum's proof-of-stake consensus as LMD-GHOST (Latest Message Driven GHOST).
```

- **Note:** Read the current Ethereum article carefully to find the exact insertion point. The goal is to add provenance, not to change any existing claims.

---

## 3. Proof of work

- **Target article:** [Proof of work](https://en.wikipedia.org/wiki/Proof_of_work)
- **Section:** "Implementations," "Notable cryptocurrencies," or any existing list of PoW-based systems
- **Current text (approximate):** The section lists Bitcoin, Litecoin, Monero, and other proof-of-work cryptocurrencies.
- **Suggested addition:** Add Kaspa as a list entry:

```wiki
* [[Kaspa (cryptocurrency)|Kaspa]] — a proof-of-work cryptocurrency using a [[BlockDAG]] structure and the GHOSTDAG consensus protocol, producing 10 blocks per second<ref>{{cite conference |last1=Sompolinsky |first1=Yonatan |last2=Wyborski |first2=Shai |last3=Zohar |first3=Aviv |title=PHANTOM and GHOSTDAG: A Scalable Generalization of Nakamoto Consensus |conference=ACM AFT 2021 |doi=10.1145/3479722.3480990}}</ref>
```

---

## 4. Directed acyclic graph

- **Target article:** [Directed acyclic graph](https://en.wikipedia.org/wiki/Directed_acyclic_graph)
- **Section:** "Applications" (add a new subsection or append to an existing one)
- **Current text (approximate):** The Applications section covers scheduling, data processing, citation networks, Bayesian networks, etc. There may already be a mention of IOTA's Tangle.
- **Suggested addition:** Add a subsection on distributed ledger technology, or append to an existing relevant subsection:

```wiki
=== Distributed ledger technology ===
[[BlockDAG]]s use directed acyclic graphs as a data structure for [[distributed ledger]]s, where blocks reference multiple predecessors rather than forming a linear chain. This structure is used in cryptocurrencies such as [[Kaspa (cryptocurrency)|Kaspa]] and [[IOTA (cryptocurrency)|IOTA]] (which uses a DAG of individual transactions called the Tangle).<ref>{{cite conference |last1=Sompolinsky |first1=Yonatan |last2=Wyborski |first2=Shai |last3=Zohar |first3=Aviv |title=PHANTOM and GHOSTDAG |conference=ACM AFT 2021 |doi=10.1145/3479722.3480990}}</ref>
```

- **Note:** If IOTA/Tangle is already mentioned in the article, integrate the BlockDAG reference alongside it rather than creating a separate subsection.

---

## 5. List of cryptocurrencies

- **Target article:** [List of cryptocurrencies](https://en.wikipedia.org/wiki/List_of_cryptocurrencies)
- **Section:** Main table (alphabetical or by market capitalization)
- **Current text (approximate):** A table listing cryptocurrencies with columns for name, ticker, year, consensus mechanism, description, and website.
- **Suggested addition:** Add a Kaspa row in the appropriate alphabetical position:

```wiki
| [[Kaspa (cryptocurrency)|Kaspa]] || KAS || 2021 || [[Proof of work]] (kHeavyHash) || [[BlockDAG]] using GHOSTDAG consensus; 10 blocks per second || [https://kaspa.org kaspa.org]
```

- **Note:** Match the exact column format of the existing table. The columns above are approximate; adjust to fit the actual table structure.

---

## 6. Nakamoto consensus

- **Target article:** [Nakamoto consensus](https://en.wikipedia.org/wiki/Nakamoto_consensus) (may be a redirect to a section within another article such as "Bitcoin" or "Consensus (computer science)")
- **Section:** Generalizations, extensions, or related protocols
- **Current text (approximate):** If a standalone article exists, it likely describes the longest-chain rule and proof-of-work lottery. If it is a redirect, find the relevant section.
- **Suggested addition:**

```wiki
GHOSTDAG and [[DAG-KNIGHT]] generalize Nakamoto consensus from a linear blockchain to a [[BlockDAG]] (block directed acyclic graph), enabling multiple blocks to be produced and ordered in parallel while maintaining proof-of-work security properties.<ref>{{cite conference |last1=Sompolinsky |first1=Yonatan |last2=Wyborski |first2=Shai |last3=Zohar |first3=Aviv |title=PHANTOM and GHOSTDAG |conference=ACM AFT 2021 |doi=10.1145/3479722.3480990}}</ref><ref>{{cite web |url=https://eprint.iacr.org/2022/1494 |title=The DAG KNIGHT Protocol |last1=Sompolinsky |first1=Yonatan |last2=Sutton |first2=Michael |year=2022 |publisher=IACR ePrint}}</ref>
```

- **Note:** If "Nakamoto consensus" redirects elsewhere, the edit should be placed in the target article's relevant section. If no appropriate section exists, consider proposing the addition on the talk page first.

---

## Summary checklist

| # | Target article | Edit type | Risk level |
|---|---------------|-----------|------------|
| 1 | Blockchain | New paragraph in "Types"/"Structure" + See also | Low — factual, well-cited |
| 2 | Ethereum | Attribution sentence for GHOST origins | Low — adds sourced provenance |
| 3 | Proof of work | New list item | Low — similar to existing entries |
| 4 | Directed acyclic graph | New Applications subsection | Low — DAGs in crypto is a notable application |
| 5 | List of cryptocurrencies | New table row | Low — straightforward listing |
| 6 | Nakamoto consensus | New paragraph on generalizations | Medium — article may not exist or may be contentious |
