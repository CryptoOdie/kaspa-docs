# Fast Proof-of-Work: Decoupling Speed from Decentralization

## The Assumed Tradeoff

The conventional wisdom in blockchain design is that speed requires centralization:

- Fast block times → high orphan rates → large miners win disproportionately → centralization
- Fast finality → small committee coordination → fewer participants → centralization
- High throughput → expensive hardware → fewer node operators → centralization

Proof-of-Stake protocols accept this tradeoff explicitly: they achieve speed by coordinating a fixed validator set rather than waiting for open competition. **Kaspa rejects this tradeoff.** The DAG structure eliminates the mechanism by which speed causes centralization in PoW, enabling high throughput without sacrificing the open, permissionless mining model.

---

## Why Traditional PoW Has a Speed Limit

### The Orphan Rate Problem

In a single-chain PoW system (Bitcoin), if two miners find blocks at nearly the same time, only one survives — the other becomes an orphan. The orphan rate is a function of:

```
orphan_rate ≈ 1 - e^(-block_rate × propagation_delay)
```

As block rate increases (faster blocks) or propagation delay increases (larger blocks, slower network), orphan rates rise.

### How Orphans Cause Centralization

Orphan blocks are wasted work. But they're not wasted equally:

- **Large mining pools** discover blocks more frequently, so they learn about their own blocks immediately (zero propagation delay to themselves). They start mining on their own blocks before the rest of the network even knows the block exists.
- **Small miners** must wait for blocks to propagate before they can mine on them. During propagation delay, small miners are more likely to mine orphans.

This creates a structural advantage for large pools that increases with block rate. At Bitcoin's 10-minute block time, the orphan rate is negligible (~0.1%). At 1-second block times on a single chain, orphan rates would be catastrophic — 30%+ — and mining would centralize rapidly.

This is why Bitcoin's 10-minute block time is not just conservative; it's a **security constraint** dictated by the single-chain architecture.

---

## How the DAG Eliminates Orphans

### The BlockDAG Insight

PHANTOM/GHOSTDAG's foundational insight: **parallel blocks are not a problem to be eliminated — they are information to be incorporated.**

In a blockDAG:
- Every block references **all known tips** (unreferenced blocks) as parents
- Parallel blocks — which would be orphans in a single chain — are all included in the DAG
- The GHOSTDAG algorithm orders all blocks, including parallel ones, into a consistent total order

**There are no orphans in a DAG.** Every honestly-mined block contributes to the ledger and earns its miner a reward. The orphan-rate centralization pressure that limits single-chain PoW simply **does not exist** in a DAG.

### What k Represents

The parameter k in GHOSTDAG represents the expected number of parallel blocks during one propagation delay:

```
k ≈ 2 × D × λ
```

Where D is network propagation delay and λ is the block creation rate. Honest blocks created during propagation delay have anticones of size ≤ k (they reference each other as parents). Adversarial blocks (withheld and released later) tend to have anticones > k.

This separation — honest parallel blocks are well-connected, adversarial blocks are not — is what allows GHOSTDAG to distinguish between them and maintain security at high block rates.

---

## The PoS Speed-Centralization Tension

PoS systems face a different version of the speed-centralization tradeoff:

### Fast Finality Requires Fast Supermajority Coordination

To finalize a block in PoS, a supermajority (typically 2/3) of the validator set must coordinate:

1. A block is proposed
2. Validators attest/vote on it
3. Enough attestations must be collected and verified
4. The block is marked as finalized

The time this takes is bounded by:
- Communication rounds between validators
- Total number of validators that must participate
- Network latency between validators

**To make this faster, you must either:**
- Reduce the number of validators (fewer messages, faster coordination)
- Restrict validators to low-latency infrastructure (faster message delivery)
- Use committee sampling (fewer participants per round)

All three push toward centralization.

### Examples

| Protocol | Finality Time | Validator Set Size | Tradeoff |
|----------|--------------|-------------------|----------|
| Ethereum | ~13 minutes | ~962,941 active (2.2M registered) | Slow finality, high decentralization |
| Solana | ~400ms optimistic, 6-12s rooted | ~795 (down 68% from 2,560) | Fast finality, extreme hardware (256 GB–1 TB RAM, 24-32 cores) |
| Aptos | ~1 second | ~153 | Very fast, effectively permissioned (1M APT min) |
| Sui | ~390ms consensus | ~122 | Very fast, very small (30M SUI min) |
| Algorand | <3 seconds | ~1,600+ | Fast, committee-sampled (not all validators participate per round) |

The pattern is clear: faster PoS finality correlates with smaller or more restricted validator sets. Ethereum is the slowest PoS finalizer *because* it has the most validators.

### PoW Confirmation Is Different

PoW confirmation security scales with **cumulative work**, independent of miner count:

- A transaction with 6 Bitcoin confirmations (~1 hour) has the same security whether there are 100 miners or 100,000 miners (assuming the same total hashrate)
- Adding more miners doesn't slow confirmation — it increases decentralization without affecting speed
- The security guarantee is: "reversing this transaction requires re-doing X amount of computational work"

In a DAG, this property is preserved while dramatically reducing the time needed to accumulate sufficient work:
- 10 BPS × 10 seconds = 100 blocks of cumulative work
- Bitcoin: 1 block per 10 minutes × 60 minutes = 6 blocks of cumulative work
- Equal security, 1/6 the wait time (with sufficient per-block work)

---

## Work-Then-Select vs. Select-Then-Work

This is perhaps the most underappreciated distinction between PoW and PoS.

### PoW: Work-Then-Select

1. Miner performs computational work (hashing)
2. If the hash meets the difficulty target, the miner has "won"
3. The miner broadcasts the block
4. The network learns who produced the block only when it arrives

**Properties:**
- Block producer is unknown until the block exists
- An adversary cannot target the next producer (they don't know who it is)
- Bribery is impossible before the fact (you can't bribe an unknown miner)
- DDoS is impossible against the producer (they're anonymous until they produce)

### PoS: Select-Then-Work

1. Protocol selects the next block producer (via stake-weighted random selection)
2. The selected validator assembles and signs the block
3. The validator broadcasts the block

**Properties:**
- Block producer is known before the block exists (sometimes far in advance)
- **Solana:** Leader schedule is deterministic and known in advance
- **Ethereum:** Proposer known one epoch (~6.4 minutes) in advance
- An adversary can target the known producer with DDoS, bribery, or coercion

### Adaptive Adversary Resistance

An **adaptive adversary** is one who can change their target based on protocol state — e.g., corrupt or DDoS the next known block producer.

PoW is inherently resistant to adaptive adversaries because the producer is unknown until they produce. The adversary cannot adapt to something they cannot predict.

PoS protocols attempt various mitigations:
- **Algorand:** VRF-based selection keeps proposers secret until reveal (best PoS defense)
- **Ethereum:** Single secret leader election (SSLE) is an active research area
- **Solana:** No mitigation — leader schedule is public and exploitable

But even Algorand's approach has a window: once the proposer reveals themselves (necessary to prove they were selected), they can be targeted for the remainder of the round.

PoW has no such window. The "reveal" and the "block production" are the same event.

---

## Kaspa's Unique Position: Fast PoW Without Centralization

Kaspa achieves what was previously thought impossible: PoW block production at 10 blocks per second (100ms block times) without the centralization that would destroy a single-chain PoW system.

### Why It Works

1. **No orphans:** DAG includes all parallel blocks → no wasted work → no advantage for large miners
2. **Decoupled from propagation delay:** Parallel blocks are expected and incorporated, not penalized
3. **Cumulative work still provides security:** 10 BPS means 100 blocks per 10 seconds of cumulative PoW
4. **Mining decentralization preserved:** High block rate with reduced variance actually reduces pool centralization pressure (more frequent, smaller rewards instead of rare, large rewards)
5. **Work-then-select preserved:** Block producers are unknown until they produce, maintaining adaptive adversary resistance

### Comparison

| Property | Bitcoin | Kaspa | Ethereum | Solana |
|----------|---------|-------|----------|--------|
| Block time | 10 min | 100ms | 12s | 400ms |
| Orphan/wasted blocks | Yes (~0.1%) | No (DAG) | No (selected proposer) | No (selected leader) |
| Producer known in advance | No | No | 1 epoch ahead | Full schedule public |
| Adaptive adversary resistance | Strong | Strong | Moderate | Weak |
| Confirmation mechanism | Cumulative PoW | Cumulative PoW in DAG | 2/3 stake attestation | 2/3 stake votes |
| Speed-decentralization tradeoff | Severe (orphan rate) | Eliminated (DAG) | Present (validator set size) | Severe (hardware requirements) |
| Miner/validator count | Thousands of pools, millions of machines | Multiple ASIC manufacturers, pools | ~962,941 active validators | ~795 validators |

---

## The Throughput Story

Kaspa's speed is not an end in itself. It serves two purposes:

1. **User experience:** 100ms block times mean transactions are visible in ~1 second and confirmed in ~10 seconds — comparable to PoS chains, without PoS trust assumptions

2. **Security budget sustainability:** High throughput = more transactions per second = more total fee revenue at lower per-transaction cost = sustainable fee-based security (see [security-budget.md](./security-budget.md))

Both purposes are achieved **without** the centralization tradeoffs that PoS systems make for speed, and **without** the throughput limitation that single-chain PoW imposes.

---

## References

- Sompolinsky, Y., Wyborski, S., Zohar, A. "PHANTOM and GHOSTDAG: A Scalable Generalization of Nakamoto Consensus." AFT 2021. [ePrint 2018/104](https://eprint.iacr.org/2018/104)
- Sompolinsky, Y., Sutton, M. "The DAG KNIGHT Protocol." [ePrint 2022/1494](https://eprint.iacr.org/2022/1494)
- Kaspa Crescendo hard fork: [kaspa.org](https://kaspa.org/kaspa-updates-to-crescendo-and-10bps/)
- Solana consensus: [docs.solanalabs.com](https://docs.solanalabs.com/implemented-proposals/tower-bft)
- Ethereum proposer selection: [ethereum.org](https://ethereum.org/developers/docs/consensus-mechanisms/pos/)
- Algorand VRF: [algorand.co](https://algorand.co/technology/pure-proof-of-stake)
