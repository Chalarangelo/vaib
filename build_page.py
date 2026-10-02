#!/usr/bin/env python3
import os
import re
from bs4 import BeautifulSoup
import markdown

def syntax_highlight_vaib(raw_code):
    """Vibrant, multi-token syntax grammar for the vaib code editor component."""
    # Frontmatter keys (Rose Pink)
    raw_code = re.sub(r'\b(vaib|stack|output_format):', r"<span class='token-key'>\1:</span>", raw_code)
    
    # Strings in double or single quotes (Vibrant Emerald)
    raw_code = re.sub(r'("[^"]*"|\'[^\']*\')', r"<span class='token-string'>\1</span>", raw_code)

    # Core structural markers & functions (Amber/Gold)
    raw_code = re.sub(r'(- fn\s+)([A-Za-z0-9_]+)', r"<span class='token-fn-prefix'>\1</span><span class='token-fn-name'>\2</span>", raw_code)
    raw_code = raw_code.replace("# State:", "<span class='token-section'># State:</span>")
    raw_code = raw_code.replace("# Logic", "<span class='token-section'># Logic</span>")
    
    # Primitive types & keywords (Bright Blue)
    raw_code = re.sub(r'\b(enum|decimal!|char|string|boolean|int)\b', r"<span class='token-type'>\1</span>", raw_code)
    raw_code = re.sub(r'\b(match|throw|rescue|mutate)\b', r"<span class='token-keyword'>\1</span>", raw_code)

    # Operators & Arrows (Electric Cyan)
    operators = ["->", "=>", "|>", "==", "!=", ">=", "<="]
    for op in operators:
        raw_code = raw_code.replace(op, f"<span class='token-operator'>{op}</span>")
        
    # Execution hooks & macros (Purple Accent)
    commands = ["&grill", "&architect", "&mentor", "&canary", "&run", "&call", "&investigate", "&memorize", "&review", "&wait", "&ask", "&pr", "&trace"]
    for cmd in commands:
        raw_code = raw_code.replace(cmd, f"<span class='token-command'>{cmd}</span>")
        
    # Comments (Muted Slate)
    raw_code = re.sub(r'(?m)^#\s*(.*)$', r"<span class='token-comment'># \1</span>", raw_code)
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

    if md_text.startswith("---"):
        parts = md_text.split("---", 2)
        if len(parts) >= 3:
            md_text = parts[2]

    html_raw = markdown.markdown(md_text, extensions=['tables', 'fenced_code'])
    soup = BeautifulSoup(html_raw, 'html.parser')

    for h2 in soup.find_all('h2'):
        h2['class'] = 'text-xl sm:text-2xl font-bold tracking-tight text-zinc-100 border-b border-zinc-800 pb-2.5 mt-12 mb-5 font-sans'

    for h3 in soup.find_all('h3'):
        h3['class'] = 'text-base sm:text-lg font-semibold text-zinc-200 mt-8 mb-3 font-sans'

    # Rich Code Window Shell
    for pre in soup.find_all('pre'):
        code = pre.find('code')
        if code:
            highlighted_content = syntax_highlight_vaib(code.decode_contents())
            code.clear()
            code.append(BeautifulSoup(highlighted_content, 'html.parser'))
            
            frame = soup.new_tag('div', attrs={'class': 'my-6 border border-zinc-800/90 rounded-xl bg-[#070b14] overflow-hidden shadow-2xl w-full ring-1 ring-white/5'})
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
            
            right_side = soup.new_tag('span', attrs={'class': 'text-[10px] text-zinc-500 uppercase tracking-wider font-mono'})
            right_side.string = "UTF-8"
            
            header.append(left_side)
            header.append(right_side)
            frame.insert(0, header)
            
            pre['class'] = 'p-5 overflow-x-auto text-zinc-200 font-mono text-[13px] leading-relaxed bg-transparent border-0 m-0 w-full block'
            code['class'] = 'p-0 bg-transparent border-0 font-mono block'

    hero_html = '''
    <section class="text-left pt-10 pb-8 space-y-5 max-w-3xl font-sans">
        <h1 class="text-3xl sm:text-5xl font-extrabold tracking-tight text-white leading-tight">
            Semantic constraints <br>
            <span class="text-transparent bg-clip-text bg-gradient-to-r from-purple-400 to-cyan-400">for agentic engineering.</span>
        </h1>
        <p class="text-zinc-400 text-sm sm:text-base font-normal leading-relaxed max-w-2xl">
            High-density architectural primitives that convert loose intents into verified code structures.
        </p>
        
        <div class="pt-1 flex flex-wrap items-center gap-3">
            <a href="https://github.com/Chalarangelo/vaib" target="_blank" class="bg-zinc-100 text-zinc-900 px-4 py-2 rounded-lg font-bold text-xs hover:bg-white transition-all shadow-md flex items-center space-x-2">
                <span>View Repository</span>
                <span class="text-zinc-500">↗</span>
            </a>
            <a href="https://github.com/Chalarangelo/vaib/releases" target="_blank" class="text-xs font-semibold text-zinc-400 hover:text-white transition-colors">
                Downloads & Releases
            </a>
        </div>
        
        <div class="pt-1 max-w-xl">
            <div class="bg-[#070b14] border border-zinc-800/80 px-3.5 py-2.5 rounded-lg flex items-center space-x-3 text-zinc-300 shadow-md">
                <span class="text-purple-400 font-bold select-none text-xs font-mono">$</span>
                <input type="text" readonly value="git clone https://github.com/Chalarangelo/vaib.git" 
                       class="bg-transparent border-none focus:outline-none font-mono text-xs w-full select-all text-zinc-300">
            </div>
        </div>
    </section>
    '''

    compiled_body = hero_html + f'<div class="markdown-body max-w-3xl mx-auto">{str(soup)}</div>'
    final_output = template.replace("__VAIB_CONTENT__", compiled_body)

    with open(output_path, "w", encoding="utf-8") as out:
        out.write(final_output)
    print("🚀 Site built successfully!")

if __name__ == "__main__":
    compile_premium_site()