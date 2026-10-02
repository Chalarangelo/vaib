#!/usr/bin/env python3
import os
import re
from bs4 import BeautifulSoup
import markdown

def syntax_highlight_vaib(raw_code):
    """Vibrant, multi-token syntax grammar for the vaib code editor component."""
    # Protect quote literals from HTML attribute collisions during regex replacement
    strings = []
    def save_string(match):
        strings.append(match.group(0))
        return f"__STR_{len(strings)-1}__"

    raw_code = re.sub(r'("[^"]*"|\'[^\']*\')', save_string, raw_code)

    # Key-value frontmatter headers
    raw_code = re.sub(r'\b(vaib|stack|output_format):', r"<span class='token-key'>\1:</span>", raw_code)
    
    # Function declarations
    raw_code = re.sub(r'(- fn\s+)([A-Za-z0-9_]+)', r"<span class='token-fn-prefix'>\1</span><span class='token-fn-name'>\2</span>", raw_code)
    
    # State & Logic structural markers
    raw_code = raw_code.replace("# State:", "<span class='token-section'># State:</span>")
    raw_code = raw_code.replace("# Logic", "<span class='token-section'># Logic</span>")
    
    # Comments
    raw_code = re.sub(r'(?m)^#\s*(.*)$', r"<span class='token-comment'># \1</span>", raw_code)

    # Data types & Flow Control Keywords
    raw_code = re.sub(r'\b(enum|decimal!|char|string|boolean|int)\b', r"<span class='token-type'>\1</span>", raw_code)
    raw_code = re.sub(r'\b(match|throw|rescue|mutate|if|unless)\b', r"<span class='token-keyword'>\1</span>", raw_code)

    # Flow Operators
    operators = ["->", "=>", "|>", "==", "!=", ">=", "<="]
    for op in operators:
        raw_code = raw_code.replace(op, f"<span class='token-operator'>{op}</span>")
        
    # Command Directives
    commands = [
        "&grill", "&architect", "&mentor", "&canary", "&run", "&call", 
        "&investigate", "&memorize", "&review", "&wait", "&ask", "&pr", 
        "&trace", "&scope", "&dry", "&submit", "&explain"
    ]
    for cmd in commands:
        raw_code = raw_code.replace(cmd, f"<span class='token-command'>{cmd}</span>")

    # Restore string literals with highlighting tag
    for i, s in enumerate(strings):
        raw_code = raw_code.replace(f"__STR_{i}__", f"<span class='token-string'>{s}</span>")

    return raw_code

def compile_premium_site():
    readme_path = "README.md"
    template_path = "template.html"
    output_path = "index.html"

    if not os.path.exists(readme_path) or not os.path.exists(template_path):
        print("Missing README.md or template.html files.")
        return

    with open(readme_path, "r", encoding="utf-8") as r:
        md_text = r.read()
    with open(template_path, "r", encoding="utf-8") as t:
        template = t.read()

    # Strip YAML frontmatter if present
    if md_text.startswith("---"):
        parts = md_text.split("---", 2)
        if len(parts) >= 3:
            md_text = parts[2]

    html_raw = markdown.markdown(md_text, extensions=['tables', 'fenced_code'])
    soup = BeautifulSoup(html_raw, 'html.parser')

    # Remove top-level h1 headers from README parser output
    for h1 in soup.find_all('h1'):
        h1.decompose()

    # Remove duplicated tagline paragraphs parsed from top of README
    for p in list(soup.find_all('p')):
        p_text = p.get_text().strip()
        if "Assembly for LLM Agents" in p_text or \
           "Semantic constraints for agentic engineering" in p_text or \
           "High-density notation for flow-state vibe coding" in p_text or \
           "High-density architectural primitives that convert loose intents" in p_text:
            p.decompose()

    # Remove leading horizontal rules before first content section
    for hr in list(soup.find_all('hr')):
        if hr.find_previous_sibling() is None or not any(hr.previous_siblings):
            hr.decompose()

    # Uniform dark subtle borders for h2
    for h2 in soup.find_all('h2'):
        h2['class'] = 'text-xl sm:text-2xl font-bold tracking-tight text-zinc-100 border-b border-zinc-800/60 pb-2.5 mt-12 mb-5 font-sans'

    for h3 in soup.find_all('h3'):
        h3['class'] = 'text-base sm:text-lg font-semibold text-zinc-200 mt-8 mb-3 font-sans'

    # Uniform dark subtle horizontal rules (<hr>)
    for hr in soup.find_all('hr'):
        hr['class'] = 'border-t border-zinc-800/60 my-10'

    # Highlight and wrap code blocks with Copy buttons
    for pre in soup.find_all('pre'):
        code = pre.find('code')
        if code:
            highlighted_content = syntax_highlight_vaib(code.decode_contents())
            code.clear()
            code.append(BeautifulSoup(highlighted_content, 'html.parser'))
            
            frame = soup.new_tag('div', attrs={'class': 'my-6 border border-zinc-800/90 rounded-xl bg-[#070b14] overflow-hidden shadow-2xl w-full ring-1 ring-white/5 relative group'})
            pre.wrap(frame)
            
            header = soup.new_tag('div', attrs={'class': 'bg-[#0b101d] px-4 py-2.5 border-b border-zinc-800/90 text-xs text-zinc-400 font-mono flex items-center justify-between select-none'})
            
            left_side = soup.new_tag('div', attrs={'class': 'flex items-center space-x-2'})
            dot1 = soup.new_tag('span', attrs={'class': 'w-2.5 h-2.5 rounded-full bg-rose-500/80 inline-block'})
            dot2 = soup.new_tag('span', attrs={'class': 'w-2.5 h-2.5 rounded-full bg-amber-500/80 inline-block'})
            dot3 = soup.new_tag('span', attrs={'class': 'w-2.5 h-2.5 rounded-full bg-emerald-500/80 inline-block'})
            label = soup.new_tag('span', attrs={'class': 'pl-2 text-zinc-400 text-xs font-mono font-medium'})
            label.string = "vaib logic spec"
            
            left_side.append(dot1)
            left_side.append(dot2)
            left_side.append(dot3)
            left_side.append(label)
            
            right_side = soup.new_tag('div', attrs={'class': 'flex items-center space-x-3'})
            
            copy_btn = soup.new_tag('button', attrs={
                'onclick': 'copyCodeBlock(this)',
                'class': 'copy-btn text-[11px] text-zinc-400 hover:text-white bg-zinc-800/60 hover:bg-zinc-700/80 px-2.5 py-1 rounded transition-colors flex items-center space-x-1 font-mono cursor-pointer border border-zinc-700/50'
            })
            copy_btn.string = "Copy"
            
            right_side.append(copy_btn)
            
            header.append(left_side)
            header.append(right_side)
            frame.insert(0, header)
            
            pre['class'] = 'p-5 overflow-x-auto text-zinc-200 font-mono text-[13px] leading-relaxed bg-transparent border-0 m-0 w-full block'
            code['class'] = 'p-0 bg-transparent border-0 font-mono block'

    # Upgrade trailing punchline into a high-energy CTA banner
    for p in soup.find_all('p'):
        if 'Stop coding. Start vibing.' in p.text:
            banner_html = '''
            <div class="my-14 p-8 rounded-2xl bg-gradient-to-r from-purple-900/30 via-indigo-900/20 to-cyan-900/30 border border-purple-500/30 text-center relative overflow-hidden shadow-2xl backdrop-blur-sm">
                <div class="absolute -top-12 -right-12 w-40 h-40 bg-purple-500/10 rounded-full blur-3xl pointer-events-none"></div>
                <h3 class="text-2xl sm:text-3xl font-extrabold text-white tracking-tight mb-2">
                    Stop coding. <span class="text-transparent bg-clip-text bg-gradient-to-r from-purple-400 to-cyan-400">Start vibing.</span> 🌊
                </h3>
                <p class="text-zinc-400 text-xs sm:text-sm max-w-md mx-auto mb-6">
                    Elevate your AI agent workflows with zero-compilation high-density notation today.
                </p>
                <a href="https://github.com/Chalarangelo/vaib" target="_blank" class="inline-flex items-center space-x-2 bg-gradient-to-r from-purple-500 to-cyan-500 text-white font-bold text-xs px-6 py-3 rounded-lg hover:opacity-90 transition-all shadow-lg hover:shadow-purple-500/25">
                    <span>Get Started on GitHub</span>
                    <span>→</span>
                </a>
            </div>
            '''
            p.replace_with(BeautifulSoup(banner_html, 'html.parser'))

    # Hero section with updated tagline & installer command
    hero_html = '''
    <section class="text-center pt-12 pb-10 space-y-6 max-w-2xl mx-auto font-sans">
        <h1 class="text-3xl sm:text-5xl font-extrabold tracking-tight text-white leading-tight">
            Assembly for LLM Agents. <br>
            <span class="text-transparent bg-clip-text bg-gradient-to-r from-purple-400 to-cyan-400">High-density notation for flow-state vibe coding.</span>
        </h1>
        <p class="text-zinc-400 text-sm sm:text-base font-normal leading-relaxed">
            An open-source, zero-compilation linguistic wrapper and cognitive-steering protocol built for agentic terminals.
        </p>
        
        <div class="pt-2 flex flex-wrap items-center justify-center gap-3">
            <a href="https://github.com/Chalarangelo/vaib" target="_blank" class="bg-zinc-100 text-zinc-900 px-4 py-2 rounded-lg font-bold text-xs hover:bg-white transition-all shadow-md flex items-center space-x-2">
                <span>View Repository</span>
                <span class="text-zinc-500">↗</span>
            </a>
            <a href="https://github.com/Chalarangelo/vaib/releases" target="_blank" class="text-xs font-semibold text-zinc-400 hover:text-white transition-colors">
                Downloads & Releases
            </a>
        </div>
        
        <div class="pt-2 max-w-lg mx-auto">
            <div class="bg-[#070b14] border border-zinc-800/80 px-4 py-3 rounded-lg flex items-center space-x-3 text-zinc-300 shadow-md">
                <span class="text-purple-400 font-bold select-none text-xs font-mono">$</span>
                <input id="hero-cmd" type="text" readonly value="curl -sSL https://raw.githubusercontent.com/Chalarangelo/vaib/main/install.sh | bash" 
                       class="bg-transparent border-none focus:outline-none font-mono text-xs w-full select-all text-zinc-300 text-left">
                <button onclick="copyHeroCmd(this)" class="text-xs text-zinc-400 hover:text-white font-mono bg-zinc-800/80 hover:bg-zinc-700 px-2 py-1 rounded transition-colors flex-shrink-0 border border-zinc-700/50 cursor-pointer">
                    Copy
                </button>
            </div>
        </div>
    </section>
    '''

    compiled_body = hero_html + f'<div class="markdown-body max-w-2xl mx-auto">{str(soup)}</div>'
    final_output = template.replace("__VAIB_CONTENT__", compiled_body)

    with open(output_path, "w", encoding="utf-8") as out:
        out.write(final_output)
    print("🚀 Site built successfully!")

if __name__ == "__main__":
    compile_premium_site()