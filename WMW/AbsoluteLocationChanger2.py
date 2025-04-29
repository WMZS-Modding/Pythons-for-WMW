import argparse
import xml.etree.ElementTree as ET

def parse_args():
    parser = argparse.ArgumentParser(description="Change AbsoluteLocation of objects with matching Filename in XML.")
    parser.add_argument("input_xml", help="Path to the input XML file.")
    parser.add_argument("-o", "--output", required=True, help="Path to the output XML file.")
    parser.add_argument("-value", nargs=2, type=float, metavar=("x", "y"), help="Offset to apply to X and Y values.")
    parser.add_argument("-hs", required=True, help="Comma-separated list of .hs file paths to match in Filename.")
    return parser.parse_args()

def modify_absolute_locations(tree, offset_x, offset_y, hs_list):
    root = tree.getroot()
    for obj in root.findall(".//Object"):
        filename_property = obj.find("./Properties/Property[@name='Filename']")
        if filename_property is not None:
            filename_value = filename_property.attrib.get("value", "").strip()
            if filename_value in hs_list:
                abs_loc = obj.find("AbsoluteLocation")
                if abs_loc is not None:
                    try:
                        x_str, y_str = abs_loc.attrib["value"].split()
                        x_new = float(x_str) + offset_x
                        y_new = float(y_str) + offset_y
                        abs_loc.set("value", f"{x_new:.6f} {y_new:.6f}")
                    except ValueError:
                        print(f"Warning: Can't parse AbsoluteLocation in object {obj.attrib.get('name', '')}")
    return tree

def main():
    args = parse_args()
    hs_list = [hs.strip() for hs in args.hs.split(",")]
    offset_x = args.value[0] if args.value else 0
    offset_y = args.value[1] if args.value else 0

    tree = ET.parse(args.input_xml)
    tree = modify_absolute_locations(tree, offset_x, offset_y, hs_list)
    tree.write(args.output, encoding="utf-8", xml_declaration=True)

if __name__ == "__main__":
    main()
