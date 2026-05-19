import os
import xml.etree.ElementTree as ET

xml_folder = "annotations"
output_folder = "dataset/labels/train"

os.makedirs(output_folder, exist_ok=True)

for xml_file in os.listdir(xml_folder):
    tree = ET.parse(os.path.join(xml_folder, xml_file))
    root = tree.getroot()

    width = int(root.find("size/width").text)
    height = int(root.find("size/height").text)

    txt_filename = xml_file.replace(".xml", ".txt")
    txt_path = os.path.join(output_folder, txt_filename)

    with open(txt_path, "w") as f:
        for obj in root.findall("object"):
            class_name = obj.find("name").text

            if class_name != "sofa":
                continue

            xmin = float(obj.find("bndbox/xmin").text)
            ymin = float(obj.find("bndbox/ymin").text)
            xmax = float(obj.find("bndbox/xmax").text)
            ymax = float(obj.find("bndbox/ymax").text)

            x_center = ((xmin + xmax) / 2) / width
            y_center = ((ymin + ymax) / 2) / height
            box_width = (xmax - xmin) / width
            box_height = (ymax - ymin) / height

            f.write(f"0 {x_center} {y_center} {box_width} {box_height}\n")

print("Conversion Completed!")