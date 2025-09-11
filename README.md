# Enhancing Children’s Pool Safety via Deep Learning–Based Activity Recognition and Pose Estimation

**Code archive:**  
[Google Drive (project files)](https://drive.google.com/file/d/1eTN3nvnB9T4eKQtzZj-G0sj9D9y6Pe0B/view?usp=drive_link)

> This repository contains the scripts I use to segment subjects into videos, select targets, and train models.  
> Questions? Email **jmayhugh@tamu.edu**.

---

## Abstract

Swimming pools pose substantial risks for children, with many injuries occurring during lessons and unstructured play. This thesis presents a real-time video system that detects unsafe poolside behaviors using human-pose sequences and temporal modeling.

Raw videos are segmented into labeled clips, and 2D skeletal keypoints are extracted per frame with **YOLOv11-pose**. Detections are associated over time with **BoT-SORT** to maintain person IDs. From the resulting sequences, we derive position and velocity features and train a **Long Short-Term Memory (LSTM)** network to classify actions that may precede risk (e.g., entering or exiting the pool).

On held-out data, the model achieves **97.4%** test accuracy and **98.9%** validation accuracy. We discuss deployment constraints in aquatic environments (reflections, occlusions, lighting), ethical safeguards (consent, face blurring, data minimization), and edge inference on resource-limited hardware. Ongoing work targets pool-specific datasets, subject-wise evaluation to avoid identity leakage, and integration with facility alerting. Results highlight the potential of pose-based sequence models to support timely intervention and improve children’s pool safety.

---

## What’s in Here

- **Video segmentation:** split long recordings into labeled activity clips.  
- **Target selection & tracking:** identify subjects and keep stable IDs across frames.  
- **Model training:** prepare pose sequences and train/evaluate LSTM classifiers.

---

## Contact

- **Joshua Mayhugh** — jmayhugh@tamu.edu
