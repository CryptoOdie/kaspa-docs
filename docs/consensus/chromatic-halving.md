# Chromatic Halving: Kaspa's Emission Schedule

## Overview

Kaspa uses a **chromatic halving** emission schedule — a smooth, continuous reduction in block rewards that eliminates the supply shocks of Bitcoin's abrupt halvings.

## How It Works

Block rewards decrease **every month** by a factor of:

```
(1/2)^(1/12) ≈ 0.9439
```

This means the reward halves once per year, but the reduction is spread smoothly across 12 monthly steps rather than occurring as a single event.

### Why "Chromatic"?

The ratio of block rewards in consecutive months is identical to the frequency ratio of two consecutive semitones in a **tempered chromatic musical scale**. The 12-step annual halving mirrors the 12 semitones in an octave.

## Comparison with Bitcoin

| Property | Bitcoin | Kaspa |
|----------|---------|-------|
| Halving frequency | Every ~4 years (210,000 blocks) | Smooth monthly reduction |
| Reward reduction | 50% at once | ~5.6% per month |
| Supply shocks | Yes (abrupt 50% drops) | No (continuous curve) |
| Miner disruption | Mass capitulation events post-halving | Gradual, predictable decline |
| Maximum supply | 21 million BTC | 28.7 billion KAS |
| Emission curve shape | Staircase | Smooth exponential decay |

### Bitcoin's Halving Problem

Every ~4 years, Bitcoin miners experience a sudden **50% income reduction**:
- 50 → 25 → 12.5 → 6.25 → 3.125 BTC (current) → 1.5625 BTC (2028)

These shocks force less efficient miners offline immediately, temporarily reduce hashrate, and create speculative market cycles. The network becomes temporarily less secure in the period between the halving and price adjustment.

### Kaspa's Smooth Approach

Kaspa miners experience a gradual, predictable income decline:
- Each month, rewards drop by ~5.6%
- No single event forces mass miner capitulation
- The fee market has time to develop organically as subsidies decrease
- No speculative "halving cycles" based on discrete events

## Implications for Security

The chromatic halving is directly relevant to the [security budget problem](../security/security-budget.md):

- **Smoother security transition:** The gradual reduction gives the fee market time to compensate, rather than requiring sudden fee increases post-halving
- **Miner stability:** Continuous operation without capitulation events maintains consistent hashrate and network security
- **Market predictability:** Predictable issuance reduces uncertainty for miners making infrastructure investments

## Technical Specification

The emission began on **May 8, 2022** with a starting reward of 440 KAS per second (across all blocks). The reward decreases monthly according to the chromatic schedule until the maximum supply of **28.7 billion KAS** is reached.

## References

- Kaspa tokenomics: [kaspa.org/tokenomics-emission-and-mining](https://kaspa.org/tokenomics-emission-and-mining/)
- Chromatic halving explanation: [The Chromatic Symphony of Kaspa](https://medium.com/kaspa-currency/the-chromatic-symphony-of-kaspa-3b1e72796977)
- Kaspa Wiki tokenomics: [wiki.kaspa.org/en/tokenomics](https://wiki.kaspa.org/en/tokenomics)
