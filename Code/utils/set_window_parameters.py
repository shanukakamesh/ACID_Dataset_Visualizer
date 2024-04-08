

def init_window_parameters(main_window):
    main_window.ui.comboDetectionSegmentation.setCurrentIndex(0)
    main_window.ui.lblAnnotationPath.setVisible(False)
    main_window.ui.txtAnnotationPath.setVisible(False)
    main_window.ui.btnAnnotationPath.setVisible(False)
    main_window.ui.lblAnnotationPathDetectionSegmentation.setVisible(False)
    main_window.ui.txtAnnotationPathDetectionSegmentation.setVisible(False)
    main_window.ui.btnAnnotationPathDetetctionSegmentation.setVisible(False)
    main_window.ui.frameAnnotation.setMinimumHeight(40)
    main_window.ui.frameAnnotation.setMaximumHeight(40)
    main_window.ui.graphicsViewLegend.setMinimumHeight(0)
    main_window.ui.graphicsViewLegend.setMaximumHeight(0)
    main_window.ui.lblPenSize.setMaximumWidth(0)
    main_window.ui.sliderPenSize.setMaximumWidth(0)
    main_window.ui.graphicsImageDisplay2.setMaximumWidth(0)