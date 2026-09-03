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

Start: March 2026

End: July 2026

## Repository Timeline

The project work was carried out during the March–July 2026 project
period. The GitHub repository was subsequently consolidated and
structured to provide a reproducible and organized presentation of
the project work. Therefore, Git commit dates may reflect the
repository consolidation and documentation process rather than the
original project activity dates.

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

``text
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

---

## 7. Daily Execution Plan

The project is executed in focused daily sessions of approximately
2 hours. Each day has a defined objective and a limited scope to
maintain steady progress and avoid unnecessary implementation or
debugging beyond the planned session.

The plan serves as a working roadmap. Individual tasks may be
adjusted when required by implementation results or project
dependencies, while maintaining the overall progression toward the
project objectives.

### Day 1 — Development Foundation

- Set up the development environment
- Configure VS Code and Python virtual environment
- Establish Git and GitHub workflow
- Create the initial repository structure
- Verify the development environment

### Day 2 — Classical Lane Detection

- Implement classical OpenCV lane detection
- Validate the pipeline on multiple road images
- Calculate lane centre and normalized lateral error
- Visualize intermediate and final results
- Investigate limitations of the classical approach
- Document validation results and identified limitations

### Day 3 — Learning-Based Perception Introduction

- Understand the basic CNN structure
- Understand convolution and feature extraction
- Verify PyTorch availability
- Study a minimal CNN example
- Implement and run a small CNN example
- Document the concepts and observations

### Day 4 — CNN Image Classification

- Study the basic image-classification workflow
- Prepare a small image dataset
- Define training and validation data
- Build a simple CNN classifier
- Train the model
- Evaluate basic classification performance

### Day 5 — CNN Evaluation and Improvement

- Analyse classification results
- Inspect incorrect predictions
- Understand overfitting and underfitting
- Introduce basic data augmentation
- Compare results before and after improvement
- Document observations

### Day 6 — Learning-Based Lane Perception

- Introduce learning-based lane perception
- Understand the difference between classification and
  lane-coordinate or pixel-based prediction
- Study a minimal lane-perception approach
- Define the required input and output representation

### Day 7 — Lane-Perception Experiment

- Implement a minimal learning-based lane-perception experiment
- Test the model on sample road images
- Compare the result with the classical baseline
- Document strengths and limitations

### Day 8 — Object Detection Introduction

- Understand object-detection concepts
- Study bounding boxes and confidence scores
- Understand the difference between classification and detection
- Run a minimal object-detection example

### Day 9 — Object Detection Experiment

- Test object detection on sample images
- Inspect detection results
- Analyse false and missed detections
- Document observations

### Day 10 — Object Tracking

- Understand the purpose of object tracking
- Study basic tracking concepts
- Introduce tracking across consecutive frames
- Test a minimal tracking example

### Day 11 — State Estimation

- Introduce state estimation
- Understand the Kalman-filter concept
- Study prediction and measurement updates
- Implement a minimal Kalman-filter example

### Day 12 — Localization

- Understand vehicle localization requirements
- Study coordinate frames and pose representation
- Introduce sensor-based localization concepts

### Day 13 — SLAM

- Understand the purpose of SLAM
- Study mapping and localization together
- Understand landmarks, pose estimation, and map representation

### Day 14 — Motion Planning

- Introduce path planning
- Implement a minimal A* example
- Understand global versus local planning

### Day 15 — Path Smoothing and Local Planning

- Study path smoothing
- Introduce local obstacle avoidance
- Evaluate planned paths

### Day 16 — Vehicle Dynamics and Control

- Introduce basic vehicle modelling
- Understand steering, velocity, and vehicle motion
- Study open-loop and closed-loop control

### Day 17 — Pure Pursuit

- Understand the Pure Pursuit controller
- Implement a minimal path-tracking example
- Evaluate steering behaviour

### Day 18 — PID Control

- Understand proportional, integral, and derivative terms
- Implement a minimal PID controller
- Study the effect of controller parameters

### Day 19 — Closed-Loop Vehicle Control

- Combine vehicle motion and controller logic
- Test closed-loop path tracking
- Analyse tracking error

### Day 20 — ROS 2 Introduction

- Understand ROS 2 architecture
- Study nodes, topics, and messages
- Create a minimal ROS 2 example

### Day 21 — ROS 2 Communication

- Implement publisher/subscriber communication
- Understand message flow
- Introduce TF2 concepts

### Day 22 — Robot Description and Visualization

- Introduce URDF
- Understand robot links and joints
- Visualize the robot using RViz

### Day 23 — Gazebo Simulation

- Introduce Gazebo
- Load a basic vehicle or robot model
- Understand simulation-world concepts

### Day 24 — Autonomous Vehicle Simulation

- Connect perception, planning, and control concepts
- Establish a basic simulated vehicle workflow
- Identify interface requirements between subsystems

### Day 25 — MATLAB/Simulink Introduction

- Introduce MATLAB/Simulink vehicle modelling
- Understand blocks, signals, and subsystem structure
- Build a minimal vehicle-model example

### Day 26 — Vehicle Modelling

- Study basic vehicle dynamics
- Implement a simplified vehicle model
- Analyse model inputs and outputs

### Day 27 — MIL and SIL Concepts

- Understand Model-in-the-Loop
- Understand Software-in-the-Loop
- Compare the two validation approaches

### Day 28 — Closed-Loop Simulation

- Connect vehicle model and controller
- Run a closed-loop simulation
- Evaluate tracking behaviour

### Day 29 — JetRacer Vehicle Modelling

- Study the JetRacer platform and architecture
- Identify vehicle hardware and software interfaces
- Relate the physical platform to the autonomous-driving pipeline

### Day 30 — JetRacer Integration Concepts

- Connect perception, control, and vehicle interfaces
- Study the software structure required for vehicle operation
- Document the proposed modular architecture

### Day 31 — Project Integration Review

- Review perception, state estimation, planning, control,
  robotics, and simulation components
- Identify missing interfaces and dependencies
- Consolidate the overall autonomous-driving architecture

### Day 32 — Validation and Testing

- Review implemented experiments
- Organize validation results
- Identify limitations and failure cases
- Ensure reproducibility of important experiments

### Day 33 — Documentation and Repository Cleanup

- Review project documentation
- Update PROJECT_CONTEXT.md
- Update LEARNING_LOG.md
- Update README.md
- Organize results and supporting files

### Day 34 — Final Project Review

- Review the complete autonomous-driving pipeline
- Verify repository structure
- Review Git history and documentation
- Identify remaining gaps

### Day 35 — Final Consolidation

- Finalize project documentation
- Verify reproducibility
- Perform final repository check
- Prepare the project for presentation or submission

### Daily Workflow

Each working day follows the general sequence:

1. Review the day's planned objective
2. Learn the required concepts
3. Implement only the required work
4. Test the implementation
5. Debug or improve where necessary
6. Document the result
7. Review the repository changes
8. Commit and push the completed work

The scope of a day may be adjusted when necessary. If a task
requires additional work, the remaining work should continue on the
following day rather than extending the session unnecessarily.

## 8. Project Execution and Traceability Rules

The project follows the Daily Execution Plan defined in Section 7.
The plan is the primary roadmap for the project and should not be
replaced or substantially changed during daily execution unless a
dependency, implementation result, or documented project requirement
makes a change necessary.

### Plan Continuity

- Use the existing Daily Execution Plan as the primary reference for
  deciding what to work on each day.
- Do not introduce a new daily plan that replaces the existing plan
  without first reviewing the current plan and completed work.
- Previously completed tasks must not be repeated unless they need to
  be revisited because of an identified problem.
- If part of a day's work has already been completed, continue from
  the remaining tasks rather than restarting the day.
- If a task cannot be completed within the approximately 2-hour daily
  session, carry the remaining work forward instead of unnecessarily
  extending the session.

### File and Project Continuity

- Continue working in the existing notebook, Python file, MATLAB
  file, or other project file when the current task belongs to an
  already established project component.
- Create a new notebook, Python file, MATLAB file, configuration
  file, dataset-related file, or other project file when the project
  plan or the technical structure of the project requires a separate
  component.
- A new project day does not by itself require a new file.
- The decision to use an existing file or create a new file must be
  based on the project requirement, the functionality being
  implemented, and the existing repository structure.
- Before creating a new file, clearly identify:
  - why the file is required
  - what project component it belongs to
  - the exact repository folder where it should be placed
  - the file name
  - whether it is replacing, extending, or complementing an
    existing file
- Preserve the existing repository structure and avoid creating
  duplicate or parallel implementations of the same functionality.
- When the project requires a new component, place the corresponding
  files in the appropriate existing project directory rather than
  placing them arbitrarily.
- If the required directory does not yet exist, create it only when
  it is justified by the project structure and explain why it is
  needed.
- The current repository/folder structure should be reviewed before
  deciding where a new file belongs.
- The repository structure takes precedence over assumptions about
  where a file should be placed.

### Notebook Block Numbering

- Existing notebooks retain their current sequential block numbering.
- Each new code block added to an existing notebook uses the next
  available numerical block number followed by the current day
  identifier, for example `38-D3`, `39-D3`, and `40-D3`.
- The block number must follow the actual numerical sequence already
  present in that notebook.
- Terminal commands, Git commands, environment checks, and other
  actions outside the notebook do not consume notebook block numbers.
- Before adding a new notebook block, identify the previous block
  number and explicitly state where the new block should be inserted.

### New Python, MATLAB, or Other Code Files

- A newly created Python file starts its own internal code-block
  numbering from `1`.
- A newly created MATLAB file or other source file follows the same
  principle if numbered code sections are used: numbering starts from
  `1` within that new file.
- The file's internal numbering is independent of the block numbering
  of an existing notebook or another source file.
- A new file must not inherit the block number from the notebook or
  file from which the code was developed.
- The new file and its location must be explicitly identified before
  code is provided.
- Example:
  - Existing notebook: next block is `38-D3`.
  - New Python file: first code block is `1-D3`.
  - Second code block in that new Python file is `2-D3`.
- Do not create a new file solely to obtain a new block-number
  sequence.

### Daily Communication Workflow

For each task:

1. State the current project day and the specific task being
   performed.
2. State whether we are using an existing file or creating a new
   file.
3. Identify the exact file and location where the work belongs.
4. If a notebook or numbered source file is used, state the exact
   block number.
5. Provide only the code or action required for that step.
6. Wait for the user to run or complete the step and report the
   result.
7. Check the result before proceeding to the next step.
8. Do not introduce additional diagnostic code unless it is necessary
   to understand or resolve the current problem.
9. Keep the work within the planned daily scope.

### Documentation Workflow

- `PROJECT_CONTEXT.md` contains the project goal, technical scope,
  repository structure, daily roadmap, current project status, and
  project execution rules.
- `LEARNING_LOG.md` records the detailed concepts learned,
  implementations, experiments, problems, observations, and lessons
  learned.
- `README.md` provides the concise public-facing description of the
  project and repository.
- Update the existing documentation files rather than creating a new
  documentation file for each day.
- Documentation should reflect the actual work completed and should
  not claim work that has not been performed.

### End-of-Day Workflow

At the end of each day:

1. Verify that the planned work for the day has been completed or
   clearly record what remains.
2. Update `LEARNING_LOG.md` with the day's actual learning and work.
3. Update `PROJECT_CONTEXT.md` current project status when required.
4. Review `README.md` only when the day's work requires a public
   repository description update.
5. Review Git changes.
6. Commit the completed work with a clear commit message.
7. Push the commit to GitHub.
8. Verify that the working tree is clean.

The repository history represents the organization and consolidation
of the project work and may therefore contain Git dates that differ
from the original project activity dates.

### Repository Structure Verification

- When a task may require creating or modifying a project file,
  inspect the current repository structure before deciding the file
  location.
- Use the actual repository structure together with the intended
  top-level structure defined in Section 6 of this document.
- The actual repository structure is the primary reference for
  determining where an existing file or new file belongs.
- Do not assume that a planned directory or file already exists.
- Inspect relevant nested folders and existing files before creating a
  new implementation.
- When the actual repository structure differs from the planned
  structure, identify the difference before making structural changes.
- Avoid creating duplicate files or parallel implementations when a
  suitable existing component already exists.
- When a new component is required, place it within the appropriate
  existing project area and maintain the modular separation of
  perception, deep learning, localization, planning, control,
  robotics, simulation, documentation, tests, and results.
- As the repository grows, use the current repository tree rather than
  relying only on the abbreviated top-level structure in Section 6.
- Before making significant structural changes, review the current
  repository tree and update the project documentation when the
  structure itself has materially changed.
  
## 9. Current Project Status

### Day 1 — Development Foundations

Status: Complete

### Day 2 — Classical Lane Detections

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

The classical detector works on the initial road image but does not
reliably detect both lane boundaries on all validation images. This
limitation has been investigated and documented rather than hidden.

### Current Stage D2

Day 2 complete.

Next: Day 3.

### Day 3 — Learning Based Perception Introduction

Status: Complete

Implemented and studied:

- PyTorch availability verification
- Basic convolution operation
- CNN filters and feature maps
- Minimal CNN architecture using PyTorch
- Tensor-shape tracing through the CNN
- CNN forward pass
- Raw model outputs and logits
- Softmax probability conversion
- Class selection using `argmax`
- Classification loss using cross-entropy
- Backpropagation and gradient calculation
- SGD-based parameter update demonstration

Implementation:

`deep_learning/cnn_from_scratch/01_cnn_basics.ipynb`

Current learning result:

The basic CNN forward and learning mechanisms are understood,
including the relationship between architecture parameters,
predictions, loss, gradients, and optimizer-based parameter updates.

The CNN was not trained on a dataset during Day 3. Dataset preparation,
CNN training, and classification evaluation were completed as part of
the following CNN image-classification stage.

### Day 4 — CNN-Image Classification

Status: Complete

Implemented and studied:

- MNIST image-classification dataset preparation
- Training and validation dataset split
- DataLoader and batch processing
- Image and label representation
- Simple CNN classifier
- Forward pass on real image data
- Cross-entropy classification loss
- Adam optimizer
- Backpropagation and parameter updates
- One-epoch CNN training
- Validation evaluation
- Independent test-set evaluation

Implementation:

`deep_learning/cnn_from_scratch/02_image_classification.ipynb`

Results after one training epoch:

- Training accuracy: 89.48%
- Validation accuracy: 95.62%
- Test accuracy: 96.30%
- Test correct predictions: 9,630 / 10,000

Current learning result:

A complete supervised image-classification workflow was implemented
and understood, from labelled image data through CNN training and
independent test evaluation.

The experiment is a controlled MNIST classification exercise and does
not represent autonomous-driving performance.

### Current Stage D4

Day 4 complete.

Next: Day 5.

### Day 5 — CNN Evaluation and Improvements

Status: Complete

Implemented and studied:

- Classification error analysis on the MNIST test set
- Incorrect prediction inspection
- Confusion matrix analysis
- Per-class test accuracy
- Extended baseline CNN training
- Training and validation learning curves
- Basic data augmentation
- Controlled comparison of augmented and non-augmented training
- Class-level performance comparison

Implementation:

`deep_learning/cnn_from_scratch/02_image_classification.ipynb`

Results:

- Extended baseline test accuracy: 98.58%
- Augmented model test accuracy: 98.44%
- Overall difference: -0.14 percentage points

Key observation:

The selected augmentation configuration did not improve overall
test accuracy. However, substantial class-level improvements were
observed for previously difficult classes, particularly digit 8
(+5.85 percentage points) and digit 9 (+5.75 percentage points).
Some other classes showed a decrease in accuracy.

Current learning result:

The effect of data augmentation was evaluated experimentally rather
than assumed. The results showed that augmentation can change
class-level robustness without necessarily improving overall test
accuracy. The experiment also reinforced the importance of controlled
model comparison using the same starting state and unchanged
validation and test datasets.

### Current Stage D5

Day 5 complete.

Next: Day 6.

### Day 6 — Learning-Based-Lane Perception

Status: Complete

Implemented and studied:

- Learning-based lane-perception problem formulation
- Difference between classification and geometric lane prediction
- Minimal four-coordinate lane representation
- Lane-centre calculation from predicted lane boundaries
- Relationship between lane perception and lateral-error estimation
- Dataset and ground-truth annotation requirements

Implementation:

`perception/lane_detection/02_learning_based_lane_perception.ipynb`

Key observation:

The current lane-perception dataset contains three road images but no
lane-coordinate annotation files. Therefore, the available images are
not sufficient for supervised lane-coordinate regression without an
additional annotation step or an appropriately labelled dataset.

Current learning result:

The learning-based lane-perception problem was defined without
introducing unsupported training labels.

### Current Stage D6

Day 6 complete.

Next: Day 7 — Lane-Perception Experiment.

### Day 7 — Learning-Based Lane Perception Experiment — COMPLETE

Implemented a minimal CNN-based lane-perception experiment in:

`perception/lane_detection/02_learning_based_lane_perception.ipynb`

The experiment formulated lane perception as a regression problem in which a CNN predicts four normalized lane-boundary coordinates from a road image.

Because the available dataset contained only three road images without independent lane-coordinate annotations, the three images were manually annotated specifically for this experiment. The CNN was trained and evaluated on these same three samples.

Results:

- Final training-set MSE: `0.000024`
- Overall mean absolute coordinate error: `12.86 px`
- Maximum individual coordinate error: `40.12 px`

The predicted lane boundaries were visually compared with the manually annotated reference boundaries and showed generally close agreement on the three samples.

The learning-based approach was also compared qualitatively with the existing classical OpenCV lane-detection baseline. No direct numerical performance ranking was made because both approaches were not evaluated against the same quantitative ground-truth metric.

The experiment is considered a **proof-of-concept rather than a validated lane-perception system**. Generalization and robustness were not established because of the very limited dataset, training-set evaluation, manual annotations, aspect-ratio-changing image resize, and lack of evaluation under varied environmental conditions.

**Next focus:** Continue with the planned perception-stack development, including object detection/tracking and subsequent integration of perception outputs into the broader autonomous-driving pipeline.

### Current Stage D7

Day 7 complete.

Next: Day 8 — Object Detection and Tracking.
