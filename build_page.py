<!DOCTYPE html>
<html lang="en" class="bg-[#030712] text-zinc-300">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>vaib — Vibe-Accelerated Intent Blocks</title>
    
    <!-- Official Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    
    <!-- Geist + JetBrains Mono Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
    
    <style>
        body { font-family: 'Geist', sans-serif; background-color: #030712; color: #9ca3af; margin: 0; padding: 0; }
        code, pre, .mono { font-family: 'JetBrains Mono', monospace; }
        
        .grid-bg {
            background-size: 32px 32px;
            background-image: radial-gradient(circle, rgba(255, 255, 255, 0.05) 1px, transparent 1px);
            mask-image: radial-gradient(ellipse at top, black 60%, transparent 100%);
            -webkit-mask-image: radial-gradient(ellipse at top, black 60%, transparent 100%);
        }
        
        .markdown-body h1 { font-size: 2rem; font-weight: 800; color: #ffffff; margin-top: 3.5rem; margin-bottom: 1.25rem; border-bottom: 1px solid #1f2937; padding-bottom: 0.5rem; }
        .markdown-body h2 { font-size: 1.5rem; font-weight: 800; color: #ffffff; margin-top: 3rem; margin-bottom: 1rem; border-bottom: 1px solid #1f2937; padding-bottom: 0.5rem; }
        .markdown-body h3 { font-size: 1.1rem; font-weight: 700; color: #38bdf8; margin-top: 2rem; margin-bottom: 0.75rem; text-transform: uppercase; }
        .markdown-body p { color: #9ca3af; font-size: 1rem; line-height: 1.7; margin-bottom: 1.25rem; }
        .markdown-body ul { list-style-type: none; padding-left: 0; margin-bottom: 1.5rem; }
        .markdown-body li { position: relative; padding-left: 1.5rem; margin-bottom: 0.5rem; color: #e5e7eb; font-size: 0.95rem; line-height: 1.6; }
        .markdown-body li::before { content: "•"; position: absolute; left: 0.25rem; color: #a855f7; font-weight: bold; }
        .markdown-body blockquote { border-left: 3px solid #a855f7; background-color: rgba(17, 24, 39, 0.6); padding: 1rem 1.25rem; border-radius: 0 0.5rem 0.5rem 0; color: #e5e7eb; margin: 1.5rem 0; }
        
        .markdown-body table { width: 100%; text-align: left; border-collapse: collapse; margin: 1.5rem 0; font-size: 0.875rem; border: 1px solid #1f2937; border-radius: 0.5rem; overflow: hidden; }
        .markdown-body th { background-color: #111827; padding: 0.75rem 1rem; color: #f3f4f6; font-weight: 600; border-bottom: 1px solid #1f2937; }
        .markdown-body td { padding: 0.75rem 1rem; color: #9ca3af; border-bottom: 1px solid #1f2937; font-family: 'JetBrains Mono', monospace; font-size: 0.8rem; }
        .markdown-body tr:last-child td { border-bottom: 0; }
        
        .markdown-body code { padding: 0.15rem 0.4rem; background-color: #111827; border: 1px solid #1f2937; color: #38bdf8; border-radius: 0.375rem; font-size: 0.85rem; font-family: 'JetBrains Mono', monospace; }
        
        .token-keyword { color: #f43f5e; font-weight: 600; }
        .token-symbol { color: #38bdf8; }
        .token-string { color: #34d399; }
        .token-comment { color: #6b7280; font-style: italic; }
        .token-macro { color: #fbbf24; font-weight: 500; }
    </style>
</head>
<body class="min-h-screen bg-[#030712] text-zinc-300 antialiased flex flex-col justify-between relative">

    <div class="absolute inset-0 pointer-events-none z-0 grid-bg min-h-[1200px]"></div>

    <!-- Header Navigation -->
    <header class="border-b border-zinc-800/80 bg-[#030712]/80 backdrop-blur-md sticky top-0 z-50">
        <div class="max-w-3xl mx-auto px-6 h-16 flex items-center justify-between">
            <div class="flex items-center space-x-3">
                <a href="#" class="text-base font-black text-white tracking-wider uppercase font-sans">vaib</a>
                <span class="px-2 py-0.5 text-[10px] font-semibold bg-purple-500/10 text-purple-400 rounded-full border border-purple-500/20">v1.0</span>
            </div>
            
            <div class="flex items-center space-x-4 font-sans">
                <a href="https://github.com/Chalarangelo/vaib" target="_blank" class="px-3 py-1.5 text-xs font-semibold bg-zinc-900 text-zinc-300 rounded-lg border border-zinc-800 hover:text-white hover:border-zinc-700 transition-all flex items-center space-x-2">
                    <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/></svg>
                    <span>GitHub</span>
                </a>
            </div>
        </div>
    </header>

    <!-- Main Content Canvas -->
    <main class="max-w-3xl mx-auto px-6 py-8 w-full flex-grow relative z-10">
        <div id="vaib-compiled-root" class="w-full">
            <!-- {{VAIB_DYNAMIC_MARKDOWN_BODY}} -->
        </div>
    </main>

    <!-- Footer -->
    <footer class="border-t border-zinc-800/80 py-8 bg-[#030712] relative z-10 text-xs text-zinc-500 font-sans">
        <div class="max-w-3xl mx-auto px-6 flex flex-col sm:flex-row items-center justify-between gap-4">
            <div>
                <span class="font-bold text-zinc-300">vaib</span> &copy; 2026. MIT Licensed.
            </div>
            <div class="flex items-center space-x-4">
                <a href="https://github.com/Chalarangelo/vaib" target="_blank" class="hover:text-zinc-300 transition-colors">Repository</a>
            </div>
        </div>
    </footer>

</body>
</html>