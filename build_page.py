#!/usr/bin/env python3
import os
from bs4 import BeautifulSoup
import markdown

def compile_premium_site():
    readme_path = "README.md"
    template_path = "template.html"
    output_path = "index.html"

    if not os.path.exists(readme_path) or not os.path.exists(template_path):
        print("Missing baseline files for compilation pipeline.")
        return

    with open(readme_path, "r") as r:
        md_text = r.read()
    with open(template_path, "r") as t:
        template = t.read()

    # Clear out repository frontmatter blocks safely
    if md_text.startswith("---"):
        parts = md_text.split("---", 2)
        if len(parts) >= 3:
            md_text = parts[2]

    # Pre-render standard markdown text to basic HTML first
    html_raw = markdown.markdown(md_text, extensions=['tables', 'fenced_code'])
    
    # Initialize BeautifulSoup to parse structural layout nodes reliably
    soup = BeautifulSoup(html_raw, 'html.parser')

    # 1. Transform Headings with clean structural properties
    for h1 in soup.find_all('h1'):
        h1['class'] = 'text-3xl font-black text-white mt-12 mb-6 border-b border-zinc-900 pb-3 tracking-tight font-sans'
    for h2 in soup.find_all('h2'):
        h2['class'] = 'text-xl font-bold text-white mt-10 mb-4 border-b border-zinc-900 pb-2 tracking-tight font-sans'
    for h3 in soup.find_all('h3'):
        h3['class'] = 'text-base font-semibold text-cyan-400 mt-6 mb-3 font-mono tracking-wider uppercase'

    # 2. Transform Paragraphs, Lists & Blocks safely
    for p in soup.find_all('p'):
        p['class'] = 'text-zinc-400 text-sm leading-relaxed mb-4 font-sans'
    for ul in soup.find_all('ul'):
        ul['class'] = 'list-disc list-inside text-zinc-400 text-sm pl-4 space-y-2 mb-4 font-sans'
    for li in soup.find_all('li'):
        li['class'] = 'leading-relaxed'
    for blockquote in soup.find_all('blockquote'):
        blockquote['class'] = 'border-l-2 border-cyan-500 bg-zinc-900/20 px-4 py-3 rounded-r-xl italic text-zinc-300 my-6 max-w-2xl text-xs sm:text-sm leading-relaxed font-sans'

    # 3. Transform Complex High-Density Data Tables
    for table in soup.find_all('table'):
        # Wrap table with a clean responsive scrolling frame container
        wrapper = soup.new_tag('div', attrs={'class': 'overflow-x-auto my-6 border border-zinc-900 rounded-xl bg-zinc-950/20 backdrop-blur-sm'})
        table.wrap(wrapper)
        table['class'] = 'w-full text-left border-collapse text-xs sm:text-sm'
        
    for th in soup.find_all('th'):
        th['class'] = 'bg-zinc-900/50 px-4 py-3 text-zinc-200 font-bold border-b border-zinc-900 font-sans tracking-wide'
    for td in soup.find_all('td'):
        td['class'] = 'px-4 py-3 text-zinc-400 border-b border-zinc-900/60 font-mono text-[11px] sm:text-xs'

    # 4. Transform Script Code Snippets and Inline Keyboards
    for code in soup.find_all('code'):
        # If it is inside a pre-formatted block code array
        if code.parent and code.parent.name == 'pre':
            pre = code.parent
            # Check what framework language it is
            lang_class = code.get('class', ['script'])[0]
            lang_name = lang_class.replace('language-', '') if 'language-' in lang_class else lang_class
            
            # Wrap pre with a t3-style mock window frame shell
            frame = soup.new_tag('div', attrs={'class': 'my-6 border border-zinc-900 rounded-xl bg-zinc-950/40 backdrop-blur-sm overflow-hidden shadow-2xl'})
            pre.wrap(frame)
            
            # Prepend a premium script header tab item box
            header = soup.new_tag('div', attrs={'class': 'bg-zinc-900/40 px-4 py-2 border-b border-zinc-900 text-[10px] text-zinc-500 font-mono tracking-wider flex items-center space-x-2'})
            dot1 = soup.new_tag('span', attrs={'class': 'w-2 h-2 rounded-full bg-zinc-800'})
            dot2 = soup.new_tag('span', attrs={'class': 'w-2 h-2 rounded-full bg-zinc-800'})
            label = soup.new_tag('span')
            label.string = f"{lang_name.upper()} MATRIX"
            
            header.append(dot1)
            header.append(dot2)
            header.append(label)
            frame.insert(0, header)
            
            pre['class'] = 'p-5 overflow-x-auto text-zinc-300 font-mono text-xs sm:text-sm leading-relaxed bg-transparent border-0 m-0'
            code['class'] = 'p-0 bg-transparent border-0 text-zinc-200 font-mono text-xs sm:text-sm'
        else:
            # Inline character text highlight mapping
            code['class'] = 'px-1.5 py-0.5 bg-zinc-900 border border-zinc-800 text-cyan-400 rounded-md font-mono text-xs mx-0.5'

    # 5. Build Hero Header Module Component dynamically
    hero_soup = BeautifulSoup('''
    <section class="text-center py-12 max-w-3xl mx-auto space-y-6">
        <h1 class="text-4xl sm:text-6xl font-black tracking-tight text-white leading-[1.1] font-sans">
            The open-source wrapper<br>for coding agents.
        </h1>
        <p class="text-zinc-400 text-base sm:text-lg font-medium leading-relaxed max-w-2xl mx-auto font-sans">
            vaib is a compressed linguistic framework built for Vibe Engineers. Write ultra-dense intent blueprints and let the underlying model handle the syntax execution loops perfectly.
        </p>
        <div class="pt-4 flex justify-center">
            <div class="bg-zinc-900/60 border border-zinc-800 px-4 py-3.5 rounded-xl flex items-center space-x-3 text-zinc-300 w-full max-w-lg shadow-2xl backdrop-blur-sm group hover:border-zinc-700 transition-colors">
                <span class="mono text-cyan-400 font-bold select-none text-sm font-mono">\$</span>
                <input type="text" readonly value="curl -sSL https://githubusercontent.com | bash" class="bg-transparent border-none focus:outline-none mono text-xs sm:text-sm w-full select-all overflow-x-auto text-zinc-200">
            </div>
        </div>
    </section>
    ''', 'html.parser')

    # Merge structural parts together cleanly
    compiled_body = str(hero_soup) + str(soup)
    final_output = template.replace("<!-- {{VAIB_DYNAMIC_MARKDOWN_BODY}} -->", compiled_body)

    with open(output_path, "w") as out:
        out.write(final_output)
    print("🚀 Premium static landing page safely generated via node-tree compiler pipeline!")

if __name__ == "__main__":
    compile_premium_site()
