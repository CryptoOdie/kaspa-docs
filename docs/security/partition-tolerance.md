# Network Partition Tolerance

## Overview

A network partition occurs when segments of nodes lose connectivity with each other -- whether from undersea cable cuts, state-level internet shutdowns, natural disasters, or targeted infrastructure attacks. For a protocol aspiring to function as global money, partition tolerance is not optional. It is the **minimum requirement**.

The CAP theorem (Brewer, 2000) establishes that distributed systems can provide at most two of three properties: **C**onsistency, **A**vailability, and **P**artition tolerance. Since partitions are inevitable in global networks, the practical choice is between consistency and availability during a partition.

---

## Partition Behavior Comparison

### During a Partition

| Protocol | Consensus | Behavior |
|----------|-----------|----------|
| **Bitcoin** | PoW chain | Both sides continue mining independently on separate chains. |
| **Ethereum** | PoS (Casper) | Finality halts if neither side holds 2/3 of stake. Chain continues producing unfinalized blocks. Inactivity leak begins draining offline validators after 4 epochs (~25 min). |
| **Solana** | PoS (Tower BFT) | Network halts entirely if >1/3 of validators are unreachable. No blocks produced. No transactions processed. |
| **Avalanche** | PoS (Snowball) | Degrades without 2/3 supermajority. May halt or produce conflicting decisions depending on partition geometry. |
| **Kaspa** | PoW DAG ([GHOSTDAG](../consensus/ghostdag.md)) | Both sides continue producing blocks independently. The DAG grows on both sides. |

### After Reconnection

| Protocol | Recovery Mechanism | Work/Stake Wasted |
|----------|-------------------|-------------------|
| **Bitcoin** | Shorter chain is orphaned. Transactions return to mempool. | 100% of losing fork's mining energy |
| **Ethereum** | Inactivity leak continues until finality restores. Recovery can take weeks. | Offline validators permanently lose stake |
| **Solana** | Manual validator coordination required to restart. | All transactions during downtime are lost |
| **Avalanche** | Requires reconnection of sufficient validators. | Depends on partition duration |
| **Kaspa** | **All blocks from both sides merge into the DAG.** [GHOSTDAG](../consensus/ghostdag.md) orders all blocks. Conflicting transactions resolved by ordering. | **Zero** -- all honestly-mined blocks incorporated |

### The Critical Difference

In Kaspa, a partition is simply a period of high-latency parallel mining. The DAG structure inherently accommodates it. No blocks are wasted, no miners are punished, and no manual intervention is required. When connectivity returns, everything merges.

---

## Solana Outage History

Solana's design prioritizes consistency over availability -- when the network cannot reach a 2/3 supermajority, it halts entirely. This has produced multiple documented outages:

| Date | Duration | Cause |
|------|----------|-------|
| Dec 3, 2020 | ~6 hours | Turbine bug; two validators produced conflicting blocks |
| Sep 14, 2021 | ~17 hours | Grape Protocol IDO bot flood overwhelmed consensus |
| Jan 6--12, 2022 | ~1 week degraded | High-compute transactions overwhelmed capacity |
| Apr 30--May 1, 2022 | Hours | Metaplex NFT mint; 6M requests/second, 100+ Gbps per node |
| Jun 1, 2022 | Hours | Consensus failure and clock drift |
| Sep 2022 | Hours | Duplicate block bug from hot-spare validator |
| Feb 25, 2023 | Several hours | Oversized block overwhelmed Turbine propagation |
| Feb 2024 | ~5 hours | LoadedPrograms bug; required coordinated validator restart |

In aggregate, 2022 saw approximately 26 issues ranging from degraded performance to full outages. Stability improved significantly from 2023 onward, but the architectural susceptibility to halts remains inherent to the consensus design.

Each outage represents a period where **no transactions were processed**. For a protocol handling financial infrastructure, a payment network that stops working under stress is categorically different from one that slows down.

**Sources:** [CoinLaw Solana Statistics](https://coinlaw.io/solana-statistics/) -- [Helius Blog](https://www.helius.dev/blog/consensus-on-solana)

---

## Ethereum's Inactivity Leak

Ethereum's partition handling introduces a mechanism that can punish honest validators:

1. A partition occurs (e.g., an entire country loses internet connectivity).
2. Validators in the disconnected region cannot attest to blocks.
3. After 4 epochs without finalization (~25 minutes), the **inactivity leak** activates.
4. Disconnected validators' stakes are drained quadratically -- penalties escalate over time.
5. The leak continues until remaining online validators control 2/3 of remaining stake.

Validators disconnected through no fault of their own -- undersea cable cuts, government shutdowns, natural disasters -- are financially punished. This creates incentives for:

- **Geographic concentration** -- locate near the majority of validators
- **Infrastructure consolidation** -- use the same cloud providers as everyone else
- **Jurisdictional avoidance** -- avoid regions with unreliable internet

These incentives push against the decentralization and geographic distribution that partition tolerance is supposed to support.

**Source:** [Ethereum Inactivity Leak](https://eth2book.info/latest/part2/incentives/inactivity/)

---

## Why Partition Tolerance Is Non-Negotiable for Global Money

Partitions are not theoretical edge cases. They are routine operational events:

| Event Type | Frequency | Example |
|-----------|-----------|---------|
| Undersea cable cuts | Multiple per year | Affects entire continents |
| State-level internet shutdowns | Regular occurrence | Iran, Myanmar, Russia, Egypt, India |
| Natural disasters | Seasonal | Can isolate regions for days or weeks |
| Military conflicts | Ongoing | Deliberate targeting of communications infrastructure |

A protocol that halts (Solana), punishes honest participants (Ethereum), or discards valid work (Bitcoin) during these events cannot reliably serve as global money. Only a protocol that absorbs partitions gracefully -- continuing on all sides, merging when connectivity returns, wasting nothing -- meets the minimum requirement.

---

## DAG-KNIGHT: Adaptive Partition Response

When [DAG-KNIGHT](../consensus/dag-knight.md) is deployed, Kaspa's partition handling gains an additional property: **adaptive confirmation times**.

| Network State | DAG Topology | Confirmation Time |
|--------------|-------------|-------------------|
| Normal (low latency) | Blocks have small anticones; tight connectivity | Short (a few round-trip times) |
| Partitioned (high latency) | Blocks have large anticones; disconnected segments | Automatically increases to maintain security |
| Reconnected (recovering) | Topology shows improving connectivity | Automatically decreases back to normal |

DAG-KNIGHT is the first permissionless PoW protocol with no a priori bound on network latency. It infers all necessary parameters from the DAG topology itself. No manual intervention, no parameter changes, no validator coordination.

This is what "parameterless consensus" means in practice: the protocol handles whatever network conditions it encounters, including conditions the designers never explicitly anticipated.

**Paper:** Sompolinsky, Y. & Sutton, M. "The DAG KNIGHT Protocol: A Parameterless Generalization of Nakamoto Consensus." [ePrint 2022/1494](https://eprint.iacr.org/2022/1494)

> **Note:** DAG-KNIGHT is not yet deployed on Kaspa mainnet as of early 2026. An early Rust implementation exists. Deployment is planned as part of a bundled hard fork targeting 2026--2027.

---

## References

- Sompolinsky, Y., Wyborski, S., Zohar, A. "PHANTOM and GHOSTDAG: A Scalable Generalization of Nakamoto Consensus." AFT 2021. [ePrint 2018/104](https://eprint.iacr.org/2018/104)
- Sompolinsky, Y., Sutton, M. "The DAG KNIGHT Protocol." [ePrint 2022/1494](https://eprint.iacr.org/2022/1494)
- Brewer, E. "Towards Robust Distributed Systems." ACM PODC Keynote, 2000.
- Solana outage history: [CoinLaw](https://coinlaw.io/solana-statistics/) -- [Helius Blog](https://www.helius.dev/blog/consensus-on-solana)
- Ethereum inactivity leak: [eth2book.info](https://eth2book.info/latest/part2/incentives/inactivity/)
- Wyborski security proof: [GHOSTDAG 101 Workshop](https://dblp.org/pid/307/5516.html)
