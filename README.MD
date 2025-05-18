# BengalDeltaFish Dataset

The **BengalDeltaFish** dataset is a curated collection of 4,560 annotated images of various fish species, captured in natural market environments across Bangladesh.  
Designed to support object detection and computer vision research, this dataset offers a rich resource for developing models in real-world settings.

---

## 📦 Dataset Overview

- **Title**: BengalDeltaFish: A Local Dataset for Fish Detection in Bangladeshi Markets  
- **DOI**: [10.17632/ywfx54ktvn.4](https://doi.org/10.17632/ywfx54ktvn.4)  
- **Contributors**: Md Shoaib Shahria Alif, Sabrina Alim Dipa, Arjun Pal, Md Delwar Shahadat Deepu  
- **Published**: May 12, 2025  
- **License**: Creative Commons Attribution 4.0 (CC BY 4.0)  
- **Categories**: Computer Vision, Fish, Object Detection, Deep Learning  
- **Institution**: United International University  

---

## 🐟 Data Collection

Images were captured using the main cameras of three different smartphone devices at various fish markets in Bangladesh:

- Natun Bazar Kacha Bazar, Dhaka  
- Fashertek Hazi Market, Dhaka  
- Kawran Bazar, Dhaka  
- Tongi Wholesale Fish Market, Abdullapur  
- Fateh Ali Bazaar, Bogura  
- Chashi Bazar Fish Market, Bogura  
- Sherpur Bikal Bazaar, Bogura  

The dataset emphasizes real-world conditions, capturing images with natural lighting and varying backgrounds to reflect authentic market scenarios.

---

## 🧹 Preprocessing

- **Auto-Orientation**: Applied to ensure consistent image orientation.  
- **Resizing**: Images resized to fit within 640x640 pixels.  
- **Quality Control**: Excluded heavily overlapping fish and low-quality images (e.g., blurry or distorted) to maintain dataset integrity.  

---

## 🗂️ Dataset Split

- **Training Set**: 70% (3,193 images)  
- **Validation Set**: 20% (912 images)  
- **Test Set**: 10% (455 images)  

---

## 🔽 Download and Setup Instructions

### 1. Download the Dataset

Access the dataset from Mendeley Data:  
[https://data.mendeley.com/datasets/ywfx54ktvn/4](https://data.mendeley.com/datasets/ywfx54ktvn/4)  

Click on the "Download All" button to obtain the dataset archive.

### 2. Unzip the Dataset

After downloading, extract the contents of the ZIP file:

```bash
unzip BengalDeltaFish.zip -d BengalDeltaFish
```

### 3. Load the Dataset Using sample.py

Ensure you have the necessary dependencies installed (e.g., opencv-python, numpy).

Run the provided sample.py script to load and visualize the dataset:

```powershell
python sample.py
```

This script demonstrates how to read images and corresponding annotations, facilitating model training and evaluation.

---

## 📄 Citation
If you utilize the BengalDeltaFish dataset in your research, please cite it as follows:

Md Shoaib Shahria Alif, Sabrina Alim Dipa, Arjun Pal, Md Delwar Shahadat Deepu (2025),
"BengalDeltaFish: A Local Dataset for Fish Detection in Bangladeshi Markets",
Mendeley Data, V4, https://doi.org/10.17632/ywfx54ktvn.4

---

## 📬 Contact
For questions or collaborations, please contact the dataset contributors via the Mendeley Data page:
https://data.mendeley.com/datasets/ywfx54ktvn/4
