# Brain Tumor Detection using YOLOv8

## Overview

This project presents a deep learning-based approach for detecting brain tumors in MRI images using the YOLOv8 object detection model. The model is trained to identify and localize tumor regions by predicting bounding boxes around tumors in MRI scans.

## Dataset

- Source: Roboflow Universe
- Image Type: Brain MRI
- Total Images: ~1229
- Classes: 1 (Tumor)

## Technologies Used

- Python
- YOLOv8 (Ultralytics)
- PyTorch
- OpenCV
- NumPy
- Matplotlib
- Pandas
- Google Colab


## Model Performance

| Metric | Score |
|--------|------:|
| Precision | 0.91 |
| Recall | 0.90 |
| mAP@0.5 | 0.95 |
| mAP@0.5:0.95 | 0.79 |

## Results

The trained YOLOv8 model successfully detects and localizes brain tumors in MRI images with high accuracy. The repository includes the trained model, notebook, evaluation plots, and project report.

## Future Work

- Train on larger MRI datasets
- Detect multiple tumor types
- Deploy as a web application
- Improve performance through hyperparameter tuning

## Author

**Saharsh Kumar Singh**

Summer of Code – AI for Healthcare
