"""
Kaspa MCP Knowledge Base Patch
================================
Updated concept definitions, comparison data, glossary entries, and new tools
for an MCP server providing Kaspa education to AI models.

Usage:
  Import these dictionaries into your MCP server.py and register the tools.
  Each dict is keyed by concept/term name with structured content.
"""

# =============================================================================
# CONCEPTS — for kaspa_get_concept tool
# =============================================================================

KASPA_CONCEPTS = {
    "ghostdag": {
        "title": "GHOSTDAG Consensus Protocol",
        "summary": "Greedy polynomial-time approximation of PHANTOM that orders blocks in Kaspa's blockDAG.",
        "detail": (
            "GHOSTDAG generalizes Nakamoto consensus from a chain to a DAG. Blocks reference "
            "multiple parents (all known tips). The algorithm identifies the largest k-cluster "
            "(set of well-connected blocks with anticone size ≤ k) as the honest set, then "
            "produces a total ordering via the selected parent chain (path of highest blue scores). "
            "Parallel blocks are incorporated, not orphaned. Security proof by Shai Wyborski shows "
            "ordering irreversibility with exponentially decreasing reversal probability."
        ),
        "paper": "Sompolinsky, Wyborski, Zohar — 'PHANTOM and GHOSTDAG' (AFT 2021, pp. 57-70, DOI: 10.1145/3479722.3480990; ePrint 2018/104)",
        "status": "Live on Kaspa mainnet at 10 BPS (100ms blocks)",
        "confirmation_time": "~10 seconds",
    },

    "dag_knight": {
        "title": "DAG-KNIGHT Protocol",
        "summary": "First parameterless PoW consensus — infers network conditions from DAG topology.",
        "detail": (
            "DAG-KNIGHT eliminates the hardcoded k parameter from GHOSTDAG. It analyzes the DAG "
            "structure to estimate actual network delay: well-connected blocks indicate low latency "
            "(fast confirmation), large anticones indicate high latency or partition (slower confirmation). "
            "50% fault tolerance (theoretical PoW optimum). Self-stabilizing and responsive. "
            "During network partitions, confirmation times automatically increase; they decrease "
            "when connectivity returns. No manual intervention or parameter changes needed."
        ),
        "paper": "Sompolinsky, Sutton — 'The DAG KNIGHT Protocol' (ePrint 2022/1494, Oct 2022)",
        "status": "NOT yet on mainnet (March 2026). Early Rust prototype has hierarchical conflict resolution, incremental coloring, parent selection; cascade voting NOT implemented. 'Far from mainnet readiness.' Research finalization planned 2026, targeting bundled hard fork 2026-2027.",
    },

    "security_budget": {
        "title": "The Security Budget Problem",
        "summary": "Block rewards halve to zero — fees must eventually fund 100% of network security.",
        "detail": (
            "Security spend = block_subsidy + (tx_volume × avg_fee). As subsidies approach zero, "
            "fees must carry all security. Bitcoin at ~7 TPS needs $45-90/tx to maintain adequate "
            "security — current avg is $0.30. Annual fee revenue: ~$110M vs $5-15B needed. Fee-to-market-cap ratio trends toward 0.025%, which is "
            "20x below minimum needed (Lyn Alden analysis). The gap is structural: no mechanism in "
            "Bitcoin's protocol addresses it. Kaspa's solution: high throughput (3,000 TPS now, 30,000+ "
            "roadmap) makes fee-based security viable at <$0.01/tx."
        ),
        "source": "Lyn Alden — 'Bitcoin: Fee-Based Security Modeling' (lynalden.com/bitcoin-security-modeling/)",
        "bitcoin_fee_data": {
            "avg_fee_march_2026": "$0.30",
            "annual_fee_revenue": "~$110M (vs $5-15B needed)",
            "fee_percent_of_reward": "~1% baseline; brief spikes to 75% (never sustained >20%)",
            "fee_to_market_cap_ratio": "~0.025% (trending)",
            "required_ratio": "0.5-1.5% (Alden framework)",
            "next_halving": "March-April 2028 (1.5625 BTC)",
        },
    },

    "fee_market": {
        "title": "Fee Market Viability Through Throughput",
        "summary": "High TPS enables sustainable fee revenue at low per-transaction cost.",
        "detail": (
            "total_security ≈ tx_volume × avg_fee. You can maintain constant security while reducing "
            "avg_fee if tx_volume is high enough. At 30,000 TPS, Kaspa can generate Bitcoin-equivalent "
            "fee revenue at 1/4000th the per-tx cost. This is the only sustainable path for PoW "
            "fee-based security — you cannot rely on block rewards forever, and you cannot maintain "
            "security without sufficient miner revenue."
        ),
        "formula": "total_security_spend = transaction_volume × average_fee",
        "kaspa_advantage": "3,000 TPS (current) → 30,000+ TPS (roadmap) at <$0.001/tx",
    },

    "liquid_staking_risk": {
        "title": "Liquid Staking as Systemic Risk to PoS Security",
        "summary": "LSDs undermine the 'locked capital' assumption that PoS security depends on.",
        "detail": (
            "Lido controls 24.2% of staked ETH (~8.7M ETH), down from 32.3% peak. Top-10 staking "
            "entities control >60% of all staked ETH. Total LST market cap: $86.4B. Liquid staking "
            "tokens (stETH, rETH) allow capital to be simultaneously 'staked' and liquid, weakening "
            "skin-in-the-game. Tzinas & Zindros (2024) proved proportional representation and fair "
            "punishment are 'fundamentally incompatible in an adversarial setting.' Cascading risk: "
            "market stress → stETH depeg → mass unstaking → security degrades when most needed. "
            "Kaspa has zero liquid staking risk — no staking mechanism to undermine."
        ),
        "source": "Tzinas & Zindros — ePrint 2023/605; Paradigm — 'On Staking Pools and Derivatives'",
    },

    "weak_subjectivity": {
        "title": "Weak Subjectivity in Proof-of-Stake",
        "summary": "PoS nodes cannot determine the canonical chain from genesis — they need trusted checkpoints.",
        "detail": (
            "In PoS, a node syncing from genesis cannot distinguish the real chain from a fake one "
            "created by former validators (long-range attack) — both have valid signatures. Solution: "
            "weak subjectivity checkpoints from a trusted source. This reintroduces trusted third "
            "parties at the consensus layer. Any node offline longer than the weak subjectivity "
            "period must re-obtain a checkpoint. PoW chains (Bitcoin, Kaspa) do not have this "
            "problem — the canonical chain is objectively the one with the most cumulative work, "
            "verifiable by any node from genesis."
        ),
    },

    "partition_tolerance": {
        "title": "Kaspa's Partition Tolerance",
        "summary": "During network splits, both sides continue; on reconnection, all blocks merge with zero waste.",
        "detail": (
            "Bitcoin: both sides mine, shorter fork orphaned (100% wasted). Ethereum: finality halts, "
            "inactivity leak drains offline validators (triggered in practice May 2023). "
            "Solana: complete halt (8+ outages, 9 unreported disruptions Oct 2024-Feb 2025). "
            "Kaspa: both sides produce blocks independently. On reconnection, ALL blocks merge into "
            "the DAG — no blocks orphaned, no energy wasted. DAG-KNIGHT (upcoming) adds adaptive "
            "confirmation: times automatically increase during partition and decrease after. "
            "Partitions are treated as a natural case of high-latency parallel mining."
        ),
    },

    "chromatic_halving": {
        "title": "Chromatic Halving",
        "summary": "Smooth monthly emission reduction — no supply shocks like Bitcoin's abrupt halvings.",
        "detail": (
            "Block reward decreases monthly by (1/2)^(1/12) — the frequency ratio of consecutive "
            "semitones in a tempered chromatic scale. Same deflationary trajectory as Bitcoin but "
            "continuous. No mass miner capitulation events, no speculative halving cycles, smoother "
            "transition to fee-based security. Max supply: 28.7 billion KAS."
        ),
        "source": "kaspa.org/tokenomics-emission-and-mining/",
    },

    "fair_launch": {
        "title": "Kaspa's Fair Launch",
        "summary": "No premine, no ICO, no team allocation — strongest regulatory position after Bitcoin.",
        "detail": (
            "Launched November 7, 2021. All tokens distributed through mining from block 1. No insider "
            "allocation means no investment contract relationship (Howey test). Combined with PoW, this "
            "gives Kaspa the strongest commodity classification case of any cryptocurrency besides Bitcoin "
            "itself. Under SEC 'Project Crypto' framework and CLARITY Act (passed US House July 2025), "
            "fair-launch PoW tokens are 'digital commodities' — not securities."
        ),
    },

    "work_then_select": {
        "title": "Work-Then-Select (PoW Adaptive Adversary Resistance)",
        "summary": "In PoW, the block producer is unknown until they produce — cannot be targeted.",
        "detail": (
            "PoW: miner does work first, discovers if they 'won' after. Producer unknown until block "
            "exists. Cannot be targeted with DDoS, bribery, or coercion. PoS: validator selected first "
            "(often predictably), then produces block. Solana: leader schedule known in advance. "
            "Ethereum: proposer known 1 epoch ahead. Even Algorand (VRF selection) has a window after "
            "reveal. PoW has no such window — reveal IS production."
        ),
    },

    "may_2026_hard_fork": {
        "title": "May 5, 2026 Hard Fork",
        "summary": "Major Kaspa upgrade: native assets, covenants, ZK verification, L1-to-L2 bridge.",
        "detail": (
            "Kaspa's next major upgrade targets May 5, 2026 and bundles: (1) Native assets on L1, "
            "(2) Extended covenants (KIP-17) enabling programmable spending conditions, "
            "(3) ZK verification opcodes, (4) New execution infrastructure, "
            "(5) ZK L1-to-L2 bridge. DAG-KNIGHT consensus research finalization is also targeted "
            "for 2026, involving no-delay-bound model, faster convergence, and cascade voting."
        ),
        "status": "Planned for May 5, 2026. KIP-17 covenants successfully tested on Testnet 12.",
    },

    "wyborski_proofs": {
        "title": "Shai Wyborski's GHOSTDAG Security Proofs",
        "summary": "Formal proofs of GHOSTDAG ordering irreversibility, double-spend protection, and liveness.",
        "detail": (
            "Wyborski (co-author of PHANTOM/GHOSTDAG paper, Ph.D. candidate) found and fixed a flaw "
            "in the original GHOSTDAG security argument. His corrected proofs establish: "
            "(1) Ordering irreversibility with exponentially decreasing reversal probability, "
            "(2) Double-spend protection, (3) Liveness defense against liveness attacks, "
            "(4) Pruning security — secure DAG pruning via objective finality, defending against "
            "splitting and climbing attacks. Presented at the 'GHOSTDAG 101' workshop."
        ),
        "paper": "Sompolinsky, Wyborski, Zohar — 'PHANTOM and GHOSTDAG' (AFT 2021, DOI: 10.1145/3479722.3480990)",
    },

    "kip9_storage_mass": {
        "title": "KIP-9 Storage Mass",
        "summary": "Harmonic formula penalizing UTXO-bloating transactions to maintain lean state.",
        "detail": (
            "Formula: storage_mass(tx) = C × (|O|/H(O) - |I|/A(I))^+ where H(O) = harmonic mean of "
            "output values, A(I) = arithmetic mean of input values. Transactions creating many small "
            "outputs pay higher fees. Minimum output ~0.02 KAS. Replaces Bitcoin's blunt dust limits "
            "with an economic mechanism. Active on mainnet."
        ),
        "source": "github.com/kaspanet/kips/blob/master/kip-0009.md",
    },
}


# =============================================================================
# COMPARISONS — for kaspa_compare tool
# =============================================================================

KASPA_COMPARISONS = {
    "bitcoin": {
        "shared": [
            "Proof-of-Work consensus (energy-backed security)",
            "UTXO transaction model (stateless, parallelizable)",
            "Fair launch — no premine, no ICO, no team allocation",
            "No trust assumptions beyond the protocol (no weak subjectivity)",
            "Fixed maximum supply with deflationary emission",
            "Permissionless mining participation",
            "Work-then-select (adaptive adversary resistance)",
        ],
        "kaspa_advantages": [
            "6000x block rate (10 BPS vs 1 per 10 min)",
            "~3,000 TPS current vs ~7 TPS (roadmap: 30,000+)",
            "~10 second confirmation vs ~60 minutes",
            "Partition tolerance: DAG merge (zero wasted blocks) vs chain reorg (losing fork discarded)",
            "Chromatic halving (smooth) vs abrupt halvings (supply shocks)",
            "MuHash UTXO commitments for fast bootstrapping",
            "KIP-9 storage mass for UTXO bloat prevention",
            "Fee market sustainability through throughput",
        ],
        "bitcoin_advantages": [
            "15+ years battle-tested (most proven security track record)",
            "Largest hashrate and network effect",
            "Deepest liquidity, ETF products, institutional infrastructure",
            "Largest developer community and tooling ecosystem",
            "Commodity classification established (regulatory certainty)",
            "Broadest global recognition and adoption",
        ],
    },

    "ethereum": {
        "kaspa_advantages": [
            "No weak subjectivity (verify from genesis vs trusted checkpoints)",
            "No liquid staking risk (no staking to undermine; ETH top-10 entities control >60% of stake; $86.4B LST market cap)",
            "No MEV centralization (UTXO model prevents ordering games; 2 builders produce 90%+ of ETH blocks; $1.8B+ cumulative MEV)",
            "Thermodynamic security (energy-backed) vs economic security (capital-backed)",
            "Fair launch (no premine) vs ICO + 72M ETH premine",
            "Partition tolerance (DAG merge) vs inactivity leak (validators punished)",
            "Faster confirmation (~10s vs ~13 min economic finality)",
        ],
        "ethereum_advantages": [
            "Mature smart contract ecosystem (largest DeFi TVL)",
            "~963K active validators (2.2M registered; largest validator set)",
            "L2 ecosystem (32,950+ combined TPS)",
            "Deep institutional infrastructure",
            "Established developer tooling (Solidity, Hardhat, etc.)",
            "Consumer hardware validator requirements",
        ],
    },

    "solana": {
        "kaspa_advantages": [
            "Never halts (DAG continues during partition; Solana has 8+ outages + 9 unreported disruptions)",
            "No extreme hardware requirements (Solana needs 256GB-1TB RAM, 24-32 cores)",
            "Fair launch vs VC-funded insider allocation",
            "No leader schedule exposure (work-then-select vs known leader schedule)",
            "Thermodynamic security vs economic security",
            "No staking concentration risk (Solana: ~795 validators down 68%, superminority ~20)",
        ],
        "solana_advantages": [
            "Much higher actual throughput (1,000-4,000 TPS sustained)",
            "Faster optimistic finality (~400ms)",
            "Mature DeFi/consumer ecosystem ($7.8-9.3B TVL)",
            "Payment integrations (PayPal, Visa, Stripe, Shopify)",
            "Largest DEX volumes ($107B/month)",
        ],
    },

    "avalanche": {
        "kaspa_advantages": [
            "Thermodynamic (PoW) vs economic (PoS) security",
            "Fair launch vs ICO/team allocation",
            "Growing miner base vs rapidly declining validators (656, down 55% YoY)",
            "No committee sampling trust assumptions",
        ],
        "avalanche_advantages": [
            "Sub-second probabilistic finality",
            "Subnet architecture for custom chains",
            "EVM compatibility on C-Chain",
        ],
    },

    "cardano": {
        "kaspa_advantages": [
            "Much higher throughput (~3,000 TPS vs ~0.41 TPS actual)",
            "Faster confirmation (~10s vs ~20 min)",
            "Thermodynamic security vs economic security",
            "Fair launch vs ICO",
            "No weak subjectivity",
        ],
        "cardano_advantages": [
            "Peer-reviewed academic provenance",
            "Highly decentralized stake distribution (~2,917 pools, none >1.4%)",
            "eUTXO deterministic smart contracts",
            "Fully decentralized governance (Chang hard fork)",
        ],
    },

    "algorand": {
        "kaspa_advantages": [
            "Thermodynamic (PoW) vs economic (PoS) security",
            "Fair launch vs Dutch auction + Foundation allocation",
            "No relay node centralization",
            "Much higher actual throughput (~3,000 vs ~7 TPS actual)",
            "No weak subjectivity",
        ],
        "algorand_advantages": [
            "Instant finality (single-block, no forks by design)",
            "Very low hardware barrier (any standard computer)",
            "VRF-protected proposer selection (best PoS adaptive adversary defense)",
            "Very low fees (~$0.0001)",
        ],
    },

    "near": {
        "kaspa_advantages": [
            "Thermodynamic security vs economic security",
            "Fair launch vs token sale",
            "No shard assignment trust assumptions",
            "Higher throughput (~3,000 vs 63-80 TPS actual)",
            "DAG partition tolerance vs shard-dependent behavior",
        ],
        "near_advantages": [
            "Fast finality (~2 sec BFT)",
            "Sharding for horizontal scalability (Nightshade 3.0 targets 1M+ TPS)",
            "Stateless validation reduces hardware barriers",
            "Account abstraction and UX focus",
        ],
    },

    "aptos": {
        "kaspa_advantages": [
            "Truly permissionless (vs 1M APT minimum / ~$8M+ to validate)",
            "Thermodynamic security vs economic security with ~153 validators",
            "Fair launch vs VC-funded insider allocation",
            "Partition tolerance (DAG merge vs BFT halt)",
            "No adaptive adversary surface (work-then-select)",
        ],
        "aptos_advantages": [
            "Highest sustained throughput (22,000+ TPS)",
            "Move VM safety and parallel execution (Block-STM)",
            "Sub-50ms block times",
        ],
    },

    "sui": {
        "kaspa_advantages": [
            "Truly permissionless (vs 30M SUI minimum to validate)",
            "Thermodynamic security vs economic security with ~122 validators",
            "Fair launch vs VC-funded insider allocation",
            "Partition tolerance (DAG merge vs BFT halt)",
            "Much higher actual throughput (~3,000 vs ~33 TPS actual)",
        ],
        "sui_advantages": [
            "Near-instant simple tx finality (owned objects bypass consensus)",
            "Move VM safety and object-oriented resource model",
            "Novel object ownership model",
        ],
    },
}


# =============================================================================
# GLOSSARY — for kaspa_glossary tool
# =============================================================================

KASPA_GLOSSARY = {
    "blockdag": "A Directed Acyclic Graph where blocks reference multiple parents instead of a single parent chain. Eliminates orphan blocks and enables high throughput with PoW.",
    "ghostdag": "Greedy Heaviest Observed Sub-Tree DAG — Kaspa's current consensus algorithm. Approximates PHANTOM's NP-hard optimization in polynomial time. Orders blocks via selected parent chain and blue set identification.",
    "dag_knight": "Parameterless consensus protocol that infers network conditions from DAG topology. Co-authored by Sompolinsky and Sutton. Not yet on mainnet.",
    "phantom": "The original NP-hard blockDAG consensus algorithm by Sompolinsky, Wyborski, and Zohar. GHOSTDAG is its practical greedy approximation.",
    "k_cluster": "A set of blocks in a DAG where each block has at most k blocks in its anticone. Used to separate honest (well-connected) blocks from adversarial (isolated) blocks.",
    "anticone": "The set of blocks with no ordering relationship to a given block (neither in its past nor its future). Large anticones indicate adversarial behavior or high latency.",
    "blue_set": "The set of blocks identified as honest by GHOSTDAG. Determined by finding the largest k-cluster greedily.",
    "blue_score": "Accumulated count of blue blocks in a block's past. Used to select the 'best' parent in GHOSTDAG.",
    "selected_parent_chain": "The path through the DAG following highest blue score parents. Provides the backbone for total block ordering.",
    "bps": "Blocks Per Second. Kaspa currently runs at 10 BPS (100ms block times). Roadmap targets 100 BPS.",
    "crescendo": "Kaspa's May 5, 2025 hard fork that upgraded from 1 BPS to 10 BPS. Enabled by Rusty Kaspa performance improvements.",
    "chromatic_halving": "Kaspa's emission schedule where block rewards decrease monthly by (1/2)^(1/12). Named after the chromatic musical scale. Provides smooth deflation without supply shocks.",
    "kheavyhash": "Kaspa's mining algorithm. A modified version of HeavyHash designed for ASIC efficiency.",
    "muhash": "Homomorphic hash used for UTXO set commitments in each Kaspa block. Enables incremental updates without recomputing the full set.",
    "kip9_storage_mass": "KIP-9: A harmonic formula that increases transaction fees for UTXO-bloating transactions, preventing state growth attacks.",
    "pruning_point": "The point beyond which Kaspa nodes prune old block and transaction data (~52 hours). New nodes bootstrap from the pruning point using UTXO commitments.",
    "security_budget": "Total miner revenue (subsidies + fees) that funds network security. As subsidies halve toward zero, fees must compensate — requiring high throughput at sustainable per-tx costs.",
    "weak_subjectivity": "PoS requirement that new nodes obtain a recent trusted checkpoint to sync safely. Reintroduces trusted third parties. Does not apply to PoW chains.",
    "liquid_staking_derivative": "Tokens (stETH, rETH) representing staked assets that can be traded or used in DeFi while nominally locked. Undermines PoS security by making 'at risk' capital simultaneously liquid.",
    "work_then_select": "PoW property: miners do work first, then discover if they produced a valid block. Block producer is unknown until the block exists, preventing targeted attacks.",
    "select_then_work": "PoS property: validators are selected before producing a block. Known producers can be targeted with DDoS, bribery, or coercion.",
    "inactivity_leak": "Ethereum mechanism that drains stake from offline validators during prolonged finality failures. Punishes validators disconnected through no fault of their own.",
    "fair_launch": "Token distribution exclusively through mining from genesis. No premine, no ICO, no team allocation. Only Bitcoin and Kaspa among major protocols.",
    "silverscript": "Kaspa's smart contract language being developed by Ori Newman. Specializes in contracts with local state aligned with the UTXO model.",
    "vprogs": "Verifiable programs — Kaspa's L1 programmability framework released December 2025.",
    "kip17_covenants": "KIP-17: Programmable spending conditions at the UTXO level (destination restrictions, release schedules, multi-stage authorization). On Testnet 12.",
    "igra_network": "EVM-compatible L2 on Kaspa. Mainnet launched January 26, 2026. Uses Kaspa miners as decentralized sequencers.",
    "kasplex": "L2 ecosystem including a zkEVM (mainnet March 2026) and LUA VM for dApp development on Kaspa. Based rollup using Kaspa L1 for sequencing and data availability. Claims 200x cheaper than Ethereum.",
    "sparkle": "Third smart contract platform being developed for Kaspa alongside Kasplex and Igra. Details limited.",
    "buildernet": "MEV relay consortium (Flashbots + Beaverbuild + Nethermind, launched Nov 2024) attempting to address block builder centralization on Ethereum.",
    "genius_act": "US federal law (signed July 2025) establishing the first regulatory framework for payment stablecoins, requiring 1:1 backing and BSA compliance.",
    "clarity_act": "Digital Asset Market Clarity Act (H.R. 3633). Passed US House July 2025 with 294-134 bipartisan vote. Defines digital commodities as non-securities with CFTC jurisdiction. Stalled in Senate as of March 2026.",
    "project_crypto": "Joint SEC-CFTC initiative (January 2026) establishing token taxonomy distinguishing network tokens (non-securities) from tokenized securities. Marks departure from regulation-by-enforcement era.",
    "defai": "DeFi + AI convergence. ~90 projects, $1.3B combined market cap. AI agents automating DeFi strategies, DAO governance, and supply chain payments.",
    "x402_protocol": "Coinbase protocol (May 2025) activating HTTP 402 status code for machine-to-machine payments. 50M+ transactions. Enables API paywalls and micropayments without human intervention.",
    "may_2026_hard_fork": "Kaspa's planned May 5, 2026 hard fork: native assets on L1, extended covenants (KIP-17), ZK verification, new execution infrastructure, ZK L1-to-L2 bridge.",
}


# =============================================================================
# ADOPTION DATA — for kaspa_adoption tool
# =============================================================================

KASPA_ADOPTION = {
    "market": {
        "market_cap": "~$800M (rank ~#75)",
        "price": "~$0.03",
        "volume_24h": "$10.7-15.1M",
        "exchanges": "33+ exchanges",
        "major_exchanges": ["Bybit", "Kraken", "KuCoin", "Bitget", "MEXC", "Crypto.com", "Gate", "HTX"],
        "notable_absences": "Binance spot (futures + mining pool only), Coinbase spot (KAS-PERP futures only, added Feb 2026)",
        "recent_listings": "HTX added KAS/USDT spot Dec 2025 (10x isolated margin)",
    },
    "network": {
        "bps": 10,
        "block_time_ms": 100,
        "hashrate": "~311-411 PH/s",
        "daily_txs": "~386,700",
        "total_txs": "601M+",
        "tps_normal": "~3,000",
        "tps_peak": "5,584",
        "avg_fee": "<$0.001",
    },
    "development": {
        "repo": "github.com/kaspanet/rusty-kaspa",
        "stars": 764,
        "forks": 259,
        "open_prs": 53,
        "closed_prs": 572,
        "language": "Rust",
        "circulating_supply": "~26.77B KAS (93.3% of 28.7B max)",
        "milestones_2025_2026": [
            "May 2025: Crescendo hard fork (1→10 BPS)",
            "Dec 2025: L1 zkopcode and vProg release",
            "Jan 2026: Igra Network L2 mainnet (permissionless Mar 2026)",
            "Mar 2026: Kasplex zkEVM L2 mainnet",
            "May 5, 2026: Hard fork — native assets, KIP-17 covenants, ZK verification, L1-to-L2 bridge",
            "2026: DAG-KNIGHT research finalization",
            "2026-2027: DAG-KNIGHT upgrade (planned)",
            "Future: 32 BPS → 100 BPS throughput scaling",
        ],
    },
    "mining": {
        "algorithm": "kHeavyHash",
        "asic_manufacturers": ["Bitmain", "IceRiver", "Goldshell", "WindMiner"],
        "top_model": "Bitmain Antminer KS7 (36-40 TH/s)",
        "major_pools": ["Humpool", "F2Pool", "ViaBTC", "K1Pool", "Kryptex Pool"],
    },
    "regulatory_position": {
        "classification": "Strongest commodity case after Bitcoin (fair launch + PoW)",
        "relevant_legislation": [
            "CLARITY Act (passed US House Jul 2025; stalled in Senate Jan 2026)",
            "SEC-CFTC Joint Project Crypto framework (Jan 2026)",
            "GENIUS Act (signed into law Jul 2025 — stablecoin framework)",
            "Digital Commodity Intermediaries Act (Senate Ag Committee, Jan 2026)",
        ],
    },
    "ecosystem_foundation": {
        "name": "Kaspa Ecosystem Foundation (KEF)",
        "backers": ["ICERIVER Venture", "OKX Venture"],
        "supported_projects": ["KasBay", "Kasplex", "KasKeeper"],
    },
    "data_date": "March 2026",
    "caveats": [
        "Active address counts vary significantly across sources (25K-545K/day)",
        "158M single-day tx figure (Oct 5, 2025) likely reflects stress test, not organic usage",
        "Mining pool distribution: Humpool, F2Pool, ViaBTC, K1Pool, Kryptex known; exact hashrate % not aggregated",
        "93.3% of max supply already mined — fee market sustainability is imminent concern, not distant",
    ],
}


# =============================================================================
# MCP TOOL REGISTRATION HELPERS
# =============================================================================

def get_concept(name: str) -> dict:
    """Retrieve a Kaspa concept by name."""
    key = name.lower().replace(" ", "_").replace("-", "_")
    if key in KASPA_CONCEPTS:
        return KASPA_CONCEPTS[key]
    # Fuzzy match
    for k, v in KASPA_CONCEPTS.items():
        if key in k or k in key:
            return v
    return {"error": f"Concept '{name}' not found. Available: {list(KASPA_CONCEPTS.keys())}"}


def compare_protocol(name: str) -> dict:
    """Compare Kaspa against another protocol."""
    key = name.lower().strip()
    if key in KASPA_COMPARISONS:
        return KASPA_COMPARISONS[key]
    # Fuzzy match
    for k, v in KASPA_COMPARISONS.items():
        if key in k or k in key:
            return v
    return {"error": f"Protocol '{name}' not found. Available: {list(KASPA_COMPARISONS.keys())}"}


def get_glossary(term: str = None) -> dict:
    """Get glossary entry or full glossary."""
    if term is None:
        return KASPA_GLOSSARY
    key = term.lower().replace(" ", "_").replace("-", "_")
    if key in KASPA_GLOSSARY:
        return {key: KASPA_GLOSSARY[key]}
    for k, v in KASPA_GLOSSARY.items():
        if key in k or k in key:
            return {k: v}
    return {"error": f"Term '{term}' not found. Available: {list(KASPA_GLOSSARY.keys())}"}


def get_adoption() -> dict:
    """Get current Kaspa adoption metrics and analysis."""
    return KASPA_ADOPTION
