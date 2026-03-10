# What Proof-of-Stake Actually Trades Away

## Purpose

This document enumerates the specific engineering tradeoffs inherent in Proof-of-Stake consensus. It is not an attack on PoS — it is a factual inventory of what PoS systems give up in exchange for what they gain. Every engineering decision involves tradeoffs; understanding them is a prerequisite for informed protocol selection.

**What PoS gains:** Lower energy consumption, potentially faster finality, validator participation without specialized hardware.

**What PoS trades away:** The properties enumerated below.

---

## 1. Thermodynamic Security → Economic Security

### PoW: Energy as Irreversible Commitment

In Proof-of-Work, attacking a network requires expending energy — a thermodynamically irreversible process. Once a miner spends electricity to produce a block, that energy is gone regardless of whether the attack succeeds. This creates a **proactive** cost: the attacker pays before and during the attack, not after.

- Bitcoin's network hashrate: ~1,045 ZH/s (March 2026)
- Mining difficulty: 145.04T
- Attack cost: The electricity and hardware required to sustain 51% of this hashpower for any duration

The cost is real, physical, and cannot be circumvented through financial engineering.

### PoS: Capital as Reversible Commitment

In Proof-of-Stake, security derives from capital locked as collateral. The cost of attacking is the risk of losing that capital through slashing. This creates several differences:

- **Capital is recoverable:** Unlike spent energy, staked capital can be withdrawn after the unbonding period. An attacker who succeeds may recover their stake.
- **Slashing is reactive:** Punishment occurs after detection and attribution, not during the attack itself. This assumes the network can correctly identify and attribute malicious behavior.
- **Liquid staking makes capital simultaneously "at risk" and liquid:** stETH, rETH, and similar tokens allow stakers to use their capital in DeFi while it's nominally locked. The "skin in the game" assumption is weakened.

### The Fundamental Difference

PoW security is thermodynamic: governed by physics, not protocol rules. Energy expenditure is enforced by the laws of thermodynamics, not by code that can be exploited, gamed, or socially overridden.

PoS security is economic: governed by protocol rules, slashing conditions, and social consensus about how to handle edge cases. This is a different — and more complex — trust model.

---

## 2. Permissionless Participation → Plutocratic Participation

### The Stake Barrier

PoS systems inherently weight influence by capital:

| Protocol | Minimum Stake | USD Equivalent (approx.) |
|----------|--------------|-------------------------|
| Ethereum | 32 ETH | ~$100,000+ |
| Solana | No minimum (but economics favor large stakes) | — |
| Avalanche | 2,000 AVAX | ~$25,000+ |
| Aptos | 1,000,000 APT | ~$8,000,000+ |
| Sui | 30,000,000 SUI | ~$30,000,000+ |
| Cardano | ~500 ADA (pool deposit) | ~$200 |

In PoW, anyone with a CPU (historically) or an ASIC can participate in mining. The barrier is hardware cost, which is a one-time purchase with a secondary market. In PoS, the barrier is holding sufficient tokens — which requires either buying them (capital outlay) or having received them (often through insider allocation).

### Validator Set Concentration

| Protocol | Validator Count | Superminority (33% of stake) |
|----------|----------------|------------------------------|
| Ethereum | 2,210,484 registered; ~962,941 active | Top-10 entities >60% of stake |
| Solana | ~795 (down 68% from 2,560 in 2023) | ~20 validators |
| Avalanche | ~656 (down 55% YoY) | Not publicly reported |
| NEAR | ~254–411 | Not publicly reported |
| Aptos | ~153 | Not publicly reported |
| Sui | ~122 | Not publicly reported |
| Cardano | ~2,917 pools | None >1.4% of stake |

Solana's validator count has **collapsed 68%** since March 2023, accelerated by the Solana Foundation's April 2025 pruning of underperforming validators. Superminority of ~20 validators controlling 33% of stake. Aptos requires 1M APT (~$8M+) minimum stake, creating a validator set that is effectively permissioned. Avalanche dropped from 1,436 validators (Q2 2025) to just 656 (Q4 2025) — a 55% year-over-year decline.

---

## 3. Full-Network Confirmation → Committee Sampling

### PoW: Every Miner Confirms Every Block

In PoW, security scales with total network hashpower. Every miner independently validates and builds on the chain. There is no committee, no delegation, no sampling — the full network's energy expenditure secures every block.

### PoS: Committee-Based Confirmation

Most PoS systems use committee sampling for efficiency:

- **Ethereum:** Each epoch (6.4 minutes), the validator set is shuffled into committees. Each slot's committee attests to a single block. Not all validators attest to every block.
- **Algorand:** VRF-based sortition selects a small random committee for each round. Committee members are unknown until they reveal their proof.
- **Solana:** A single leader is designated per slot via a deterministic schedule (known in advance — an attack surface).
- **NEAR:** Chunk producers validate individual shards, not the full chain.

Committee sampling introduces a tradeoff: reduced communication overhead at the cost of security depending on a subset rather than the full network. If the committee sampling is predictable or manipulable, the security guarantee degrades.

---

## 4. Objective Consensus → Weak Subjectivity

### The Problem

In PoW, any node can determine the canonical chain by independently verifying proof-of-work from genesis. No external information is needed beyond the protocol rules and the block data itself.

In PoS, this is not possible. A node syncing from genesis cannot distinguish between:
- The real chain (with legitimate validator signatures)
- A fake chain created by validators who have since unstaked (a **long-range attack**)

Both chains have valid signatures. The signatures were created by validators who legitimately held stake at the time — they just don't anymore.

### The Solution: Weak Subjectivity

PoS chains require nodes to start from a recent **weak subjectivity checkpoint** — a finalized block obtained from a trusted source. This creates a dependency:

- **Ethereum:** New nodes must obtain a checkpoint from a trusted provider. The weak subjectivity period defines how recent it must be, based on validator set size and churn.
- Any node offline longer than the weak subjectivity period must re-obtain a checkpoint from a trusted source before syncing.

**What this means:** PoS reintroduces a trusted third party at the consensus layer. You must trust someone to give you the right checkpoint. This is a meaningful departure from the trustless model that cryptocurrency was designed to provide.

### PoW Does Not Have This Problem

In PoW, the canonical chain is the one with the most cumulative work. This is objectively verifiable by any node, at any time, from genesis, without trusting anyone. The physics of energy expenditure cannot be faked retroactively.

---

## 5. Adaptive Adversary Resistance: "Work-Then-Select" vs. "Select-Then-Work"

### PoW: Work-Then-Select

In PoW, a miner does computational work first, then discovers whether they "won" the right to produce a block. The selection is a consequence of the work, not a precondition. An adversary cannot target the block producer because the producer is unknown until the block is produced.

### PoS: Select-Then-Work

In PoS, validators are selected (often predictably) to produce blocks, then they do the work of assembling and signing the block. This creates an adaptive adversary surface:

- **Solana:** Leader schedule is deterministic and known in advance. An attacker can target the next leader with DDoS or bribery.
- **Ethereum:** Proposer selection is known one epoch in advance (~6.4 minutes). While less predictable than Solana, it still provides an attack window.
- **Algorand:** VRF-based selection keeps proposers secret until they reveal — the strongest PoS defense against adaptive adversaries. However, once revealed, the proposer can be targeted for the remainder of the round.

In PoW, there is no "next block producer" to target. The producer emerges from the work itself.

---

## 6. Partition Tolerance

### PoS Partition Behavior

When a network partitions (segments lose connectivity with each other):

| Protocol | Behavior | Recovery |
|----------|----------|----------|
| Ethereum | Finality halts if neither side has 2/3 stake. Inactivity leak drains offline validators. Chain continues producing unfinalized blocks. | Automatic but slow (inactivity leak takes weeks). Offline validators permanently lose stake. |
| Solana | **Network halts entirely** if >1/3 of validators are unreachable. No blocks produced. | Manual validator coordination required. Historical recovery: 6–17+ hours. |
| Avalanche | Degrades without 2/3 supermajority. May halt or produce conflicting decisions. | Requires reconnection of sufficient validators. |

### PoW Partition Behavior

| Protocol | Behavior | Recovery |
|----------|----------|----------|
| Bitcoin | Both sides continue mining independently. Shorter chain orphaned on reconnection (reorg). | Automatic. Orphaned blocks' transactions return to mempool. Energy on losing fork is wasted. |
| Kaspa | Both sides continue producing blocks independently. On reconnection, **all blocks merge into the DAG** — no blocks orphaned. | Automatic. Zero wasted work. Conflicting transactions resolved by GHOSTDAG ordering. |

Kaspa's DAG structure treats partitions as a natural case of high-latency parallel mining. No blocks are wasted, no energy is lost, no manual intervention is needed.

---

## 7. Liquid Staking as Systemic Risk

Liquid staking has become the dominant mode of PoS participation:

- **Lido:** ~8.7M ETH staked (**24.2% of all staked ETH**, down from 32.3% peak in late 2023). Node operator base expanded across three modules: Curated (professional operators), SimpleDVT (261 operators, ~9,500 validators), and Community Staking Module (312+ operators, 5,857 validators).
- **Top-10 staking entities** control over **60% of all staked Ethereum**
- Total liquid staking TVL exceeds **$66.86 billion**; LST market cap: **$86.4 billion**
- **Rocket Pool:** More decentralized (permissionless node operators) but smaller

### The Principal-Agent Problem

Research by Tzinas & Zindros (2024) formally demonstrates:

> "Proportional representation and fair punishment are fundamentally incompatible in an adversarial setting."

Stakers delegate to liquid staking protocols, which decide how to allocate stake among validators. The interests of delegators (maximize yield, minimize risk) and validators (maximize MEV, minimize costs) are not aligned. The protocol layer that mediates between them (Lido, Rocket Pool) becomes a point of leverage and potential failure.

### Cascading Risk

During market stress:
1. Staked ETH price drops
2. stETH may depeg from ETH (as happened in June 2022)
3. Holders rush to unstake through the protocol
4. Mass withdrawal queue creates delays
5. If withdrawal pressure is severe enough, the protocol's validator set shrinks
6. Network security degrades at the moment it's most needed

This cascading risk is structural to any system where staking participation is mediated by financial intermediaries that issue derivative tokens.

---

## 8. Validator Cartel Formation and MEV

### MEV Creates Economies of Scale

Maximal Extractable Value (MEV) — profit from transaction ordering, insertion, and sandwich attacks — creates structural advantages for large validators:

- Cumulative MEV on Ethereum: **$1.8 billion+**
- The MEV relay landscape has shifted dramatically: Flashbots dropped from **84% dominance to just 3.52%** of blocks. Ultrasound relay (33%), Titan (21%), and bloXroute (31.7%) now dominate.
- However, **block builder centralization has worsened**: just **2 operators build over 90% of Ethereum blocks**
- BuilderNet (Flashbots + Beaverbuild + Nethermind, launched November 2024) was created to address this but hasn't solved it
- Large validators form exclusive relationships with top block builders
- Smaller validators cannot compete for MEV revenue

This creates a centralizing force: validators with more stake can extract more MEV, use MEV profits to acquire more stake, and compound their advantage.

### Censorship Capability

A validator cartel controlling 33%+ of stake can:
- Prevent finality (liveness attack)
- At 51%+: control block production and censor transactions
- At 67%+: finalize arbitrary state transitions

MEV extraction infrastructure (Flashbots relay dominance) creates a natural coordination layer for such cartels.

### UTXO vs. Account Model MEV Exposure

Kaspa's UTXO model inherently limits MEV extraction:
- No global state means no state-dependent ordering games
- No smart contract composability means no sandwich attacks
- Transaction outcomes are deterministic and independent of ordering

---

## 9. The Energy Argument — A Brief Reframe

PoS's primary claimed advantage is energy efficiency. This is real — PoS uses orders of magnitude less energy than PoW. However, the framing deserves scrutiny:

**What PoW energy expenditure buys:**
- Thermodynamic irreversibility (spent energy cannot be recovered)
- Objective consensus (any node can verify from genesis)
- No trusted third parties (no weak subjectivity checkpoints)
- Adaptive adversary resistance (work-then-select)
- The only known mechanism where attack cost is physically enforced

**The question is not "does PoS use less energy?"** — it obviously does. The question is: **"Is the energy expenditure of PoW the price of properties that PoS cannot replicate?"**

If you believe trustless consensus, objective verifiability, and thermodynamic attack resistance are essential properties for sound money, then PoW energy expenditure is not waste — it's the cost of those properties.

If you believe economic security (capital at risk) is sufficient and the properties above are not critical, then PoS's energy savings are a net gain.

This is a values question, not a purely technical one.

---

## Summary: PoS Tradeoff Inventory

| Property | PoW | PoS |
|----------|-----|-----|
| Security basis | Thermodynamic (physics) | Economic (protocol rules) |
| Attack cost recovery | Irrecoverable (energy spent) | Partially recoverable (capital at risk) |
| Punishment model | Proactive (cost during attack) | Reactive (slashing after detection) |
| Consensus objectivity | Full (verifiable from genesis) | Weak subjectivity (trusted checkpoints) |
| Adaptive adversary resistance | Strong (work-then-select) | Variable (select-then-work) |
| Participation model | Permissionless (hardware) | Plutocratic (capital-weighted) |
| Liquid staking risk | N/A | Systemic (LSDs undermine lock-up) |
| MEV centralization | Minimal (no smart contract ordering) | Severe (structural advantage for large validators) |
| Partition behavior | Continue + reorg (PoW) or merge (DAG) | Halt or degrade |
| Energy cost | High | Low |

Every item in this table is a tradeoff, not a flaw. Reasonable engineers can disagree about which tradeoffs are acceptable. This document aims to ensure the tradeoffs are visible.

---

## References

- Tzinas, E. & Zindros, D. "The Principal-Agent Problem in Liquid Staking." [ePrint 2023/605](https://eprint.iacr.org/2023/605)
- Buterin, V. & Griffith, V. "Casper the Friendly Finality Gadget." [arXiv 1710.09437](https://arxiv.org/pdf/1710.09437)
- "Three Attacks on Proof-of-Stake Ethereum." [ePrint 2021/1413](https://eprint.iacr.org/2021/1413.pdf)
- Paradigm. "On Staking Pools and Staking Derivatives." [paradigm.xyz](https://www.paradigm.xyz/2021/04/on-staking-pools-and-staking-derivatives)
- Ethereum weak subjectivity: [ethereum.org](https://ethereum.org/developers/docs/consensus-mechanisms/pos/weak-subjectivity/)
- Ethereum inactivity leak: [eth2book.info](https://eth2book.info/latest/part2/incentives/inactivity/)
- Solana consensus: [helius.dev](https://www.helius.dev/blog/consensus-on-solana)
- Algorand PPoS: [algorand.co](https://algorand.co/technology/pure-proof-of-stake)
