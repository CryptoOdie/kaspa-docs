# Security Budget & Fee Markets

## Overview

Every proof-of-work blockchain faces a structural economic question: when block subsidies expire, can transaction fees alone fund sufficient network security? This is the **security budget problem**, and its resolution depends entirely on throughput.

---

## The Security Budget Equation

Miner revenue -- and therefore network security -- is determined by:

```
total_security_spend = block_subsidy + (transaction_volume x average_fee)
```

As the block subsidy trends toward zero over successive halvings:

```
total_security_spend = transaction_volume x average_fee
```

There are exactly two levers:

| Lever | Effect | Consequence |
|-------|--------|-------------|
| Increase average fee | Higher per-transaction cost | Prices out users, undermines utility |
| Increase transaction volume | More fee-paying transactions | Maintains security at affordable fees |

No protocol can rely on subsidies indefinitely. Fee-based security is the only long-term model.

---

## Bitcoin's Structural Gap

Lyn Alden's fee-based security modeling ([lynalden.com](https://www.lynalden.com/bitcoin-security-modeling/)) establishes a quantitative framework: to secure a multi-trillion dollar network, annual fee revenue must reach 0.5--1.5% of market capitalization. This translates to $5--15 billion per trillion dollars of market cap per year.

As Alden notes: "The long-term expectation from the beginning, even in Satoshi's own words, was that fees eventually would be the primary and eventually only source of revenue for Bitcoin miners."

### Current Fee Market Reality

| Metric | Value |
|--------|-------|
| Effective throughput | ~7 TPS |
| Average transaction fee (2025) | ~$0.62 USD |
| Daily fee revenue (late 2025) | ~$300,000 |
| Fee share of miner income | < 1% (June 2025: 0.96%) |
| Current block subsidy | 3.125 BTC/block (~$50M+/day) |

External analysis (Data Always) observed that Bitcoin's actual fee-to-market-cap ratio trends toward ~0.025% -- roughly 20x lower than Alden's most conservative 0.5% scenario.

### Required Fees at 7 TPS

Assuming a $2 trillion market cap with Alden's framework:

| Security Target | Annual Revenue Needed | Daily Fee Revenue | Required Fee per Transaction |
|----------------|----------------------|-------------------|------------------------------|
| 0.5% of market cap | $10 billion | $27.4 million | **~$45** |
| 1.0% of market cap | $20 billion | $54.8 million | **~$90** |

The current average fee of $0.62 is 70--145x below what is needed. There is no plausible path to $45--90 per transaction fees without destroying Bitcoin's utility as a payment network. Lightning Network does not resolve this: L2 transactions generate L1 fee revenue only when they settle on-chain, and settlement frequency is structurally limited.

### The Halving Timeline

| Period | Block Subsidy | Fraction of Current |
|--------|--------------|---------------------|
| 2024--2028 | 3.125 BTC | 1x |
| 2028--2032 | 1.5625 BTC | 1/2 |
| 2032--2036 | 0.78125 BTC | 1/4 |
| 2036--2040 | 0.390625 BTC | 1/8 |
| 2040--2044 | 0.1953125 BTC | 1/16 |

Each halving cuts the subsidy in half. The industry consensus threshold is that fees should consistently account for >20% of miner revenue for sustainability. Bitcoin has never sustained above 15% outside brief spikes.

---

## Throughput as the Solution

The equation makes the path clear. If transaction volume increases by 100x while average fee remains constant, total security spend increases 100x. Equivalently, the same security spend can be maintained while reducing per-transaction fees by 100x.

**High throughput is not about speed for its own sake. It is the mechanism that makes fee-based security sustainable.**

### Kaspa's Fee Market Position

| Metric | Bitcoin | Kaspa (Current) | Kaspa (Roadmap) |
|--------|---------|-----------------|-----------------|
| Blocks per second | ~0.0017 | 10 | 100 |
| Effective TPS | ~7 | ~60 | 30,000+ |
| Block time | 10 minutes | 100 ms | 10 ms |
| Fee per tx for $10B annual security | ~$45 | ~$5 | ~$0.01 |

At 30,000 TPS with full utilization, Kaspa could generate Bitcoin-equivalent total fee revenue at roughly 1/4000th the per-transaction cost. This is the only demonstrated path to sustainable fee-based security that does not price out users.

For details on how Kaspa achieves this throughput without centralization, see [GHOSTDAG](../consensus/ghostdag.md).

---

## Chromatic Halving

Bitcoin's abrupt halvings -- a sudden 50% reduction every ~4 years -- create supply shocks that destabilize miner economics. Less efficient miners are forced offline immediately, hashrate drops, and the network becomes temporarily less secure.

Kaspa uses **chromatic halving**: block rewards decrease smoothly every month by a factor of (1/2)^(1/12). The ratio between consecutive months' rewards matches the frequency ratio of two consecutive semitones in a tempered chromatic scale.

| Property | Bitcoin Halving | Kaspa Chromatic Halving |
|----------|----------------|------------------------|
| Reduction schedule | 50% every ~4 years | ~5.6% per month, continuously |
| Miner impact | Sudden cliff; mass capitulation risk | Gradual, predictable decline |
| Security transition | Abrupt; fee market must compensate immediately | Smooth; fee market develops organically |
| Speculative cycles | Halving-driven boom/bust | No discrete halving events |
| Maximum supply | 21 million BTC | 28.7 billion KAS |

**Sources:** [Kaspa Tokenomics](https://kaspa.org/tokenomics-emission-and-mining/) -- [The Chromatic Symphony of Kaspa](https://medium.com/kaspa-currency/the-chromatic-symphony-of-kaspa-3b1e72796977)

---

## Key Takeaways

1. Fee-based security is the only sustainable long-term model for any PoW blockchain.
2. Fee-based security requires high throughput to generate sufficient revenue at affordable per-transaction costs.
3. Bitcoin's ~7 TPS creates a structural gap that requires $45--90 per-transaction fees -- an implausible outcome.
4. Kaspa's [DAG architecture](../consensus/ghostdag.md) enables the throughput needed to close this gap while preserving PoW's thermodynamic security model.
5. Chromatic halving eliminates the supply shocks that make Bitcoin's transition to fee-based security more disruptive.

---

## References

- Alden, L. "Bitcoin: Fee-Based Security Modeling." [lynalden.com](https://www.lynalden.com/bitcoin-security-modeling/)
- Bitcoin fee data: [BitInfoCharts](https://www.bitinfocharts.com/bitcoin/) -- [Bitbo Charts](https://charts.bitbo.io/fees-percent-of-reward/)
- Kaspa metrics: [Kaspalytics](https://www.kaspalytics.com/) -- [Kaspa Explorer](https://explorer.kaspa.org/)
- Kaspa tokenomics: [kaspa.org/tokenomics-emission-and-mining](https://kaspa.org/tokenomics-emission-and-mining/)
