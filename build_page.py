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

    # Clear out repo frontmatter layers cleanly
    if md_text.startswith("---"):
        parts = md_text.split("---", 2)
        if len(parts) >= 3:
            md_text = parts

    # Parse baseline markdown into clean HTML first
    html_raw = markdown.markdown(md_text, extensions=['tables', 'fenced_code'])
    soup = BeautifulSoup(html_raw, 'html.parser')

    # 1. Transform Headings with Big, Fat t3-Style Typography
    for h1 in soup.find_all('h1'):
        h1['class'] = 'text-3xl sm:text-4xl font-extrabold tracking-tight text-white mt-16 mb-6 border-b border-zinc-900 pb-3 font-sans'
    for h2 in soup.find_all('h2'):
        h2['class'] = 'text-2xl font-bold tracking-tight text-white mt-16 mb-6 border-b border-zinc-900 pb-3 font-sans'
    for h3 in soup.find_all('h3'):
        h3['class'] = 'text-base font-bold text-cyan-400 mt-8 mb-4 font-mono tracking-wider uppercase'

    # 2. Transform Paragraphs, Lists & Blockquotes safely
    for p in soup.find_all('p'):
        p['class'] = 'text-zinc-400 text-base leading-relaxed mb-6 font-sans'
    for ul in soup.find_all('ul'):
        ul['class'] = 'list-disc list-inside text-zinc-400 text-sm pl-4 space-y-2.5 mb-6 font-sans'
    for li in soup.find_all('li'):
        li['class'] = 'leading-relaxed'
    for blockquote in soup.find_all('blockquote'):
        blockquote['class'] = 'border-l-2 border-cyan-500 bg-zinc-900/30 px-5 py-4 rounded-r-xl italic text-zinc-300 my-6 max-w-2xl text-sm leading-relaxed font-sans'

    # 3. Transform Complex Metrics & Layout Data Tables
    for table in soup.find_all('table'):
        wrapper = soup.new_tag('div', attrs={'class': 'overflow-x-auto my-6 border border-zinc-900 rounded-xl bg-zinc-950/40 backdrop-blur-sm'})
        table.wrap(wrapper)
        table['class'] = 'w-full text-left border-collapse text-xs sm:text-sm'
        
    for th in soup.find_all('th'):
        th['class'] = 'bg-zinc-900/60 px-4 py-3.5 text-zinc-200 font-bold border-b border-zinc-900 font-sans tracking-wide'
    for td in soup.find_all('td'):
        td['class'] = 'px-4 py-3.5 text-zinc-400 border-b border-zinc-900/60 font-mono text-xs'

    # 4. Transform Code Snippet Blocks and Micro Primitives
    for code in soup.find_all('code'):
        if code.parent and code.parent.name == 'pre':
            pre = code.parent
            lang_class = code.get('class', ['script'])
            lang_name = lang_class[0].replace('language-', '') if 'language-' in lang_class[0] else 'script'
            
            # Create a t3-inspired structural mock code editor panel box
            frame = soup.new_tag('div', attrs={'class': 'my-8 border border-zinc-900 rounded-xl bg-[#09090b]/80 backdrop-blur-md overflow-hidden shadow-2xl'})
            pre.wrap(frame)
            
            # Inject top tracking dot controls layer
            header = soup.new_tag('div', attrs={'class': 'bg-zinc-900/40 px-4 py-2.5 border-b border-zinc-900 text-[10px] text-zinc-500 font-mono tracking-widest flex items-center space-x-2'})
            dot1 = soup.new_tag('span', attrs={'class': 'w-2 h-2 rounded-full bg-zinc-800/80'})
            dot2 = soup.new_tag('span', attrs={'class': 'w-2 h-2 rounded-full bg-zinc-800/80'})
            label = soup.new_tag('span')
            label.string = f"{lang_name.upper()} DATA MODEL"
            
            header.append(dot1)
            header.append(dot2)
            header.append(label)
            frame.insert(0, header)
            
            pre['class'] = 'p-5 overflow-x-auto text-zinc-300 font-mono text-xs sm:text-sm leading-relaxed bg-transparent border-0 m-0'
            code['class'] = "p-0 bg-transparent border-0 text-zinc-200 font-['JetBrains_Mono',monospace] text-xs sm:text-sm"
        else:
            # Inline primitive highlights
            code['class'] = "px-1.5 py-0.5 bg-zinc-900 border border-zinc-800 text-cyan-400 rounded-md font-['JetBrains_Mono',monospace] text-xs mx-0.5"

    # 5. Build the Big Fat Hero Title & Terminal Input Box (t3.codes Clone)
    hero_soup = BeautifulSoup('''
    <section class="text-center py-20 max-w-4xl mx-auto space-y-8 relative">
        <h1 class="text-5xl sm:text-7xl font-black tracking-tight text-white leading-[1.05] font-sans">
            The shorthand engine <br>
            <span class="text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 via-sky-400 to-blue-500">for vibe coding agents.</span>
        </h1>
        <p class="text-zinc-400 text-lg sm:text-xl font-medium leading-relaxed max-w-2xl mx-auto font-sans">
            vaib is a zero-compilation linguistic wrapper for Claude Code and Cursor. Write high-leverage intent architecture trees and let the AI manage the syntax bloat.
        </p>
        <div class="pt-6 flex justify-center">
            <div class="bg-zinc-900/50 border border-zinc-800 px-4 py-3.5 rounded-xl flex items-center space-x-3 text-zinc-300 w-full max-w-xl shadow-2xl backdrop-blur-md hover:border-zinc-700 transition-colors">
                <span class="text-cyan-500 font-bold select-none text-sm font-mono">\$</span>
                <input type="text" readonly value="curl -sSL https://githubusercontent.com | bash" 
                       class="bg-transparent border-none focus:outline-none font-mono text-xs sm:text-sm w-full select-all text-zinc-200">
            </div>
        </div>
    </section>
    ''', 'html.parser')

    # Stitch the sections together
    compiled_body = str(hero_soup) + str(soup)
    final_output = template.replace("<!-- {{VAIB_DYNAMIC_MARKDOWN_BODY}} -->", compiled_body)

    with open(output_path, "w") as out:
        out.write(final_output)
    print("🚀 Premium static page generated flawlessly with native pre-baked Tailwind parameters!")

if __name__ == "__main__":
    compile_premium_site()
