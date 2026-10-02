# Code Editor Window Component
for pre in soup.find_all('pre'):
    code = pre.find('code')
    if code:
        highlighted_content = syntax_highlight_vaib(code.decode_contents())
        code.clear()
        code.append(BeautifulSoup(highlighted_content, 'html.parser'))
        
        frame = soup.new_tag('div', attrs={'class': 'my-6 border border-zinc-800/80 rounded-xl bg-[#090d16] overflow-hidden shadow-2xl w-full'})
        pre.wrap(frame)
        
        header = soup.new_tag('div', attrs={'class': 'bg-[#0d1322] px-4 py-2 border-b border-zinc-800/80 text-xs text-zinc-400 font-mono flex items-center justify-between select-none'})
        
        left_side = soup.new_tag('div', attrs={'class': 'flex items-center space-x-2'})
        dot1 = soup.new_tag('span', attrs={'class': 'w-2.5 h-2.5 rounded-full bg-red-500/60 inline-block'})
        dot2 = soup.new_tag('span', attrs={'class': 'w-2.5 h-2.5 rounded-full bg-yellow-500/60 inline-block'})
        dot3 = soup.new_tag('span', attrs={'class': 'w-2.5 h-2.5 rounded-full bg-green-500/60 inline-block'})
        label = soup.new_tag('span', attrs={'class': 'pl-2 text-zinc-400 text-xs font-mono'})
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
        
        # Ensure pre and code have clean transparency and block layout
        pre['class'] = 'p-4 sm:p-5 overflow-x-auto text-zinc-100 font-mono text-[13px] leading-relaxed bg-transparent border-0 m-0 w-full block'
        code['class'] = 'p-0 bg-transparent border-0 font-mono block'