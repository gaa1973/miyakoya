from PIL import Image

def make_brown_bg_logo(input_path, output_path, bg_color):
    try:
        # Open the original image
        img = Image.open(input_path).convert("RGBA")
        width, height = img.size
        
        # Create a new image with the brown background
        # bg_color is (R, G, B, A) or (R, G, B)
        new_img = Image.new("RGBA", (width, height), bg_color)
        
        # Prepare the logo data (White text)
        datas = img.getdata()
        white_logo_data = []
        
        for item in datas:
            # item is (R, G, B, A)
            if item[3] > 0:  # If not transparent
                # Change visible pixels to White
                white_logo_data.append((255, 255, 255, item[3]))
            else:
                # Keep transparent pixels transparent (so we can paste over background)
                # But wait, we want a solid background. 
                # Actually, we should just paste the white logo ON TOP of the solid background.
                # So here we make a transparent layer with white logo.
                white_logo_data.append((0, 0, 0, 0))

        # Create the transparent layer with white text
        logo_layer = Image.new("RGBA", (width, height), (0,0,0,0))
        logo_layer.putdata(white_logo_data)
        
        # Composite: Place logo_layer over new_img (brown background)
        # Note: If the original logo had anti-aliasing (semi-transparent pixels), 
        # pasting it directly might lose some quality if we don't handle alpha blending correctly.
        # Image.alpha_composite requires both to be RGBA.
        
        final_img = Image.alpha_composite(new_img, logo_layer)
        
        final_img.save(output_path, "PNG")
        print(f"Successfully created {output_path}")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Brown color from CSS: #4a3b32 -> (74, 59, 50)
    brown_color = (74, 59, 50, 255) 
    make_brown_bg_logo("miyakoya_sub_logo.png", "miyakoya_sub_logo_brown_bg.png", brown_color)
