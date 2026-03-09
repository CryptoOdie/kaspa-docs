# GHOSTDAG: Kaspa's Consensus Protocol

## Overview

GHOSTDAG (Greedy Heaviest Observed Sub-Tree DAG) is the consensus protocol running on Kaspa's mainnet. It is a greedy polynomial-time approximation of the PHANTOM protocol, designed to order blocks in a blockDAG while maintaining proof-of-work security guarantees equivalent to Bitcoin's Nakamoto consensus.

**Paper:** "PHANTOM and GHOSTDAG: A Scalable Generalization of Nakamoto Consensus"
**Authors:** Yonatan Sompolinsky, Shai Wyborski, Aviv Zohar
**Published:** ACM Conference on Advances in Financial Technologies (AFT 2021), pp. 57-70
**ePrint:** [2018/104](https://eprint.iacr.org/2018/104)

## The Problem GHOSTDAG Solves

In Bitcoin's single-chain architecture, blocks are produced sequentially. When two miners find blocks at nearly the same time, only one survives — the other becomes an **orphan** (wasted work). This creates a fundamental tradeoff:

- **Faster blocks → more orphans → centralization pressure** (large miners waste less work)
- **Slower blocks → fewer orphans → low throughput**

Bitcoin's 10-minute block time exists because of this constraint. It keeps the orphan rate below ~0.1% but limits throughput to ~7 TPS.

GHOSTDAG eliminates this tradeoff by replacing the chain with a **Directed Acyclic Graph** where parallel blocks are incorporated rather than discarded.

## How GHOSTDAG Works

### BlockDAG Structure

In Kaspa's blockDAG, each block references **multiple parents** — all blocks the miner knew about when producing the block (all "tips" of the DAG). This means:

- Blocks produced simultaneously by different miners are **both included**
- No blocks are orphaned
- The DAG naturally captures the network's parallel activity

### k-Clusters: Separating Honest from Adversarial Blocks

The core concept is the **k-cluster**. A subset S of the DAG is a k-cluster if:

```
For every block B in S: |anticone(B) ∩ S| ≤ k
```

Where the **anticone** of a block is the set of blocks with no ordering relationship to it (neither in its past nor its future).

The parameter k represents the expected number of parallel blocks during one network propagation delay:

```
k ≈ 2 × D × λ
```

Where D is propagation delay and λ is the block creation rate.

**Why this works:** Honest miners reference all known blocks as parents. When they produce blocks in parallel (during propagation delay), these blocks are well-connected — they have small anticones relative to each other. An attacker who withholds blocks and releases them later creates blocks with **large anticones** (they don't reference recent honest blocks, and recent honest blocks don't reference them).

The k-cluster concept captures exactly this distinction: honest parallel blocks fit within a k-cluster; adversarial blocks don't.

### The GHOSTDAG Algorithm

1. **Select blue parent:** Each block selects the parent with the highest **blue score** (accumulated count of "blue" blocks in its past).

2. **Build the blue set:** Following the chain of selected parents (the **selected parent chain**), the algorithm greedily adds blocks to the "blue set" if their anticone within the blue set doesn't exceed k.

3. **Order all blocks:** The selected parent chain provides the backbone ordering. Non-chain blocks are interleaved based on when they were "merged" by chain blocks.

4. **Resolve conflicts:** The total ordering induces a transaction ordering. Conflicting transactions (e.g., double-spends) are resolved by the first-seen rule within this ordering.

### Security Guarantee

Shai Wyborski provided the formal proof:

> The ordering produced by GHOSTDAG is **irreversible up to an exponentially negligible probability** — the probability of reversing a confirmed transaction decreases exponentially with depth.

Wyborski notably found and corrected a faulty argument in the original security proof, then proved the corrected statement. This is the foundational security result underpinning Kaspa.

## Current Deployment

| Parameter | Value |
|-----------|-------|
| Status | Live on Kaspa mainnet |
| Block rate | 10 BPS (100ms block times) |
| Confirmation time | ~10 seconds |
| Upgrade | Crescendo hard fork (May 5, 2025) — from 1 BPS to 10 BPS |
| Implementation | Rust ([rusty-kaspa](https://github.com/kaspanet/rusty-kaspa)) |

## GHOSTDAG's Limitation

The parameter k must be set **before deployment** as a conservative upper bound on expected network delay. If k is too low, the protocol may incorrectly classify honest parallel blocks as adversarial under high latency. If k is too high, confirmation times are unnecessarily slow.

This static parameter means GHOSTDAG cannot adapt to changing network conditions. The [DAG-KNIGHT protocol](dag-knight.md) addresses this limitation by making consensus entirely parameterless.

## References

- Sompolinsky, Y., Wyborski, S., Zohar, A. "PHANTOM and GHOSTDAG: A Scalable Generalization of Nakamoto Consensus." [ePrint 2018/104](https://eprint.iacr.org/2018/104). Published at ACM AFT 2021. [DOI](https://dl.acm.org/doi/10.1145/3479722.3480990)
- Wyborski, S. "GHOSTDAG 101 Workshop." [DBLP](https://dblp.org/pid/307/5516.html)
- Kaspa documentation: [kaspa.org](https://kaspa.org/what-is-ghostdag-and-dagknight/)
