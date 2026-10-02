#!/usr/bin/env python3
import os
from bs4 import BeautifulSoup
import markdown

def compile_premium_site():
    readme_path = "README.md"
    template_path = "template.html"
    output_path = "index.html"

    if not os.path.exists(readme_path) or not os.path.exists(template_path):
        print("Missing setup source configurations.")
        return

    with open(readme_path, "r") as r:
        md_text = r.read()
    with open(template_path, "r") as t:
        template = t.read()

    # Clear repository frontmatter configuration blocks safely
    if md_text.startswith("---"):
        parts = md_text.split("---", 2)
        if len(parts) >= 3:
            md_text = parts[2]

    # Render basic markdown to HTML tree layers
    html_raw = markdown.markdown(md_text, extensions=['tables', 'fenced_code'])
    soup = BeautifulSoup(html_raw, 'html.parser')

    # Apply strict markdown-body container classes to root elements
    for el in soup.find_all(True, recursive=False):
        if el.name in ['h2', 'h3', 'p', 'ul', 'ol', 'blockquote', 'table']:
            # Append local tracking class signatures
            existing_classes = el.get('class', [])
            if not existing_classes:
                el['class'] = f"markdown-body"

    # Process all headers contextually and add clean tracking sub-banners
    for h2 in soup.find_all('h2'):
        if "Contributing" in h2.text or "Upstream" in h2.text:
            banner = soup.new_tag('div', attrs={'class': 'text-center text-[10px] uppercase font-mono font-bold tracking-widest text-zinc-600 mb-2 mt-16'})
            banner.string = "OPEN SOURCE COMPONENT"
            h2.insert_before(banner)

    # Re-structure Code Snippets into precise Single-Frame Dark Terminal Panels
    for pre in soup.find_all('pre'):
        code = pre.find('code')
        if code:
            # Wrap pre inside a pristine single container block frame
            frame = soup.new_tag('div', attrs={'class': 'my-6 border border-zinc-900 rounded-xl bg-[#09090b] overflow-hidden shadow-2xl w-full max-w-full'})
            pre.wrap(frame)
            
            # Inject top header panel dot controls
            header = soup.new_tag('div', attrs={'class': 'bg-[#121214] px-4 py-2.5 border-b border-zinc-900 text-[10px] text-zinc-500 font-mono tracking-wider flex items-center space-x-1.5 select-none'})
            dot1 = soup.new_tag('span', attrs={'class': 'w-1.5 h-1.5 rounded-full bg-zinc-800'})
            dot2 = soup.new_tag('span', attrs={'class': 'w-1.5 h-1.5 rounded-full bg-zinc-800'})
            dot3 = soup.new_tag('span', attrs={'class': 'w-1.5 h-1.5 rounded-full bg-zinc-800'})
            label = soup.new_tag('span', attrs={'class': 'pl-1 text-zinc-500 text-[9px] uppercase tracking-widest'})
            label.string = "vaib file block"
            
            header.append(dot1)
            header.append(dot2)
            header.append(dot3)
            header.append(label)
            frame.insert(0, header)
            
            # Reset text to highly readable clean white monospaced canvas layouts
            pre['class'] = 'p-5 overflow-x-auto text-zinc-100 font-mono text-[13px] leading-relaxed bg-transparent border-0 m-0'
            code['class'] = 'p-0 bg-transparent border-0 text-zinc-100 font-mono text-[13px]'

    # 3. Build the Premium t3.codes Hero Blueprint Header Block
    hero_html = '''
    <section class="text-left pt-16 pb-12 space-y-6 max-w-2xl">
        <h1 class="text-4xl sm:text-5xl font-black tracking-tight text-white leading-[1.1] tracking-tighter font-sans">
            The open-source control plane <br>
            <span class="text-zinc-500">for coding agents.</span>
        </h1>
        <p class="text-zinc-400 text-[15px] font-normal leading-relaxed font-sans">
            Orchestrate Claude Code, Cursor, and terminal agents from a single structured layer. Turn your development loops into highly compressed intent declarations.
        </p>
        
        <!-- Action Buttons Block -->
        <div class="pt-2 flex items-center space-x-4">
            <a href="https://github.com" target="_blank" class="bg-zinc-100 text-black px-4 py-2 rounded-lg font-bold text-xs hover:bg-zinc-200 transition-all shadow-sm">
                Deploy Globally
            </a>
            <a href="https://github.com" target="_blank" class="text-xs font-semibold text-zinc-500 hover:text-zinc-300 transition-colors flex items-center space-x-0.5">
                <span>Steal our code (legally)</span>
                <span class="text-[9px] font-light text-zinc-600">↗</span>
            </a>
        </div>
        
        <!-- Terse Inline Shell Input Block -->
        <div class="pt-4 max-w-xl">
            <div class="bg-[#09090b] border border-zinc-900 px-4 py-3 rounded-lg flex items-center space-x-3 text-zinc-300 shadow-md hover:border-zinc-800 transition-colors">
                <span class="text-zinc-600 font-bold select-none text-xs font-mono">\$</span>
                <input type="text" readonly value="curl -sSL https://githubusercontent.com | bash" 
                       class="bg-transparent border-none focus:outline-none font-mono text-xs w-full select-all text-zinc-200">
            </div>
        </div>
    </section>
    '''

    # Blend Hero block and inject everything cleanly under the markdown wrapper layout boundaries
    compiled_body = hero_html + f'<div class="markdown-body max-w-3xl mx-auto">{str(soup)}</div>'
    final_output = template.replace("<!-- {{VAIB_DYNAMIC_MARKDOWN_BODY}} -->", compiled_body)

    with open(output_path, "w") as out:
        out.write(final_output)
    print("🚀 Premium website successfully generated via loop-safe node compiler pipeline!")

if __name__ == "__main__":
    compile_premium_site()
