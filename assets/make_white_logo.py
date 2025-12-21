from PIL import Image

def make_white_logo(input_path, output_path):
    try:
        img = Image.open(input_path)
        img = img.convert("RGBA")
        
        datas = img.getdata()
        new_data = []
        
        for item in datas:
            # item is (R, G, B, A)
            if item[3] > 0:  # If not transparent
                # Change to White (255, 255, 255) but keep original Alpha
                new_data.append((255, 255, 255, item[3]))
            else:
                new_data.append(item)
                
        img.putdata(new_data)
        img.save(output_path, "PNG")
        print(f"Successfully created {output_path}")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    make_white_logo("miyakoya_sub_logo.png", "miyakoya_sub_logo_white.png")
