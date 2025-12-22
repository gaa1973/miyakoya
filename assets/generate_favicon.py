from PIL import Image
import os

def generate_favicon(input_path, output_path, size=(256, 256)):
    try:
        if not os.path.exists(input_path):
            print(f"Error: Input file {input_path} not found.")
            return

        img = Image.open(input_path)
        img = img.convert("RGBA")
        
        # Calculate aspect ratio preserving resize
        img.thumbnail((int(size[0]*0.8), int(size[1]*0.8)), Image.Resampling.LANCZOS)
        
        # Create a new transparent square image
        favicon = Image.new("RGBA", size, (0, 0, 0, 0))
        
        # Calculate position to center the image
        bg_w, bg_h = size
        img_w, img_h = img.size
        offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
        
        # Paste the logo
        favicon.paste(img, offset, img)
        
        # Save
        favicon.save(output_path, "PNG")
        print(f"Successfully created {output_path}")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(current_dir, "miyakoya_sub_logo.png")
    output_file = os.path.join(current_dir, "favicon.png")
    
    generate_favicon(input_file, output_file)
