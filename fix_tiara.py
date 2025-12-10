from PIL import Image
import os

def fix_image():
    input_path = "assets/collection_tiara.png"
    output_path = "assets/collection_tiara_fixed.jpg"
    
    try:
        # 1. Open image
        print(f"Opening {input_path}...")
        img = Image.open(input_path)
        
        # 2. Rotate -2 degrees (clockwise)
        print("Rotating image...")
        # expand=True to keep the whole image, then crop? 
        # Or keep False to maintain size but having black borders?
        # User requested "crop center to remove whitespace".
        # If we use expand=True, we get whitespace (transparent/black).
        # We'll stick to simple rotation and crop.
        # Let's rotate with expand=False (default) first to see. 
        # Actually better to rotate with expand=True and then crop.
        rotated = img.rotate(2, expand=True, resample=Image.BICUBIC) # Positive is counter-clockwise. User said "Clockwise" (-2 to -5). So we use -2.
        # User said: "時計回りに少し回転させて（例えば -2度 〜 -5度くらい...）"
        # In Pillow, rotate argument is counter-clockwise degrees.
        # So "Clockwise" is negative degrees?
        # "rotate(-2)" -> 2 degrees clockwise.
        # The user said "-2 to -5".
        # If I use `rotate(-2)`, it rotates clockwise.
        
        rotated = img.rotate(-2, expand=True, resample=Image.BICUBIC)
        
        # 3. Crop center to remove empty space
        # Simple crop: remove 5% from edges?
        width, height = rotated.size
        left = width * 0.05
        top = height * 0.05
        right = width * 0.95
        bottom = height * 0.95
        
        print("Cropping image...")
        cropped = rotated.crop((left, top, right, bottom))
        
        # 4. Save
        print(f"Saving to {output_path}...")
        # Since input is PNG (RGBA) and output is JPG (RGB), we need to convert mode.
        if cropped.mode in ('RGBA', 'LA'):
            background = Image.new(cropped.mode[:-1], cropped.size, (255, 255, 255))
            background.paste(cropped, cropped.split()[-1])
            cropped = background
        
        cropped = cropped.convert('RGB')
        cropped.save(output_path, quality=95)
        print("Done.")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    fix_image()
