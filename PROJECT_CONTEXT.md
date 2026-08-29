# Autonomous Driving Research Project

## 1. Project Goal

Develop and understand a modular autonomous-driving system through
computer vision, deep learning, object detection, object tracking,
localization, SLAM, motion planning, vehicle control, ROS 2, Gazebo,
and MATLAB/Simulink simulation.

The project should demonstrate the complete autonomous-driving pipeline:

Perception → State Estimation → Planning → Control → Vehicle

The primary objective is not only to produce a working simulation,
but to understand the engineering principles behind each subsystem,
implement selected algorithms, test them, validate their behavior,
and integrate them into a coherent autonomous system.

---

## 2. Project Period

Start: 27 August 2026

End: 30 September 2026

Available time: approximately 2 hours per day.

---

## 3. Development Philosophy

For each major topic:

1. Learn the theory
2. Study a minimal example
3. Implement the concept
4. Test the implementation
5. Debug and improve
6. Document the result
7. Integrate it into the larger system where applicable

---

## 4. Main Technical Areas

### Perception

- Computer vision
- Classical lane detection
- CNN-based perception
- Object detection
- Semantic segmentation
- Lane perception

### State Estimation

- Kalman filtering
- Object tracking
- Localization
- SLAM

### Planning

- A* path planning
- Path smoothing
- Local obstacle avoidance
- Global/local planning concepts

### Control

- Vehicle dynamics
- Pure Pursuit
- PID concepts
- Closed-loop path tracking

### Robotics

- ROS 2
- Nodes
- Topics
- Messages
- TF2
- URDF
- Gazebo
- RViz
- Nav2

### Simulation and Validation

- MATLAB
- Simulink
- Simscape where applicable
- Model-in-the-Loop (MIL)
- Software-in-the-Loop (SIL)
- Closed-loop simulation

### Development

- Python
- PyTorch
- OpenCV
- Git
- GitHub
- VS Code

---

## 5. Development Environment

Operating system: Windows

Primary development environment: VS Code

Programming languages:

- Python
- MATLAB

Version control:

- Git
- GitHub

---

## 6. Repository Structure

```text
autonomous-driving-research/

├── docs/
├── datasets/
├── perception/
├── deep_learning/
├── localization/
├── planning/
├── control/
├── ros2/
├── matlab/
├── simulation/
├── tests/
├── results/
├── PROJECT_CONTEXT.md
└── README.md

## 7. Current Project Status

### Day 1 — Development Foundation
Status: Complete

### Day 2 — Classical Lane Detection
Status: Complete

Implemented:
- Image loading and preprocessing
- Grayscale conversion
- Gaussian blur
- Canny edge detection
- Region of interest
- Bright-pixel lane-marking filtering
- Hough line detection
- Left/right lane candidate separation
- Geometric filtering
- Robust lane-boundary estimation
- Lane-centre estimation
- Normalized lateral error
- Validation on three road images
- Diagnostic visualization of lane candidates

Current limitation:
The classical detector works on the initial road image but does not reliably detect both lane boundaries on all validation images. This limitation is recorded for future improvement rather than being hidden.

### Current Stage
Day 2 complete.
Next: Day 3.
