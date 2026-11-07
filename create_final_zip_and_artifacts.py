import os, zipfile, shutil

zip_filename = "ITALSPORT_Piano_Social_e_Mockup_2026.zip"
files_to_zip = [
    "Piano_Social_Italsport_2026.pdf",
    "Instagram_Mockup_Italsport.html",
    "Piano_Strategico_Social_Instagram_Italsport.md",
    "README_PACCHETTO_ITALSPORT.txt",
    "cropped-cropped-italsportlogo.png",
    "img_post1_jersey.jpg",
    "img_post2_3d.jpg",
    "img_post3_fidelity.jpg",
    "img_post4_stack.jpg",
    "img_post5_portal.jpg",
    "img_post6_winter.jpg",
    "img_post7_celebration.jpg"
]

print(f"Creating {zip_filename}...")
with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for f in files_to_zip:
        if os.path.exists(f):
            zipf.write(f, arcname=f)
            print(f"  Added {f} ({os.path.getsize(f)} bytes)")
        else:
            print(f"  WARNING: {f} not found!")

print(f"ZIP created successfully, total size: {os.path.getsize(zip_filename)} bytes")

# Copy to artifacts directory
artifact_dir = r"C:\Users\salvo\.gemini\antigravity\brain\dc9abd1d-f990-4c44-a20b-bd6ec7f9af7d"
if os.path.exists(artifact_dir):
    shutil.copyfile(zip_filename, os.path.join(artifact_dir, zip_filename))
    shutil.copyfile("Piano_Social_Italsport_2026.pdf", os.path.join(artifact_dir, "Piano_Social_Italsport_2026.pdf"))
    print("Copied files to artifact directory.")
else:
    print("Artifact directory not found!")
