import os
import re

files_to_edit = ['index.html', 'id.html', 'privacy.html']

word_replacements = {
    # Indonesian
    r'\bskalabilitas\b': 'skala<wbr>bilitas',
    r'\bmengintegrasikan\b': 'meng<wbr>integrasikan',
    r'\bmengoptimalkannya\b': 'meng<wbr>optimalkannya',
    r'\bPemrosesan\b': 'Pem<wbr>rosesan',
    r'\boperasional\b': 'opera<wbr>sional',
    r'\btransformasi\b': 'trans<wbr>formasi',
    r'\bkomprehensif\b': 'kompre<wbr>hensif',
    r'\bberkomunikasi\b': 'ber<wbr>komunikasi',
    r'\bproduktivitas\b': 'produk<wbr>tivitas',
    r'\bmenyinkronkan\b': 'menyin<wbr>kronkan',
    r'\botomatisasi\b': 'otoma<wbr>tisasi',
    r'\bOtomatisasi\b': 'Otoma<wbr>tisasi',

    # English
    r'\bscalability\b': 'scala<wbr>bility',
    r'\bintelligently\b': 'intelli<wbr>gently',
    r'\bcommunicating\b': 'communi<wbr>cating',
    r'\barchitecture\b': 'archi<wbr>tecture',
    r'\bcomprehensively\b': 'compre<wbr>hensively',
    r'\bTransformation\b': 'Trans<wbr>formation',
    r'\btransformation\b': 'trans<wbr>formation',
    r'\bOptimization\b': 'Optimi<wbr>zation',
    r'\bIntegration\b': 'Inte<wbr>gration',
    r'\bIntelligent\b': 'Intelli<wbr>gent',
    r'\bAutonomous\b': 'Autono<wbr>mous',
}

def inject_wbr():
    for filename in files_to_edit:
        if not os.path.exists(filename):
            continue
            
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Protect against replacing text that's part of HTML tags/attributes
        # We only want to replace words in the plain text space.
        # A simple robust way: split by tags, replace in text nodes
        parts = re.split(r'(<[^>]+>)', content)
        
        for i in range(len(parts)):
            if not parts[i].startswith('<'):
                for pattern, replacement in word_replacements.items():
                    # We use re.sub with regex to match whole words while avoiding existing <wbr>s
                    parts[i] = re.sub(pattern, replacement, parts[i])
                    
        new_content = ''.join(parts)
        
        # Also let's safely split info@divisi.ai emails outside of href attributes
        # actually, mailto tags contain info@divisi.ai in the inner text. Let's just catch info@divisi.ai text manually inside the loop above
        for i in range(len(parts)):
            if not parts[i].startswith('<'):
                parts[i] = parts[i].replace('info@divisi.ai', 'info@<wbr>divisi.ai')
                
        new_content = ''.join(parts)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
            
inject_wbr()
print("WBR successfully injected.")
