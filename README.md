# 🌊 vaib

**Assembly for LLM Agents.** High-density notation for flow-state vibe coding.

---

## ⚡ Why vaib?
Traditional LLM prompts waste tokens on conversational filler, imprecise descriptions, and redundant file rewrites. **vaib** is an open-source, zero-compilation linguistic wrapper and cognitive-steering protocol built for agentic terminals (`claude-code`, Cursor, VS Code Agents).

* **The 3 Zeroes**: **Zero Fluff** (up to 85% token reduction via `caveman` mode), **Zero Redo Tax** (guard clauses eliminate hallucinated logic bugs), **Zero Setup** (runs natively in your agent context).
* **Prefix-Cache Optimized**: Declarative frontmatter triggers 100% LLM cache hits.
* **Single-Line Friendly**: Type rapid multi-step logic on a single line using inline `;` chaining without messy multiline chat boxes.
* **Diff-Only Output**: `terse_diff` saves 65%–75% output costs by emitting raw line mutations instead of full-file rewrites.

---

## 🚀 60-Second Quickstart
Inject the core linguistic engine directly into your global agent profile:

```bash
curl -sSL [https://raw.githubusercontent.com/Chalarangelo/vaib/main/install.sh](https://raw.githubusercontent.com/Chalarangelo/vaib/main/install.sh) | bash
```

Fire up your agentic CLI terminal, type `/skills` (or verify `~/.claude/skills/vaib`), and `vaib` becomes an active protocol layer.

---

## 📉 Token Overclocking & Performance Metrics

Because `vaib` structures your inputs into high-density declarative data maps and skips conversational AI fluff, it leverages modern LLM **prefix-caching** to its absolute limits:

*   **`output_format: terse_diff`** – Slashes output costs by **65%–75%** by forcing the agent to output raw structural Git line mutations instead of rewriting full files.
*   **`output_format: caveman`** – Achieves a brutal **85% text compression rate**. The AI strips out verbs, pronouns, and polite greetings—speaking in pure, token-lean engineering fragments while maintaining 100% byte-exact code precision.

---

## 💎 Semantic Toolkit
Stop writing paragraphs. Steer your agent with precise structural operators:

### 🚦 Flow & Logic Control
* `;` — **Inline Chain.** Express multi-statement workflows on a single line.
* `unless cond` — **Postfix Guard.** Early-exit guard clause (`throw: Err unless user.active?`).
* `given: [a, b]` — **Preconditions.** Logical assertion array before execution.
* `:symbol` — **Enum Keys.** Concise status mapping (`:pending`, `:approved`).
* `method?` — **Inspection Suffix.** Side-effect-free boolean checks.
* `action!` — **Enforcement Suffix.** Hard database commits or runtime exception throws.
* `{{ loose thoughts }}` — **Natural Escape.** Drop raw, unstructured thoughts mid-syntax.
* `"literal"` / `'char'` — **Text Lock.** Guarantees exact UI string or character preservation.

### 🎭 Cognitive Identity & Context Controls
* `&scope("path")` — **Context Guard.** Restricts agent focus strictly to specified path(s).
* `&dry` — **Plan Lockdown.** Forces a 3-line structural dry run before touching files.
* `&grill` — Shifts agent into a hostile Principal Engineer hunting defects and security leaks.
* `&architect` — Systems optimization mode. Forces schema trees and service boundaries first.
* `&mentor` — Deep educational mode with pattern breakdowns and metaphors.

---

## ⚡ vaib in Action (Showcase & Examples)

See how `vaib` strips away the conversational noise and boilerplate, turning you into a high-leverage intent designer.

### 1. The Secure Payment Loop (Backend & Logic Architecture)
Instead of typing out a wall of text detailing database safety, retry limits, and errors, express your transaction layer in just a few structured lines.

```yaml
---
vaib: Payments/Capture/v2
stack: [TypeScript, Prisma, Stripe]
output_format: terse_diff
---

# State: Wallet
- balance: decimal! [invariant: >= 0]
- status: enum(:active, :frozen, :flagged)

# Logic
- fn ProcessTransfer(from_id, to_id, amount) {
    from = Wallet.find(from_id) ; to = Wallet.find(to_id)
    
    # Postfix guards & enum symbols eliminate multi-line nested IFs
    throw: InsufficientFunds unless from.balance >= amount
    throw: FrozenAccount if from.status == :frozen || to.status == :frozen
    
    # Destructive action with backoff retry and fallback
    Stripe.charge!(from.customer_id, amount) [retry: 3]
    rescue: -> &ask("Gateway timed out. Fallback to local ledger?")
    
    from.balance -= amount ; to.balance += amount
    -> mutate: Wallet.save_all!([from, to])
}
```

### 2. The Dynamic UI Component (Text & State Preservation)
When building layouts, stop the AI from guessing your exact interface copy. Enforce strict character literals (`'X'`) and string locks (`"Text"`) to map Tailwind arrays cleanly.

```yaml
---
vaib: Views/Dashboard/Alert
stack: [React, TailwindCSS]
output_format: terse_diff
---

# State: Banner
- variant: enum(info, warning, danger)
- active_tab: char [default: 'A']

# Logic
- fn RenderAlert() {
    match(variant):
      "danger" => 
        Text.label = "🚨 CRITICAL FAULT: Action Required Immediately!"
        Container.style = "bg-red-500 border-l-4 border-red-700"
      "warning" => 
        Text.label = "Warning: Check system status metrics."
        Container.style = "bg-amber-400"
        
    Button.on_click -> 
        &trace -> {{ Dispatch telemetry, close banner, switch active_tab to 'B' }}
}
```

### 3. High-Leverage Non-Technical Steering (Ops & Automation)
`vaib` isn't just for writing raw code files. You can command your terminal agent to orchestrate deep diagnostics, handle telemetry issues, and translate the data for the rest of your company seamlessly.

```yaml
---
vaib: Ops/IncidentTriage/v1
output_format: eli5
---

- Action:
    # Directly calls system logs and attaches tracking history
    tail("-n 100", "/var/log/nginx/error.log")
    &investigate("src/middleware/auth.ts")
    
    # Tell the agent to switch into a Principal Engineer mindset, audit its own finding,
    # and explain the fix like the reader is 5 years old.
    then:
      &grill -> &canary
      => &explain(to: "eli5")
```

---

## 🤝 Upstream Rule Synchronization

Persist custom shortcuts locally or share them upstream without leaving your agent terminal:

```yaml
&memorize("Data/UltraCaching") -> &submit("Core/Syntax")
```

The engine distills execution history, builds a clean syntax snippet, stages a branch, and opens an upstream GitHub PR.

---

**Stop coding. Start vibing.** 🌊
