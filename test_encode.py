import os, base64, subprocess

def get_base64_image(filename):
    if os.path.exists(filename):
        with open(filename, 'rb') as f:
            b64 = base64.b64encode(f.read()).decode('utf-8')
            ext = 'png' if filename.endswith('.png') else 'jpeg'
            return f"data:image/{ext};base64,{b64}"
    return ""

print("Encoding images...")
logo_b64 = get_base64_image("cropped-cropped-italsportlogo.png")
post1_b64 = get_base64_image("img_post1_jersey.jpg")
post2_b64 = get_base64_image("img_post2_3d.jpg")
post3_b64 = get_base64_image("img_post3_fidelity.jpg")
post4_b64 = get_base64_image("img_post4_stack.jpg")
post5_b64 = get_base64_image("img_post5_portal.jpg")
post6_b64 = get_base64_image("img_post6_winter.jpg")
post7_b64 = get_base64_image("img_post7_celebration.jpg")

# Also raw assets for rich layout
cfg_b64 = get_base64_image("site_configuratore.jpg")
portal_b64 = get_base64_image("site_membro_myitalsport.jpg")
fullprint_b64 = get_base64_image("store_full_print.jpg")

print("Encoded successfully.")
