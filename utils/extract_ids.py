import xml.etree.ElementTree as ET
import json


def extract_svg_ids_to_json(svg_file, output_file):
    tree = ET.parse(svg_file)
    root = tree.getroot()

    namespaces = {"svg": "http://www.w3.org/2000/svg"}

    elements_with_ids = root.findall(".//*[@id]", namespaces)

    ids_dict = {element.attrib["id"]: -1 for element in elements_with_ids}

    with open(output_file, "w") as file:
        json.dump(ids_dict, file, indent=2)

    print(f"IDs have been saved to {output_file}")


if __name__ == "__main__":
    # Example usage
    svg_file = "approximation/body_front_back.svg"  # Replace with SVG file path
    output_file = "approximation/drawing_ids.json"  # Output JSON file
    extract_svg_ids_to_json(svg_file, output_file)
