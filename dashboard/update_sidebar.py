import os
import re

files = [
    ('overview.html', 'Overview'),
    ('date_explorer.html', 'Date Explorer'),
    ('monthly_trends.html', 'Monthly Trends'),
    ('pollutant.html', 'Pollutant Explorer'),
    ('predictor.html', 'AQI Predictor'),
    ('correlation.html', 'Correlation Insights')
]

links = [
    ('overview.html', 'Overview', 'dashboard'),
    ('date_explorer.html', 'Date Explorer', 'calendar_month'),
    ('monthly_trends.html', 'Monthly Trends', 'stacked_line_chart'),
    ('pollutant.html', 'Pollutant Explorer', 'air'),
    ('predictor.html', 'AQI Predictor', 'batch_prediction'),
    ('correlation.html', 'Correlation Insights', 'query_stats')
]

for file, current_page in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Generate the nav links
    nav_links = ""
    for href, text, icon in links:
        if text == current_page:
            classes = "flex items-center gap-3 px-4 py-3 bg-[#00b4d8]/10 text-[#00b4d8] border-r-4 border-[#00b4d8] font-medium transition-all duration-200"
        else:
            classes = "flex items-center gap-3 px-4 py-3 text-slate-400 hover:text-slate-200 hover:bg-white/5 font-medium transition-all duration-200"
            
        nav_links += f"""
        <a class="{classes}" href="{href}">
            <span class="material-symbols-outlined" data-icon="{icon}">{icon}</span>
            <span>{text}</span>
        </a>"""

    aside_html = f"""<aside class="flex flex-col fixed left-0 top-0 h-full py-6 bg-[#16213e] w-64 border-r border-white/5 font-inter text-sm antialiased z-50">
    <div class="px-6 mb-10">
        <h1 class="text-xl font-black text-[#00b4d8]">Ahmedabad AQI</h1>
        <p class="text-slate-400 text-xs mt-1">Precision Monitoring</p>
    </div>
    <nav class="flex flex-col flex-1">
{nav_links}
    </nav>
    <div class="px-6 mt-auto">
        <div class="p-4 bg-white/5 rounded-lg border border-white/5">
            <p class="text-[10px] uppercase tracking-widest text-slate-500 mb-2">System Status</p>
            <div class="flex items-center gap-2 text-[#00b4d8]">
                <span class="w-2 h-2 rounded-full bg-[#00b4d8] animate-pulse"></span>
                <span class="text-xs font-medium">Live Feed Active</span>
            </div>
        </div>
    </div>
</aside>"""

    # Replace the existing aside tag and everything inside it
    # We use re.sub with DOTALL to match across newlines
    new_content = re.sub(r'<aside[^>]*>.*?</aside>', aside_html, content, flags=re.DOTALL)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Updated sidebar in {file}")
