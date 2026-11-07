import urllib.request
from PIL import Image
import os

images_to_download = {
    'real_post1_jersey.jpg': 'https://images.unsplash.com/photo-1522778119026-d647f0596c20?w=1200&q=85',
    'real_post4_warehouse.jpg': 'https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?w=1200&q=85',
    'real_post6_winter.jpg': 'https://images.unsplash.com/photo-1516726817505-f5ed825624d8?w=1200&q=85',
    'real_post7_celebrate.jpg': 'https://images.unsplash.com/photo-1517466787929-bc90951d0974?w=1200&q=85',
    'real_locker_room.jpg': 'https://images.unsplash.com/photo-1587280501635-68a0e82cd5ff?w=1200&q=85',
    'real_youth_soccer.jpg': 'https://images.unsplash.com/photo-1517927033932-b3d18e61fb3a?w=1200&q=85',
    'real_textile.jpg': 'https://images.unsplash.com/photo-1558769132-cb1aea458c5e?w=1200&q=85'
}

for name, url in images_to_download.items():
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = resp.read()
            with open(name, 'wb') as f:
                f.write(data)
            im = Image.open(name)
            print(f"Downloaded {name}: {im.size} {len(data)} bytes")
    except Exception as e:
        print(f"Error {name}: {e}")
