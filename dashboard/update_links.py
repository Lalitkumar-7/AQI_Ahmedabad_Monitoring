import os
import re

files = ['overview.html', 'date_explorer.html', 'monthly_trends.html', 'pollutant.html', 'predictor.html', 'correlation.html']

mapping = {
    'Overview': 'overview.html',
    'Date Explorer': 'date_explorer.html',
    'Monthly Trends': 'monthly_trends.html',
    'Pollutant Explorer': 'pollutant.html',
    'AQI Predictor': 'predictor.html',
    'Correlation Insights': 'correlation.html'
}

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    chunks = content.split('<a ')
    new_chunks = [chunks[0]]
    
    for chunk in chunks[1:]:
        end_idx = chunk.find('</a>')
        if end_idx != -1:
            a_tag_content = chunk[:end_idx]
            found_key = None
            for key in mapping:
                if re.search(r'>\s*' + re.escape(key) + r'\s*<', a_tag_content):
                    found_key = key
                    break
            
            if found_key:
                chunk = re.sub(r'href="[^"]*"', f'href="{mapping[found_key]}"', chunk, count=1)
                
        new_chunks.append(chunk)

    with open(file, 'w', encoding='utf-8') as f:
        f.write('<a '.join(new_chunks))
    print(f'Updated {file}')
