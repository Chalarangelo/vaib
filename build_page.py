#!/usr/bin/env python3
import os
import re
from bs4 import BeautifulSoup
import markdown

def syntax_highlight_vaib(raw_code):
    """Safely tokenizes the custom vaib syntax grammar primitives without breaking HTML tags."""
    # Frontmatter parameters
    raw_code = raw_code.replace("vaib:", "<span class='token-keyword'>vaib:</span>")
    raw_code = raw_code.replace("stack:", "<span class='token-keyword'>stack:</span>")
    raw_code = raw_code.replace("output_format:", "<span class='token-keyword'>output_format:</span>")
    
    # Core pipeline headers
    raw_code = raw_code.replace("- fn ", "<span class='token-macro'>- fn </span>")
    raw_code = raw_code.replace("# State:", "<span class='token-macro'># State:</span>")
    raw_code = raw_code.replace("# Logic", "<span class='token-macro'># Logic</span>")
    
    # Special operators and control hooks
    operators = ["->", "=>", "|>"]
    for op in operators:
        raw_code = raw_code.replace(op, f"<span class='token-symbol'>{op}</span>")
        
    commands = ["&grill", "&architect", "&mentor", "&canary", "&run", "&call", "&investigate", "&memorize", "&review", "&wait", "&ask", "&pr"]
    for cmd in commands:
        raw_code = raw_code.replace(cmd, f"<span class='token-macro'>{cmd}</span>")
        
    # Standard configuration comments (only matching start of lines to avoid tag breaking)
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

    # Clear out git repository frontmatter blocks if present
    if md_text.startswith("---"):
        parts = md_text.split("---", 2)
        if len(parts) >= 3:
            md_text = parts[2]

    # Parse baseline markdown to standard HTML
    html_raw = markdown.markdown(md_text, extensions=['tables', 'fenced_code'])
    soup = BeautifulSoup(html_raw, 'html.parser')

    # Convert section headings and insert sub-banners where appropriate
    for h2 in soup.find_all('h2'):
        if any(term in h2.text.lower() for term in ["contributing", "upstream", "community"]):
            banner = soup.new_tag('div', attrs={'class': 'text-center text-[10px] uppercase font-mono font-bold tracking-widest text-zinc-500 mb-2 mt-16'})
            banner.string = "OPEN SOURCE COMPONENT"
            h2.insert_before(banner)
        h2['class'] = 'text-2xl sm:text-3xl font-extrabold tracking-tight text-white border-b border-zinc-800 pb-3 mt-12 mb-6 font-sans'

    for h3 in soup.find_all('h3'):
        h3['class'] = 'text-lg font-bold text-cyan-400 mt-8 mb-3 tracking-wide uppercase font-mono'

    # Package code blocks into clean T3 dark panels
    for pre in soup.find_all('pre'):
        code = pre.find('code')
        if code:
            highlighted_content = syntax_highlight_vaib(code.decode_contents())
            code.clear()
            code.append(BeautifulSoup(highlighted_content, 'html.parser'))
            
            frame = soup.new_tag('div', attrs={'class': 'my-6 border border-zinc-800 rounded-xl bg-[#090d16] overflow-hidden shadow-2xl w-full'})
            pre.wrap(frame)
            
            header = soup.new_tag('div', attrs={'class': 'bg-[#0f172a] px-4 py-2.5 border-b border-zinc-800 text-[10px] text-zinc-400 font-mono tracking-wider flex items-center space-x-2 select-none'})
            dot1 = soup.new_tag('span', attrs={'class': 'w-2 h-2 rounded-full bg-red-500/50'})
            dot2 = soup.new_tag('span', attrs={'class': 'w-2 h-2 rounded-full bg-yellow-500/50'})
            dot3 = soup.new_tag('span', attrs={'class': 'w-2 h-2 rounded-full bg-green-500/50'})
            label = soup.new_tag('span', attrs={'class': 'pl-2 text-zinc-400 text-[10px] tracking-wider uppercase font-mono font-semibold'})
            label.string = "vaib logic matrix"
            
            header.append(dot1)
            header.append(dot2)
            header.append(dot3)
            header.append(label)
            frame.insert(0, header)
            
            pre['class'] = 'p-5 overflow-x-auto text-zinc-200 font-mono text-[13px] leading-relaxed bg-transparent border-0 m-0 w-full'
            code['class'] = 'p-0 bg-transparent border-0 text-zinc-200 font-mono text-[13px]'

    # T3 Hero Header Section
    hero_html = '''
    <section class="text-left pt-12 pb-10 space-y-6 max-w-3xl font-sans">
        <h1 class="text-4xl sm:text-6xl font-black tracking-tight text-white leading-tight">
            The open-source control plane <br>
            <span class="text-transparent bg-clip-text bg-gradient-to-r from-purple-400 to-cyan-400">for vibe engineering.</span>
        </h1>
        <p class="text-zinc-400 text-base sm:text-lg font-normal leading-relaxed">
            Stop typing long paragraphs of instructions to your AI tools. <strong>vaib</strong> converts hyper-dense architectural intentions and logical flows into production-grade repositories.
        </p>
        
        <div class="pt-2 flex flex-wrap items-center gap-4">
            <a href="https://github.com/Chalarangelo/vaib" target="_blank" class="bg-white text-black px-5 py-2.5 rounded-lg font-bold text-xs hover:bg-zinc-200 transition-all shadow-md">
                View on GitHub
            </a>
            <a href="#vaib-compiled-root" class="text-xs font-semibold text-zinc-400 hover:text-white transition-colors flex items-center space-x-1">
                <span>Read Documentation</span>
                <span>↓</span>
            </a>
        </div>
        
        <div class="pt-2 max-w-xl">
            <div class="bg-[#090d16] border border-zinc-800 px-4 py-3 rounded-lg flex items-center space-x-3 text-zinc-300 shadow-md">
                <span class="text-purple-400 font-bold select-none text-xs font-mono">$</span>
                <input type="text" readonly value="git clone https://github.com/Chalarangelo/vaib.git" 
                       class="bg-transparent border-none focus:outline-none font-mono text-xs w-full select-all text-zinc-300">
            </div>
        </div>
    </section>
    '''

    compiled_body = hero_html + f'<div class="markdown-body max-w-3xl mx-auto">{str(soup)}</div>'
    final_output = template.replace("<!-- {{VAIB_DYNAMIC_MARKDOWN_BODY}} -->", compiled_body)

    with open(output_path, "w", encoding="utf-8") as out:
        out.write(final_output)
    print("🚀 Page compiled successfully!")

if __name__ == "__main__":
    compile_premium_site()