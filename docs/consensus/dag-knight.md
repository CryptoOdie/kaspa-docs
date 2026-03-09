# DAG-KNIGHT: Parameterless Consensus

## Overview

DAG-KNIGHT is the **first permissionless proof-of-work protocol with no a priori bound on network latency**. It eliminates the static k parameter from [GHOSTDAG](ghostdag.md), instead inferring network conditions directly from the DAG topology.

**Paper:** "The DAG KNIGHT Protocol: A Parameterless Generalization of Nakamoto Consensus"
**Authors:** Yonatan Sompolinsky, Michael Sutton
**Published:** October 31, 2022 (Bitcoin whitepaper's 14th anniversary)
**ePrint:** [2022/1494](https://eprint.iacr.org/2022/1494)
**Affiliation:** Harvard CRCS (Center for Research on Computation and Society)

## What "Parameterless" Means

An ordering rule is **parameterless** if its only input is a block DAG with valid proof-of-work. No latency assumptions, no pre-configured constants about network conditions.

GHOSTDAG requires parameter k to be set before deployment as a conservative upper bound on propagation delay. This creates a tradeoff:
- k too low → security degrades under high latency
- k too high → unnecessarily slow confirmations under low latency

DAG-KNIGHT removes this tradeoff entirely.

## How It Infers Network Conditions

DAG-KNIGHT reads the network's state from the DAG structure itself:

1. **Low latency** → blocks are well-connected (small anticones) → DAG is tightly structured → orderings converge quickly → **fast confirmation**

2. **High latency / partition** → blocks have large anticones → DAG reveals disconnection → protocol requires more depth for confirmation → **slower but secure confirmation**

3. **Partition heals** → DAG connectivity improves → confirmation times automatically decrease

The protocol examines k-clusters sampled from the DAG, selects a cluster covering 50% of hashrate with the most conservative delay estimate, and adapts confirmation accordingly.

## Formal Properties

| Property | Guarantee |
|----------|-----------|
| Fault tolerance | 50% of hashrate (theoretical PoW optimum) |
| Responsiveness | Confirmation adapts to actual conditions, not worst-case |
| Self-stabilizing | Recovers automatically from adverse conditions |
| Scalability | Supports arbitrarily high block rates (bounded by node capacity) |
| Input | Only the DAG + valid PoW (no external parameters) |

## Partition Behavior

During a network partition:
- Both sides continue producing blocks independently
- The DAG topology reveals the partition (large anticones between segments)
- Confirmation times automatically increase to maintain security

After reconnection:
- All blocks from both sides merge into the DAG
- The protocol detects improved connectivity
- Confirmation times automatically decrease to normal

No manual intervention. No parameter changes. No validator coordination.

## Deployment Status

> **DAG-KNIGHT is not yet deployed on Kaspa mainnet** (as of March 2026).

- An early Rust implementation exists with core components (hierarchical conflict resolution, incremental coloring, parent selection)
- Cascade voting is not yet implemented
- Planned as part of a bundled hard fork targeting 2026-2027
- Will be deployed alongside ZK bridge integration

## Comparison: GHOSTDAG vs DAG-KNIGHT

| Property | GHOSTDAG | DAG-KNIGHT |
|----------|----------|------------|
| Parameter k | Required (static) | None (inferred) |
| Adapts to latency changes | No | Yes |
| Confirmation under low latency | Fixed (conservative) | Fast (responsive) |
| Confirmation under high latency | Fixed | Slower (secure) |
| Partition handling | Merge, fixed confirmation | Merge, adaptive confirmation |
| Status | Live on mainnet | In development |

## References

- Sompolinsky, Y., Sutton, M. "The DAG KNIGHT Protocol: A Parameterless Generalization of Nakamoto Consensus." [ePrint 2022/1494](https://eprint.iacr.org/2022/1494)
- Harvard CRCS: [DAG-KNIGHT publication page](https://projects.iq.harvard.edu/applied-cryptography-society/publications/he-dag-knight-protocol-parameterless-generalization)
- Kaspa documentation: [kaspa.org](https://kaspa.org/the-dag-knight-protocol-elevating-kaspa/)
