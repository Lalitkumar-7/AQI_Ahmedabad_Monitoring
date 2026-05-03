import os
import re

files = ['overview.html', 'date_explorer.html', 'monthly_trends.html', 'pollutant.html', 'predictor.html', 'correlation.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Search inputs
    content = re.sub(r'<div class="relative group">\s*<span[^>]*>.*?data-icon="search".*?</span>\s*</span>\s*<input[^>]*placeholder="Search[^"]*"[^>]*>\s*</div>', '', content, flags=re.DOTALL)
    content = re.sub(r'<div[^>]*>\s*<span[^>]*>.*?data-icon="search".*?</span>\s*</span>\s*<input[^>]*placeholder="Search[^"]*"[^>]*>\s*</div>', '', content, flags=re.DOTALL)
    content = re.sub(r'<span[^>]*>.*?data-icon="search".*?</span>\s*</span>', '', content, flags=re.DOTALL)
    content = re.sub(r'<input[^>]*placeholder="Search[^"]*"[^>]*>', '', content, flags=re.DOTALL)

    # Profile images and their containers
    content = re.sub(r'<img[^>]*alt="User Profile"[^>]*>', '', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<img[^>]*alt="Administrator"[^>]*>', '', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<img[^>]*src="https://lh3.googleusercontent[^>]*>', '', content, flags=re.DOTALL | re.IGNORECASE)
    
    # Profile labels
    content = re.sub(r'<p[^>]*>\s*User Profile\s*</p>', '', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<p[^>]*>\s*Administrator\s*</p>', '', content, flags=re.DOTALL | re.IGNORECASE)
    
    # Clean up empty containers
    content = re.sub(r'<div[^>]*>\s*JD\s*</div>', '', content, flags=re.DOTALL)
    content = re.sub(r'<div class="w-8 h-8[^>]*>\s*</div>', '', content, flags=re.DOTALL)
    content = re.sub(r'<div class="relative group">\s*</div>', '', content, flags=re.DOTALL)
    content = re.sub(r'<div class="flex items-center gap-4 text-slate-400">\s*</div>', '', content, flags=re.DOTALL)
    
    # Also if the entire <div class="flex items-center gap-6"> has become empty except spaces/newlines
    # It might contain other things, so let's only remove if it's completely empty
    content = re.sub(r'<div class="flex items-center gap-[46]">\s*</div>', '', content, flags=re.DOTALL)
    content = re.sub(r'<div class="flex items-center gap-[46]">\s*<div class="flex items-center gap-[46] text-slate-400">\s*</div>\s*</div>', '', content, flags=re.DOTALL)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Cleaned more in {file}")
