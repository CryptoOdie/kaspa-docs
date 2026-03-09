# Kaspa vs Ethereum

Kaspa and Ethereum represent fundamentally different approaches to blockchain design. Kaspa extends Bitcoin's PoW security model into a high-throughput [blockDAG](../consensus/ghostdag.md). Ethereum moved from PoW to PoS with The Merge (September 2022), gaining energy efficiency and economic finality while accepting a different set of trust assumptions.

This comparison documents the engineering tradeoffs on both sides.

---

## Security Model: PoW vs PoS

### Thermodynamic vs Economic Security

| Property | Kaspa (PoW) | Ethereum (PoS) |
|----------|-------------|-----------------|
| Security basis | Energy expenditure (physics) | Capital at risk (protocol rules) |
| Attack cost | Sustain 51% hashrate (electricity + hardware) | Acquire 1/3 staked ETH (~$40B+) |
| Cost recovery | Irrecoverable -- energy is spent | Partially recoverable -- capital can be withdrawn |
| Punishment | Proactive (cost during attack) | Reactive (slashing after detection) |

In PoW, the cost to attack is physically enforced by thermodynamics. In PoS, security depends on protocol rules, slashing conditions, and social consensus about handling edge cases.

### Weak Subjectivity

Kaspa nodes can verify the canonical DAG from genesis using only protocol rules and block data. No external trust is required.

Ethereum requires new nodes to obtain a **weak subjectivity checkpoint** from a trusted source. A node syncing from genesis cannot distinguish the real chain from a fake chain created by validators who have since unstaked (a long-range attack). Any node offline longer than the weak subjectivity period must re-obtain a trusted checkpoint.

This reintroduces a trusted third party at the consensus layer -- a meaningful departure from the trustless model that cryptocurrency was designed to provide.

### Adaptive Adversary Resistance

- **Kaspa (work-then-select):** A miner does computational work first, then discovers whether they produced a valid block. Block producers are unknown until the block exists. No one to target.
- **Ethereum (select-then-work):** Proposer selection is known one epoch in advance (~6.4 minutes). While less predictable than some PoS chains, it still provides an attack window for DDoS or bribery.

---

## Liquid Staking Risk

Liquid staking has become the dominant mode of Ethereum participation:

- **Lido:** ~9.8M ETH staked (~28-31% of all staked ETH), operated by only **39 node operators**
- Liquid staking derivatives (stETH, rETH) allow capital to be simultaneously "at stake" and liquid in DeFi, weakening the skin-in-the-game assumption

Research by Tzinas & Zindros (2024) formally demonstrates that proportional representation and fair punishment are fundamentally incompatible in an adversarial setting ([ePrint 2023/605](https://eprint.iacr.org/2023/605)).

**Cascading risk during market stress:** stETH depeg (as in June 2022) triggers mass withdrawal queues, shrinking the validator set and degrading security at the moment it is most needed.

Kaspa has no staking, therefore no liquid staking risk, no delegation principal-agent problems, and no derivative-driven concentration.

---

## MEV: Structural vs Minimal

Maximal Extractable Value creates structural centralizing pressure on Ethereum:

- Cumulative MEV: **$1.8B+** by mid-2025
- **82% of Ethereum blocks** go through Flashbots-affiliated relays
- Large validators form exclusive relationships with top block builders
- MEV profits compound into more stake, concentrating power

Kaspa's UTXO model inherently limits MEV exposure:

- No global state means no state-dependent ordering games
- No smart contract composability means no sandwich attacks
- Transaction outcomes are deterministic and independent of ordering

---

## Partition Behavior

| Scenario | Kaspa | Ethereum |
|----------|-------|----------|
| During partition | Both sides continue producing blocks | Finality halts if neither side has 2/3 stake; inactivity leak drains offline validators |
| After reconnection | All blocks merge into DAG, zero wasted work | Slow recovery (weeks); offline validators permanently lose stake |
| Honest participants | Not punished | Financially punished for being on the wrong side |

Ethereum's inactivity leak creates perverse incentives: geographic concentration (be near the majority), infrastructure consolidation (use the same cloud providers), and avoiding jurisdictions with unreliable internet. These push against the decentralization that partition tolerance should support.

See [partition tolerance](../architecture/partition-tolerance.md) for the full analysis.

---

## Launch and Distribution

| Property | Kaspa | Ethereum |
|----------|-------|----------|
| Launch model | Fair launch, mining only | ICO (2014) |
| Premine | None | ~72M ETH to contributors/foundation |
| Team allocation | None | Included in premine |
| Regulatory posture | Strongest commodity case | Securities scrutiny (Howey analysis) |

---

## Throughput Comparison

| Metric | Kaspa | Ethereum L1 | Ethereum L1+L2 |
|--------|-------|-------------|----------------|
| Block time | 100ms | 12s | Varies by L2 |
| Actual TPS | ~60 | 15-30 | 32,950+ |
| Max recorded | 5,584 | ~63 | -- |
| Avg fee | <$0.001 | ~$0.10 | $0.001-$0.01 |
| Finality | ~10s (probabilistic) | ~13 min (economic) | Varies |

---

## Honest Assessment: Ethereum's Advantages

| Dimension | Details |
|-----------|---------|
| Smart contract ecosystem | Largest and most mature (Solidity/Vyper), deep DeFi liquidity |
| Validator count | 1,060,000+ validators -- largest validator set of any PoS chain |
| L2 ecosystem | Multiple rollups (Arbitrum, Optimism, Base, zkSync) scaling throughput |
| Developer tooling | Most extensive tooling, documentation, and developer community |
| Institutional infrastructure | ETFs, custody solutions, established on-ramps |
| Battle-testing | 10+ years of operation (including PoW era), survived The Merge |

These are substantial advantages. Kaspa's smart contract layer (KIP-17 covenants, Igra EVM L2, Kasplex zkEVM) is still maturing. Kaspa has a smaller developer community, fewer tools, and no mature DeFi ecosystem yet.

---

## Summary: Different Tradeoffs

| Property | Kaspa | Ethereum |
|----------|-------|----------|
| Security basis | Thermodynamic (physics) | Economic (protocol rules) |
| Consensus objectivity | Full (verify from genesis) | Weak subjectivity (trusted checkpoints) |
| Participation model | Permissionless (hardware) | Plutocratic (capital-weighted) |
| Liquid staking risk | None | Systemic |
| MEV exposure | Minimal (UTXO) | Severe (account model) |
| Partition behavior | Continue + merge | Halt finality + punish offline |
| Energy cost | High | Low |
| Smart contracts | Maturing | Mature |
| Ecosystem size | Small | Large |

Every item is a tradeoff, not a flaw. Reasonable engineers can disagree about which tradeoffs are acceptable.

---

## References

- Tzinas, E. & Zindros, D. "The Principal-Agent Problem in Liquid Staking." [ePrint 2023/605](https://eprint.iacr.org/2023/605)
- Buterin, V. & Griffith, V. "Casper the Friendly Finality Gadget." [arXiv 1710.09437](https://arxiv.org/pdf/1710.09437)
- "Three Attacks on Proof-of-Stake Ethereum." [ePrint 2021/1413](https://eprint.iacr.org/2021/1413.pdf)
- Ethereum weak subjectivity: [ethereum.org](https://ethereum.org/developers/docs/consensus-mechanisms/pos/weak-subjectivity/)
- Ethereum inactivity leak: [eth2book.info](https://eth2book.info/latest/part2/incentives/inactivity/)
- Sompolinsky, Y. et al. "PHANTOM and GHOSTDAG." [ePrint 2018/104](https://eprint.iacr.org/2018/104)
