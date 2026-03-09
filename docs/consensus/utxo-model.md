# Kaspa's UTXO Model & KIP-9 Storage Mass

## UTXO Model

Kaspa uses the **Unspent Transaction Output (UTXO)** model — the same transaction model as Bitcoin. Transactions consume existing UTXOs and create new ones.

### Properties

- **Stateless:** Transaction validity depends only on the inputs being unspent and properly signed — not on any global state
- **Deterministic:** Transaction outcomes can be predicted before execution
- **Naturally parallel:** Non-conflicting transactions (spending different UTXOs) can be processed simultaneously
- **No global state contention:** Unlike account-model chains (Ethereum), there is no shared state that creates bottlenecks

### Extensions Beyond Bitcoin

Kaspa extends Bitcoin's UTXO model with several innovations:

#### UTXO Commitments (MuHash)

Each Kaspa block contains a cryptographic commitment to the **entire UTXO set state** using MuHash — a homomorphic hash function that allows incremental updates without recomputing the full set.

**Why this matters:**
- New nodes can bootstrap from a recent **pruning point** rather than replaying all historical transactions
- The UTXO commitment proves the state is correct without trusting the source
- Enables Kaspa's aggressive pruning strategy

#### Aggressive Pruning

Kaspa nodes prune old block and transaction data after approximately **52 hours**. Full pruned nodes keep:
- All past block headers
- The complete current UTXO set
- A compact "proof of proof-of-work" summary

The proof-of-proof-of-work grows so slowly it would take **10,000+ years to reach 100MB**.

This means running a full Kaspa node requires far less storage than Bitcoin (~500+ GB full blockchain) while maintaining equivalent security guarantees through the UTXO commitment chain.

#### Conflict Resolution in a DAG

In Bitcoin, UTXO conflicts (double-spends) are prevented by the linear chain — only one block can reference a given UTXO. In Kaspa's DAG, parallel blocks **can** contain conflicting transactions spending the same UTXO.

Resolution: [GHOSTDAG's](ghostdag.md) total ordering determines which transaction came first. The first in the ordering is accepted; the conflict is rejected. This is deterministic — all nodes agree.

## KIP-9: Storage Mass

**Status:** Active on Kaspa mainnet
**Specification:** [github.com/kaspanet/kips/blob/master/kip-0009.md](https://github.com/kaspanet/kips/blob/master/kip-0009.md)

### The Problem

UTXO set growth is a systemic risk for any UTXO-based chain. Transactions that create many small outputs ("dust") bloat the UTXO set, increasing memory requirements for all nodes. Bitcoin addresses this with blunt minimum relay fees and dust limits.

### The Solution: Harmonic Mass Formula

KIP-9 introduces a **storage mass** component to transaction fees based on the ratio of inputs to outputs:

```
storage_mass(tx) = C × (|O|/H(O) - |I|/A(I))⁺
```

Where:
- `|O|` = number of outputs
- `H(O)` = harmonic mean of output values
- `|I|` = number of inputs
- `A(I)` = arithmetic mean of input values
- `C` = constant
- `(x)⁺` = max(x, 0)

### How It Works

- **Transactions that fan out** (few inputs → many small outputs) pay **higher fees** — the harmonic mean of outputs is low when outputs are small, making the ratio large
- **Transactions that consolidate** (many inputs → few outputs) pay **lower fees** — they reduce the UTXO set
- **Balanced transactions** (similar input/output structure) pay moderate fees

### Key Constraints

- Outputs cannot exceed 10x the number of inputs
- Minimum output value: ~0.02 KAS
- Applied at the mempool level

### Why This Is Better Than Dust Limits

Bitcoin's dust limit is a binary threshold: below it, transactions are rejected. KIP-9 uses a **continuous economic mechanism** — creating dust is increasingly expensive rather than forbidden. This allows edge cases while making spam economically irrational.

**Co-devised by:** Yonatan Sompolinsky, Michael Sutton, and Shai Wyborski.

## References

- KIP-9 specification: [GitHub](https://github.com/kaspanet/kips/blob/master/kip-0009.md)
- Storage mass documentation: [kaspa.aspectron.org](https://kaspa.aspectron.org/transactions/fees/storage-mass.html)
- Kaspa UTXO documentation: [wiki.kaspa.org](https://wiki.kaspa.org/en/utxo)
