# Wikipedia Submission Guide

This guide covers the practical steps for submitting the drafted Wikipedia articles. Follow each section carefully — Wikipedia has strict policies, and failing to comply will result in rejected submissions or account blocks.

---

## 1. Account Requirements

Wikipedia restricts certain actions to **autoconfirmed** accounts. To reach autoconfirmed status, your account must be:

- At least **4 days old**
- Have at least **10 edits**

Articles for Creation (AfC) submissions require autoconfirmed status.

**Building your edit history:**

1. Create a Wikipedia account at [en.wikipedia.org/wiki/Special:CreateAccount](https://en.wikipedia.org/wiki/Special:CreateAccount).
2. Start with small, uncontroversial edits to build credibility:
   - Fix typos and grammatical errors in existing articles.
   - Add missing citations to unsourced statements.
   - Improve formatting or wikilinks in articles you know well.
   - Participate in talk page discussions on topics you understand.
3. Make your edits genuine and constructive — do not make token edits solely to reach the threshold.
4. **Do NOT create multiple accounts.** Using more than one account (known as "sockpuppeting") is a bannable offense. Wikipedia actively detects this through behavioral analysis and IP correlation.

---

## 2. Conflict of Interest (COI) Disclosure

Wikipedia has strict conflict of interest policies. Transparent disclosure is mandatory if it applies to you.

**When COI disclosure is required:**

- You hold Kaspa tokens or have a financial interest in Kaspa's success.
- You are affiliated with the Kaspa project, its development team, or related organizations.
- You have a personal relationship with article subjects (e.g., Yonatan Sompolinsky).

**How to disclose:**

Add the following statement to your **user talk page** (not your user page):

> I have a conflict of interest regarding [Kaspa/BlockDAG/Yonatan Sompolinsky]. I am [describe your relationship — e.g., "a holder of KAS tokens" or "a contributor to the Kaspa open-source project"]. I will follow Wikipedia's conflict of interest guidelines and submit articles through Articles for Creation for review.

**Rules for COI editors:**

- **Do NOT directly create articles** in mainspace. Use the AfC process instead.
- **Do NOT directly edit existing articles** about your COI subject. Instead, suggest edits on the article's talk page and let uninvolved editors implement them.
- You **can** fix clear-cut errors (broken links, typos) even in COI-related articles, but substantive changes should go through talk pages.

---

## 3. Articles for Creation (AfC) Process

AfC is the standard path for new article submissions, and the required path for COI editors.

**Step-by-step:**

1. Go to [Wikipedia:Articles for creation](https://en.wikipedia.org/wiki/Wikipedia:Articles_for_creation).
2. Click **"Submit your draft for review"** or use the AfC wizard.
3. The wizard will walk you through creating a draft in your userspace (e.g., `User:YourName/Draft:Article_Title`).
4. Paste the article content, converting from the `.wiki` draft files in this repository.
5. Preview the article to verify formatting, citations, and wikilinks render correctly.
6. Submit the draft for review.

**What reviewers evaluate:**

| Criterion | What they check |
|---|---|
| Notability | Does the subject meet Wikipedia's notability guidelines? Are there enough independent reliable sources? |
| Neutrality | Is the tone encyclopedic? Free of promotional language? |
| Reliable sources | Are citations from independent, published sources? Not just the project's own website? |
| Formatting | Proper wiki markup, categories, infoboxes, and structure? |

**Timeline and outcomes:**

- **Response time:** 1 to 8 weeks, depending on the review backlog. Do not ping reviewers or complain about wait times.
- **If accepted:** The article moves to mainspace and goes live. It may still receive cleanup tags (e.g., "needs more sources") — address these promptly.
- **If declined:** Read the decline reason carefully. The reviewer will explain what needs to change. Fix the identified issues and resubmit. Do not resubmit without making changes.

---

## 4. Submission Order (Strategic)

Submit articles in this order to build a foundation of accepted articles before tackling higher-COI subjects.

| Order | Article | Rationale |
|---|---|---|
| 1st | **GHOST protocol** | Strongest notability case. Cited in the Ethereum whitepaper. Published at Financial Cryptography 2015. Low COI concern if you are not directly affiliated with the original research. |
| 2nd | **BlockDAG** | Academic computer science concept with ACM publication history. Encyclopedic scope extends well beyond Kaspa. |
| 3rd | **PHANTOM protocol** | ACM peer-reviewed. Distinct protocol with formal CS properties (NP-hardness of block ordering). Stands on its own as a CS topic. |
| 4th | **Cryptocurrency emission schedule** | Broad-scope article covering multiple protocols. Low COI concern due to wide applicability. |
| 5th | **Fair launch (cryptocurrency)** | Broad concept article with examples from multiple projects. Low COI concern. |
| 6th | **Blockchain data management** | Comparative article covering multiple protocols and approaches. |
| 7th | **Kaspa (cryptocurrency)** | Submit after the concept articles (GHOST, BlockDAG, PHANTOM) exist so the Kaspa article can link to them. Higher COI concern — the preceding articles establish context and notability independently. |
| 8th | **Yonatan Sompolinsky** | Submit after GHOST and PHANTOM articles are accepted. Academic notability is established by those articles' existence. |

**Spacing:** Wait at least **1 to 2 weeks** between submissions. Submitting many articles at once on related topics raises red flags with reviewers.

---

## 5. Avoiding Promotional Tone Flags

Promotional tone is the most common reason cryptocurrency-related articles are declined or deleted. Review every draft against these criteria before submitting.

**Language to remove:**

| Problem | Examples | Fix |
|---|---|---|
| Superlatives | "best," "only," "revolutionary," "groundbreaking," "first-of-its-kind" | Remove entirely or replace with sourced factual statements |
| Peacock terms | "world-class," "leading," "innovative," "cutting-edge" | Use neutral descriptions: "notable," "published," "peer-reviewed" |
| Weasel words | "many experts believe," "it is widely considered," "some say" | Cite specific sources: "According to [Author] (2024)..." |
| Marketing tone | Enthusiastic, pitch-like language that reads like a press release | Rewrite to read like an encyclopedia entry |

**Source quality rules:**

- **Primary sources** (the project's own website, GitHub, blog posts) can support basic factual claims but should not be the backbone of an article.
- **Independent secondary sources** (news articles from established outlets, academic papers by uninvolved researchers, exchange listing announcements) are what establish notability.
- Aim for at least **3 or more independent reliable sources** that are not affiliated with the subject.

**Balance:**

- Include limitations, criticisms, or competing approaches — not just positive aspects.
- If a protocol has known trade-offs (e.g., increased bandwidth requirements), mention them.
- Avoid comparisons that exist only to make the subject look favorable.

**Pre-submission checklist:**

- [ ] No superlatives or peacock terms
- [ ] At least 3+ independent reliable sources (not from the project itself)
- [ ] ACM/IEEE/academic citations for technical claims
- [ ] Neutral tone throughout — reads like an encyclopedia
- [ ] No original research (all claims are sourced)
- [ ] Proper wiki markup and formatting
- [ ] Categories assigned
- [ ] COI disclosed on user page (if applicable)

---

## 6. Handling Reviewer Feedback

Wikipedia reviewers are volunteers. Treat them with respect and address their feedback constructively.

**General principles:**

- **Do not argue with reviewers.** If you disagree, explain your reasoning calmly on the draft's talk page, citing Wikipedia policies.
- **Do not re-submit without changes.** This wastes reviewer time and may result in your drafts being deprioritized.
- Use the talk page for discussion — never add rebuttals or meta-commentary inside the article itself.

**Common decline reasons and fixes:**

| Decline reason | What it means | How to fix |
|---|---|---|
| "Not notable" | The reviewer does not see enough evidence that the subject meets Wikipedia's notability guidelines. | Add more independent reliable sources. News coverage, academic citations, and third-party analysis carry the most weight. |
| "Promotional tone" | The article reads like marketing material rather than an encyclopedia entry. | Remove all marketing language. Add balance (limitations, criticisms). Rewrite in a neutral, factual voice. |
| "Original research" | Claims in the article are not supported by published sources. | Add citations for every substantive claim. If a claim cannot be sourced, remove it. |
| "Primary sources only" | The article relies too heavily on the subject's own publications. | Find independent coverage: news articles, academic papers by uninvolved researchers, analyst reports. |
| "Too short / stub" | The article does not have enough content to stand as a full article. | Expand sections, add more context, include additional sourced information. |

**After a decline:**

1. Read the full decline rationale.
2. Make all requested changes.
3. If unclear on what the reviewer wants, ask on the draft's talk page.
4. Resubmit only after substantive improvements.

---

## 7. Cross-Link Edit Guidelines

Cross-linking connects the submitted articles to each other and to existing Wikipedia articles. This must be done carefully.

**Rules:**

- Make cross-link edits **only after** the target article exists and has been accepted into mainspace. Do not add links to non-existent articles.
- Each edit must be **independently justifiable**. The link should genuinely help the reader, not serve as promotion.
- **Space edits out** over weeks or months. A burst of edits adding links to Kaspa-related articles will look coordinated and may trigger scrutiny.
- If an edit is reverted by another editor, **do not re-add it**. Instead, discuss on the article's talk page and make your case. If consensus is against the link, accept that.
- Write clear, neutral edit summaries: "Added see also link to BlockDAG article" or "Added citation for GHOST protocol origin."

**Examples of good cross-link edits:**

- Adding a "See also" link from the existing Ethereum article to the GHOST protocol article (GHOST is cited in Ethereum's whitepaper — this is independently justifiable).
- Adding a citation to the Directed Acyclic Graph article that references BlockDAG as an application.
- Linking from an existing consensus mechanism article to PHANTOM as an example.

**Examples of bad cross-link edits:**

- Adding Kaspa links to dozens of cryptocurrency articles in a short time period.
- Adding comparative statements like "Unlike Bitcoin, Kaspa achieves..." to Bitcoin's article.
- Adding links before the target articles have been accepted.

---

## 8. Translation Submissions

Each language Wikipedia operates independently with its own community, standards, and review processes.

**Key points:**

- A translated article still needs to meet the **local Wikipedia's notability standards**. Translation alone does not guarantee acceptance.
- The German, Spanish, and Chinese Wikipedias each have their own equivalents of the AfC process. Research each one before submitting.
- **Machine translations are frequently rejected.** Native speaker review is essential for grammar, terminology, and cultural appropriateness of the writing style.
- Start with languages where you have **native speaker contacts** who can review and refine the translation.
- Technical terminology may not have standard translations in all languages. Check existing articles in the target language Wikipedia for established conventions.

**Interwiki links:**

- Connections between the same article in different languages are managed through [Wikidata](https://www.wikidata.org/).
- After an article is accepted in a second language, create or update the Wikidata item to link both language versions.
- Do not add interwiki links manually in article text — this is handled automatically through Wikidata.

---

## 9. Ongoing Maintenance

Wikipedia articles are not "submit and forget." They require ongoing attention.

**Monitoring:**

- Add articles to your **watchlist** after they are accepted. You will receive notifications of changes.
- Watch for vandalism (unconstructive edits, blanking, spam) and revert it promptly.
- Monitor talk pages for discussions about the articles.

**Updating content:**

- Add new citations as independent coverage appears (news articles, new academic papers, conference proceedings).
- Update time-sensitive information (hashrate figures, market statistics) periodically, always with current citations.
- If a major development occurs (e.g., a hard fork, a new peer-reviewed publication), add it with proper sourcing.

**Community engagement:**

- Respond to talk page discussions constructively and in good faith.
- If another editor proposes changes you disagree with, discuss rather than edit-war.
- Thank editors who improve the articles — building goodwill in the Wikipedia community helps long-term.
- Consider joining relevant WikiProjects (e.g., WikiProject Cryptocurrency, WikiProject Computer Science) to connect with editors who work on related topics.
