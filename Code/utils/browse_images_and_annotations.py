from PyQt6.QtWidgets import QFileDialog, QMessageBox
import json
import os
import xml.etree.ElementTree as ET

def browse_image_folder(main_window):
    folder_path = QFileDialog.getExistingDirectory(main_window, "Select Folder")
    if folder_path:
        # If a folder is selected, update the text in the txtImagePath widget
        main_window.ui.txtImagePath.setText(folder_path)
        main_window.populate_image_list(folder_path)

def browse_annotation_file(main_window):
        file_path, _ = QFileDialog.getOpenFileName(main_window, "Select File")
        if file_path:
            main_window.enable_or_disable_buttons(False)
            try:
                with open(file_path, 'r') as file:
                    data = json.load(file)

                for annotation in data["annotations"]:
                    image_id = annotation["image_id"]
                    file_name = next(image["file_name"] for image in data["images"] if image["id"] == image_id)
                    caption = annotation["caption"]
                    if file_name not in main_window.caption_mapping:
                        main_window.caption_mapping[file_name] = [caption]
                    else:
                        main_window.caption_mapping[file_name].append(caption)
                main_window.ui.txtAnnotationPath.setText(file_path)
            except (json.JSONDecodeError, KeyError, IndexError, FileNotFoundError) as e:
                main_window.showErrorMessage(f"Error processing file {file_path}: {e}")
            main_window.enable_or_disable_buttons(True)

def browse_annotation_detection_segmentation(main_window):
    if main_window.object_detetction:
        #VOC format
        #load_bounding_box_data(main_window)
        folder_path = QFileDialog.getExistingDirectory(main_window, "Select Folder")
        if folder_path:
            main_window.enable_or_disable_buttons(False)
            # If a folder is selected, update the text in the txtImagePath widget

            for filename in os.listdir(folder_path):
                if filename.endswith('.xml'):
                    xml_file = os.path.join(folder_path, filename)
                
                    # Parse the XML file
                    tree = ET.parse(xml_file)
                    root = tree.getroot()

                    # Extract file name
                    image_filename = root.find('filename').text
                    image_filename = image_filename.split('.')[0]

                    # Initialize list to store bounding box data for this image
                    main_window.bbox_data[image_filename] = []

                    # Iterate over each object in the XML
                    for obj in root.findall('object'):
                        obj_name = obj.find('name').text
                        bbox = obj.find('bndbox')
                        xmin = int(bbox.find('xmin').text)
                        ymin = int(bbox.find('ymin').text)
                        xmax = int(bbox.find('xmax').text)
                        ymax = int(bbox.find('ymax').text)

                        # Store bounding box data in the dictionary
                        main_window.bbox_data[image_filename].append({'class': obj_name, 'bbox': (xmin, ymin, xmax, ymax)})
            if main_window.bbox_data:
                main_window.ui.txtAnnotationPathDetectionSegmentation.setText(folder_path)
            else:
                main_window.showErrorMessage("Selected folder does not have any xml files.")
                
            main_window.enable_or_disable_buttons(True)
        
    if main_window.instance_segmentation:
        #COCO format
        file_path, _ = QFileDialog.getOpenFileName(main_window, "Select File")
        if file_path:
            # If a folder is selected, update the text in the txtImagePath widget
            main_window.enable_or_disable_buttons(False)
            try:
                with open(file_path, "r") as file:
                    data = json.load(file)
                main_window.segmentation_dict = {}
                main_window.image_id_info = {}
                main_window.category_id_info = {}
                for image in data["images"]:
                    main_window.image_id_info[image["file_name"].split("/")[1]] = image["id"]
                for category in data["categories"]:
                    main_window.category_id_info[category["id"]] = category["name"]
                for annotation in data["annotations"]:
                    annotation_info = {
                        "id": annotation["id"],
                        "iscrowd": annotation["iscrowd"],
                        "category_id": annotation["category_id"],
                        "area": annotation["area"],
                        "bbox": annotation["bbox"],
                        "segmentation": annotation["segmentation"]
                    }
                    
                    # Get the image ID
                    image_id = annotation["image_id"]
                    
                    # Check if the image ID exists in the segmentation dictionary
                    if image_id not in main_window.segmentation_dict:
                        main_window.segmentation_dict[image_id] = []
                    
                    # Append annotation info to the segmentation dictionary
                    main_window.segmentation_dict[image_id].append(annotation_info)
                main_window.ui.txtAnnotationPathDetectionSegmentation.setText(file_path)
            except (json.JSONDecodeError, KeyError, IndexError, FileNotFoundError) as e:
                main_window.showErrorMessage(f"Error processing file {file_path}: {e}")

            main_window.enable_or_disable_buttons(True)