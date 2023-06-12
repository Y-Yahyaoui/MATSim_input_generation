import xml.etree.ElementTree as ET

def concatenate_xml_files(files, output_file):
    # Create an empty root element
    root = ET.Element("plans")

    # Iterate over the input files
    for file in files:
        # Read the contents of each XML file
        with open(file, 'r') as f:
            xml = f.read()

        # Create ElementTree object from the XML string
        tree = ET.ElementTree(ET.fromstring(xml))

        # Get the root element of the tree
        file_root = tree.getroot()

        # Append the root element to the main root
        root.extend(file_root)

    # Create a new ElementTree with the combined root element
    combined_tree = ET.ElementTree(root)

    # Output the combined XML
    combined_xml = ET.tostring(root, encoding='unicode')

    # Write the combined XML to the output file
    with open(output_file, 'w') as output:
        output.write(combined_xml)

# Example usage
files = ['path/to/file1.xml', 'path/to/file2.xml', 'path/to/file3.xml']
output_file = 'path/to/output.xml'
concatenate_xml_files(files, output_file)
print(f"Combined XML file saved to {output_file}")
