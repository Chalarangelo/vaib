---
name: 🌊 vaib Feature / Dictionary Request
about: Propose new architectural shorthand symbols, macro commands, or reference packs using the vaib dialect.
title: "[MACRO]: "
labels: ["enhancement", "vibe-check"]
assignees: "Chalarangelo"
---

### 📝 Shorthand Spec Request Blueprint

```yaml
---
vaib: Request/Extension/v1
author: "{{ github.user }}"
type: "dictionary" # or "core-symbol"
---

# 📦 Target Proposal
- scope: {{ e.g., references/graphql-api.md or Core/Symbols }}
- semantic_intent: {{ Tell us what rule or shorthand abbreviation you want added }}

# 🚦 Intended Grammar & Translation Map
- `proposed_macro!` => 
    pseudocode:
      DESCRIBE the production code expansion the agent should generate
      WHEN it parses this specific shorthand token.
```

### 🧠 Why this improves the Vibe
{{ Explain how this rule keeps Vibe Engineers in their flow state, cuts down output token counts, or solves a repetitive prompt issue }}
