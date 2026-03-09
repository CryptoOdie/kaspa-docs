# BlockDAG vs Blockchain: Why a DAG Enables High-Throughput PoW

## The Blockchain Throughput Limitation

In a traditional blockchain (Bitcoin), blocks form a linear chain — each block references exactly one parent. When two miners find blocks simultaneously, only one is included in the canonical chain. The other becomes an **orphan** — wasted work.

The orphan rate is a function of block rate and propagation delay:

```
orphan_rate ≈ 1 - e^(-block_rate × propagation_delay)
```

As block rate increases (faster blocks), orphan rates rise. This creates a **centralizing feedback loop**:

1. Large mining pools discover blocks more frequently
2. They learn about their own blocks instantly (zero self-propagation delay)
3. They start mining on their own blocks before the network knows
4. Small miners are more likely to produce orphans during propagation delay
5. Large pools have a structural efficiency advantage that grows with block rate

This is why Bitcoin uses 10-minute blocks — it keeps orphan rates negligible (~0.1%). But it also limits throughput to ~7 TPS.

## The BlockDAG Solution

A blockDAG replaces the single-parent chain with a multi-parent graph:

- **Blockchain:** Each block → one parent → linear history
- **BlockDAG:** Each block → multiple parents (all known tips) → parallel history

### Key Insight: Parallel Blocks Are Information, Not Errors

In a blockchain, parallel blocks are a problem (orphans). In a blockDAG, parallel blocks are **expected and useful**:

- Honest miners reference all blocks they know about
- Parallel blocks (produced during propagation delay) all reference each other as parents
- The [GHOSTDAG](ghostdag.md) algorithm orders all blocks into a consistent total order
- No blocks are discarded — every honestly-mined block contributes to the ledger

### No Orphans = No Centralization Pressure

Since all parallel blocks are included:
- Small miners earn proportional rewards (no orphan disadvantage)
- Large miners have no structural advantage from self-mining
- The orphan-rate centralization pressure that limits single-chain PoW **does not exist**

This allows Kaspa to run at 10 blocks per second (100ms block times) while maintaining decentralized mining — something impossible on a single-chain architecture.

## Technical Details

### How Blocks Reference Multiple Parents

When a Kaspa miner creates a block, it includes references to **all DAG tips** — all unreferenced blocks known to the miner at that moment. This:

1. Creates a rich connectivity structure that GHOSTDAG uses for ordering
2. Ensures honest blocks are well-connected (small anticones)
3. Reveals adversarial blocks as poorly connected (large anticones — they don't reference recent tips because they were withheld)

### How Transactions Are Ordered

The [GHOSTDAG algorithm](ghostdag.md) produces a **total order** over all blocks:
1. Follow the selected parent chain (highest blue scores)
2. Interleave non-chain blocks at their merge points
3. Within each block, transactions maintain their included order
4. Conflicting transactions: first in the total order wins

### Conflict Resolution

When parallel blocks contain conflicting transactions (e.g., spending the same UTXO):
- GHOSTDAG's total ordering determines which transaction came "first"
- The first transaction is accepted; the conflicting one is rejected
- This is deterministic — all nodes agree on the ordering

## Comparison

| Property | Blockchain (Bitcoin) | BlockDAG (Kaspa) |
|----------|---------------------|------------------|
| Block references | 1 parent | Multiple parents (all tips) |
| Parallel blocks | Orphaned (wasted) | Included (ordered) |
| Orphan rate | ~0.1% at 10-min blocks | 0% (by design) |
| Block time | 10 minutes | 100ms |
| Blocks per second | ~0.0017 | 10 |
| Throughput | ~7 TPS | ~60 TPS (roadmap: 30,000+) |
| Mining centralization pressure | Increases with block rate | Eliminated |

## Why Not Just Increase Bitcoin's Block Size or Rate?

**Increasing block size** at constant block rate increases throughput linearly but also increases propagation delay (larger blocks take longer to propagate), which increases orphan rate.

**Increasing block rate** at constant block size increases throughput but directly increases orphan rate.

Both approaches hit the same wall: on a single chain, throughput and orphan rate are coupled. The DAG decouples them by making orphans impossible.

## References

- Sompolinsky, Y., Wyborski, S., Zohar, A. "PHANTOM and GHOSTDAG." [ePrint 2018/104](https://eprint.iacr.org/2018/104)
- Kaspa features: [kaspa.org/features](https://kaspa.org/features/)
