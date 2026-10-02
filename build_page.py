#!/usr/bin/env python3
import os
import re
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

    # Clear out git repository frontmatter blocks
    if md_text.startswith("---"):
        parts = md_text.split("---", 2)
        if len(parts) >= 3:
            md_text = parts[2]

    # 1. Custom Hero Segment Processing (Extract and build t3 header)
    hero_title = "The linguistic wrapper<br>for coding agents."
    tagline = "Turn your development loops into a high-leverage intent architecture playground while saving up to 75% on token bills."
    
    hero_html = f'''
    <section class="text-center py-12 max-w-3xl mx-auto space-y-6">
        <h1 class="text-4xl sm:text-6xl font-black tracking-tight text-white leading-[1.1] font-sans">
            {hero_title}
        </h1>
        <p class="text-zinc-400 text-lg sm:text-xl font-medium leading-relaxed max-w-2xl mx-auto">
            {tagline}
        </p>
        <div class="pt-6 flex justify-center">
            <div class="bg-zinc-900/60 border border-zinc-800 px-4 py-3.5 rounded-xl flex items-center space-x-3 text-zinc-300 w-full max-w-lg shadow-2xl backdrop-blur-sm group hover:border-zinc-700 transition-colors">
                <span class="mono text-cyan-400 font-bold select-none text-sm font-mono">\$</span>
                <input type="text" readonly value="curl -sSL https://githubusercontent.com | bash" class="bg-transparent border-none focus:outline-none mono text-xs sm:text-sm w-full select-all overflow-x-auto text-zinc-200">
            </div>
        </div>
    </section>
    '''

    # Convert core body elements cleanly via markdown compiler engine extensions
    html_body = markdown.markdown(md_text, extensions=['tables', 'fenced_code'])

    # 2. Structural Regular Expression replacements to convert markdown defaults into sleek t3 metrics cards
    # Wrap standard headers with sleek underlines
    html_body = re.sub(r'<h2>(.*?)</h2>', r'<h2 class="text-2xl font-bold tracking-tight text-white border-b border-zinc-900 pb-3 mt-16 mb-6 flex items-center">\1</h2>', html_body)
    html_body = re.sub(r'<h3>(.*?)</h3>', r'<h3 class="text-lg font-semibold tracking-tight text-zinc-100 mt-8 mb-4 font-mono text-cyan-400">\1</h3>', html_body)
    html_body = re.sub(r'<p>(.*?)</p>', r'<p class="text-zinc-400 text-base leading-relaxed mb-4 font-sans">\1</p>', html_body)
    
    # Restyle tables to capture high-density grid lines
    html_body = re.sub(r'<table>', r'<div class="overflow-x-auto my-6 border border-zinc-900 rounded-xl bg-zinc-950/20 backdrop-blur-sm"><table class="w-full text-left border-collapse text-sm">', html_body)
    html_body = re.sub(r'</table>', r'</table></div>', html_body)
    html_body = re.sub(r'<th>(.*?)</th>', r'<th class="bg-zinc-900/40 px-4 py-3 text-zinc-200 font-semibold border-b border-zinc-900 font-sans tracking-wide">\1</th>', html_body)
    html_body = re.sub(r'<td>(.*?)</td>', r'<td class="px-4 py-3.5 text-zinc-400 border-b border-zinc-900/60 font-mono text-xs">\1</td>', html_body)

    # Wrap code blocks inside container frames
    html_body = re.sub(r'<pre><code class="(.*?)">', r'<div class="my-6 border border-zinc-900 rounded-xl bg-zinc-950/40 backdrop-blur-sm overflow-hidden shadow-2xl"><div class="bg-zinc-900/40 px-4 py-2 border-b border-zinc-900 text-[11px] text-zinc-500 font-mono tracking-wider flex items-center space-x-1.5"><span class="w-2.5 h-2.5 rounded-full bg-zinc-800"></span><span class="w-2.5 h-2.5 rounded-full bg-zinc-800"></span><span>\1 script</span></div><pre class="p-5 overflow-x-auto text-zinc-300 font-mono text-xs sm:text-sm leading-relaxed"><code>', html_body)
    html_body = re.sub(r'</code></pre>', r'</code></pre></div>', html_body)
    html_body = re.sub(r'(?<!<pre>)<code>(.*?)</code>', r'<code class="px-1.5 py-0.5 bg-zinc-900 border border-zinc-800 text-cyan-400 rounded-md font-mono text-xs mx-0.5">\1</code>', html_body)
    
    # Style standard blockquotes like highlighted tips
    html_body = re.sub(r'<blockquote>', r'<blockquote class="border-l-2 border-cyan-500 bg-zinc-900/20 px-4 py-3 rounded-r-xl italic text-zinc-300 my-6 max-w-2xl text-sm leading-relaxed">', html_body)

    # Combine everything and populate the template file frame
    final_output = template.replace("<!-- {{VAIB_DYNAMIC_MARKDOWN_BODY}} -->", hero_html + html_body)

    with open(output_path, "w") as out:
        out.write(final_output)
    print("✨ index.html built successfully with premium t3.codes aesthetics!")

if __name__ == "__main__":
    compile_premium_site()
