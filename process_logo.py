from PIL import Image, ImageOps
import sys

def process_logo(input_path, output_black, output_white):
    try:
        # Load image
        img = Image.open(input_path).convert("RGBA")
        datas = img.getdata()

        # Create transparent version (assume white background)
        newData = []
        for item in datas:
            # Change all white (also shades of whites) to transparent
            if item[0] > 220 and item[1] > 220 and item[2] > 220:
                newData.append((255, 255, 255, 0))
            else:
                newData.append(item)

        img.putdata(newData)

        # Crop transparent areas
        bbox = img.getbbox()
        if bbox:
            img = img.crop(bbox)

        # Save Black Version
        img.save(output_black, "PNG")
        print(f"Saved {output_black}")

        # Create White Version
        white_data = []
        datas = img.getdata()
        for item in datas:
            # If transparent, keep transparent
            if item[3] == 0:
                white_data.append((255, 255, 255, 0))
            else:
                # Make non-transparent pixels white
                white_data.append((255, 255, 255, 255))
        
        white_img = Image.new("RGBA", img.size)
        white_img.putdata(white_data)
        white_img.save(output_white, "PNG")
        print(f"Saved {output_white}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    process_logo(
        "assets/logo_v3.png", 
        "assets/logo_black.png", 
        "assets/logo_white.png"
    )
