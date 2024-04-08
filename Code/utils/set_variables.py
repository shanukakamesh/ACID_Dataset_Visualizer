from PyQt6.QtWidgets import QGraphicsScene
from PyQt6.QtGui import  QColor
from PyQt6.QtCore import Qt, QThread, pyqtSignal
import xml.etree.ElementTree as ET
import os


def set_variable(main_window):
    main_window.annotations = {}
    main_window.caption_mapping = {}
    main_window.file_names = []
    main_window.current_file_index = 0
    main_window.object_detetction = False
    main_window.instance_segmentation = False
    main_window.bbox_data = {}
    main_window.segmentation_dict = {}
    main_window.image_id_info = {}
    main_window.category_id_info = {}
    main_window.penSize = 10
    main_window.scene = QGraphicsScene()
    main_window.scene2 = QGraphicsScene()
    main_window.class_legend_scene = QGraphicsScene()
    
    main_window.legend_data = {
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

    main_window.legend_data_segmentation = {
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
    
