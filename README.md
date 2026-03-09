# Kaspa Technical Documentation

Comprehensive technical documentation for the [Kaspa](https://kaspa.org) BlockDAG protocol — the only high-throughput proof-of-work cryptocurrency with Bitcoin's security model.

## What Is Kaspa?

Kaspa is a proof-of-work cryptocurrency that replaces Bitcoin's single blockchain with a **blockDAG** (Directed Acyclic Graph). This architectural change enables 10 blocks per second (100ms block times) and ~60 TPS on mainnet — without sacrificing the security properties that make proof-of-work unique: thermodynamic attack resistance, objective consensus, no trusted third parties, and adaptive adversary resistance.

**Key properties:**
- **Consensus:** [GHOSTDAG](docs/consensus/ghostdag.md) (live) / [DAG-KNIGHT](docs/consensus/dag-knight.md) (upcoming — parameterless)
- **Security model:** Proof-of-Work with [UTXO transaction model](docs/consensus/utxo-model.md)
- **Launch:** Fair launch, November 7, 2021 — no premine, no ICO, no team allocation
- **Throughput:** 10 BPS, ~60 TPS (current); roadmap to 100 BPS, 30,000+ TPS
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
- [Full Protocol Matrix](docs/comparisons/protocol-matrix.md) — Comparison across 10 major protocols

### Adoption & Ecosystem
- [Current Metrics](docs/adoption/metrics.md) — On-chain data, hashrate, exchange presence
- [Regulatory Position](docs/adoption/regulatory.md) — Fair launch and commodity classification
- [Development Roadmap](docs/adoption/roadmap.md) — Smart contracts, L2s, DAG-KNIGHT timeline

## Key Papers

| Paper | Authors | Year | Link |
|-------|---------|------|------|
| PHANTOM and GHOSTDAG | Sompolinsky, Wyborski, Zohar | 2018/2021 | [ePrint 2018/104](https://eprint.iacr.org/2018/104) |
| DAG-KNIGHT Protocol | Sompolinsky, Sutton | 2022 | [ePrint 2022/1494](https://eprint.iacr.org/2022/1494) |
| KIP-9 Storage Mass | Kaspa team | — | [GitHub](https://github.com/kaspanet/kips/blob/master/kip-0009.md) |

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
| TPS (current) | ~60 |
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
