import re
import argparse

def shift_absolute_locations(xml_text, shift_x=0, shift_y=0):
    # Regex find <AbsoluteLocation value="x y"/>
    pattern = re.compile(r'<AbsoluteLocation value="([\d\-\.\+eE]+) ([\d\-\.\+eE]+)"/>')

    def replace_location(match):
        x, y = float(match.group(1)), float(match.group(2))
        new_x = x + shift_x
        new_y = y + shift_y
        return f'<AbsoluteLocation value="{new_x:.6f} {new_y:.6f}"/>'

    new_xml = pattern.sub(replace_location, xml_text)
    return new_xml

def main():
    parser = argparse.ArgumentParser(description="Shift AbsoluteLocation of all Objects in XML.")
    parser.add_argument("input_xml", help="Path to the input XML file.")
    parser.add_argument("-o", "--output", required=True, help="Path to the output XML file.")
    parser.add_argument("-value", required=True, help="Shift values in format 'x y'")
    args = parser.parse_args()

    # Read file input
    with open(args.input_xml, "r", encoding="utf-8") as f:
        xml_text = f.read()

    # Split shift_x, shift_y values
    try:
        shift_x_str, shift_y_str = args.value.strip().split()
        shift_x = float(shift_x_str)
        shift_y = float(shift_y_str)
    except ValueError:
        print("Error: -value must be in the form 'x y' with 2 numbers separated by a space.")
        return

    # Make changes
    shifted_xml = shift_absolute_locations(xml_text, shift_x, shift_y)

    # Write file output
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(shifted_xml)

    print(f"Changed all AbsoluteLocation ({shift_x}, {shift_y}) successfully!")
    print(f"New file: {args.output}")

if __name__ == "__main__":
    main()
