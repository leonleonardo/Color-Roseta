import sys

def scale_component(component, n_bits, m_bits):
    max_value_n = (1 << n_bits) - 1
    max_value_m = (1 << m_bits) - 1

    return (component * max_value_m + max_value_n // 2) // max_value_n

# Function to generate a new color by averaging with the known colors
def generate_new_color(rgb_color):
    # Extract the RGB888 components
    red_8bit = (rgb_color >> 16) & 0xFF
    green_8bit = (rgb_color >> 8) & 0xFF
    blue_8bit = rgb_color & 0xFF

    # Scale each component to fit BGR565 format (5 or 6 bits)
    red_5bit = scale_component(red_8bit, 8, 5)
    green_6bit = scale_component(green_8bit, 8, 6)
    blue_5bit = scale_component(blue_8bit, 8, 5)
    

    # Combine the new color components into BGR565 format
    new_color = (blue_5bit << 11) | (green_6bit << 5) | red_5bit

    return new_color

def main():
    if len(sys.argv) != 2:
        print("Usage: python color_converter.py <RGB_HEX_COLOR>")
        sys.exit(1)

    try:
        rgb_color = int(sys.argv[1], 16)
    except ValueError:
        print("Invalid RGB color format. Please provide a valid hexadecimal RGB color.")
        sys.exit(1)

    new_color = generate_new_color(rgb_color)
    print("Original RGB888 Color: 0x{:06X}".format(rgb_color))
    print("New BGR565 Color: 0x{:04X}".format(new_color))

if __name__ == "__main__":
    main()