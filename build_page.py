#!/usr/bin/env python3
import os
from bs4 import BeautifulSoup
import markdown

def syntax_highlight_vaib(raw_code):
    """Safely tokenizes the custom vaib syntax grammar primitives for light highlighting inside the dark box."""
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
        
    # Standard configuration comment tracks
    raw_code = raw_code.replace("# ", "<span class='token-comment'># ")
    return raw_code

def compile_premium_site():
    readme_path = "README.md"
    template_path = "template.html"
    output_path = "index.html"

    if not os.path.exists(readme_path) or not os.path.exists(template_path):
        print("Missing setup file configurations.")
        return

    with open(readme_path, "r") as r:
        md_text = r.read()
    with open(template_path, "r") as t:
        template = t.read()

    # Clear out git repository frontmatter blocks
    if md_text.startswith("---"):
        parts = md_text.split("---", 2)
        if len(parts) >= 3:
            md_text = parts

    # Parse baseline markdown to standard HTML nodes
    html_raw = markdown.markdown(md_text, extensions=['tables', 'fenced_code'])
    soup = BeautifulSoup(html_raw, 'html.parser')

    # Convert titles and insert the clean text "OPEN SOURCE COMPONENT" sub-banners
    for h2 in soup.find_all('h2'):
        if "Contributing" in h2.text or "Upstream" in h2.text:
            banner = soup.new_tag('div', attrs={'class': 'text-center text-[10px] uppercase font-mono font-bold tracking-widest text-[#636366] mb-2 mt-16'})
            banner.string = "OPEN SOURCE COMPONENT"
            h2.insert_before(banner)
        h2['class'] = 'text-2xl sm:text-3xl font-extrabold tracking-tight text-white border-b border-[#1c1c1e] pb-3 mt-16 mb-6 tracking-tighter font-sans'

    # Package code sections into clean, single-frame dark file panels (White text baseline)
    for pre in soup.find_all('pre'):
        code = pre.find('code')
        if code:
            highlighted_content = syntax_highlight_vaib(code.decode_contents())
            code.clear()
            code.append(BeautifulSoup(highlighted_content, 'html.parser'))
            
            frame = soup.new_tag('div', attrs={'class': 'my-6 border border-[#1c1c1e] rounded-xl bg-[#09090b] overflow-hidden shadow-2xl w-full max-w-full'})
            pre.wrap(frame)
            
            header = soup.new_tag('div', attrs={'class': 'bg-[#121214] px-4 py-2.5 border-b border-[#1c1c1e] text-[10px] text-[#636366] font-mono tracking-wider flex items-center space-x-1.5 select-none'})
            dot1 = soup.new_tag('span', attrs={'class': 'w-1.5 h-1.5 rounded-full bg-[#ff3b30]/30'})
            dot2 = soup.new_tag('span', attrs={'class': 'w-1.5 h-1.5 rounded-full bg-[#ff9500]/30'})
            dot3 = soup.new_tag('span', attrs={'class': 'w-1.5 h-1.5 rounded-full bg-[#34c759]/30'})
            label = soup.new_tag('span', attrs={'class': 'pl-1 text-zinc-500 text-[9px] tracking-wider uppercase font-mono'})
            label.string = "vaib logic matrix"
            
            header.append(dot1)
            header.append(dot2)
            header.append(dot3)
            header.append(label)
            frame.insert(0, header)
            
            pre['class'] = 'p-5 overflow-x-auto text-zinc-100 font-mono text-[13px] leading-relaxed bg-transparent border-0 m-0 w-full'
            code['class'] = 'p-0 bg-transparent border-0 text-zinc-100 font-mono text-[13px]'

    # Apply global class designations to raw components
    for el in soup.find_all(True, recursive=False):
        if el.name in ['h3', 'p', 'ul', 'ol', 'blockquote', 'table']:
            el['class'] = el.get('class', []) + ['markdown-body']

    # 3. Render Your Authentic, Centered vaib Hero Header Section (No t3 plagiarism!)
    hero_html = '''
    <section class="text-left pt-16 pb-12 space-y-6 max-w-2xl font-sans">
        <h1 class="text-4xl sm:text-5xl font-black tracking-tight text-white leading-[1.1] tracking-tighter">
            The open-source control plane <br>
            <span class="text-zinc-500">for vibe engineering teams.</span>
        </h1>
        <p class="text-zinc-400 text-[15px] font-normal leading-relaxed">
            Stop typing long paragraphs of instructions to your terminal tools. vaib converts hyper-dense architectural intentions and loose logical flows into bulletproof production-grade repositories.
        </p>
        
        <!-- Premium Action Badges Links -->
        <div class="pt-2 flex items-center space-x-4">
            <a href="https://github.com" target="_blank" class="bg-zinc-100 text-black px-4 py-2 rounded-lg font-bold text-xs hover:bg-zinc-200 transition-all shadow-sm">
                Deploy Framework
            </a>
            <a href="https://github.com" target="_blank" class="text-xs font-semibold text-zinc-500 hover:text-zinc-300 transition-colors flex items-center space-x-0.5">
                <span>Steal our code (legally)</span>
                <span class="text-[9px] font-light text-zinc-600">↗</span>
            </a>
        </div>
        
        <!-- Terse curl Installer Box -->
        <div class="pt-4 max-w-xl">
            <div class="bg-[#09090b] border border-[#1c1c1e] px-4 py-3 rounded-lg flex items-center space-x-3 text-zinc-300 shadow-md hover:border-zinc-800 transition-colors">
                <span class="text-zinc-600 font-bold select-none text-xs font-mono">\$</span>
                <input type="text" readonly value="curl -sSL https://githubusercontent.com | bash" 
                       class="bg-transparent border-none focus:outline-none font-mono text-xs w-full select-all text-zinc-200">
            </div>
        </div>
    </section>
    '''

    compiled_body = hero_html + f'<div class="markdown-body max-w-3xl mx-auto">{str(soup)}</div>'
    final_output = template.replace("<!-- {{VAIB_DYNAMIC_MARKDOWN_BODY}} -->", compiled_body)

    with open(output_path, "w") as out:
        out.write(final_output)
    print("🚀 Premium website rebuilt successfully to precise vaib structural specifications!")

if __name__ == "__main__":
    compile_premium_site()
