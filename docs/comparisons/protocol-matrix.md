# Full Protocol Comparison Matrix

A comprehensive, honest comparison of Kaspa against every major L1 protocol. Not marketing -- a reference document that acknowledges tradeoffs on all sides, including Kaspa's. Every claim is sourced or derivable from protocol mechanics.

For detailed pairwise comparisons, see: [Kaspa vs Bitcoin](./kaspa-vs-bitcoin.md) | [Kaspa vs Ethereum](./kaspa-vs-ethereum.md) | [Kaspa vs Solana](./kaspa-vs-solana.md)

---

## Consensus and Finality

| Protocol | Type | Finality | Cost to Attack | Trust Assumptions |
|----------|------|----------|---------------|-------------------|
| Bitcoin | PoW chain | ~60 min (probabilistic) | 51% hashrate (~$1B+/hr) | None |
| **Kaspa** | **PoW DAG** | **~10 sec (probabilistic)** | **51% hashrate** | **None** |
| Ethereum | PoS BFT (Gasper) | ~13 min (economic) | 1/3 staked ETH (~$40B+) | Weak subjectivity |
| Solana | PoS BFT (Tower BFT) | ~400ms-12s | 1/3 staked SOL | Leader schedule, PoH |
| Avalanche | PoS sampling (Snow) | <1 sec (probabilistic) | 1/3 staked AVAX | Sub-sampling model |
| Cardano | PoS VRF (Ouroboros) | ~20 min (probabilistic) | 51% stake | Standard PoS |
| Algorand | PPoS VRF (BA*) | Instant (single-block) | 1/3 stake | Relay nodes (transitioning) |
| NEAR | PoS sharded (Nightshade) | ~2 sec | Shard-level attack | Shard assignment |
| Aptos | PoS BFT (AptosBFT) | ~1 sec | 1/3 of 152 validators | Permissioned-in-practice |
| Sui | PoS BFT (Mysticeti) | <400ms | 1/3 of ~100 validators | Object ownership model |

Kaspa and Bitcoin are the only protocols with zero trust assumptions beyond the protocol itself. All PoS chains introduce some form of additional trust -- whether weak subjectivity checkpoints, leader schedules, or validator set assumptions.

---

## Throughput and Fees

| Protocol | Actual TPS | Max Recorded | Block Time | Avg Fee |
|----------|-----------|-------------|------------|---------|
| Bitcoin | ~7 | ~7 | 10 min | ~$0.62 |
| **Kaspa** | **~60** | **5,584** | **100ms** | **<$0.001** |
| Ethereum L1 | 15-30 | ~63 | 12s | ~$0.10 |
| Solana | 1,000-4,000 | 55,000+ | 400ms | ~$0.0005 |
| Avalanche | ~30 | ~123 | ~2s | Very low |
| Cardano | ~0.41 | ~12 | 20s | ~$0.12 |
| Algorand | ~7 | 5,716 | <3s | ~$0.0001 |
| NEAR | 63-80 | 4,135 | ~1s | <$0.0001 |
| Aptos | 22,000+ | 22,000+ | <50ms | Very low |
| Sui | ~33 | ~927 | 67ms | ~$0.03 |

Kaspa's current ~60 TPS is modest compared to Solana and Aptos. The roadmap targets 30,000+ TPS, but significant engineering separates the current state from that target. Stress tests reaching 5,584 TPS demonstrate headroom, not sustained capacity.

---

## Decentralization

| Protocol | Validators/Miners | Superminority (33%) | Hardware Barrier | Launch |
|----------|-------------------|---------------------|------------------|--------|
| Bitcoin | Millions of machines | Large pool concentration | ASIC | Fair, no premine |
| **Kaspa** | **Multiple ASIC mfrs** | **Not reported** | **ASIC** | **Fair, no premine** |
| Ethereum | 1,060,000+ | Lido + top pools | Consumer HW | ICO, premine |
| Solana | 906-2,560 | ~20 validators | Extreme (256 GB+ RAM) | VC-funded |
| Avalanche | ~855 (declining) | Not reported | Moderate | ICO |
| Cardano | 3,200+ pools | None >1.4% | Consumer HW | ICO |
| Algorand | ~1,739 | Not reported | Very low | Dutch auction |
| NEAR | ~254 | Not reported | Moderate | Token sale |
| Aptos | 152 | Not reported | High; 1M APT min | VC-funded |
| Sui | ~100+ | Not reported | High | VC-funded |

Only Bitcoin and Kaspa combine fair launch (no premine, no ICO, no insider allocation) with permissionless mining. Cardano has the most evenly distributed stake among PoS chains. Solana, Aptos, and Sui have the most concentrated validator sets.

---

## Partition Behavior

| Protocol | During Partition | After Reconnection | Work/Stake Lost |
|----------|-----------------|-------------------|-----------------|
| Bitcoin | Both sides mine | Shorter fork orphaned | 100% of losing fork |
| **Kaspa** | **Both sides produce blocks** | **All blocks merge** | **Zero** |
| Ethereum | Finality halts; inactivity leak | Slow recovery; validators lose stake | Offline validators penalized |
| Solana | **Complete halt** | Manual restart (6-17 hrs) | All txs during downtime |
| Avalanche | Degrades/halts | Reconnection needed | Varies |
| Cardano | Shorter chain orphaned | Automatic (longer chain wins) | Losing fork |
| Algorand | Halts without 2/3 | Automatic on reconnection | Downtime period |
| NEAR | Shard-dependent | Varies | Varies |
| Aptos | Halts without 2/3 | Validator coordination | Downtime period |
| Sui | Halts without 2/3 | Validator coordination | Downtime period |

Kaspa is the only protocol that loses zero work during a partition. Bitcoin continues operating but discards the losing fork. All PoS chains either halt entirely or degrade, with some (Ethereum) financially punishing honest validators who happen to be on the disconnected side. See [partition tolerance](../architecture/partition-tolerance.md).

---

## Kaspa's Honest Tradeoffs

### Acknowledged Weaknesses

1. **Younger ecosystem:** ~2 years vs Bitcoin's 15+. Less battle-tested, smaller developer community, fewer tools.
2. **Smart contracts maturing:** L1 covenants ([KIP-17](../smart-contracts/kip-17.md)) in development. L2s (Igra EVM, Kasplex zkEVM) just launching. No mature DeFi ecosystem.
3. **ASIC-concentrated mining:** Multiple manufacturers exist (Bitmain, IceRiver, Goldshell, WindMiner), but the hardware base is narrower than Bitcoin's.
4. **Smaller market presence:** Limited exchange listings, minimal institutional infrastructure compared to BTC/ETH/SOL.
5. **[DAG-KNIGHT](../consensus/dag-knight.md) not yet deployed:** Mainnet runs [GHOSTDAG](../consensus/ghostdag.md) with a static k parameter. Adaptive consensus is theoretical until deployed.
6. **Throughput gap:** Current ~60 TPS is far from the 30,000+ TPS roadmap target. The engineering path is significant.

### Genuine Advantages (Sourced)

1. **Only high-throughput PoW chain:** No other protocol combines PoW + UTXO + fair launch + no premine at 10 BPS. Verified against all protocols in this matrix.
2. **Fee sustainability through throughput:** The only PoW chain with sufficient throughput to potentially sustain fee-based security long-term. See Lyn Alden's [security modeling framework](https://www.lynalden.com/bitcoin-security-modeling/).
3. **Partition tolerance with zero waste:** DAG merge means no wasted work, no punished miners, no downtime. Unique among all compared protocols. Derived from [GHOSTDAG](https://eprint.iacr.org/2018/104) and [DAG-KNIGHT](https://eprint.iacr.org/2022/1494) design.
4. **No adaptive adversary surface:** Work-then-select means block producers are unknown until they produce. Fundamental PoW property.
5. **No liquid staking risk:** No staking means no Lido-style concentration, no derivative cascading risk.
6. **No weak subjectivity:** New nodes verify from genesis. No trusted checkpoints.
7. **Chromatic halving:** Smooth emission curve with no supply shocks. Source: [Kaspa tokenomics](https://kaspa.org/tokenomics-emission-and-mining/).
8. **Fair launch regulatory clarity:** No premine, no ICO, no insider allocation -- strongest case for commodity classification.

---

## References

- Bitcoin: [BitInfoCharts](https://www.bitinfocharts.com/bitcoin/) | [CoinWarz](https://www.coinwarz.com/mining/bitcoin/hashrate-chart)
- Kaspa: [Kaspalytics](https://www.kaspalytics.com/) | [kaspa.org](https://kaspa.org/) | [ePrint 2018/104](https://eprint.iacr.org/2018/104) | [ePrint 2022/1494](https://eprint.iacr.org/2022/1494)
- Ethereum: [ethereum.org](https://ethereum.org/) | [beaconcha.in](https://beaconcha.in/)
- Solana: [docs.solanalabs.com](https://docs.solanalabs.com/) | [Helius](https://www.helius.dev/)
- Avalanche: [build.avax.network](https://build.avax.network/)
- Cardano: [cardano.org](https://cardano.org/)
- Algorand: [algorand.co](https://algorand.co/)
- NEAR: [pages.near.org](https://pages.near.org/)
- Aptos/Sui: [VanEck analysis](https://www.vaneck.com/us/en/blogs/digital-assets/sui-vs-aptos-competitive-analysis-and-price-prediction/)
