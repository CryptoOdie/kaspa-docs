# Fee Markets and the Security Budget: Why Throughput Is Security

## The Most Important Unsolved Problem in Cryptocurrency

Every proof-of-work blockchain faces a fundamental economic question: **what happens when block rewards run out?**

Block rewards — newly minted coins given to miners for producing blocks — are the primary funding mechanism for network security in every PoW chain. They pay for the hashpower that makes attacks expensive. But block rewards are designed to decrease over time. Bitcoin's halve every ~4 years; Kaspa's decrease smoothly via chromatic halving. Eventually, in every PoW system, transaction fees must fund **100% of network security**.

This is the security budget problem. It applies to Bitcoin. It applies to Kaspa. And the only sustainable solution is **high throughput**.

---

## The Security Budget Equation

Network security in PoW is a function of total miner revenue:

```
total_security_spend = block_subsidy + (transaction_volume × average_fee)
```

As `block_subsidy → 0` over time:

```
total_security_spend ≈ transaction_volume × average_fee
```

This means there are exactly two ways to maintain security spending when subsidies decline:

1. **Increase average fee per transaction** — prices out users, undermines utility
2. **Increase transaction volume** — maintains security while keeping fees affordable

There is no third option. You cannot rely on block rewards forever, and you cannot maintain security without sufficient miner revenue.

---

## Bitcoin's Security Budget Is Structurally Broken

This is not a speculative concern. The data is clear.

Lyn Alden's fee-based security modeling ([lynalden.com/bitcoin-security-modeling](https://www.lynalden.com/bitcoin-security-modeling/)) establishes the framework:

**Alden's framework:** If Bitcoin sustains a multi-trillion dollar market cap, fees must reach 0.5–1.5% of market capitalization annually to fund adequate security. This translates to **$5–15 billion per trillion dollars of market cap** in annual miner revenue.

**Alden's key insight:** "The long-term expectation from the beginning, even in Satoshi's own words, was that fees eventually would be the primary and eventually only source of revenue for Bitcoin miners, which is important for the long-term immutability and censorship-resistance of the network."

### The Numbers Show the Model Is Failing

**Bitcoin's current fee market (March 2026):**
- ~453,000 transactions per day (~7 TPS capacity)
- Average transaction fee: ~$0.30 USD (March 8, 2026); 2026 average ~$0.82
- Fee revenue: ~$300,000/day — **~1% of total miner income** in baseline conditions
- March 2025: fees were just **1.25% of the block reward** — the lowest in three years
- August 2025: nearly **15% of blocks were "free"** (mined with ~1 sat/vB fees)
- Daily transaction fees collapsed **>80%** from April 2025 peaks
- Current block subsidy: 3.125 BTC per block (~$50M+/day at current prices)

**The trend is not ambiguous:** External analysis (Data Always) observed that Bitcoin's actual fee-to-market-cap ratio trends toward ~0.025% — roughly **20x lower** than even Alden's most conservative scenario of 0.5%. There is no indication — in current data, in usage trends, or in protocol mechanics — that fees will close this gap.

### The Scale of the Problem

Let's put concrete numbers on what's needed. Assume Bitcoin reaches $2 trillion market cap and needs a security budget of 0.5% of market cap (Alden's low-case scenario):

- **Required annual security spend:** $10 billion/year
- **Required daily miner revenue from fees:** ~$27.4 million/day
- **At ~7 TPS (604,800 tx/day):** Average fee must be **~$45 per transaction**

At 1% of market cap (mid-case):
- **Required daily fee revenue:** ~$54.8 million/day
- **At ~7 TPS:** Average fee must be **~$90 per transaction**

**Current reality:** Average fee is $0.30. The gap is not 2x or 5x — it's **150–300x**. And the block subsidy is still providing 85–99% of miner revenue. Current daily fee revenue of ~$300K annualizes to ~$110 million — orders of magnitude below the $5–15 billion needed. When the subsidy drops to 0.2% of its current value (which the halving schedule guarantees), fees must increase by two orders of magnitude just to maintain current security levels — at a throughput of 7 TPS.

**There is no plausible scenario where this happens.** $45–90 per transaction would price out virtually all users and make Bitcoin unusable as a payment network. Ethereum researcher Justin Drake has called Bitcoin's security model a "ticking time bomb."

Lightning Network doesn't solve this — L2 transactions don't generate L1 fee revenue unless they settle on-chain. Lightning processed ~$1.1 billion across 5.2 million transactions in November 2025, with network capacity reaching 5,606 BTC by December 2025. But only channel opens and closes touch L1. Lightning structurally reduces L1 fee demand by moving small payments off-chain — potentially **worsening** the security budget problem rather than solving it.

### The Halving Timeline Creates a Deadline, Not an Opportunity

- Current: 3.125 BTC subsidy (2024–2028)
- Next halving: **March–April 2028** (block 1,050,000) → 1.5625 BTC
- 2036: 0.390625 BTC — subsidy is 1/8 of current
- 2044: 0.024414 BTC — subsidy is effectively negligible

Each halving cuts the subsidy in half. The industry consensus threshold is that fees should consistently account for **>20% of miner revenue** for long-term sustainability. Bitcoin has **never sustained above 20%** outside of brief event-driven spikes:

- **April 20, 2024 (Runes launch + halving):** Fees hit **75% of total block revenue** — an all-time record. Daily miner revenue reached $107.8 million with average fees of **$127.97** per transaction. The Runes fee share collapsed from 50%+ to **1.67%** within weeks.
- **May 2023 (Ordinals surge):** Fees briefly exceeded the block subsidy — then collapsed.

These spikes lasted days, not months. There is no mechanism in Bitcoin's protocol design that addresses this.

### Bitcoin's Throughput Constraint Is the Root Cause

Bitcoin processes ~7 transactions per second. This is a hard architectural limit — 1 block per 10 minutes, ~1 MB of transaction data per block. At this throughput, the math is simple and unforgiving:

```
Required per-tx fee = Required annual security / (7 TPS × 31.5M seconds/year)
                    = $10B / 220.5M tx/year
                    = ~$45 per transaction
```

There are exactly two solutions:
- **Increase per-transaction fees to $45–90+** — which destroys utility
- **Increase throughput by 100–1000x** — which Bitcoin's single-chain architecture cannot do

This is not a future concern. This is a structural deficiency that becomes more acute with every halving. The block subsidy is masking a security model that cannot sustain itself on fees alone at 7 TPS.

---

## The Throughput Solution

The security budget equation makes the solution clear:

```
total_security_spend = transaction_volume × average_fee
```

If you can increase `transaction_volume` by 100x while keeping `average_fee` constant, total security spend increases 100x. Alternatively, you can **maintain the same security spend** while reducing per-transaction fees by 100x.

**This is the core argument for high-throughput PoW:** not speed for speed's sake, but throughput as the mechanism that makes fee-based security sustainable.

### Kaspa's Position

Kaspa currently operates at **10 blocks per second** (post-Crescendo hard fork, May 5, 2025), achieving ~3,000 TPS in normal operation with demonstrated peaks of 5,584 TPS in stress testing. Future targets include 32 BPS and eventually 100 BPS with 30,000+ TPS.

**Fee-market viability comparison:**

| Metric | Bitcoin | Kaspa (current) | Kaspa (roadmap) |
|--------|---------|-----------------|-----------------|
| Blocks per second | ~0.0017 (1 per 10 min) | 10 | 32 → 100 |
| Effective TPS | ~7 | ~3,000 | 30,000+ |
| Block time | 10 minutes | 100ms | 31ms → 10ms |
| Per-tx fee needed for $10B annual security | ~$45+ | ~$0.10 | ~$0.01 |

At 30,000 TPS with full blocks, Kaspa could generate Bitcoin-equivalent total fee revenue at **1/4000th the per-transaction cost**. This is the only path to sustainable fee-based security that doesn't price out users.

Note: ~93.3% of Kaspa's 28.7 billion KAS max supply has already been mined (~26.77 billion circulating), meaning the transition to fee-based security is not a distant concern — it's already underway.

---

## Kaspa's Chromatic Halving: A Smoother Transition

Bitcoin's abrupt halvings — a sudden 50% reduction in block rewards every ~4 years — create supply shocks that destabilize miner economics. Less efficient miners are forced offline immediately, hashrate drops, and the network temporarily becomes less secure until price appreciation compensates.

Kaspa uses **chromatic halving**: block rewards decrease smoothly every month by a factor of (1/2)^(1/12). The ratio of rewards in consecutive months is identical to the frequency ratio of two consecutive semitones in a tempered chromatic scale — hence the name.

**Advantages:**
- **No supply shocks:** Miners experience gradual, predictable income decline
- **No mass capitulation events:** Eliminates the "halving cliff" that forces miners offline
- **Smoother security transition:** The fee market has time to develop organically as subsidies decrease
- **Market predictability:** No speculative halving cycles

Maximum supply: **28.7 billion KAS** (deflationary trajectory matching Bitcoin's, without the discrete shocks).

**Source:** [Kaspa Tokenomics](https://kaspa.org/tokenomics-emission-and-mining/) · [The Chromatic Symphony of Kaspa](https://medium.com/kaspa-currency/the-chromatic-symphony-of-kaspa-3b1e72796977)

---

## The PoS Security Budget Problem

Proof-of-Stake advocates often present PoS as solving the security budget problem because validators require less revenue (no energy costs). This framing misses several critical issues:

### 1. Liquid Staking Undermines the "Locked Capital" Assumption

PoS security depends on capital being **locked and at risk**. Liquid staking derivatives (LSDs) break this assumption:

- **Lido** controls **24.2% of all staked ETH** (~8.7M ETH), down from a peak of 32.3% in late 2023. Its node operator base has expanded across three modules (Curated, SimpleDVT with 261 operators, Community Staking with 312+ operators), but remains a significant concentration risk.
- The top 10 staking entities control **over 60% of all staked ETH**
- Stakers receive stETH tokens that are simultaneously staked AND liquid — capital is "at risk" in name only
- Total liquid staking TVL exceeds **$66.86 billion** with an LST market cap of **$86.4 billion**
- Academic research (Tzinas & Zindros, 2024, Financial Cryptography proceedings) demonstrates this introduces a **principal-agent problem**: delegators cede control to protocols who decide how to allocate stake among validators
- Research proves that "proportional representation and fair punishment are fundamentally incompatible in an adversarial setting"

**The systemic risk:** Lido peaked above 32% (approaching the 33% liveness attack threshold) before declining. During market stress, mass unstaking through LSDs could force withdrawals that undermine security at precisely the moment it's most needed.

**Sources:** [Tzinas & Zindros 2024](https://eprint.iacr.org/2023/605) · [Paradigm: On Staking Pools](https://www.paradigm.xyz/2021/04/on-staking-pools-and-staking-derivatives) · [CoinDesk: Does Lido Control Too Much?](https://www.coindesk.com/consensus-magazine/2023/09/28/does-lido-control-too-much-liquid-staking)

### 2. Validator Revenue = Inflation + Fees

PoS validators earn from:
- **Staking rewards** (protocol inflation) — the equivalent of block subsidies
- **Transaction fees**
- **MEV extraction** (a centralizing force — see below)

If inflation is reduced to control supply, validator revenue drops unless fees compensate. **This is the same security budget problem as PoW**, but without the thermodynamic cost floor that makes PoW attacks irreversibly expensive.

### 3. MEV as Centralization Force

Maximal Extractable Value (MEV) — profit from transaction ordering — creates structural centralization:

- Cumulative MEV extracted from Ethereum exceeds **$1.8 billion**
- The MEV relay landscape has shifted: Ultrasound relay (33%), Titan (21%), bloXroute (31.7%), while Flashbots dropped from 84% dominance to just **3.52%**
- However, **block builder centralization** has worsened: just 2 operators build over **90% of Ethereum blocks**
- BuilderNet (Flashbots + Beaverbuild + Nethermind, launched Nov 2024) attempts to address this but hasn't solved it
- Large validators form exclusive relationships with top block builders, sidelining smaller participants

MEV creates economies of scale that push toward validator concentration — the opposite of decentralization.

### 4. Nothing-at-Stake and Weak Subjectivity

- **Nothing-at-stake:** Validators can sign conflicting blocks at zero marginal cost (no energy expenditure). Slashing is reactive, not proactive — it assumes correct attribution after the fact.
- **Weak subjectivity:** New nodes must obtain a recent checkpoint from a trusted source to sync safely. This reintroduces trusted third parties — the exact thing cryptocurrency was designed to eliminate.
- **Long-range attacks:** An attacker who once controlled significant stake can create an alternate history. Only weak subjectivity (trusted checkpoints) prevents this.

---

## Kaspa's Unique Position

Kaspa is the only protocol that addresses the security budget problem while maintaining Bitcoin's security model:

| Property | Bitcoin | Kaspa | Ethereum (PoS) |
|----------|---------|-------|-----------------|
| Security model | Thermodynamic (energy) | Thermodynamic (energy) | Economic (capital) |
| Attack cost | Energy expenditure | Energy expenditure | Capital at risk (undermined by LSDs) |
| Throughput for fee market | ~7 TPS | ~3,000 TPS (roadmap: 30,000+) | 15–30 TPS L1 |
| Emission schedule | Abrupt halvings | Chromatic (smooth) | Variable inflation |
| Trust assumptions | None beyond protocol | None beyond protocol | Weak subjectivity, trusted checkpoints |
| Liquid staking risk | N/A | N/A | Systemic (Lido 24.2%, top-10 entities >60%) |
| MEV exposure | Limited | Minimal (UTXO model) | Severe ($1.8B+ cumulative; 2 builders control 90%+ of blocks) |

**The argument is not "PoW good, PoS bad."** The argument is:

1. Fee-based security is the only sustainable long-term model for any blockchain
2. Fee-based security requires high throughput to generate sufficient revenue at affordable per-tx costs
3. PoW's thermodynamic security model provides attack resistance that capital-based models cannot match (energy spent is energy gone; staked capital can be made liquid)
4. Kaspa combines PoW's security model with the throughput needed for sustainable fee markets
5. No other protocol does this

---

## Research Gaps and Caveats

> **FLAG:** The 158 million single-day transaction figure for Kaspa (October 5, 2025) likely reflects stress testing or token protocol activity rather than organic usage. Verify against primary chain data.

> **FLAG:** Bitcoin fee revenue figures vary significantly across timeframes. Fee % of miner revenue swings from ~1% in baseline conditions to brief spikes of 75% (April 2024 Runes launch). The 2026 average stabilizes around ~15% but this is heavily influenced by outlier events.

---

## Key References

- Alden, L. "Bitcoin: Fee-Based Security Modeling." [lynalden.com](https://www.lynalden.com/bitcoin-security-modeling/)
- Tzinas, E. & Zindros, D. "The Principal-Agent Problem in Liquid Staking." Financial Cryptography 2024. [ePrint 2023/605](https://eprint.iacr.org/2023/605)
- Bitcoin fee data: [BitInfoCharts](https://www.bitinfocharts.com/bitcoin/) · [Bitbo Charts](https://charts.bitbo.io/fees-percent-of-reward/) · [YCharts](https://ycharts.com/indicators/bitcoin_average_transaction_fee)
- Bitcoin security analysis: [Cointelegraph](https://cointelegraph.com/news/bitcoin-fee-crisis-miners-btcfi-2025) · [The Block](https://www.theblock.co/post/379291/bitcoin-miner-fees-fall-12-month-low-underscoring-long-term-reliance-block-subsidies)
- Lightning Network data: [Bitcoin Magazine](https://bitcoinmagazine.com/news/bitcoins-lightning-network-surpasses) · [CoinLaw](https://coinlaw.io/bitcoin-lightning-network-usage-statistics/)
- Ethereum MEV relays: [relayscan.io](https://www.relayscan.io/) · BuilderNet (Flashbots + Beaverbuild + Nethermind)
- Kaspa metrics: [Kaspalytics](https://www.kaspalytics.com/) · [Kaspa Explorer](https://explorer.kaspa.org/)
- Kaspa tokenomics: [kaspa.org/tokenomics-emission-and-mining](https://kaspa.org/tokenomics-emission-and-mining/)
