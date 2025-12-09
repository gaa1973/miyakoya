from PIL import Image
import os

input_path = "assets/Gemini_Generated_Image_qr20ftqr20ftqr20.png"
output_path = "assets/hero_bg_optimized.jpg"

try:
    with Image.open(input_path) as img:
        print(f"Original size: {img.size}")
        print(f"Original format: {img.format}")
        
        # Convert to RGB if necessary (PNG might have alpha channel)
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
            
        # Save as JPEG with high quality
        img.save(output_path, "JPEG", quality=90, optimize=True)
        
        input_size = os.path.getsize(input_path) / (1024 * 1024)
        output_size = os.path.getsize(output_path) / (1024 * 1024)
        
        print(f"Successfully optimized image!")
        print(f"Input: {input_size:.2f} MB")
        print(f"Output: {output_size:.2f} MB")
        print(f"Reduction: {(1 - output_size/input_size)*100:.1f}%")

except Exception as e:
    print(f"Error optimizing image: {e}")
