import os
import re

files = ['overview.html', 'date_explorer.html', 'monthly_trends.html', 'pollutant.html', 'predictor.html', 'correlation.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove System Status from the sidebar. 
    # It looks like: <div class="px-6 mt-auto">...</div>\n</aside>
    content = re.sub(r'<div class="px-6 mt-auto">.*?</div>\s*</div>\s*</aside>', '</aside>', content, flags=re.DOTALL)

    # 2. Remove the profile, notification, settings from the header.
    # In pollutant.html, it's inside <div class="flex items-center gap-6"> or similar which contains "notifications", "settings", "profile".
    # Let's just find the <header> tag, and remove buttons/divs that contain these icons.
    
    # A robust way is to just find the <div class="flex items-center gap-6"> ... </div> or <div class="flex items-center gap-4"> inside header that contains the icons.
    # Since headers have a right-side div for these controls, let's find it.
    
    # It typically looks like:
    # <div class="flex items-center gap-...">
    #   <div ... notifications ...>
    #   <div ... profile ...>
    # </div>
    # </header>
    
    # Let's remove any <button> that contains 'data-icon="notifications"', 'data-icon="settings"', 'data-icon="help"', etc.
    content = re.sub(r'<button[^>]*>.*?data-icon="notifications".*?</button>', '', content, flags=re.DOTALL)
    content = re.sub(r'<button[^>]*>.*?data-icon="settings".*?</button>', '', content, flags=re.DOTALL)
    content = re.sub(r'<button[^>]*>.*?data-icon="help".*?</button>', '', content, flags=re.DOTALL)
    
    # And for profile image/div:
    # it might be an img with alt="User profile" or User Profile text
    # In pollutant: <img ... alt="User profile" ...>
    # Let's remove the div containing the profile img
    content = re.sub(r'<div[^>]*>\s*<img[^>]*alt="User profile"[^>]*>.*?\s*</div>', '', content, flags=re.DOTALL)
    content = re.sub(r'<div[^>]*>\s*<img[^>]*src="https://images.unsplash[^>]*>.*?\s*</div>', '', content, flags=re.DOTALL)
    
    # In overview.html:
    # <img src="https://ui-avatars.com/api/?name=Admin+User..." class="w-8 h-8 rounded-full border border-white/10" alt="Profile">
    content = re.sub(r'<img[^>]*alt="Profile"[^>]*>', '', content, flags=re.DOTALL)
    content = re.sub(r'<img[^>]*ui-avatars[^>]*>', '', content, flags=re.DOTALL)
    
    # In date_explorer.html:
    # <div class="p-6 mt-auto border-t border-white/5 flex items-center gap-3">
    # <div class="w-8 h-8 rounded-full bg-primary-container flex items-center justify-center text-on-primary-container font-bold text-xs">JD</div>
    # <div>
    # <p class="text-sm font-semibold text-slate-100">User Profile</p>
    # <p class="text-[10px] text-slate-500">Administrator</p>
    content = re.sub(r'<div class="p-6 mt-auto border-t border-white/5 flex items-center gap-3">.*?User Profile.*?</div>\s*</div>', '', content, flags=re.DOTALL)

    # In overview.html it also has:
    # <button class="p-2 text-slate-400 hover:bg-white/5 rounded-full transition-colors">
    # <span class="material-symbols-outlined" data-icon="account_circle">account_circle</span>
    content = re.sub(r'<button[^>]*>.*?data-icon="account_circle".*?</button>', '', content, flags=re.DOTALL)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Cleaned {file}")
