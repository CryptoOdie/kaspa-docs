# Kaspa vs Solana

Kaspa and Solana occupy opposite ends of the L1 design spectrum. Kaspa extends Bitcoin's PoW security model into a high-throughput [blockDAG](../consensus/ghostdag.md). Solana maximizes raw throughput through a PoS architecture with Proof of History, accepting centralization and availability tradeoffs in exchange for speed.

---

## Partition Tolerance: The Core Difference

The most fundamental difference between these protocols is what happens when the network splits.

| Scenario | Kaspa | Solana |
|----------|-------|--------|
| During partition | Both sides continue producing blocks | **Network halts entirely** |
| Threshold | No threshold -- always available | Halts if >1/3 validators offline |
| After reconnection | All blocks merge into DAG, zero waste | Manual validator coordination required |
| Historical recovery time | N/A (never halts) | 6-17+ hours |

### Solana Halt History

Solana has experienced 8+ documented outages due to its consistency-over-availability design:

| Date | Duration | Cause |
|------|----------|-------|
| Sep 14, 2021 | ~17 hours | Bot flood overwhelmed consensus |
| Apr-May 2022 | Hours | NFT mint: 6M requests/sec |
| Feb 25, 2023 | Several hours | Oversized block overwhelmed propagation |
| Feb 2024 | ~5 hours | Bug required coordinated validator restart |

During each outage, **zero transactions were processed**. For a protocol targeting global payments, halting under stress is a critical failure mode.

Kaspa's DAG structure treats partitions as a natural case of high-latency parallel mining. No blocks wasted, no energy lost, no manual intervention needed. See [partition tolerance](../architecture/partition-tolerance.md) for the full analysis.

---

## Hardware Requirements

| Requirement | Kaspa (Node) | Solana (Validator) |
|-------------|-------------|-------------------|
| CPU | Consumer hardware | 24-32 cores |
| RAM | Standard | 256 GB - 1 TB |
| Storage | Modest (aggressive pruning) | NVMe SSDs |
| Network | Standard broadband | 1 Gbps+ dedicated |
| Estimated cost | ~$200-500 | ~$5,000-10,000+ |

Solana's extreme hardware requirements create a natural barrier to validator participation. Running a Solana validator is closer to operating a data center node than running software on a home computer.

Kaspa nodes prune aggressively (~52 hours of data retained), keeping storage requirements minimal. Mining requires ASICs (kHeavyHash), but node operation remains accessible on consumer hardware.

---

## Validator Concentration

| Metric | Kaspa | Solana |
|--------|-------|--------|
| Consensus participants | Multiple ASIC manufacturers, open mining | 906-2,560 validators |
| Superminority (33% stake) | Not applicable (PoW) | **~20 validators** |
| Participation model | Permissionless (buy hardware, mine) | Capital-weighted (economics favor large stakes) |

Solana's superminority of approximately 20 validators controlling 33% of stake is a concrete centralization concern. These 20 entities could collectively halt the network by going offline. In Kaspa's PoW model, there is no equivalent chokepoint -- mining is permissionless and no fixed set of participants controls consensus.

---

## Launch and Distribution

| Property | Kaspa | Solana |
|----------|-------|--------|
| Launch model | Fair launch, mining only | VC-funded |
| Premine | None | Significant insider allocation |
| Team allocation | None | Yes |
| VC investment | None | Multiple rounds |
| Anyone could participate from block 1 | Yes | No |
| Regulatory posture | Strongest commodity case | Securities scrutiny |

---

## Consensus Architecture

### Work-Then-Select vs Known Leader Schedule

- **Kaspa:** Miners perform computational work, then discover whether they produced a valid block. Block producers are unknown until the block exists. An adversary cannot target the next block producer because no one knows who it will be.
- **Solana:** The leader schedule is **deterministic and known in advance**. An attacker can target the next leader with DDoS, bribery, or censorship before they produce their block. This is a fundamental adaptive adversary surface.

### Finality Model

| Metric | Kaspa | Solana |
|--------|-------|--------|
| Finality type | Probabilistic (cumulative PoW) | Optimistic ~400ms; rooted ~6-12s |
| Trust basis | Thermodynamic (energy spent) | Economic (2/3 stake supermajority) |
| Confirmation time | ~10 seconds | ~400ms optimistic |
| Weak subjectivity | None | Trust in leader schedule, PoH generator |

---

## Throughput Comparison

| Metric | Kaspa | Solana |
|--------|-------|--------|
| Block time | 100ms | 400ms |
| Actual TPS | ~3,000 | 1,000-4,000 |
| Max recorded | 5,584 | 55,000+ |
| Theoretical target | 30,000+ (roadmap) | 65,000 |
| Avg fee | <$0.001 | ~$0.0005 |

Kaspa's throughput is now competitive with Solana's normal operation range. At ~3,000 TPS, Kaspa matches or exceeds Solana's typical 1,000-4,000 TPS range, with the roadmap targeting 30,000+ TPS at 100 BPS.

---

## MEV Exposure

| Dimension | Kaspa | Solana |
|-----------|-------|--------|
| Model | UTXO (stateless) | Account (global state) |
| MEV infrastructure | None | Jito MEV dominant |
| Sandwich attacks | Not possible (no composable state) | Common |
| Known leader targeting | Not possible (work-then-select) | Possible (known schedule) |

---

## Honest Assessment: Solana's Advantages

| Dimension | Details |
|-----------|---------|
| Raw throughput | Highest real-world TPS of any major L1 |
| Payment integrations | PayPal, Visa, Stripe, Shopify partnerships |
| DeFi ecosystem | $7.8-9.3B TVL, mature DEXs and lending |
| Consumer adoption | Strong NFT and consumer app ecosystem |
| Fees | Among the lowest in crypto (~$0.0005) |
| Developer momentum | Large and growing Rust/Anchor developer base |

These advantages are significant. Solana has real-world payment adoption that Kaspa does not yet have. Its DeFi ecosystem is mature while Kaspa's smart contract layer (KIP-17, Igra, Kasplex) is still in development.

---

## Summary: Different Design Philosophies

| Property | Kaspa | Solana |
|----------|-------|--------|
| Design priority | Security + availability | Throughput + speed |
| Security model | Thermodynamic (PoW) | Economic (PoS) |
| Partition behavior | Continue + merge | Halt |
| Hardware barrier (nodes) | Low | Extreme |
| Validator concentration | Distributed mining | ~20 entity superminority |
| Leader predictability | Unknown (work-then-select) | Known in advance |
| Launch fairness | Fair, no premine | VC-funded, insider allocation |
| Current throughput | ~3,000 TPS | 1,000-4,000 TPS |
| Smart contracts | Maturing | Mature |
| Payment adoption | Early | Established |

Kaspa prioritizes the properties that make a protocol trustworthy under adversarial conditions: partition tolerance, permissionless participation, and thermodynamic security. Solana prioritizes the properties that make a protocol fast and usable today: raw throughput, low latency, and ecosystem integrations. These are genuinely different engineering philosophies, not a case where one is strictly superior.

---

## References

- Sompolinsky, Y. et al. "PHANTOM and GHOSTDAG." [ePrint 2018/104](https://eprint.iacr.org/2018/104)
- Sompolinsky, Y., Sutton, M. "The DAG KNIGHT Protocol." [ePrint 2022/1494](https://eprint.iacr.org/2022/1494)
- Solana consensus: [helius.dev](https://www.helius.dev/blog/consensus-on-solana)
- Solana outage data: [CoinLaw](https://coinlaw.io/solana-statistics/)
- Solana docs: [docs.solanalabs.com](https://docs.solanalabs.com/)
