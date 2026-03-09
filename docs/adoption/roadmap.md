# Kaspa Development Roadmap

> **Last updated:** March 2026. Dates for future milestones are estimates and subject to change.

## Overview

Kaspa's development roadmap is focused on scaling throughput, adding base-layer programmability, and enabling a smart contract ecosystem -- all while preserving the PoW security model and UTXO architecture that define the protocol.

Development is led by a core group of researchers and engineers, including Yonatan Sompolinsky (PHANTOM/GHOSTDAG/DAG-KNIGHT author), Michael Sutton (Rusty Kaspa lead), Ori Newman, and Shai Wyborski.

## Timeline

| Date | Milestone | Status |
|---|---|---|
| May 5, 2025 | **Crescendo hard fork** -- 1 to 10 BPS | Completed |
| Dec 2025 | **L1 vProgs / zkopcodes** | Completed |
| Testnet 12 | **KIP-17 covenants** | In testing |
| Jan 2026 | **Igra Network L2** mainnet | Live |
| Mar 2026 | **Kasplex zkEVM L2** mainnet | Live |
| Q1-Q2 2026 | **Covenants++ hard fork** | Upcoming |
| 2026-2027 | **DAG-KNIGHT consensus upgrade** | In development |

## Completed Milestones

### Crescendo Hard Fork (May 5, 2025)

The Crescendo upgrade increased Kaspa's block rate from 1 BPS to **10 BPS**, reducing block time to 100ms. This was a coordinated hard fork that required consensus across the mining network.

**Impact:**
- Baseline throughput increased to ~60 TPS (with stress test peaks of 3,000-5,500 TPS).
- Reduced reward variance for miners, structurally reducing pool centralization incentives.
- Demonstrated the community's ability to execute a major consensus change.

See [current network metrics](./metrics.md) for live performance data.

### L1 vProgs and zkopcodes (December 2025)

The release of **virtual programs (vProgs)** and **zero-knowledge opcodes (zkopcodes)** on L1 introduced base-layer programmability to Kaspa for the first time. This enables ZK proof verification directly on the main chain, which is a prerequisite for trustless L2 bridges and advanced covenant logic.

### KIP-17 Covenants (Testnet 12)

KIP-17 introduces **covenants** -- constraints on how UTXOs can be spent -- to the Kaspa base layer. Covenants enable:

- Vaults with time-locked spending conditions
- On-chain escrow without trusted third parties
- Building blocks for more advanced smart contract patterns

Currently live on Testnet 12 and expected to be included in the Covenants++ hard fork.

## Live L2 Networks

### Igra Network (January 2026)

Igra is an **EVM-compatible L2** built on Kaspa, providing a smart contract execution environment while settling to the Kaspa L1 for security. It launched on mainnet in January 2026.

### Kasplex zkEVM L2 (March 2026)

Kasplex launched a **zkEVM-based L2** on mainnet in March 2026, offering a second smart contract platform with ZK rollup architecture. The zkEVM approach allows existing Solidity developers to deploy contracts on Kaspa's L2 with minimal code changes.

> **Note:** Both L2s are newly launched. DeFi ecosystem development is in its earliest stages. See [adoption challenges](./metrics.md#known-data-gaps) for an honest assessment of the current state.

## Upcoming

### Covenants++ Hard Fork (Q1-Q2 2026)

The next consensus upgrade extends the base-layer covenant system with:

- **Extended covenant primitives** -- richer spending conditions and composable constraints.
- **ZK proof verifier on L1** -- enables trustless verification of L2 state transitions directly on the base layer.

This hard fork is the foundation for Kaspa's long-term programmability strategy: keep the L1 lean and secure, but give it enough verification capability to anchor L2 execution trustlessly.

### DAG-KNIGHT Consensus Upgrade (2026-2027)

DAG-KNIGHT is a **parameterless consensus protocol** authored by Yonatan Sompolinsky. It replaces the current GHOSTDAG protocol with one that:

- Adapts automatically to network conditions without preset parameters.
- Provides stronger confirmation guarantees under adversarial conditions.
- Represents the next generation of BlockDAG consensus theory.

This is the most significant long-term protocol upgrade on the roadmap.

## Key Contributors

| Person | Role |
|---|---|
| Yonatan Sompolinsky | PHANTOM, GHOSTDAG, and DAG-KNIGHT protocol author |
| Michael Sutton | Rusty Kaspa lead developer |
| Ori Newman | Core developer |
| Shai Wyborski | Core developer and researcher |

> **Data gap:** Exact contributor count and external developer ecosystem size are not available from public sources. The [rusty-kaspa repository](https://github.com/kaspanet/rusty-kaspa) (764 stars, 259 forks) is the primary codebase.

## Sources

- [kaspa.org/developments](https://kaspa.org/developments/)
- [GitHub -- kaspanet/rusty-kaspa](https://github.com/kaspanet/rusty-kaspa)
- [Kaspa On-Chain Metrics](./metrics.md) -- current network performance
- [Regulatory Position](./regulatory.md) -- fair launch and commodity classification
