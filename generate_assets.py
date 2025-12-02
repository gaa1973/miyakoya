from PIL import Image, ImageDraw, ImageFont
import os

def create_placeholder(filename, width, height, color, text):
    img = Image.new('RGB', (width, height), color=color)
    d = ImageDraw.Draw(img)
    
    # Add some texture or gradient (simple lines for now)
    for i in range(0, width, 20):
        d.line([(i, 0), (i, height)], fill=(255, 255, 255, 30), width=1)
    
    # Add text if possible (basic)
    # d.text((20, 20), text, fill=(255, 255, 255)) # Default font might be too small/ugly, skipping text for clean look or just simple center
    
    # Save
    path = os.path.join('assets', filename)
    img.save(path)
    print(f"Created {path}")

def create_hero_bg():
    # Soft Pink & Rose Gold Gradient for "Extreme Elegance"
    width, height = 1920, 1080
    img = Image.new('RGB', (width, height), color=(255, 240, 245)) # Lavender Blush base
    d = ImageDraw.Draw(img)
    
    # Complex gradient simulation
    for i in range(height):
        # Interpolate between Soft Pink -> Rose Gold -> Pale Lavender
        ratio = i / height
        r = int(255 - (ratio * 20))     # 255 -> 235
        g = int(240 - (ratio * 60))     # 240 -> 180
        b = int(245 - (ratio * 40))     # 245 -> 205
        
        # Add a subtle "gold" tint in the middle
        if 0.3 < ratio < 0.7:
            gold_factor = 1 - abs(ratio - 0.5) * 2 # 0 at edges, 1 at center
            r = min(255, r + int(20 * gold_factor))
            g = min(255, g + int(10 * gold_factor))
            b = max(0, b - int(20 * gold_factor))
            
        d.line([(0, i), (width, i)], fill=(r, g, b))

    # Add subtle "sparkles"
    import random
    for _ in range(200):
        x = random.randint(0, width)
        y = random.randint(0, height)
        size = random.randint(1, 3)
        opacity = random.randint(50, 150)
        d.ellipse([x, y, x+size, y+size], fill=(255, 255, 255, opacity))

    path = os.path.join('assets', 'hero_bg.png')
    img.save(path)
    print(f"Created {path}")

if __name__ == "__main__":
    if not os.path.exists('assets'):
        os.makedirs('assets')
    
    create_hero_bg()
    
    # Create Collection Images
    # Tutu: Soft White/Pink
    create_placeholder('collection_tutu.png', 600, 800, (255, 250, 250), "Classical Tutu")
    
    # Tiara: Silver/Goldish
    create_placeholder('collection_tiara.png', 600, 800, (240, 248, 255), "Tiara")
    
    # Accessories: Soft Lavender
    create_placeholder('collection_accessory.png', 600, 800, (245, 240, 255), "Accessories")
    
    # Favicon (small square)
    create_placeholder('favicon.png', 64, 64, (255, 182, 193), "M")

