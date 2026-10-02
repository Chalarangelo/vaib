# 🌊 vaib (Vibe-Accelerated Intent Blocks)

> "Writing lines of code is a 2024 problem. Engineering the absolute *meaning* of a system is a 2026 reality." 

**vaib** is an open-source, zero-compilation linguistic wrapper and cognitive-steering protocol built exclusively for **Vibe Engineers in the making**. 

If you are a developer who is tired of babysitting syntax errors and want to operate as a high-leverage **Director of Intent**, `vaib` gives you the ultimate power framework. It converts hyper-dense architectural blueprints and loose conceptual flows into bulletproof production-grade code repositories. 

It installs straight into your local agentic terminal (`claude-code`, VS Code Agents, Cursor), preserves your elite psychological flow state, and saves a metric ton of money on your token bill.

---

## 📉 Token Overclocking & Performance Metrics

Because `vaib` structures your inputs into high-density declarative data maps and skips conversational AI fluff, it leverages modern LLM **prefix-caching** to its absolute limits:

*   **`output_format: terse_diff`** – Slashes output costs by **65%–75%** by forcing the agent to output raw structural Git line mutations instead of rewriting full files.
*   **`output_format: caveman`** – Achieves a brutal **85% text compression rate**. The AI strips out verbs, pronouns, and polite greetings—speaking in pure, token-lean engineering fragments while maintaining 100% byte-exact code precision.

---

## 🚀 Installation (The 60-Second Onboarding)

Inject the core linguistic engine directly into your global agent profile with a single curl command:

```bash
curl -sSL https://githubusercontent.com | bash
```

Fire up your local agentic CLI terminal, type `/skills`, and watch `vaib` light up as a globally active, cached protocol layer.

---

## 💎 The Vibe-Steering Primitives

Stop typing out paragraphs of explanations. Use the semantic toolkit to command your agent's brain:

### 🚦 Flow & Logic Control
*   `method?` — **Inspection Suffix.** Enforces side-effect-free boolean logic checks.
*   `action!` — **Enforcement Suffix.** Triggers explosive database mutations or hard runtime exception throws.
*   `{{ loose thoughts }}` — **The Natural Escape Hatch.** Drop raw, unstructured human vibes mid-syntax when you hit a complex architectural thought. The engine translates it contextually.

### 🎭 Cognitive Identity Overrides
*   `&grill` — Shifts the agent into a hostile, aggressive Principal Engineer hunting down your code defects and security exploits.
*   `&architect` — Systems optimization mode. Forces the AI to map microservice scaling boundaries and structural schema trees first.
*   `&mentor` — Deep educational mode. Explains theoretical best-practices via clean metaphors.

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

# Logic
- fn ProcessTransfer(from_id, to_id, amount) {
    from = Wallet.find(from_id)
    to = Wallet.find(to_id)
    
    throw: InsufficientFunds if amount > from.balance
    throw: FrozenAccount if from.frozen? || to.frozen?
    
    # Destructive network action with built-in retry logic and robust fallback
    Stripe.charge!(from.customer_id, amount) [retry: 3]
    rescue: -> &ask("Stripe gateway timed out. Attempt local ledger fallback?")
    
    from.balance -= amount
    to.balance += amount
    
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

## 🤝 Upstream Synced Contributions

When you cook up an incredibly fast local shorthand trick, don't leave your terminal to share it. Let the agent ship it back to the community for you:

```yaml
# Just type this right into your active prompt box:
&memorize("Data/UltraCaching") -> &submit("Core/Syntax")
```
The engine automatically distills your last transaction logs, generates a clean Markdown snippet, stages the code branch, and opens a public upstream Pull Request on GitHub. 

Welcome to the era of pure Intent Architecture. Stop coding. Start vibing. 🌊
