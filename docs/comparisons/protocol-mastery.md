# Complete Protocol Comparison Matrix

## Purpose

An honest, comprehensive comparison of Kaspa against every major L1 protocol. Not marketing — a reference document that acknowledges tradeoffs on ALL sides, including Kaspa's. Every claim is sourced or derivable from protocol mechanics.

---

## Protocol Summaries

### Bitcoin (BTC)

| Dimension | Details |
|-----------|---------|
| **Consensus** | Nakamoto PoW (SHA-256), longest-chain rule |
| **Finality** | Probabilistic; ~60 min (6 confirmations standard) |
| **Block time** | ~10 minutes |
| **Throughput** | ~7 TPS |
| **Miners** | Thousands of pools, millions of machines; ~1,045 ZH/s hashrate |
| **Hardware requirements** | ASIC miners (SHA-256); nodes: consumer hardware |
| **Security model** | Thermodynamic; cost to attack = energy expenditure for 51% hashrate |
| **Fee market** | Variable; avg ~$0.30 (Mar 2026); spiked to $127.97 on 2024 halving day |
| **Fee revenue % of miner income** | ~1% baseline, brief spikes to 75% (never sustained >20%); long-term sustainability uncertain |
| **Partition behavior** | Both sides continue; shorter fork orphaned on reconnection |
| **Trust assumptions** | None beyond protocol |
| **MEV exposure** | Limited (no smart contract ordering) |
| **Smart contracts** | Limited (Script); Lightning Network for payments |
| **Launch** | Fair, no premine (Jan 2009) |
| **Key strengths** | Most battle-tested (15+ years), largest network effect, institutional adoption (ETFs), commodity classification |
| **Key weaknesses** | Low throughput, slow confirmation, fee market sustainability uncertain, partition wastes blocks |

### Kaspa (KAS)

| Dimension | Details |
|-----------|---------|
| **Consensus** | GHOSTDAG (blockDAG PoW); DAG-KNIGHT upcoming (parameterless) |
| **Finality** | Probabilistic; ~10 seconds with cumulative PoW |
| **Block time** | 100ms (10 BPS post-Crescendo) |
| **Throughput** | ~3,000 TPS normal; 5,500 TPS peak; roadmap 30,000+ TPS |
| **Miners** | Multiple ASIC manufacturers (Bitmain, IceRiver, Goldshell, WindMiner); ~311–411 PH/s |
| **Hardware requirements** | ASIC miners (kHeavyHash); nodes: consumer hardware |
| **Security model** | Thermodynamic; same as Bitcoin |
| **Fee market** | Sub-$0.001 per transaction; high throughput enables fee-based sustainability |
| **Fee revenue sustainability** | Designed for throughput-based fee revenue at low per-tx cost |
| **Partition behavior** | Both sides continue; all blocks merge on reconnection (zero waste) |
| **Trust assumptions** | None beyond protocol |
| **MEV exposure** | Minimal (UTXO model, no smart contract ordering) |
| **Smart contracts** | L1: vProgs/covenants (KIP-17, targeting May 5, 2026 hard fork); L2: Igra (EVM, live Jan 2026), Kasplex zkEVM (live Mar 2026) |
| **Launch** | Fair, no premine (Nov 2021) |
| **Key strengths** | Bitcoin's security model + high throughput, partition tolerance, chromatic halving, fair launch |
| **Key weaknesses** | Young ecosystem (2+ years), smart contracts still maturing, smaller developer community, ASIC-concentrated mining, DAG-KNIGHT not yet on mainnet, less battle-tested |

### Ethereum (ETH)

| Dimension | Details |
|-----------|---------|
| **Consensus** | Gasper (Casper FFG + LMD-GHOST); PoS since The Merge (Sep 2022) |
| **Finality** | Economic; ~13 minutes (2 epochs). Reverting requires burning ≥1/3 of staked ETH. |
| **Block time** | 12 seconds |
| **Throughput** | L1: 15–30 TPS (max ~63); L1+L2: 32,950+ TPS |
| **Validators** | 2,210,484 registered; ~962,941 active; staking ~37.2M ETH (~30.6% of supply) |
| **Hardware requirements** | 16 GB RAM, 2 TB SSD, stable internet |
| **Security model** | Economic; ~$112B staked collateral; cost to attack = 1/3 of staked ETH |
| **Fee market** | L1 avg ~$0.10; L2 fees $0.001–$0.01 post-EIP-4844 |
| **Fee revenue sustainability** | Dual revenue: staking rewards (inflation) + fees + MEV |
| **Partition behavior** | Finality halts without 2/3 stake; inactivity leak drains offline validators |
| **Trust assumptions** | Weak subjectivity (trusted checkpoint for new nodes) |
| **MEV exposure** | Severe; $1.8B+ cumulative; 2 block builders produce 90%+ of blocks |
| **Smart contracts** | Mature (Solidity/Vyper); largest DeFi ecosystem |
| **Launch** | ICO (2014); premine: ~72M ETH to early contributors/foundation |
| **Key strengths** | Largest smart contract ecosystem, most L2s, deep liquidity, institutional infrastructure |
| **Key weaknesses** | Weak subjectivity, MEV builder centralization (2 builders control 90%+ blocks), liquid staking concentration (top-10 entities >60%), slow L1 finality, validator geographic concentration |

### Solana (SOL)

| Dimension | Details |
|-----------|---------|
| **Consensus** | Tower BFT (PBFT variant) + Proof of History (SHA-256 hash chain clock) |
| **Finality** | Optimistic ~400ms; rooted ~6–12 seconds |
| **Block time** | 400ms |
| **Throughput** | 1,000–4,000 TPS normal; 55,000+ TPS peak; theoretical 65,000 TPS |
| **Validators** | ~795 (down 68% from 2,560 in Mar 2023); superminority ~20 validators |
| **Hardware requirements** | Extreme: 24–32 cores, 256 GB–1 TB RAM DDR5 ECC, enterprise NVMe SSDs, 1–10 Gbps network |
| **Security model** | Economic; 2/3 stake supermajority required |
| **Fee market** | ~$0.0005 per tx; priority fees under $0.01 during congestion |
| **Partition behavior** | **Halts entirely** if >1/3 validators offline |
| **Trust assumptions** | Trust in leader schedule, Proof of History generator |
| **MEV exposure** | Significant; Jito MEV infrastructure dominant |
| **Smart contracts** | Rust/Anchor; growing DeFi ecosystem ($7.8–9.3B TVL) |
| **Launch** | VC-funded; significant insider allocation |
| **Key strengths** | Highest real-world throughput, lowest fees, strong DeFi/consumer ecosystem, payment integrations (PayPal, Visa, Stripe) |
| **Key weaknesses** | Halts on partition (8+ outages, 9 unreported disruptions Oct 2024–Feb 2025), extreme hardware requirements, 68% validator decline, concentrated validator set (~20 superminority), VC/insider distribution |

### Avalanche (AVAX)

| Dimension | Details |
|-----------|---------|
| **Consensus** | Snow protocol family (Snowball/Snowflake); repeated random sub-sampling |
| **Finality** | Probabilistic, sub-second (~0.8s); reversal probability drops exponentially |
| **Block time** | ~2 seconds |
| **Throughput** | ~30 TPS actual; max ~123 TPS; theoretical ~1,191 TPS C-Chain |
| **Validators** | ~656 (Q4 2025; down 55% YoY from 1,436) |
| **Hardware requirements** | Moderate; 2,000 AVAX minimum stake |
| **Security model** | Economic; probabilistic finality via repeated sub-sampling |
| **Fee market** | Very low post-Avalanche9000 (1 nAVAX base fee) |
| **Partition behavior** | Degrades without supermajority; may halt or produce conflicts |
| **Trust assumptions** | Trust in sub-sampling security model (less formally studied) |
| **Smart contracts** | EVM-compatible (C-Chain); custom subnet VMs |
| **Launch** | ICO (2020); team/insider allocation |
| **Key strengths** | Sub-second finality, subnet architecture for custom chains, low fees |
| **Key weaknesses** | Rapidly declining validator count (656, down 55% YoY), actual throughput much lower than theoretical, formal security proofs debated |

### Cardano (ADA)

| Dimension | Details |
|-----------|---------|
| **Consensus** | Ouroboros (Praos/Chronos); stake-weighted VRF slot leader selection |
| **Finality** | Probabilistic (Nakamoto-style); practical ~20 minutes |
| **Block time** | 20 seconds |
| **Throughput** | ~0.41 TPS actual avg; max ~12 TPS; theoretical ~18 TPS L1; Ouroboros Leios targets 1,000+ |
| **Validators** | ~2,917 active stake pools; no single pool >1.4% of stake |
| **Hardware requirements** | Modest (consumer hardware, ~24 GB RAM) |
| **Security model** | Economic; well-distributed stake; peer-reviewed academic provenance |
| **Fee market** | ~$0.12 avg; protocol-determined, not auction-based |
| **Partition behavior** | Nakamoto-style; longer chain wins, shorter fork orphaned |
| **Trust assumptions** | Bootstrap from trusted peer; standard PoS weak subjectivity concerns |
| **Smart contracts** | Plutus/Aiken (eUTXO model); deterministic execution |
| **Launch** | ICO (2017); team allocation |
| **Key strengths** | Peer-reviewed research, highly decentralized stake pool distribution, eUTXO determinism, fully decentralized governance |
| **Key weaknesses** | Very low actual throughput, slow finality, eUTXO contention limits dApp UX, smaller DeFi ecosystem |

### Algorand (ALGO)

| Dimension | Details |
|-----------|---------|
| **Consensus** | Pure PoS (PPoS); VRF-based cryptographic sortition + BA* |
| **Finality** | **Instant (single-block)**; no forks by design |
| **Block time** | <3 seconds |
| **Throughput** | ~7 TPS actual avg; max 5,716 TPS; theoretical ~10,000 TPS |
| **Validators** | ~1,600+ participation nodes; ~120 relay nodes; no token lockup required |
| **Hardware requirements** | Very low (any standard computer) |
| **Security model** | Economic; VRF ensures committee members unknown until reveal |
| **Fee market** | 0.001 ALGO per tx (~$0.0001); among lowest in crypto |
| **Partition behavior** | Requires 2/3 online; halts without it |
| **Trust assumptions** | Historically relied on permissioned relay nodes (P2P transition underway) |
| **Smart contracts** | AVM (Algorand Virtual Machine); TEAL/PyTeal |
| **Launch** | Dutch auction (2019); Foundation allocation |
| **Key strengths** | Instant finality (genuine, no reorgs), very low fees, VRF-protected proposer selection, low hardware barrier |
| **Key weaknesses** | Relay node centralization (being addressed), Foundation governance influence, low actual throughput vs theoretical |

### NEAR Protocol (NEAR)

| Dimension | Details |
|-----------|---------|
| **Consensus** | Nightshade sharding + Doomslug block production + BFT finality gadget |
| **Finality** | Doomslug: ~1 second; BFT: ~2 seconds |
| **Block time** | ~1 second |
| **Throughput** | 63–80 TPS actual; testnet peak 4,135 TPS; Nightshade 3.0 targets 1M+ TPS |
| **Validators** | ~254–411 (100 block-producing, rest via staking pools); 44.9% of NEAR staked |
| **Hardware requirements** | Moderate; reduced by stateless validation (Nightshade 2.0) |
| **Security model** | Economic; shard-level security depends on honest validator assignment |
| **Fee market** | <$0.0001 per tx; 70% of fees burned |
| **Partition behavior** | Depends on shard-level validator distribution |
| **Trust assumptions** | Random shard assignment; fishermen/fraud proofs for cross-shard security |
| **Smart contracts** | Rust/AssemblyScript (WASM); account-based |
| **Launch** | Token sale (2020); team/investor allocation |
| **Key strengths** | Fast finality, stateless validation reduces barriers, sharding for scalability, account abstraction |
| **Key weaknesses** | Very low validator count (254), shard security depends on random assignment, relatively new sharding design |

### Aptos (APT)

| Dimension | Details |
|-----------|---------|
| **Consensus** | AptosBFT (evolved from DiemBFT); leader-based BFT with pipelining |
| **Finality** | ~1 second; sub-50ms block times achieved |
| **Block time** | <50ms (December 2025) |
| **Throughput** | 22,000+ TPS sustained; theoretical 160,000 TPS |
| **Validators** | ~153; minimum stake 1M APT (~$8M+), max 50M APT |
| **Hardware requirements** | High |
| **Security model** | Economic; BFT with extremely high stake threshold |
| **Fee market** | Very low; all gas fees burned |
| **Partition behavior** | BFT; halts without 2/3 of validators |
| **Trust assumptions** | Effectively permissioned validator set (1M APT minimum) |
| **Smart contracts** | Move VM; parallel execution via Block-STM |
| **Launch** | VC-funded (Oct 2022); significant insider allocation |
| **Key strengths** | Highest sustained throughput, Move VM safety, parallel execution |
| **Key weaknesses** | Tiny validator set (152), effectively permissioned, heavy VC distribution, Diem lineage (corporate origin) |

### Sui (SUI)

| Dimension | Details |
|-----------|---------|
| **Consensus** | Mysticeti v2 (DAG-based BFT); owned-object transactions bypass consensus |
| **Finality** | Near-instant for simple txs; ~390ms for consensus txs |
| **Block time** | P50 consensus: 67ms |
| **Throughput** | ~33 TPS actual; max ~927 TPS; theoretical 100,000–120,000 TPS |
| **Validators** | ~122; minimum stake 30M SUI; ~75% of SUI staked |
| **Hardware requirements** | High |
| **Security model** | Economic; BFT with object-level ownership model |
| **Fee market** | ~$0.03 per tx; separate execution and storage fees |
| **Partition behavior** | BFT; requires 2/3 for consensus |
| **Trust assumptions** | Object ownership model introduces different security assumptions for non-consensus txs |
| **Smart contracts** | Move VM; object-oriented resource model |
| **Launch** | VC-funded (May 2023); significant insider allocation |
| **Key strengths** | Novel object model, near-instant simple tx finality, Move VM safety |
| **Key weaknesses** | Tiny validator set (~100), gap between actual and theoretical TPS, VC distribution, less battle-tested |

---

## Cross-Protocol Comparison Matrix

### Consensus & Security

| Protocol | Type | Finality | Cost to Attack | Trust Assumptions |
|----------|------|----------|---------------|-------------------|
| Bitcoin | PoW chain | ~60 min | 51% hashrate (~$1B+/hr) | None |
| **Kaspa** | **PoW DAG** | **~10 sec** | **51% hashrate** | **None** |
| Ethereum | PoS BFT | ~13 min | 1/3 staked ETH (~$37B+) | Weak subjectivity |
| Solana | PoS BFT | ~400ms–12s | 1/3 staked SOL | Leader schedule, PoH |
| Avalanche | PoS sampling | <1 sec | 1/3 staked AVAX | Sub-sampling model |
| Cardano | PoS VRF | ~20 min | 51% stake | Standard PoS |
| Algorand | PPoS VRF | Instant | 1/3 stake | Relay nodes (transitioning) |
| NEAR | PoS sharded | ~2 sec | Shard-level attack | Shard assignment |
| Aptos | PoS BFT | ~1 sec | 1/3 of ~153 validators | Permissioned-in-practice |
| Sui | PoS BFT | <400ms | 1/3 of ~122 validators | Object ownership model |

### Throughput & Fees

| Protocol | Actual TPS | Max Recorded | Block Time | Avg Fee |
|----------|-----------|-------------|------------|---------|
| Bitcoin | ~7 | ~7 | 10 min | ~$0.30 |
| **Kaspa** | **~3,000** | **5,584** | **100ms** | **<$0.001** |
| Ethereum L1 | 15–30 | ~63 | 12s | ~$0.10 |
| Solana | 1,000–4,000 | 55,000+ | 400ms | ~$0.0005 |
| Avalanche | ~30 | ~123 | ~2s | Very low |
| Cardano | ~0.41 | ~12 | 20s | ~$0.12 |
| Algorand | ~7 | 5,716 | <3s | ~$0.0001 |
| NEAR | 63–80 | 4,135 | ~1s | <$0.0001 |
| Aptos | 22,000+ | 22,000+ | <50ms | Very low |
| Sui | ~33 | ~927 | 67ms | ~$0.03 |

### Decentralization

| Protocol | Validators/Miners | Superminority | Hardware Barrier | Launch Fairness |
|----------|-------------------|---------------|-----------------|-----------------|
| Bitcoin | Millions of machines | Large pool concentration | ASIC | Fair, no premine |
| **Kaspa** | **Multiple ASIC manufacturers** | **Not reported** | **ASIC** | **Fair, no premine** |
| Ethereum | ~962,941 active (2.2M registered) | Top-10 entities >60% | Consumer hardware | ICO, premine |
| Solana | ~795 (down 68%) | ~20 validators | Extreme (256 GB–1 TB RAM) | VC-funded |
| Avalanche | ~656 (down 55% YoY) | Not reported | Moderate | ICO |
| Cardano | ~2,917 pools | None >1.4% | Consumer hardware | ICO |
| Algorand | ~1,600+ | Not reported | Very low | Dutch auction |
| NEAR | ~254–411 | Not reported | Moderate | Token sale |
| Aptos | ~153 | Not reported | High; 1M APT min stake | VC-funded |
| Sui | ~122 | Not reported | High; 30M SUI min stake | VC-funded |

### Partition Behavior

| Protocol | During Partition | After Reconnection | Work/Stake Lost |
|----------|-----------------|-------------------|-----------------|
| Bitcoin | Both sides mine | Shorter fork orphaned | 100% of losing fork |
| **Kaspa** | **Both sides produce blocks** | **All blocks merge** | **Zero** |
| Ethereum | Finality halts; inactivity leak | Slow recovery; validators lose stake | Offline validators penalized |
| Solana | **Complete halt** | Manual restart (6–17 hours) | All txs during downtime |
| Avalanche | Degrades/halts | Reconnection needed | Varies |
| Cardano | Shorter chain orphaned | Automatic (longer chain wins) | Losing fork |
| Algorand | Halts without 2/3 | Automatic on reconnection | Period of downtime |
| NEAR | Shard-dependent | Varies | Varies |
| Aptos | Halts without 2/3 | Validator coordination | Period of downtime |
| Sui | Halts without 2/3 | Validator coordination | Period of downtime |

---

## Kaspa's Honest Tradeoffs

### Acknowledged Weaknesses

1. **Younger ecosystem:** ~2 years vs Bitcoin's 15+ years. Less battle-tested, smaller developer community, fewer tools.

2. **Smart contracts still maturing:** L1 covenants (KIP-17) in development. L2s (Igra, Kasplex zkEVM) just launching. No mature DeFi ecosystem yet.

3. **ASIC-concentrated mining:** While multiple manufacturers exist (Bitmain, IceRiver, Goldshell, WindMiner), the hardware manufacturing base is narrower than Bitcoin's.

4. **Smaller market presence:** ~$800M market cap (rank ~#75). Not on Binance or Coinbase spot (both offer futures only). Listed on Bybit, Kraken, KuCoin, Bitget, MEXC, Crypto.com. HTX added KAS/USDT spot trading in December 2025.

5. **DAG-KNIGHT not yet deployed:** Mainnet still runs GHOSTDAG with its static k parameter. Early Rust prototype exists (hierarchical conflict resolution, incremental coloring, parent selection) but cascade voting not implemented. Described as "far from testnet or mainnet readiness."

6. **Less battle-tested:** No real-world network partition events to validate theoretical partition tolerance. Stress tests are not adversarial conditions.

7. **Throughput scaling:** Current ~3,000 TPS is strong but the 30,000+ TPS roadmap target at 100 BPS requires further engineering.

### Genuine Advantages (Sourced)

1. **Only high-throughput chain with Bitcoin's security model:** PoW + UTXO + fair launch + no premine + energy-backed security at 10 BPS. No other protocol combines these properties. (Verified against all protocols in this matrix.)

2. **Fee market viability through throughput:** The only PoW chain with sufficient throughput to potentially sustain fee-based security long-term. (See [security-budget.md](./security-budget.md), informed by Lyn Alden's framework.)

3. **Partition tolerance:** DAG merge means zero wasted work, zero punished miners, zero downtime. Unique among all protocols compared. (Derived from GHOSTDAG/DAG-KNIGHT design: [ePrint 2018/104](https://eprint.iacr.org/2018/104), [ePrint 2022/1494](https://eprint.iacr.org/2022/1494).)

4. **No adaptive adversary surface:** Work-then-select (PoW) means block producers are unknown until they produce. (Fundamental PoW property.)

5. **No liquid staking risk:** No staking = no liquid staking derivatives = no Lido-style concentration risk.

6. **No weak subjectivity:** New nodes can verify from genesis. No trusted checkpoints needed.

7. **Chromatic halving:** Smooth emission curve. No supply shocks, no miner capitulation events. (Source: [Kaspa tokenomics](https://kaspa.org/tokenomics-emission-and-mining/).)

8. **Fair launch = regulatory clarity:** No premine, no ICO, no insider allocation = strongest case for commodity classification under emerging US regulatory frameworks. (Context: CLARITY Act, SEC "Project Crypto" framework.)

---

## References

- Bitcoin data: [BitInfoCharts](https://www.bitinfocharts.com/bitcoin/) · [CoinWarz](https://www.coinwarz.com/mining/bitcoin/hashrate-chart)
- Kaspa: [Kaspalytics](https://www.kaspalytics.com/) · [kaspa.org](https://kaspa.org/) · [ePrint 2018/104](https://eprint.iacr.org/2018/104) · [ePrint 2022/1494](https://eprint.iacr.org/2022/1494)
- Ethereum: [ethereum.org](https://ethereum.org/) · [CoinLaw](https://coinlaw.io/eth-staking-statistics/) · [beaconcha.in](https://beaconcha.in/)
- Solana: [docs.solanalabs.com](https://docs.solanalabs.com/) · [Helius](https://www.helius.dev/) · [CoinLaw](https://coinlaw.io/solana-statistics/)
- Avalanche: [build.avax.network](https://build.avax.network/) · [Chainspect](https://chainspect.app/chain/avalanche)
- Cardano: [cardano.org](https://cardano.org/) · [CoinLaw](https://coinlaw.io/cardano-statistics/)
- Algorand: [algorand.co](https://algorand.co/) · [Chainspect](https://chainspect.app/chain/algorand)
- NEAR: [pages.near.org](https://pages.near.org/) · [CoinLaw](https://coinlaw.io/near-protocol-statistics/)
- Aptos/Sui: [VanEck](https://www.vaneck.com/us/en/blogs/digital-assets/sui-vs-aptos-competitive-analysis-and-price-prediction/) · [BlockEden](https://blockeden.xyz/blog/2026/02/08/movevm-blockchain-comparison-sui-aptos-initia/)
