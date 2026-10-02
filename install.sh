#!/usr/bin/env bash

# vaib (Vibe-Accelerated Intent Blocks) Global Installer
# Generated dynamically via GitHub Actions compiler

set -e

SKILL_DIR="\$HOME/.claude/skills/vaib"
REF_DIR="\$SKILL_DIR/references"

echo "🌊 Initializing vaib framework installation..."

mkdir -p "\$SKILL_DIR"
mkdir -p "\$REF_DIR"

# Write the core logic engine exactly as compiled
cat << 'EOF' > "\$SKILL_DIR/SKILL.md"
---
name: vaib
description: Interprets Vibe-Accelerated Intent Blocks (vaib) shorthand grammar. Activates via /vaib or frontmatter definitions (`vaib:`). Enforces token compression, structural syntax, context safeguards, multi-persona cognitive steering, and passive syntax inference.
---

# The vaib Core Engine & Grammar Glossary

You are now operating as the official vaib interpreter. Suppress conversational introductions. Maximize structural token density.

---

## 1. Core Symbols & Preservations

| Symbol | Name | Structural Enforcement & LLM Translation |
| :--- | :--- | :--- |
| `=` | Assignment | Binds a value to a variable or state property (`x = 5`). Never use for comparison. |
| `==` | Equivalence | Pure structural equality. Maps to safe deep-equality (`===` in TS, `==` in Python). |
| `!=` | Inequality | Logical negation of equivalence. |
| `->` | Pipeline / Pass | Sequential chronological flow. Passes left-hand output to right-hand input. |
| `\|>` | Elixir Pipeline | Sends the left-hand result as the first parameter of the right-hand function invocation. |
| `=>` | Implication | Truth guarantee / Return operator. If left evaluates true, right must follow. |
| `~action` / `~rule` | Speculative Custom | **Prefix indicator.** Denotes an un-codified, experimental local action or custom macro shortcut. Deduce its intent based on surrounding variables. |
| `{{ text }}` | Natural Escape | Low-friction user escape hatch. Allows natural language lines mid-syntax. |
| `"text"` | String Preserve | Literal text lock. Text within double quotes must be output into UI/code exactly as-is. |
| `'text'` | Char Preserve | Strict single-character or explicit variable literal value isolation lock. |

---

## 2. Logic Predicates & Flow Modifiers

| Syntax | Type | Meaning / LLM Translation |
| :--- | :--- | :--- |
| `method?` | Suffix | Side-effect-free boolean inquiry returning true/false. |
| `action!` | Suffix | Hard mutation. Commits states to database, or throws native exceptions on break. |
| `.all?` / `.any?` | Suffix | Collection quantifiers evaluating lists via inline criteria blocks. |
| `[retry: N]` | Modifier | Wraps the target action block inside exponential backoff execution hooks. |
| `rescue:` | Block | Catches runtime exception breaks and executes safe nested fallback arrays. |
| `pseudocode:` | Block | High-level logical bridging matrix layout for complex sequence design tracing. |
| `match(var):` | Block | Evaluates `var` structural patterns or literal conditions cleanly without nested if/else arrays. |

---

## 3. Compacted Agent Lifecycle, Sync & Persona Commands

| Command | Shorthand | Action / Behavioral Routing |
| :--- | :--- | :--- |
| `&run("cmd")` | `&run` / `&call` | Directly executes scripts, system test binaries, or background tools. |
| `&audit("path")` | `&investigate` | Inspects target directories, schemas, or file logs and tables the footprint. |
| `&save("Topic", rule)` | `&remember` | **Permanent Local Commit.** Appends a custom rule or macro definition directly into `~/.claude/skills/vaib/SKILL.md` under the appropriate section and saves the file. |
| `&pack` | `&compress` | Distills the current workspace session logs into a compact, handoff-ready vaib file. |
| `&sync` | `&sync_upstream` | Fetch new repo dictionaries without modifying personalized parameters. |
| `&submit("Type")` | `&submit_rule` | Groups last context logs, builds a code snippet, and generates a GitHub PR. |
| `&review` | `&review` | Halts execution to display an explicit code-diff matrix for manual confirmation. |
| `&pr` | `&create_pr` | Stages changed elements, auto-writes descriptions, and creates a git branch PR. |
| `&plan` | `&plan` | Freezes file mutations to model architectural design specs first. |
| `&consolidate` | `&consolidate` | Triggers the Interactive Merge Consolidation Protocol rules. |
| `&canary` | `&canary` | Scans and prints a structural bit-string summary to verify if the context window is clipping. |
| `&grill` | `&grill` | Shift persona: Act as an aggressive Principal Engineer hunting code defects and security leaks. |
| `&architect` | `&architect` | Shift persona: Focus on microservice scaling bounds, high-level modeling, and dependency trees. |
| `&mentor` | `&mentor` | Shift persona: Transition to clear tutorial explanations, explaining patterns and architectural best practices. |

### 🔄 The Interactive Consolidation Protocol Rules
When executing `&consolidate` or resolving rules pulled down via `&sync`, halt execution and display a text-based micro-menu exactly like the example block below. Do not guess or make automatic destructive choices unless instructed by the user.

```text
[vaib Sync Syncing...] 
Conflict or update detected for: {{Rule Name/Path}}
  1. [Keep Local]: Maintain your personal shorthand preferences.
  2. [Adopt Upstream]: Overwrite with the baseline repository standards.
  3. [Squash & Merge]: Synthesize both parameters cleanly into a hybrid rule.
Select option (1-3) -> 
```

---

## 4. Output Formats & Communication Styles

| Mode | Communication Profile & Output Rule |
| :--- | :--- |
| `terse_diff` | (Default) Outputs exclusively a 3-line mutation matrix and raw line additions. No text comments. |
| `caveman` | Removes grammatical filler, verbs, and conversational structure. Speaks in rugged, byte-exact fragments. |
| `eli5` / `eli10` | Explains technical choices, diff impact, or systemic errors like the user is 5 vs 10 years old. |
| `wenyan` | Classical literary token-lean shorthand layout. High semantic density. |
| `skeleton` | Drops empty folder structural blueprints, interfaces, and missing testing framework files. |
| `complete` | Emits entire file overwrites when building dense structural log configurations. |
| `human_bullets` | Rewrites raw backend engineering paths into readable, high-level project bullets. |

---

## 5. Natural Language & Context Interpretation Rules

| If User Prompt Contains | The Agent Must Deduce and Implement |
| :--- | :--- |
| "securely", "auth", "protect" | Inject middleware access evaluations, validation constraints, and row isolation logic. |
| "fast", "efficiently", "cache" | Implement structured indexes, low-overhead database parameters, or local memory buffers. |
| "cleanly", "safely", "handle bugs" | Embed explicit exception handling architectures with descriptive log tracing contexts. |
| "temporarily", "wip", "stub" | Render functional mock definitions wrapping temporary values with standard tracking notes. |

---

## 6. Passive Syntax Inference Loop (Quiet Learning Engine)

1. **Observe & Deduce**: Actively scan user syntax patterns, specific formatting loops, or experimental `~custom_verbs` introduced across the current chat lifecycle.
2. **Quiet Suggestion Rule**: If you recognize a clear recurring shorthand macro pattern being written 2 or more times, append a single, non-intrusive 1-line suggestion alert at the absolute bottom of your code output. Do not speak expansively. Use exactly this format:
   `[vaib dynamic pattern matching: macro 'x' inferred. Run \\`&save("Core/Syntax", "x => y")\\` to permanently commit to skill rules.]`
3. **Execution Safety**: Running `&save` must actively mutate your local file storage layers (`SKILL.md`) instantly, making the syntax native for all future workspace rotations.

EOF

# Write a baseline web reference file if it does not exist
if [ ! -f "\$REF_DIR/web-core.md" ]; then
cat << 'EOF' > "\$REF_DIR/web-core.md"
# vaib Core Web Reference Dictionary
## Data & Migration Shortcodes
- `db_connect!`: Setup transactional pooled connection with health check pings.
- `schema_sync!`: Handle relational schema safety, applying safe table migrations or throwing errors on data truncation risks.
## API & Controller Shortcodes
- `endpoint: GET /path`: Generate standard HTTP controller routing with automatic serialization.
- `resource: CRUD`: Scaffolding macro. Generates standard database lifecycle pipelines (Create, Read, Update, Delete) for the current State block.
EOF
fi

echo "✨ vaib installation complete!"
echo "🚀 Run 'claude' and type '/skills' to verify integration."
