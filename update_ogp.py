
from PIL import Image
import os

def update_ogp():
    # Load sub logo
    try:
        logo = Image.open('assets/miyakoya_sub_logo.png').convert("RGBA")
    except Exception as e:
        print(f"Error loading logo: {e}")
        return

    # Try to load clean background
    bg_path = 'assets/hero_bg_optimized.jpg'
    if not os.path.exists(bg_path):
        bg_path = 'assets/hero_bg.png' # Fallback to original
    
    if not os.path.exists(bg_path):
        # Fallback to existing OGP and obscure center if no BG found?
        # Ideally we want a clean BG.
        bg_path = 'assets/ogp.png'
        print("Warning: Using existing OGP as base.")

    try:
        bg = Image.open(bg_path).convert("RGBA")
    except Exception as e:
        print(f"Error loading background {bg_path}: {e}")
        return

    # OGP Standard dimension
    TARGET_W, TARGET_H = 1200, 630

    # Resize/Crop Background to fill 1200x630
    # We want to cover the area.
    bg_ratio = bg.width / bg.height
    target_ratio = TARGET_W / TARGET_H

    if bg_ratio > target_ratio:
        # BG is wider, fit height
        new_h = TARGET_H
        new_w = int(new_h * bg_ratio)
    else:
        # BG is taller/equal, fit width
        new_w = TARGET_W
        new_h = int(new_w / bg_ratio)
        
    bg = bg.resize((new_w, new_h), Image.Resampling.LANCZOS)
    
    # Center crop
    left = (new_w - TARGET_W) // 2
    top = (new_h - TARGET_H) // 2
    bg = bg.crop((left, top, left + TARGET_W, top + TARGET_H))
    
    # Resize Logo
    # Target width: 800px (approx 2/3 of OGP)
    logo_target_w = 800
    logo_ratio = logo_target_w / logo.width
    logo_target_h = int(logo.height * logo_ratio)
    
    logo = logo.resize((logo_target_w, logo_target_h), Image.Resampling.LANCZOS)
    
    # Center Overlay
    x = (TARGET_W - logo_target_w) // 2
    y = (TARGET_H - logo_target_h) // 2
    
    # Paste
    bg.paste(logo, (x, y), logo)
    
    # Save
    bg.save('assets/ogp_new.png')
    print("Created assets/ogp_new.png")

if __name__ == "__main__":
    update_ogp()
