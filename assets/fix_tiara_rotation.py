from PIL import Image
import math

def fix_tiara_rotation(input_path, output_path, angle):
    try:
        # Open original
        img = Image.open(input_path).convert("RGBA")
        
        # 1. Rotate with expand=False
        #    This keeps original dimensions but introduces empty corners.
        rotated_img = img.rotate(angle, expand=False, resample=Image.BICUBIC)
        w, h = rotated_img.size
        
        # 2. Minimal Crop Calculation
        #    For angle 'a' (radians), keeping the largest centered rectangle with consistent aspect ratio
        #    is complicated, but cropping just enough to remove the empty triangles is simpler.
        
        angle_rad = math.radians(abs(angle))
        sin_a = math.sin(angle_rad)
        cos_a = math.cos(angle_rad)
        
        # The empty wedge height at top/bottom is determined by Width.
        # h_wedge = (w/2) * sin(a) * 2 ?? No.
        
        # Let's use the safer inner-box formula for a crop that removes all alpha/black edges:
        # For a rotated image of W,H:
        # New valid height h' = h - w * sin(a)
        # New valid width w' = w - h * sin(a)
        # (Approximate for small angles)
        
        # Let's verify:
        # If we rotate a rectangle, the corners move inward. 
        # The vertical distance invaded by the side tilt is w * sin(a).
        # The horizontal distance invaded by top/bottom tilt is h * sin(a).
        # Since we centered the rotation, we lose (w * sin a) total height and (h * sin a) total width.
        
        crop_h_total = w * sin_a
        crop_w_total = h * sin_a
        
        # Values for 5 degrees (sin ~0.087)
        # If w=570, crop_h ~ 50px.
        # If h=767, crop_w ~ 67px.
        
        # Margins (each side)
        margin_top = int(crop_h_total / 2)
        margin_left = int(crop_w_total / 2)
        
        # Add a small buffer to be 100% sure we clear anti-aliasing pixels
        buffer = 2
        margin_top += buffer
        margin_left += buffer
        
        # Crop box
        crop_box = (
            margin_left, 
            margin_top, 
            w - margin_left, 
            h - margin_top
        )
        
        print(f"Original: {w}x{h}")
        print(f"Crop Margins: Top/Bot={margin_top}, Left/Rt={margin_left}")
        
        final_img = rotated_img.crop(crop_box)
        
        final_img.save(output_path, "PNG")
        print(f"Created {output_path} with Minimal Crop. Size: {final_img.size}")

    except Exception as e:
        print(f"Error: {e}")


def fix_v4(input_path, output_path, angle):
    try:
        img = Image.open(input_path).convert("RGBA")
        base_w, base_h = img.size
        
        # Rotate
        rotated_img = img.rotate(angle, expand=False, resample=Image.BICUBIC)
        
        # Crop Geometry
        # Top: 5%, Bottom: 20% (Aggressive on table), Left/Right: 8%
        
        c_top = int(base_h * 0.05)
        c_bottom = int(base_h * 0.20) 
        c_left = int(base_w * 0.08)
        c_right = int(base_w * 0.08)
        
        crop_box = (
            c_left,
            c_top,
            base_w - c_right,
            base_h - c_bottom
        )
        
        final_img = rotated_img.crop(crop_box)
        final_img.save(output_path, "PNG")
        print(f"Created {output_path} (V4). Size: {final_img.size}")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # V4: Crop more from bottom to remove table, less from top to keep head.
    # Also reducing side crop to minimal necessary to keep Aspect Ratio taller.
    
    # 1. Rotate 5 deg (Straightens head).
    # 2. Crop Bottom: 15% (Removes table).
    # 3. Crop Top: 5% (Removes rotation artifacts).
    # 4. Crop Sides: 5% (Removes rotation artifacts).
    
    # This yields an image that focuses on the head/bust.
    # To prevent "Zoomed In" look on mobile, we will adjust CSS height.
    
    fix_v4("collection_tiara.png", "collection_tiara_v4.png", 5)
