# Kaspa Technical Documentation

Comprehensive technical documentation for the [Kaspa](https://kaspa.org) BlockDAG protocol — the only high-throughput proof-of-work cryptocurrency with Bitcoin's security model.

## What Is Kaspa?

Kaspa is a proof-of-work cryptocurrency that replaces Bitcoin's single blockchain with a **blockDAG** (Directed Acyclic Graph). This architectural change enables 10 blocks per second (100ms block times) and ~3,000 TPS on mainnet — without sacrificing the security properties that make proof-of-work unique: thermodynamic attack resistance, objective consensus, no trusted third parties, and adaptive adversary resistance.

**Key properties:**
- **Consensus:** [GHOSTDAG](docs/consensus/ghostdag.md) (live) / [DAG-KNIGHT](docs/consensus/dag-knight.md) (upcoming — parameterless)
- **Security model:** Proof-of-Work with [UTXO transaction model](docs/consensus/utxo-model.md)
- **Launch:** Fair launch, November 7, 2021 — no premine, no ICO, no team allocation
- **Throughput:** 10 BPS, ~3,000 TPS (current); roadmap to 100 BPS, 30,000+ TPS
- **Confirmation:** ~10 seconds
- **Max supply:** 28.7 billion KAS ([chromatic halving](docs/consensus/chromatic-halving.md))

## Documentation

### Consensus & Architecture
- [GHOSTDAG Protocol](docs/consensus/ghostdag.md) — How Kaspa orders blocks in a DAG
- [DAG-KNIGHT Protocol](docs/consensus/dag-knight.md) — Parameterless consensus (upcoming)
- [BlockDAG vs Blockchain](docs/consensus/blockdag-vs-blockchain.md) — Why a DAG eliminates orphans and enables throughput
- [UTXO Model & KIP-9 Storage Mass](docs/consensus/utxo-model.md) — Transaction model and state management
- [Chromatic Halving](docs/consensus/chromatic-halving.md) — Smooth emission schedule

### Security Analysis
- [Security Budget & Fee Markets](docs/security/security-budget.md) — Why throughput is essential for long-term PoW security
- [Proof-of-Stake Tradeoffs](docs/security/pos-tradeoffs.md) — What PoS systems trade away for energy efficiency
- [Partition Tolerance](docs/security/partition-tolerance.md) — How protocols handle network splits
- [Work-Then-Select vs Select-Then-Work](docs/security/adaptive-adversary.md) — Adaptive adversary resistance in PoW

### Protocol Comparisons
- [Kaspa vs Bitcoin](docs/comparisons/kaspa-vs-bitcoin.md) — Shared security model, extended throughput
- [Kaspa vs Ethereum](docs/comparisons/kaspa-vs-ethereum.md) — PoW vs PoS security tradeoffs
- [Kaspa vs Solana](docs/comparisons/kaspa-vs-solana.md) — Partition tolerance vs throughput


### Adoption & Ecosystem
- [Current Metrics](docs/adoption/metrics.md) — On-chain data, hashrate, exchange presence
- [Regulatory Position](docs/adoption/regulatory.md) — Fair launch and commodity classification
- [Development Roadmap](docs/adoption/roadmap.md) — Smart contracts, L2s, DAG-KNIGHT timeline

## Key Papers

### Kaspa Consensus Protocols

| Paper | Authors | Year | Venue | Link |
|-------|---------|------|-------|------|
| PHANTOM and GHOSTDAG: A Scalable Generalization of Nakamoto Consensus | Sompolinsky, Wyborski, Zohar | 2018/2021 | ACM AFT 2021 | [ePrint 2018/104](https://eprint.iacr.org/2018/104) · [DOI](https://dl.acm.org/doi/10.1145/3479722.3480990) |
| The DAG-KNIGHT Protocol: A Parameterless Generalization of Nakamoto Consensus | Sompolinsky, Sutton | 2022 | Harvard CRCS / IACR ePrint | [ePrint 2022/1494](https://eprint.iacr.org/2022/1494) |
| SPECTRE: A Fast and Scalable Cryptocurrency Protocol | Sompolinsky, Lewenberg, Zohar | 2016 | IACR ePrint | [ePrint 2016/1159](https://eprint.iacr.org/2016/1159) |
| Secure High-Rate Transaction Processing in Bitcoin (GHOST Protocol) | Sompolinsky, Zohar | 2013/2015 | Financial Cryptography 2015 | [DOI](https://doi.org/10.1007/978-3-662-47854-7_32) |
| Inclusive Block Chain Protocols | Lewenberg, Sompolinsky, Zohar | 2015 | Financial Cryptography 2015 | [DOI](https://doi.org/10.1007/978-3-662-47854-7_33) |

### Kaspa Improvement Proposals (KIPs)

| KIP | Title | Link |
|-----|-------|------|
| KIP-9 | Storage Mass (UTXO bloat prevention via harmonic mass formula) | [GitHub](https://github.com/kaspanet/kips/blob/master/kip-0009.md) |

### Foundational & Related Work

| Paper | Authors | Year | Venue | Link |
|-------|---------|------|-------|------|
| Bitcoin: A Peer-to-Peer Electronic Cash System | Nakamoto | 2008 | — | [bitcoin.org](https://bitcoin.org/bitcoin.pdf) |
| The Bitcoin Backbone Protocol: Analysis and Applications | Garay, Kiayias, Leonardos | 2015 | EUROCRYPT 2015 | [DOI](https://doi.org/10.1007/978-3-662-46803-6_10) |
| Majority is not Enough: Bitcoin Mining is Vulnerable | Eyal, Sirer | 2014 | Financial Cryptography 2014 | [DOI](https://doi.org/10.1007/978-3-662-45472-5_28) |
| Casper the Friendly Finality Gadget | Buterin, Griffith | 2017 | arXiv | [arXiv 1710.09437](https://arxiv.org/abs/1710.09437) |
| Three Attacks on Proof-of-Stake Ethereum | Schwarz-Schilling, Neu, Monnot, Asgaonkar, Tas, Tse | 2021 | IACR ePrint | [ePrint 2021/1413](https://eprint.iacr.org/2021/1413) |
| The Principal–Agent Problem in Liquid Staking | Tzinas, Zindros | 2023/2024 | Financial Cryptography 2024 | [ePrint 2023/605](https://eprint.iacr.org/2023/605) |
| Towards Robust Distributed Systems (CAP Theorem) | Brewer | 2000 | ACM PODC Keynote | [PDF](https://people.eecs.berkeley.edu/~brewer/cs262b-2004/PODC-keynote.pdf) |

## Core Contributors

- **Yonatan Sompolinsky** — PHANTOM, GHOSTDAG, DAG-KNIGHT (Harvard CRCS)
- **Michael Sutton** — Rusty Kaspa lead, DAG-KNIGHT co-author
- **Shai Wyborski** — GHOSTDAG formal security proofs
- **Ori Newman** — UTXO model, Silverscript smart contract language

## Quick Facts

| Property | Value |
|----------|-------|
| Launch | November 7, 2021 |
| Premine | None |
| ICO | None |
| Team allocation | None |
| Consensus | GHOSTDAG (PoW BlockDAG) |
| Block time | 100ms (10 BPS) |
| Confirmation | ~10 seconds |
| TPS (current) | ~3,000 |
| TPS (peak tested) | 5,584 |
| TPS (roadmap) | 30,000+ |
| Max supply | 28.7 billion KAS |
| Mining algorithm | kHeavyHash |
| Transaction model | UTXO |
| Hashrate | ~411-445 PH/s (March 2026) |
| Reference implementation | [rusty-kaspa](https://github.com/kaspanet/rusty-kaspa) (Rust) |

## Links

- [kaspa.org](https://kaspa.org)
- [Kaspa Explorer](https://explorer.kaspa.org/)
- [Kaspalytics](https://www.kaspalytics.com/)
- [GitHub: kaspanet/rusty-kaspa](https://github.com/kaspanet/rusty-kaspa)
- [Kaspa Wiki](https://wiki.kaspa.org)

---

*This documentation is maintained by the Kaspa community. All claims are sourced from academic papers, protocol specifications, or on-chain data. See individual pages for references.*
