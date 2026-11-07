import urllib.request
import re
from urllib.parse import urljoin

urls = ['https://italsport-group.it', 'https://store.italsport-group.it']

for u in urls:
    req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            print(f"=== {u} (status {resp.status}, length {len(html)}) ===")
            
            # find title
            title = re.search(r'<title>(.*?)</title>', html, re.IGNORECASE)
            if title:
                print("Title:", title.group(1).strip())
                
            # find images
            imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html)
            print(f"Found {len(imgs)} images:")
            for img in imgs[:15]:
                full_img = urljoin(u, img)
                print("  ", full_img)
    except Exception as e:
        print(f"Error fetching {u}:", e)
