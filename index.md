---
layout: default
title: Kaspa Technical Documentation
---

# Kaspa Technical Documentation

Comprehensive technical documentation for [Kaspa](https://kaspa.org) — the only high-throughput proof-of-work cryptocurrency with Bitcoin's security model.

## What Is Kaspa?

Kaspa is a proof-of-work cryptocurrency using a **blockDAG** (Directed Acyclic Graph) instead of a blockchain. It achieves 10 blocks per second with 100ms block times and ~60 TPS — without sacrificing the security properties that make PoW unique.

| Property | Value |
|----------|-------|
| Consensus | GHOSTDAG (PoW BlockDAG) |
| Block time | 100ms (10 BPS) |
| Confirmation | ~10 seconds |
| TPS | ~60 (current); 30,000+ (roadmap) |
| Launch | November 7, 2021 — fair, no premine |
| Max supply | 28.7 billion KAS |
| Mining | kHeavyHash (ASIC) |
| Transaction model | UTXO |

## Documentation

### Consensus & Architecture

- **[GHOSTDAG Protocol](docs/consensus/ghostdag.md)** — How Kaspa orders blocks in a DAG using k-clusters and the selected parent chain
- **[DAG-KNIGHT Protocol](docs/consensus/dag-knight.md)** — Upcoming parameterless consensus that infers network conditions from DAG topology
- **[BlockDAG vs Blockchain](docs/consensus/blockdag-vs-blockchain.md)** — Why a DAG eliminates orphans and enables high-throughput PoW
- **[UTXO Model & KIP-9](docs/consensus/utxo-model.md)** — Transaction model, MuHash commitments, storage mass formula
- **[Chromatic Halving](docs/consensus/chromatic-halving.md)** — Smooth emission schedule without supply shocks

### Security Analysis

- **[Security Budget & Fee Markets](docs/security/security-budget.md)** — Why high throughput is essential for long-term PoW security
- **[PoS Security Tradeoffs](docs/security/pos-tradeoffs.md)** — What proof-of-stake trades away for energy efficiency
- **[Partition Tolerance](docs/security/partition-tolerance.md)** — How protocols handle network splits (Kaspa merges, Solana halts)
- **[Adaptive Adversary Resistance](docs/security/adaptive-adversary.md)** — Work-then-select vs select-then-work

### Protocol Comparisons

- **[Kaspa vs Bitcoin](docs/comparisons/kaspa-vs-bitcoin.md)** — Same security model, 6000x block rate
- **[Kaspa vs Ethereum](docs/comparisons/kaspa-vs-ethereum.md)** — PoW vs PoS, weak subjectivity, MEV
- **[Kaspa vs Solana](docs/comparisons/kaspa-vs-solana.md)** — Partition tolerance vs throughput
- **[Full Protocol Matrix](docs/comparisons/protocol-matrix.md)** — 10-protocol comparison

### Ecosystem

- **[Current Metrics](docs/adoption/metrics.md)** — On-chain data, hashrate, exchange presence
- **[Regulatory Position](docs/adoption/regulatory.md)** — Fair launch and commodity classification
- **[Development Roadmap](docs/adoption/roadmap.md)** — Smart contracts, L2s, DAG-KNIGHT

## Key Papers

| Paper | Authors | Link |
|-------|---------|------|
| PHANTOM and GHOSTDAG | Sompolinsky, Wyborski, Zohar (2018/2021) | [ePrint](https://eprint.iacr.org/2018/104) |
| DAG-KNIGHT Protocol | Sompolinsky, Sutton (2022) | [ePrint](https://eprint.iacr.org/2022/1494) |
| KIP-9 Storage Mass | Kaspa team | [GitHub](https://github.com/kaspanet/kips/blob/master/kip-0009.md) |

## Links

- [kaspa.org](https://kaspa.org) · [Explorer](https://explorer.kaspa.org/) · [Kaspalytics](https://www.kaspalytics.com/) · [GitHub](https://github.com/kaspanet/rusty-kaspa) · [Wiki](https://wiki.kaspa.org)
