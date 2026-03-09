# Kaspa On-Chain Metrics

> **Last updated:** March 2026. All figures are approximate and sourced from public aggregators unless otherwise noted.

## Market Position

| Metric | Value |
|--------|-------|
| Market cap | ~$800 million (rank ~#75 CoinGecko) |
| Price | ~$0.03 USD |
| 24-hour trading volume | $10.7-15.1 million |
| Exchange listings | 216 active markets |

**Major exchanges:** Bybit, Bitget, Gate, MEXC, LBank, Kraken (KAS/GBP, KAS/EUR).

**Not listed on:** Binance spot, Coinbase spot. Coinbase added KAS-PERP futures on February 20, 2026, which may signal movement toward a spot listing.

The absence from Binance and Coinbase spot is a direct consequence of the [fair launch](./regulatory.md) -- there are no pre-allocated tokens available for exchange listing incentives. This is a short-term adoption friction that reflects a long-term structural advantage.

## On-Chain Activity

| Metric | Value |
|--------|-------|
| Daily transactions | ~386,700 (Feb 2026 average) |
| Total transactions | 601+ million (as of Feb 20, 2026) |
| Peak daily transactions | 1.92M (Sep 2025) |
| Daily active addresses (peak) | ~545,600 (Sep 2025) |

> **Data quality flag:** A reported 158M single-day transaction spike (Oct 2025) and wide variation in active address counts (25K to 545K) across sources suggest either stress test activity, token protocol usage, or inconsistent measurement methodologies. Verify against primary chain data via [Kaspalytics](https://www.kaspalytics.com/).

## Network Performance

| Metric | Value |
|--------|-------|
| Blocks per second | 10 BPS (since [Crescendo hard fork](./roadmap.md), May 2025) |
| Block time | 100ms |
| Throughput (baseline) | ~60 TPS |
| Throughput (stress test peaks) | 3,000-5,500 TPS |
| Mining algorithm | kHeavyHash (ASIC-dominated) |
| Hashrate | ~411-445 PH/s |

## Mining Hardware Landscape

Multiple ASIC manufacturers provide hardware diversity, which is important for long-term decentralization.

| Manufacturer | Model | Hashrate | Notes |
|---|---|---|---|
| Bitmain | Antminer KS7 | 36-40 TH/s | Current generation leader |
| Bitmain | Antminer KS5 / KS5 Pro | 20-21 TH/s | Previous generation |
| IceRiver | KS5L, KS3M | Competitive | Pioneer of KAS ASICs |
| Goldshell | KA BOX | Entry-level | Lower-cost entry point |
| WindMiner | K9 | -- | Additional manufacturer |

Kaspa's high block rate (10 BPS) reduces reward variance for individual miners, which structurally reduces the economic incentive to join large mining pools.

> **Data gap:** No public data is available on mining pool distribution (e.g., top-3 pool hashrate share) or geographic concentration of miners. These are important centralization metrics that the community should work to surface.

## Developer Ecosystem

- **Repository:** [kaspanet/rusty-kaspa](https://github.com/kaspanet/rusty-kaspa) -- 764 stars, 259 forks
- **Language:** Rust
- **Key milestones:** See the [development roadmap](./roadmap.md) for recent and upcoming releases.

> **Data gap:** Exact contributor count, commit velocity, and external developer ecosystem size are not available from public sources.

## Known Data Gaps

This page aims to present Kaspa's metrics honestly. The following gaps exist:

1. **Mining centralization:** No public pool distribution or miner geography data.
2. **Developer metrics:** No contributor counts or commit frequency benchmarks.
3. **Active address consistency:** Reported figures vary significantly across aggregators.
4. **Transaction anomalies:** Occasional extreme spikes likely reflect stress tests or token protocol activity rather than organic usage.

When better data becomes available, this page will be updated.

## Sources

- [CoinMarketCap -- Kaspa](https://coinmarketcap.com/currencies/kaspa/)
- [CoinGecko -- Kaspa](https://www.coingecko.com/en/coins/kaspa)
- [Kaspalytics](https://www.kaspalytics.com/)
- [BSC News -- Kaspa 600M transactions](https://bsc.news/post/kaspa-600m-txns)
- [CryptoMinerBros -- Top Kaspa Miners](https://www.cryptominerbros.com/blog/top-kaspa-miners/)
- [ASIC Marketplace -- Top Kaspa Miners](https://asicmarketplace.com/blog/top-kaspa-miners/)
