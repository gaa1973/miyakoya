from PIL import Image
import numpy as np

def crop_whitespace(input_path, output_path):
    img = Image.open(input_path).convert("RGBA")
    print(f"Original size: {img.size}")
    
    # Get bounding box of non-transparent pixels
    bbox = img.getbbox()
    if bbox:
        # Check if we have white background that acts as "whitespace"
        # Convert to RGB to check for white
        rgb_img = img.convert("RGB")
        
        # Use a tolerance for white
        # Anything brighter than 250 in all channels is considered "white"
        # We want to find the bounding box of "non-white" content.
        
        datas = img.getdata()
        
        # We need to find the last row that has non-white pixels.
        width, height = img.size
        
        # Bottom-up scan
        bottom_crop = height
        found = False
        
        # Scan every row from bottom
        for y in range(height - 1, 0, -1):
            if found: break
            # Check this row
            for x in range(0, width):
                r, g, b, a = img.getpixel((x, y))
                # If pixel is NOT white (and not transparent)
                # Check brightness. 
                if a > 0:
                    if r < 250 or g < 250 or b < 250:
                        # Found non-white pixel
                        bottom_crop = y + 1
                        found = True
                        break
        
        print(f"Detected content bottom at: {bottom_crop} / {height}")
        
        # Crop
        crop_box = (0, 0, width, bottom_crop)
        cropped_img = img.crop(crop_box)
        cropped_img.save(output_path)
        print(f"Saved tolerance-cropped image to {output_path} with size {cropped_img.size}")
    else:
        print("Image is fully transparent?")

if __name__ == "__main__":
    crop_whitespace("collection_tiara_h1.png", "collection_tiara_final.png")
