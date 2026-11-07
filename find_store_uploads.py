import urllib.request, re
from urllib.parse import urljoin

req = urllib.request.Request("https://store.italsport-group.it", headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
        all_imgs = set(re.findall(r'(?:https://store\.italsport-group\.it)?/img/[^\s"\'\)]+\.(?:jpg|jpeg|png|webp)', html))
        slider_imgs = set(re.findall(r'(?:https://store\.italsport-group\.it)?/modules/[^\s"\'\)]+\.(?:jpg|jpeg|png|webp)', html))
        
        print(f"Found {len(all_imgs)} store images:")
        for img in sorted(all_imgs):
            print(" ", urljoin("https://store.italsport-group.it", img))
            
        print(f"Found {len(slider_imgs)} slider images:")
        for img in sorted(slider_imgs):
            print(" ", urljoin("https://store.italsport-group.it", img))
except Exception as e:
    print("Error:", e)
