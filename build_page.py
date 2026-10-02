#!/usr/bin/env python3
import os
from bs4 import BeautifulSoup
import markdown

def syntax_highlight_vaib(raw_code):
    """Injects syntax tracking classes directly into vaib dialect tokens."""
    # Handle core YAML headers parameters
    raw_code = raw_code.replace("vaib:", "<span class='token-keyword'>vaib:</span>")
    raw_code = raw_code.replace("stack:", "<span class='token-keyword'>stack:</span>")
    raw_code = raw_code.replace("output_format:", "<span class='token-keyword'>output_format:</span>")
    
    # Handle pipeline operator primitives
    raw_code = raw_code.replace("- fn ", "<span class='token-macro'>- fn </span>")
    raw_code = raw_code.replace("- state:", "<span class='token-macro'>- state:</span>")
    raw_code = raw_code.replace("- logic:", "<span class='token-macro'>- logic:</span>")
    
    # Highlight operators and interactive commands
    operators = ["->", "=>", "|>"]
    for op in operators:
        raw_code = raw_code.replace(op, f"<span class='token-symbol'>{op}</span>")
        
    commands = ["&grill", "&architect", "&mentor", "&canary", "&run", "&call", "&investigate", "&memorize", "&review", "&wait", "&ask", "&pr"]
    for cmd in commands:
        raw_code = raw_code.replace(cmd, f"<span class='token-macro'>{cmd}</span>")
        
    # Handle comments and strings styles contextually
    raw_code = raw_code.replace("# ", "<span class='token-comment'># ")
    return raw_code

def compile_premium_site():
    readme_path = "README.md"
    template_path = "template.html"
    output_path = "index.html"

    if not os.path.exists(readme_path) or not os.path.exists(template_path):
        print("Required baseline configuration files are missing.")
        return

    with open(readme_path, "r") as r:
        md_text = r.read()
    with open(template_path, "r") as t:
        template = t.read()

    if md_text.startswith("---"):
        parts = md_text.split("---", 2)
        if len(parts) >= 3:
            md_text = parts[2]

    # Pre-render standard markdown
    html_raw = markdown.markdown(md_text, extensions=['tables', 'fenced_code'])
    soup = BeautifulSoup(html_raw, 'html.parser')

    # Convert core typography blocks to match large t3 text layout signatures
    for h2 in soup.find_all('h2'):
        # Inject the premium "Open Source" tracking banner right before specific sections
        if "Contributing" in h2.string or "Upstream" in h2.string:
            banner = soup.new_tag('div', attrs={'class': 'text-center text-[10px] uppercase font-bold tracking-widest text-[#636366] mb-2 font-mono'})
            banner.string = "OPEN SOURCE COMPONENT"
            h2.insert_before(banner)
        h2['class'] = 'text-3xl sm:text-4xl font-extrabold tracking-tight text-white text-center mt-24 mb-6 tracking-tighter'
        
    for h3 in soup.find_all('h3'):
        h3['class'] = 'text-lg font-bold text-white tracking-tight mt-10 mb-4'
    for p in soup.find_all('p'):
        p['class'] = 'text-[#8e8e93] text-base leading-relaxed mb-6'

    # 1. Transform Code Blocks with Side-by-Side Horizontal Grid Layouts
    # Find all code examples and group adjacent ones into responsive column blocks
    pre_blocks = soup.find_all('pre')
    for pre in pre_blocks:
        code = pre.find('code')
        if code:
            # Run our token high-lighting logic engine safely
            highlighted_code = syntax_highlight_vaib(code.decode_contents())
            code.clear()
            code.append(BeautifulSoup(highlighted_code, 'html.parser'))
            
            # Wrap pre inside a clean t3 window frame container shell
            frame = soup.new_tag('div', attrs={'class': 'my-6 border border-[#1c1c1e] rounded-xl bg-[#09090b] overflow-hidden shadow-2xl flex-1 flex flex-col justify-between'})
            pre.wrap(frame)
            
            # Build top control badge bar
            header = soup.new_tag('div', attrs={'class': 'bg-[#121214] px-4 py-2.5 border-b border-[#1c1c1e] text-[10px] text-[#636366] font-mono tracking-wider flex items-center space-x-1.5 select-none'})
            dot1 = soup.new_tag('span', attrs={'class': 'w-1.5 h-1.5 rounded-full bg-[#ff3b30]/40'})
            dot2 = soup.new_tag('span', attrs={'class': 'w-1.5 h-1.5 rounded-full bg-[#ff9500]/40'})
            dot3 = soup.new_tag('span', attrs={'class': 'w-1.5 h-1.5 rounded-full bg-[#34c759]/40'})
            label = soup.new_tag('span', attrs={'class': 'pl-1 text-zinc-500'})
            label.string = "vaib execution layer"
            
            header.append(dot1)
            header.append(dot2)
            header.append(dot3)
            header.append(label)
            frame.insert(0, header)
            
            pre['class'] = 'p-5 overflow-x-auto text-[#ededed] font-mono text-xs sm:text-sm leading-relaxed bg-transparent border-0 m-0 flex-grow'
            code['class'] = 'p-0 bg-transparent border-0 text-[#ededed] font-mono text-xs sm:text-sm'

    # Group adjacent frame windows side-by-side to replicate the layout grid options perfectly
    frames = soup.find_all('div', attrs={'class': lambda x: x and 'my-6 border border-[#1c1c1e]' in x})
    i = 0
    while i < len(frames) - 1:
        current_frame = frames[i]
        next_frame = frames[i+1]
        
        # If two code editors exist directly next to each other in sequence
        if current_frame.next_sibling == next_frame or current_frame.next_sibling.next_sibling == next_frame:
            grid_container = soup.new_tag('div', attrs={'class': 'grid grid-cols-1 md:grid-cols-2 gap-6 my-8 w-full'})
            current_frame.insert_before(grid_container)
            grid_container.append(current_frame)
            grid_container.append(next_frame)
            # Advance loop index past combined set
            i += 2
        else:
            i += 1

    # 2. Build the Centered Core Hero Marketing Panel & CTA (t3.codes Clone)
    hero_html = '''
    <section class="text-center py-20 max-w-4xl mx-auto space-y-8 relative">
        <h1 class="text-5xl sm:text-7xl font-extrabold tracking-tight text-white leading-[1.05] tracking-tighter font-sans">
            The open-source <br>
            <span class="text-transparent bg-clip-text bg-gradient-to-r from-white via-zinc-200 to-zinc-500">control plane for coding agents.</span>
        </h1>
        <p class="text-[#8e8e93] text-lg sm:text-xl font-normal max-w-2xl mx-auto leading-relaxed font-sans">
            Orchestrate Claude Code, Cursor, and terminal agents from a single structured layer. Turn your development loops into highly compressed intent declarations.
        </p>
        
        <!-- Large Centered Action Button Block -->
        <div class="pt-4 flex flex-col sm:flex-row items-center justify-center gap-4 max-w-md mx-auto">
            <a href="https://github.com" target="_blank" class="w-full sm:w-auto bg-white text-black px-6 py-3.5 rounded-lg font-bold text-sm hover:bg-zinc-200 transition-all shadow-lg flex items-center justify-center space-x-2">
                <span>Deploy Globally</span>
            </a>
            <a href="https://github.com" target="_blank" class="w-full sm:w-auto text-xs font-semibold text-[#8e8e93] hover:text-white transition-colors flex items-center justify-center space-x-1">
                <span>Steal our code (legally)</span>
                <span class="text-[10px] text-zinc-600">↗</span>
            </a>
        </div>
        
        <!-- Terse Inline Shell Input Block -->
        <div class="pt-6 flex justify-center">
            <div class="bg-[#09090b] border border-[#1c1c1e] px-4 py-3 rounded-lg flex items-center space-x-3 text-zinc-300 w-full max-w-lg shadow-xl hover:border-zinc-800 transition-colors">
                <span class="text-cyan-400 font-bold select-none text-xs font-mono">\$</span>
                <input type="text" readonly value="curl -sSL https://githubusercontent.com | bash" 
                       class="bg-transparent border-none focus:outline-none font-mono text-xs sm:text-sm w-full select-all text-[#ededed]">
            </div>
        </div>
    </section>
    '''

    compiled_body = hero_html + f'<div class="max-w-4xl mx-auto markdown-body">{str(soup)}</div>'
    final_output = template.replace("<!-- {{VAIB_DYNAMIC_MARKDOWN_BODY}} -->", compiled_body)

    with open(output_path, "w") as out:
        out.write(final_output)
    print("🚀 Premium website rebuilt successfully to t3 design system specs!")

if __name__ == "__main__":
    compile_premium_site()
