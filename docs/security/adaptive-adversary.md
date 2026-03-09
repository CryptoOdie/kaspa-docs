# Adaptive Adversary Resistance: Work-Then-Select

## Overview

An **adaptive adversary** is one who can change their target based on protocol state -- for example, corrupting, bribing, or DDoS-attacking the next known block producer. The degree to which a consensus protocol resists adaptive adversaries is determined by a single architectural question: **does the protocol reveal the next block producer before or after the block is produced?**

This distinction -- work-then-select versus select-then-work -- is one of the most underappreciated differences between PoW and PoS consensus.

---

## Two Paradigms

### Work-Then-Select (PoW)

1. A miner performs computational work (hashing).
2. If the hash meets the difficulty target, the miner has produced a valid block.
3. The miner broadcasts the block.
4. The network learns who produced the block only when it arrives.

The block producer is unknown until the block exists. Discovery and production are the same event.

### Select-Then-Work (PoS)

1. The protocol selects the next block producer (via stake-weighted random selection).
2. The selected validator assembles and signs the block.
3. The validator broadcasts the block.

The block producer is known before the block exists -- sometimes far in advance.

### Comparison

| Property | Work-Then-Select (PoW) | Select-Then-Work (PoS) |
|----------|----------------------|----------------------|
| Producer identity | Unknown until block exists | Known before block exists |
| DDoS targeting | Impossible (target unknown) | Possible (target known) |
| Bribery before the fact | Impossible (cannot identify target) | Possible (target identifiable) |
| Coercion window | None | Duration of advance knowledge |
| Reveal timing | Reveal = production (simultaneous) | Reveal precedes production |

---

## PoS Leader Visibility by Protocol

Different PoS protocols expose leader identity to varying degrees:

| Protocol | Leader Knowledge | Attack Window | Mitigation |
|----------|-----------------|---------------|------------|
| **Solana** | Deterministic schedule, known in advance | Entire epoch; attacker can plan DDoS or bribery well ahead | None -- schedule is public by design |
| **Ethereum** | Proposer known one epoch (~6.4 min) in advance | ~6.4 minutes before the slot | Single Secret Leader Election (SSLE) is an active research area, not yet deployed |
| **Algorand** | VRF-based selection; proposer secret until self-reveal | Only after reveal (best PoS defense) | Proposer can still be targeted after reveal for remainder of round |
| **Aptos/Sui** | Leader rotation known to validator set | Variable | Small validator set limits attack surface but also limits decentralization |

Even Algorand's VRF-based approach -- the strongest PoS defense against adaptive adversaries -- has a window: once the proposer reveals themselves (necessary to prove selection), they can be targeted for the remainder of the round.

In PoW, there is no such window. The reveal and the block production are the same event.

---

## Why This Matters for Security

### DDoS Against Known Leaders

When the next block producer is known, an attacker can direct network flooding at that specific node. In Solana's case, the deterministic leader schedule makes this straightforward. A well-resourced adversary could systematically disrupt block production by targeting each leader in sequence.

### Bribery and Coercion

A known future producer can be approached with bribes (to include or exclude specific transactions) or subjected to coercion (legal, physical, or economic pressure). In PoW, there is no "future producer" to approach -- the producer emerges from the work itself.

### Targeted Censorship

If an adversary wants to censor a specific transaction, knowing the next producer allows them to target exactly the entity that will decide transaction inclusion. In PoW, the adversary would need to compromise a majority of total hashrate since any miner could be the next producer.

---

## DAG Structure Eliminates Orphan Centralization

Beyond adaptive adversary resistance, Kaspa's DAG architecture solves a second problem that traditionally limits PoW speed: the orphan rate.

### The Orphan Problem in Single-Chain PoW

In Bitcoin, if two miners find blocks at nearly the same time, only one survives. The orphan rate approximates:

```
orphan_rate ~ 1 - e^(-block_rate x propagation_delay)
```

Orphans create a structural advantage for large mining pools:

| Factor | Large Pool | Small Miner |
|--------|-----------|-------------|
| Block discovery notification | Immediate (zero self-propagation delay) | Must wait for network propagation |
| Orphan risk | Lower (starts mining own block instantly) | Higher (mining on stale tip during propagation) |
| Effective hashrate advantage | Increases with block rate | Decreases with block rate |

At Bitcoin's 10-minute block time, orphan rates are negligible (~0.1%). At 1-second block times on a single chain, orphan rates would exceed 30%, and mining would centralize rapidly.

### How the DAG Solves This

In Kaspa's [blockDAG](../consensus/ghostdag.md):

- Every block references all known tips (unreferenced blocks) as parents.
- Parallel blocks -- which would be orphans in a single chain -- are all included in the DAG.
- [GHOSTDAG](../consensus/ghostdag.md) orders all blocks into a consistent total order.

**There are no orphans in a DAG.** Every honestly-mined block contributes to the ledger and earns its miner a reward. The orphan-rate centralization pressure that limits single-chain PoW does not exist.

This is what enables Kaspa to run at 10 blocks per second (100 ms block times) without the centralization that would destroy a single-chain PoW system at equivalent speeds.

---

## Kaspa's Combined Properties

| Property | Bitcoin | Kaspa | Ethereum | Solana |
|----------|---------|-------|----------|--------|
| Block time | 10 min | 100 ms | 12 s | 400 ms |
| Orphan/wasted blocks | Yes (~0.1%) | No (DAG) | No (selected proposer) | No (selected leader) |
| Producer known in advance | No | No | 1 epoch ahead | Full schedule public |
| Adaptive adversary resistance | Strong | Strong | Moderate | Weak |
| Confirmation mechanism | Cumulative PoW | Cumulative PoW in DAG | 2/3 stake attestation | 2/3 stake votes |
| Speed-decentralization tradeoff | Severe (orphan rate) | Eliminated (DAG) | Present (validator set size) | Severe (hardware requirements) |

Kaspa preserves both of PoW's key security properties -- work-then-select and permissionless mining -- while achieving block production speeds previously available only to PoS systems.

For how this throughput enables sustainable [fee-based security](security-budget.md), see the Security Budget page.

---

## References

- Sompolinsky, Y., Wyborski, S., Zohar, A. "PHANTOM and GHOSTDAG: A Scalable Generalization of Nakamoto Consensus." AFT 2021. [ePrint 2018/104](https://eprint.iacr.org/2018/104)
- Sompolinsky, Y., Sutton, M. "The DAG KNIGHT Protocol." [ePrint 2022/1494](https://eprint.iacr.org/2022/1494)
- Solana consensus and leader schedule: [docs.solanalabs.com](https://docs.solanalabs.com/implemented-proposals/tower-bft)
- Ethereum proposer selection: [ethereum.org](https://ethereum.org/developers/docs/consensus-mechanisms/pos/)
- Algorand VRF-based selection: [algorand.co](https://algorand.co/technology/pure-proof-of-stake)
- Kaspa Crescendo hard fork (10 BPS): [kaspa.org](https://kaspa.org/kaspa-updates-to-crescendo-and-10bps/)
