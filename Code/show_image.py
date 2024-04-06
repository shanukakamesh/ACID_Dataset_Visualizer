import sys
import os
from ACID_dataset_visualizer import Ui_MainWindow
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QGraphicsScene, QGraphicsPixmapItem, QGraphicsTextItem, QSlider
from PyQt6.QtGui import QPixmap, QStandardItemModel, QStandardItem, QPen, QColor, QFont, QPainterPath
from PyQt6.QtCore import Qt, QPointF
import json
import xml.etree.ElementTree as ET

class showImage(QMainWindow):
    def __init__(self):
        super().__init__()

        # use the Ui_login_form
        self.ui = Ui_MainWindow()       
        self.ui.setupUi(self) 
        self.annotations = {}
        self.caption_mapping = {}
        self.file_names = []
        self.current_file_index = 0
        self.object_detetction = False
        self.instance_segmentation = False
        self.bbox_data = {}
        self.segmentation_dict = {}
        self.image_id_info = {}
        self.category_id_info = {}
        self.penSize = 10

        self.scene = QGraphicsScene()
        self.scene2 = QGraphicsScene()
        self.class_legend_scene = QGraphicsScene()

        # Connect the button clicked signal to a slot
        self.ui.btnImagePath.clicked.connect(self.browse_image_folder)  
        self.ui.btnAnnotationPath.clicked.connect(self.browse_annotation_file)  
        self.ui.btnAnnotationPathDetetctionSegmentation.clicked.connect(self.browse_annotation_detection_segmentation) 
        
        self.ui.btnShowImage.clicked.connect(self.display_image)

        self.ui.btnNext.clicked.connect(lambda n:self.change_image(1))
        self.ui.btnPrevious.clicked.connect(lambda n:self.change_image(-1))
        
        # Connect the resize event to the populate_image_list function
        self.resizeEvent = self.on_resize

        # Connect itemClicked signal of listImageNames to a slot
        self.ui.listImageNames.clicked.connect(self.item_clicked)

        self.ui.comboDetectionSegmentation.setCurrentIndex(0)
        self.ui.lblAnnotationPath.setVisible(False)
        self.ui.txtAnnotationPath.setVisible(False)
        self.ui.btnAnnotationPath.setVisible(False)
        self.ui.lblAnnotationPathDetectionSegmentation.setVisible(False)
        self.ui.txtAnnotationPathDetectionSegmentation.setVisible(False)
        self.ui.btnAnnotationPathDetetctionSegmentation.setVisible(False)
        self.ui.frameAnnotation.setMinimumHeight(40)
        self.ui.frameAnnotation.setMaximumHeight(40)
        self.ui.graphicsViewLegend.setMinimumHeight(0)
        self.ui.graphicsViewLegend.setMaximumHeight(0)
        self.ui.lblPenSize.setMaximumWidth(0)
        self.ui.sliderPenSize.setMaximumWidth(0)

        self.ui.checkBoxCaptioning.stateChanged.connect(self.checkbox_captioning_changed)

        self.ui.comboDetectionSegmentation.currentIndexChanged.connect(self.combo_detetction_segmentation_changed)
        self.ui.graphicsImageDisplay2.setMaximumWidth(0)

        self.ui.sliderPenSize.valueChanged.connect(self.updatePenSize)

        self.legend_data = {
            'dozer': QColor(255, 0, 0, 255),  # Red
            'backhoe_loader': QColor(0, 255, 135, 255),  # Green
            'wheel_loader': QColor(0, 0, 255, 255),  # Blue
            'excavator': QColor(250, 210, 20, 255),  # Orange
            'dump_truck': QColor(0, 255, 255, 255),  # Cyan
            'grader': QColor(255, 0, 200, 255),  # Magenta
            'compactor': QColor(168, 0, 193, 255),  # Dark Red
            'mobile_crane': QColor(60, 170, 30, 255),  # Dark Green
            'cement_truck': QColor(135, 70, 60, 255),  # Dark Orange
            'tower_crane': QColor(0, 0, 0, 255)  # Dark Cyan
        }

        self.legend_data_segmentation = {
            'dozer': QColor(255, 0, 0, 255),  # Red
            'backhoe_loader': QColor(0, 255, 135, 255),  # Green
            'wheel_loader': QColor(0, 0, 255, 255),  # Blue
            'excavator': QColor(250, 210, 20, 255),  # Orange
            'dump_truck': QColor(0, 255, 255, 255),  # Cyan
            'grader': QColor(255, 0, 200, 255),  # Magenta
            'compactor': QColor(168, 0, 193, 255),  # Dark Red
            'mobile_crane': QColor(60, 170, 30, 255),  # Dark Green
            'cement_truck': QColor(135, 70, 60, 255),  # Dark Orange
            'tower_crane': QColor(0, 0, 0, 255),  # Dark Cyan
            'concrete_mixer_truck': QColor(225, 100, 0, 255)
        }

        # show the login window
        self.show()

    def updatePenSize(self, value):
        self.penSize = value
        self.display_image()

    def browse_image_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder_path:
            # If a folder is selected, update the text in the txtImagePath widget
            self.ui.txtImagePath.setText(folder_path)
            self.populate_image_list(folder_path)

    def browse_annotation_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File")
        if file_path:
            # If a folder is selected, update the text in the txtImagePath widget
            self.enable_or_disable_buttons(False)
            self.ui.txtAnnotationPath.setText(file_path)
            with open(file_path, 'r') as file:
                data = json.load(file)

            for annotation in data["annotations"]:
                image_id = annotation["image_id"]
                file_name = next(image["file_name"] for image in data["images"] if image["id"] == image_id)
                caption = annotation["caption"]
                if file_name not in self.caption_mapping:
                    self.caption_mapping[file_name] = [caption]
                else:
                    self.caption_mapping[file_name].append(caption)
            self.enable_or_disable_buttons(True)
    
    def browse_annotation_detection_segmentation(self):
        if self.object_detetction:
            #VOC format
            folder_path = QFileDialog.getExistingDirectory(self, "Select Folder")
            if folder_path:
                self.enable_or_disable_buttons(False)
                # If a folder is selected, update the text in the txtImagePath widget
                self.ui.txtAnnotationPathDetectionSegmentation.setText(folder_path)
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
                        self.bbox_data[image_filename] = []

                        # Iterate over each object in the XML
                        for obj in root.findall('object'):
                            obj_name = obj.find('name').text
                            bbox = obj.find('bndbox')
                            xmin = int(bbox.find('xmin').text)
                            ymin = int(bbox.find('ymin').text)
                            xmax = int(bbox.find('xmax').text)
                            ymax = int(bbox.find('ymax').text)

                            # Store bounding box data in the dictionary
                            self.bbox_data[image_filename].append({'class': obj_name, 'bbox': (xmin, ymin, xmax, ymax)})
                self.enable_or_disable_buttons(True)
            
        if self.instance_segmentation:
            #COCO format
            print('instance segmentation')
            file_path, _ = QFileDialog.getOpenFileName(self, "Select File")
            if file_path:
                # If a folder is selected, update the text in the txtImagePath widget
                self.enable_or_disable_buttons(False)
                self.ui.txtAnnotationPathDetectionSegmentation.setText(file_path)
                with open(file_path, "r") as file:
                    data = json.load(file)
                self.segmentation_dict = {}
                self.image_id_info = {}
                self.category_id_info = {}
                for image in data["images"]:
                    self.image_id_info[image["file_name"].split("/")[1]] = image["id"]
                for category in data["categories"]:
                    self.category_id_info[category["id"]] = category["name"]
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
                    if image_id not in self.segmentation_dict:
                        self.segmentation_dict[image_id] = []
                    
                    # Append annotation info to the segmentation dictionary
                    self.segmentation_dict[image_id].append(annotation_info)

                self.enable_or_disable_buttons(True)
    
    def add_legend_item(self, text, color, x):
        # Create a text item
        text_item = QGraphicsTextItem(text)
        text_item.setDefaultTextColor(color)
        font = text_item.font()
        font.setPointSize(12)
        text_item.setFont(font)
        
        # Set position
        text_item.setPos(x, 10)
        
        # Add to the scene
        self.class_legend_scene.addItem(text_item)

    def display_image(self):
        image_path = self.ui.txtImagePath.text() + '/' + self.ui.txtImageName.text() + '.' + self.ui.comboImageType.currentText().lower()
        self.scene = QGraphicsScene()
        pixmap = QPixmap(image_path)
        item = QGraphicsPixmapItem(pixmap)
        self.scene.addItem(item)
        self.ui.graphicsImageDisplay.setScene(self.scene)
        self.ui.graphicsImageDisplay.fitInView(self.scene.sceneRect(), Qt.AspectRatioMode.KeepAspectRatio)
        if self.object_detetction and self.ui.txtImageName.text():
            self.scene2 = QGraphicsScene()
            pixmap2 = QPixmap(image_path)
            item2 = QGraphicsPixmapItem(pixmap2)
            self.scene2.addItem(item2)
            self.class_legend_scene = QGraphicsScene()
            self.ui.graphicsViewLegend.setScene(self.class_legend_scene)
            
            i = 0
            for index, (key, value) in enumerate(self.legend_data.items()):
                self.add_legend_item(key, value, index*130)

            for bbox_info in self.bbox_data.get(self.ui.txtImageName.text(), []):
                class_name = bbox_info['class']
                color = self.legend_data[class_name]

                # Extract bounding box coordinates
                xmin, ymin, xmax, ymax = bbox_info['bbox']
                
                # Calculate width and height of the bounding box
                width = xmax - xmin
                height = ymax - ymin

                # Draw bounding box rectangle on the image
                pen = QPen(color)
                pen.setWidth(5)
                self.scene2.addRect(xmin, ymin, width, height, pen)
                
                label_text = class_name
                label = QGraphicsTextItem(label_text)
                label.setPos(xmin, ymin)
                label.setDefaultTextColor(color)
                font = QFont()
                font.setPointSize(self.penSize)  # Change the font size as needed
                font.setBold(True)  # Make the font bold
                label.setFont(font)
                self.scene2.addItem(label)

            self.ui.graphicsImageDisplay2.setScene(self.scene2)
            self.ui.graphicsImageDisplay2.fitInView(self.scene2.sceneRect(), Qt.AspectRatioMode.KeepAspectRatio)
        if self.instance_segmentation and self.ui.txtImageName.text():
            self.scene2 = QGraphicsScene()
            pixmap2 = QPixmap(image_path)
            item2 = QGraphicsPixmapItem(pixmap2)
            self.scene2.addItem(item2)
            self.class_legend_scene = QGraphicsScene()
            self.ui.graphicsViewLegend.setScene(self.class_legend_scene)

            for index, (key, value) in enumerate(self.legend_data_segmentation.items()):
                self.add_legend_item(key, value, index*130)

            image_id = self.image_id_info[self.ui.txtImageName.text()+ '.' + self.ui.comboImageType.currentText().lower()]
            image_data = self.segmentation_dict[image_id]
            for data in image_data:
                class_name = self.category_id_info[data["category_id"]]
                color = self.legend_data_segmentation[class_name]

                xmin, ymin, width, height = data["bbox"]

                # Draw bounding box rectangle on the image
                pen = QPen(color)
                pen.setWidth(5)
                self.scene2.addRect(xmin, ymin, width, height, pen)

                # Draw segmentation mask
                segmentation = data["segmentation"]
                path = QPainterPath()
                start_point = QPointF(segmentation[0][0], segmentation[0][1])  # Start from the first point
                path.moveTo(start_point)
                for i in range(2, len(segmentation[0]), 2):
                    x = segmentation[0][i]
                    y = segmentation[0][i + 1]
                    path.lineTo(QPointF(x, y))
                path.lineTo(QPointF(segmentation[0][0], segmentation[0][1]))  # Close the path
                self.scene2.addPath(path, pen)

                label_text = class_name
                label = QGraphicsTextItem(label_text)
                label.setPos(xmin, ymin)
                label.setDefaultTextColor(color)
                font = QFont()
                font.setPointSize(self.penSize)  # Change the font size as needed
                font.setBold(True)  # Make the font bold
                label.setFont(font)
                self.scene2.addItem(label)
            self.ui.graphicsImageDisplay2.setScene(self.scene2)
            self.ui.graphicsImageDisplay2.fitInView(self.scene2.sceneRect(), Qt.AspectRatioMode.KeepAspectRatio)
                


    def populate_image_list(self, folder_path):
        if folder_path:
            self.file_names = os.listdir(folder_path)
            list_model = QStandardItemModel()
            for file_name in self.file_names:
                item = QStandardItem(file_name)
                list_model.appendRow(item)
            self.ui.listImageNames.setModel(list_model)

    def on_resize(self, event):
        # Call populate_image_list on window resize
        self.populate_image_list(self.ui.txtImagePath.text())
        self.display_image()

    def update_image_name(self, name, file_type, file_name):
        self.ui.txtImageName.setText(name)
        self.ui.comboImageType.setCurrentText(file_type)
        choices = [self.ui.comboImageType.itemText(i) for i in range(self.ui.comboImageType.count()) if self.ui.comboImageType.itemText(i) == file_type.upper()]
        if choices:
            self.ui.comboImageType.setCurrentText(choices[0])
            self.display_image()
            if self.caption_mapping:
                self.ui.txtCaptions.setPlainText('\n\n'.join(self.caption_mapping[file_name]))
                

    def item_clicked(self, index):
        # Get the item that was clicked
        item = self.ui.listImageNames.model().itemFromIndex(index)
        if item is not None:
            # Call a function based on the clicked item
            file_name = item.text()
            self.current_file_index = self.file_names.index(file_name)
            name,file_type = file_name.split('.')
            self.update_image_name(name, file_type, file_name)
    
    def change_image(self, n):
        if self.file_names:
            self.current_file_index = (self.current_file_index + n) % len(self.file_names)
            file_name = self.file_names[self.current_file_index]
            name,file_type = file_name.split('.')
            self.update_image_name(name, file_type, file_name)

    def enable_or_disable_buttons(self, value):
        self.ui.btnImagePath.setEnabled(value)
        self.ui.btnAnnotationPath.setEnabled(value)
        self.ui.btnShowImage.setEnabled(value)
        self.ui.btnNext.setEnabled(value)
        self.ui.btnPrevious.setEnabled(value)
        self.ui.listImageNames.setEnabled(value)

    def checkbox_captioning_changed(self, state):
        n = 0
        temp = [self.ui.lblAnnotationPathDetectionSegmentation, self.ui.txtAnnotationPathDetectionSegmentation, self.ui.btnAnnotationPathDetetctionSegmentation]
        if self.ui.checkBoxCaptioning.isChecked():
            # Run your function here
            self.ui.lblAnnotationPath.setVisible(True)
            self.ui.txtAnnotationPath.setVisible(True)
            self.ui.btnAnnotationPath.setVisible(True)
            self.ui.frameAnnotation.setMinimumHeight(self.ui.frameAnnotation.minimumHeight() + 30)
            self.ui.frameAnnotation.setMaximumHeight(self.ui.frameAnnotation.maximumHeight() + 30)
            if self.ui.lblAnnotationPathDetectionSegmentation.pos().y() == 30:
                n = 40
        else:
            self.ui.lblAnnotationPath.setVisible(False)
            self.ui.txtAnnotationPath.setVisible(False)
            self.ui.btnAnnotationPath.setVisible(False)
            self.ui.frameAnnotation.setMinimumHeight(self.ui.frameAnnotation.minimumHeight() - 30)
            self.ui.frameAnnotation.setMaximumHeight(self.ui.frameAnnotation.maximumHeight() - 30)
            self.ui.txtAnnotationPath.setText('')
            self.ui.txtCaptions.setText('')
            self.annotations = {}
            self.caption_mapping = {}
            if self.ui.lblAnnotationPathDetectionSegmentation.pos().y() == 70:
                n = -40
        if n != 0:
            for i in temp:
                current_pos = i.pos()
                i.move(current_pos.x(), current_pos.y() + n)
    
    def combo_detetction_segmentation_changed(self, index):
        self.ui.txtAnnotationPathDetectionSegmentation.setText('')
        self.scene.clear()
        self.scene2.clear()
        self.class_legend_scene.clear()
        if index == 0:
            self.ui.lblAnnotationPathDetectionSegmentation.setVisible(False)
            self.ui.txtAnnotationPathDetectionSegmentation.setVisible(False)
            self.ui.btnAnnotationPathDetetctionSegmentation.setVisible(False)
            self.ui.frameAnnotation.setMinimumHeight(self.ui.frameAnnotation.minimumHeight() - 40)
            self.ui.frameAnnotation.setMaximumHeight(self.ui.frameAnnotation.maximumHeight() - 40)
            self.object_detetction, self.instance_segmentation = False, False
            self.ui.graphicsViewLegend.setMinimumHeight(0)
            self.ui.graphicsViewLegend.setMaximumHeight(0)
            self.ui.graphicsImageDisplay2.setMaximumWidth(0)
            self.ui.lblPenSize.setMaximumWidth(0)
            self.ui.sliderPenSize.setMaximumWidth(0)
            self.segmentation_dict = {}
            self.image_id_info = {}
            self.category_id_info = {}
            self.bbox_data = {}
        else:
            self.ui.lblAnnotationPathDetectionSegmentation.setVisible(True)
            self.ui.txtAnnotationPathDetectionSegmentation.setVisible(True)
            self.ui.btnAnnotationPathDetetctionSegmentation.setVisible(True)
            if not(self.object_detetction or self.instance_segmentation):
                self.ui.frameAnnotation.setMinimumHeight(self.ui.frameAnnotation.minimumHeight() + 40)
                self.ui.frameAnnotation.setMaximumHeight(self.ui.frameAnnotation.maximumHeight() + 40)
            n = 0
            temp = [self.ui.lblAnnotationPathDetectionSegmentation, self.ui.txtAnnotationPathDetectionSegmentation, self.ui.btnAnnotationPathDetetctionSegmentation]
            if not self.ui.checkBoxCaptioning.isChecked() and self.ui.lblAnnotationPathDetectionSegmentation.pos().y() == 70:
                n = -40

            if n != 0:
                for i in temp:
                    current_pos = i.pos()
                    i.move(current_pos.x(), current_pos.y() + n)

            if index == 1:
                self.ui.lblAnnotationPathDetectionSegmentation.setText('Annotation path for Object Detection')
                self.object_detetction = True
                self.instance_segmentation = False
                self.segmentation_dict = {}
                self.image_id_info = {}
                self.category_id_info = {}
            else:
                self.ui.lblAnnotationPathDetectionSegmentation.setText('Annotation path for Instance Segmentation')
                self.instance_segmentation = True
                self.object_detetction = False
                self.bbox_data = {}
            self.ui.graphicsImageDisplay2.setMaximumWidth(self.ui.graphicsImageDisplay2.maximumHeight())
            self.ui.graphicsViewLegend.setMinimumHeight(40)
            self.ui.graphicsViewLegend.setMaximumHeight(40)
            self.ui.lblPenSize.setMaximumWidth(self.ui.lblPenSize.maximumHeight())
            self.ui.sliderPenSize.setMaximumWidth(self.ui.sliderPenSize.maximumHeight())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = showImage()
    sys.exit(app.exec())