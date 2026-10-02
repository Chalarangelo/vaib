# 🌊 Contributing to vaib

Welcome, Vibe Engineer. If you've been cooking up hyper-dense shorthand macros or framework dictionaries in your local sessions and want to sync them upstream to help the collective save tokens, you are in the right place.

We maintain a strict focus on high semantic density, zero conversational fluff, and structural predictability.

---

## 🛠️ The Absolute Easiest Way to Contribute

You don't need to manually clone this repo or open a browser tab to submit a new rule. `vaib` allows you to ship right from your active terminal agent prompt.

1. **Commit it locally first:** 
   Once you've tested a pattern in your prompt session, tell your agent to memorize it:
   ```yaml
   &save("Core/Logic", "~my_shortcut => Expanded.logic!")
   ```
2. **Ship it upstream:**
   Run the submission pass directly in your prompt text box:
   ```yaml
   &submit("Core/Syntax")
   ```
   The underlying engine will automatically extract the recent context history, format a standardized markdown file snippet, generate a git branch, and open a structural Pull Request directly on our GitHub queue.

---

## 📐 Rule Architecture Standards

If you choose to write modifications manually or submit a new file inside the `references/` directory, you must follow these core design paradigms:

1. **Deterministic Equivalence:** Always ensure mathematical tokens (`=`, `==`, `->`, `|>`) maintain universal, ecosystem-agnostic predictability.
2. **Zero Emojis / Zero Conversational Bloat:** Do not add decorative elements or conversational filler text to system prompt dictionaries. Every line must serve as highly compressible token syntax.
3. **Double-Brace Escape Hatches:** Always respect the `{{ natural escape hatch }}` constraint to allow developers a fallback option when they hit complex thoughts.

Thank you for overclocking the agentic era with us. Let's vibecode. 🌊

*(Repository Origin: https://github.com)*
