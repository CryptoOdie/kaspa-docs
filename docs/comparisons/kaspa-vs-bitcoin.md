# Kaspa vs Bitcoin

Kaspa is not an alternative to Bitcoin. It applies the same security philosophy -- PoW, UTXO, fair launch, no premine, energy-backed security -- with a single architectural change: replacing the single chain with a [blockDAG](../consensus/ghostdag.md). This removes Bitcoin's throughput limitation while preserving everything that makes its security model unique.

---

## Shared Properties

### Proof-of-Work Security

Both networks are secured through computational work. Attacking either requires sustained energy expenditure -- a thermodynamically irreversible cost enforced by physics, not protocol rules.

- **Bitcoin:** SHA-256 mining, ~1,045 ZH/s hashrate
- **Kaspa:** kHeavyHash mining, ~411-445 PH/s hashrate

The mining algorithm differs, but the security guarantee is identical: the canonical chain/DAG is the one with the most cumulative proof-of-work.

### UTXO Transaction Model

Both use Unspent Transaction Outputs. Transactions consume existing UTXOs and create new ones. Validity depends only on inputs being unspent and properly signed. Transactions are stateless and naturally parallelizable.

Kaspa extends the UTXO model with:

- **UTXO commitments (MuHash):** Cryptographic commitment to the full UTXO set in each block, enabling bootstrap from a recent [pruning point](../architecture/pruning.md)
- **KIP-9 storage mass:** Harmonic formula penalizing UTXO-bloating transactions, replacing Bitcoin's blunt dust limits
- **Aggressive pruning:** Nodes prune old data after ~52 hours, maintaining a compact proof history

### Fair Launch

| Property | Bitcoin | Kaspa |
|----------|---------|-------|
| Launch date | January 3, 2009 | November 7, 2021 |
| Premine | None | None |
| ICO / token sale | None | None |
| Team allocation | None | None |
| Initial distribution | Mining only | Mining only |

This matters for regulatory classification (commodity vs security), distribution fairness, and team-community alignment.

### No Trust Assumptions

Neither protocol requires trusted checkpoints, committee selection, validator registration, minimum capital, slashing conditions, or external oracles. Any node can verify the canonical chain/DAG from genesis using only protocol rules and block data. This is **objective consensus** -- the strongest form of trustlessness in distributed systems.

---

## What Kaspa Changes

### Chain to DAG

Bitcoin produces blocks sequentially: one block references one parent. Simultaneous blocks cause orphans -- wasted work. Kaspa's [GHOSTDAG](../consensus/ghostdag.md) allows blocks to reference multiple parents, incorporating all honestly-produced blocks into the ledger.

| Metric | Bitcoin | Kaspa |
|--------|---------|-------|
| Block rate | ~1 per 10 min | 10 per second |
| Orphan rate | ~0.1% | 0% (by design) |
| Throughput | ~7 TPS | ~60 TPS (current), 3,000-5,500 TPS (stress test) |
| Confirmation | ~60 min (6 conf) | ~10 seconds |

### Adaptive Consensus (DAG-KNIGHT)

Bitcoin's longest-chain rule uses a fixed 10-minute block time. [DAG-KNIGHT](../consensus/dag-knight.md), targeting deployment in 2026-2027, will make consensus fully parameterless -- inferring network conditions from DAG topology and adapting confirmation times automatically.

### Partition Tolerance

During a network partition, Bitcoin discards the losing fork entirely. Kaspa merges both sides with zero wasted work. See [partition tolerance](../architecture/partition-tolerance.md) for details.

### Emission Curve

Bitcoin halves rewards abruptly every ~210,000 blocks. Kaspa uses **chromatic halving** -- smooth monthly reduction by (1/2)^(1/12). Same deflationary trajectory toward a fixed supply (28.7B KAS), without supply shocks.

---

## What Kaspa Does NOT Change

| Property | Changed? | Detail |
|----------|----------|--------|
| Security model (PoW) | No | Same energy-backed security |
| UTXO model | No | Same stateless transaction structure |
| Fair launch | No | Same distribution model |
| No trusted third parties | No | No weak subjectivity, no checkpoints |
| Permissionless mining | No | Anyone can mine |
| Fixed maximum supply | No | Deflationary, capped emission |
| Adaptive adversary resistance | No | Work-then-select preserved |

Kaspa is not an experiment in new security models. It is the same security model with a better data structure.

---

## Honest Comparison

| Dimension | Bitcoin Advantage | Kaspa Advantage |
|-----------|-------------------|-----------------|
| Battle-tested | 15+ years, never compromised | -- |
| Network effect | Largest hashrate, institutional adoption, ETFs | -- |
| Liquidity | Deepest markets globally | -- |
| Ecosystem | Largest developer community, most tooling | -- |
| Throughput | -- | 6,000x block rate, ~10x current TPS |
| Confirmation time | -- | ~10 seconds vs ~60 minutes |
| Partition tolerance | -- | DAG merge, zero wasted blocks |
| Fee sustainability | -- | Throughput enables low per-tx fees at volume |
| Emission smoothness | -- | Chromatic halving, no supply shocks |
| UTXO management | -- | MuHash commitments, storage mass, pruning |

Bitcoin's advantages are real and significant. Network effect, battle-testing, and institutional infrastructure are not trivial. Kaspa's advantages are architectural: they address structural limitations that Bitcoin cannot fix without fundamental protocol changes.

### Bitcoin's Unsolved Challenges

1. **Security budget:** Fee revenue is ~1-15% of miner income. At ~7 TPS, sustaining security through fees alone requires very high per-tx fees or dramatically higher throughput.
2. **Confirmation time:** 60 minutes for secure settlement limits use in global commerce.
3. **Fee spikes:** April 2024 halving day average fee reached $91.89 (2,645% increase), pricing out ordinary users.
4. **Layer 2 trust assumptions:** Lightning Network requires watchtowers and channel management. Sidechains use federated custody. L2s do not generate L1 fee revenue.

---

## References

- Sompolinsky, Y., Wyborski, S., Zohar, A. "PHANTOM and GHOSTDAG." [ePrint 2018/104](https://eprint.iacr.org/2018/104)
- Sompolinsky, Y., Sutton, M. "The DAG KNIGHT Protocol." [ePrint 2022/1494](https://eprint.iacr.org/2022/1494)
- KIP-9 Storage Mass: [github.com/kaspanet/kips](https://github.com/kaspanet/kips/blob/master/kip-0009.md)
- Kaspa tokenomics: [kaspa.org](https://kaspa.org/tokenomics-emission-and-mining/)
- Bitcoin fee data: [BitInfoCharts](https://www.bitinfocharts.com/bitcoin/)
- Lyn Alden security modeling: [lynalden.com](https://www.lynalden.com/bitcoin-security-modeling/)
