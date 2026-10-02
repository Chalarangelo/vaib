#!/usr/bin/env python3
import os
from bs4 import BeautifulSoup
import markdown

def compile_premium_site():
    readme_path = "README.md"
    template_path = "template.html"
    output_path = "index.html"

    if not os.path.exists(readme_path) or not os.path.exists(template_path):
        print("Missing setup configurations.")
        return

    with open(readme_path, "r") as r:
        md_text = r.read()
    with open(template_path, "r") as t:
        template = t.read()

    # Clear repository frontmatter layers
    if md_text.startswith("---"):
        parts = md_text.split("---", 2)
        if len(parts) >= 3:
            md_text = parts[2]

    # Pre-render core markdown logic
    html_raw = markdown.markdown(md_text, extensions=['tables', 'fenced_code'])
    soup = BeautifulSoup(html_raw, 'html.parser')

    # Re-structure markdown nodes cleanly with production Tailwind classes
    for h2 in soup.find_all('h2'):
        h2['class'] = 'text-2xl sm:text-3xl font-extrabold tracking-tight text-white border-b border-zinc-900 pb-3 mt-20 mb-6'
    for h3 in soup.find_all('h3'):
        h3['class'] = 'text-lg font-bold text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 to-sky-400 mt-10 mb-4 tracking-tight'
    for p in soup.find_all('p'):
        p['class'] = 'text-zinc-400 text-base leading-relaxed mb-4'
    for ul in soup.find_all('ul'):
        ul['class'] = 'list-disc list-inside text-zinc-400 text-sm pl-2 space-y-2 mb-6'
    for blockquote in soup.find_all('blockquote'):
        blockquote['class'] = 'border-l-2 border-cyan-500 bg-zinc-900/30 px-5 py-4 rounded-r-xl italic text-zinc-200 my-6 text-sm max-w-3xl leading-relaxed'

    # Format data tables cleanly
    for table in soup.find_all('table'):
        wrapper = soup.new_tag('div', attrs={'class': 'overflow-x-auto my-6 border border-zinc-900 rounded-xl bg-zinc-950/20 backdrop-blur-sm'})
        table.wrap(wrapper)
        table['class'] = 'w-full text-left border-collapse text-xs sm:text-sm'

    # Build sleek Code Editor mock panels matching t3.codes exactly
    for code in soup.find_all('code'):
        if code.parent and code.parent.name == 'pre':
            pre = code.parent
            lang_class = code.get('class', ['script'])
            lang_name = lang_class[0].replace('language-', '') if 'language-' in lang_class[0] else 'script'
            
            frame = soup.new_tag('div', attrs={'class': 'my-8 border border-zinc-900 rounded-xl bg-[#09090b]/90 overflow-hidden shadow-2xl transition-all duration-300 hover:border-zinc-800'})
            pre.wrap(frame)
            
            header = soup.new_tag('div', attrs={'class': 'bg-[#121214] px-4 py-3 border-b border-zinc-900 text-[10px] text-zinc-500 font-mono tracking-widest flex items-center space-x-2 select-none'})
            dot1 = soup.new_tag('span', attrs={'class': 'w-2 h-2 rounded-full bg-red-500/60'})
            dot2 = soup.new_tag('span', attrs={'class': 'w-2 h-2 rounded-full bg-yellow-500/60'})
            dot3 = soup.new_tag('span', attrs={'class': 'w-2 h-2 rounded-full bg-green-500/60'})
            label = soup.new_tag('span', attrs={'class': 'pl-1 text-zinc-400 font-medium'})
            label.string = f"{lang_name.upper()} RUNTIME LAYER"
            
            header.append(dot1)
            header.append(dot2)
            header.append(dot3)
            header.append(label)
            frame.insert(0, header)
            
            pre['class'] = 'p-5 overflow-x-auto text-zinc-300 font-mono text-xs sm:text-sm leading-relaxed bg-transparent border-0 m-0'
            code['class'] = 'p-0 bg-transparent border-0 text-zinc-200 font-mono text-xs sm:text-sm'
        else:
            code['class'] = 'px-1.5 py-0.5 bg-zinc-900 border border-zinc-800 text-cyan-400 rounded-md font-mono text-xs mx-0.5'

    # 3. Build the Premium t3.codes Hero Blueprint Header
    hero_html = '''
    <section class="text-center py-16 max-w-4xl mx-auto space-y-8 relative">
        <h1 class="text-4xl sm:text-7xl font-black tracking-tight text-white leading-[1.05] max-w-3xl mx-auto">
            The open-source control plane <br>
            <span class="text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 via-sky-400 to-blue-500">for vibe coding agents.</span>
        </h1>
        <p class="text-zinc-400 text-base sm:text-xl font-normal leading-relaxed max-w-2xl mx-auto">
            vaib is a compressed linguistic framework built for Claude Code and Cursor. Write high-leverage intent architecture trees and stop babysitting syntax bloat.
        </p>
        <div class="pt-4 flex flex-col sm:flex-row items-center justify-center gap-4">
            <div class="bg-zinc-900/60 border border-zinc-800 px-4 py-3.5 rounded-xl flex items-center space-x-3 text-zinc-300 w-full max-w-xl shadow-2xl backdrop-blur-sm border-opacity-80">
                <span class="text-cyan-400 font-bold select-none text-sm font-mono">\$</span>
                <input type="text" readonly value="curl -sSL https://githubusercontent.com | bash" 
                       class="bg-transparent border-none focus:outline-none font-mono text-xs sm:text-sm w-full select-all text-zinc-100">
            </div>
        </div>
    </section>
    '''

    # Blend Hero header with structural node arrays
    compiled_body = hero_html + f'<div class="max-w-4xl mx-auto">{str(soup)}</div>'
    final_output = template.replace("<!-- {{VAIB_DYNAMIC_MARKDOWN_BODY}} -->", compiled_body)

    with open(output_path, "w") as out:
        out.write(final_output)
    print("🚀 Premium website successfully generated with absolute t3 specifications!")

if __name__ == "__main__":
    compile_premium_site()
