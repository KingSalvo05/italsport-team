import urllib.request, re, os
from urllib.parse import urljoin

req = urllib.request.Request("https://italsport-group.it", headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
        # find all image urls in html (including background-image, data-lazy-src, src, srcset)
        all_imgs = set(re.findall(r'https://italsport-group\.it/wp-content/uploads/[^\s"\'\)]+\.(?:jpg|jpeg|png|webp)', html))
        print(f"Found {len(all_imgs)} upload images:")
        for img in sorted(all_imgs):
            print(" ", img)
except Exception as e:
    print("Error:", e)
