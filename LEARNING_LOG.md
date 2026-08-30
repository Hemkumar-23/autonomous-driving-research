# Learning Log

This document records the concepts, implementations, experiments,
tests, problems, and lessons learned throughout the autonomous-driving
research project.

## Project Period

March 2026 – July 2026

The learning log records the technical work, experiments,
implementation decisions, validation activities, and lessons learned
during the project. The repository was consolidated afterward for
structured version control and presentation.

---

## Day 1 — Development Foundation

## Objective

Set up the development environment and establish a reproducible
Git/GitHub/VS Code workflow.

## Concepts Learned

### Git

Git is a distributed version-control system used to track changes
to project files.

### GitHub

GitHub is the remote hosting platform where the project's Git
repository is stored.

### Repository

The repository contains the project files together with their
version history.

### Clone

`git clone` creates a local copy of a remote repository.

### Commit

A commit records a set of changes as a versioned checkpoint.

### Push

`git push` sends local commits to the remote repository.

### Remote

The GitHub repository is configured as the remote named `origin`.

## Commands Used

```text
git --versionS
git clone
git status
git ls-remote
git config


---------------------------------------------------------------------

## Day 2 — Classical Lane Detection

## Objective

Build and understand a basic classical computer-vision lane-detection
pipeline using recorded road images.

## Concepts Learned

### Image Pre-processing

Grayscale conversion was used to represent image intensity while
removing colour information.

Gaussian blur was applied to reduce noise and small image details
before edge detection.

### Canny Edge Detection

Canny edge detection was used to identify strong intensity changes
that may correspond to lane boundaries.

The resulting edge image was checked to confirm that it contained
binary edge values.

### Region of Interest

A trapezoidal region of interest was defined to restrict processing
to the road area relevant to lane detection.

### Bright-Pixel Filtering

A brightness threshold was used to identify pixels likely to
correspond to white lane markings.

The bright-pixel mask was then restricted to the road ROI.

### Hough Line Detection

Probabilistic Hough Line Transform was used to detect straight
line segments from the filtered lane-marking regions.

### Lane Candidate Filtering

Detected line segments were separated into left and right candidates
based on their position and orientation.

Additional geometric constraints were introduced to reject candidates
that were inconsistent with the expected lane-boundary positions.

### Lane Boundary Estimation

Representative left and right lane boundaries were estimated from
the filtered line segments.

The final approach used a robust median-based estimation of the
projected lane positions.

### Lane Centre and Lateral Error

The lane centre was calculated from the estimated left and right
lane boundaries at a selected evaluation position.

The difference between the lane centre and the image centre was then
normalized to produce a lateral error value.

## Implementation

A reusable `run_lane_detection()` function was created to run the
complete lane-detection pipeline on an input image.

The pipeline was then applied to three validation images:
- road_01.jpg
- road_02.jpg
- road_03.jpg

## Validation

The pipeline successfully executed on all three validation images.

The validation results showed that the method performs differently
depending on the road image. `road_01.jpg` produced both lane
boundaries and a valid normalized lateral error, while `road_02.jpg`
and `road_03.jpg` exposed limitations in the current classical
filtering approach.

## Problems and Lessons Learned

The initial Hough-line output contained a very large number of
candidate segments. Therefore, geometric filtering was necessary
before estimating the final lane boundaries.

An implementation issue was also encountered because
`cv2.HoughLinesP()` returned line data with an additional array
dimension. Reshaping the result to `(-1, 4)` allowed the line
segments to be unpacked correctly.

The validation images demonstrated that a pipeline that works on
one road image cannot automatically be considered robust. Testing
on multiple images is therefore necessary.

### Additional Validation Diagnostics

Additional diagnostics were performed on the validation images to
understand the limitations of the classical lane-detection approach.

For `road_02.jpg`, the Hough transform detected a large number of
line segments, but the candidate classification produced a strong
imbalance between left and right lane candidates. This prevented
reliable estimation of both lane boundaries.

The brightness threshold used for lane-marking extraction was also
tested at different values. Changing this threshold did not resolve
the imbalance in the detected lane candidates, indicating that the
limitation was not caused solely by the brightness threshold.

These observations showed that the current classical approach is
sensitive to road geometry and image characteristics. The detector
therefore provides a useful baseline for understanding classical
computer-vision methods, but further improvements are required for
more robust lane perception.

## Day 2 Status

Classical lane-detection baseline implemented and tested.

The basic perception pipeline is working, with known limitations
identified for further development.

---

## Day 3 — Learning-Based Perception Introduction

## Objective

Understand the basic structure and operation of a convolutional
neural network and establish the foundation for later learning-based
perception experiments.

## Concepts Learned

### PyTorch

PyTorch was verified as available in the development environment.
The installed version was checked from the terminal before starting
the CNN implementation.

### Convolution

A convolutional layer applies learnable filters to an input image
to extract local patterns and features.

The number of filters is specified as part of the network architecture.
For example, `out_channels=4` means that the layer contains four
learnable filters. This value is an architectural design choice and
is not calculated automatically by the model.

### Feature Maps

Each convolutional filter produces a feature map. Increasing the
number of output channels therefore increases the number of feature
maps produced by the convolutional layer.

### CNN Architecture

A small CNN was implemented using PyTorch. The network contains two
convolutional layers, ReLU activation functions, max-pooling
operations, and a fully connected output layer.

The example used a grayscale 28 × 28 input image. The tensor
dimensions were traced through the complete network to understand how
the data representation changes at each stage.

### Tensor Shape Transformation

The input tensor was represented as:

`[batch, channels, height, width]`

The implemented network transformed the example input as follows:

`[1, 1, 28, 28]`
→ `[1, 4, 28, 28]`
→ `[1, 4, 14, 14]`
→ `[1, 8, 14, 14]`
→ `[1, 8, 7, 7]`
→ `[1, 392]`
→ `[1, 10]`

This demonstrated the effect of convolution, activation, pooling,
flattening, and the final fully connected layer.

### CNN Prediction

A random input image was passed through the untrained CNN to inspect
the model output.

The final layer produced ten raw output values. Softmax was then used
to convert these values into a normalized probability distribution,
and the highest-probability output was selected as the predicted
class.

Because the CNN was not trained, the resulting class prediction was
not considered a meaningful classification result.

### Loss

A target class was introduced to demonstrate how a model prediction
is compared with the expected result.

Cross-entropy loss was used to produce a numerical measure of the
classification error.

The loss value represents the disagreement between the model output
and the target class. It is not itself an accuracy or percentage
measure.

### Backpropagation and Gradients

Backpropagation was demonstrated using `loss.backward()`.

The gradients indicate how changes in the model parameters affect
the loss. The gradient tensor for the first convolutional layer had
the same shape as its corresponding weight tensor.

### Optimizer and Weight Update

Stochastic Gradient Descent (SGD) was used to demonstrate a single
parameter update.

The experiment showed that the optimizer uses the calculated
gradients to update the model parameters according to the selected
learning rate.

The simplified update relationship is:

`new weight = old weight - learning rate × gradient`

This demonstrated the basic mechanism through which a neural network
can learn during training.

## Implementation

A minimal CNN was implemented in:

`deep_learning/cnn_from_scratch/01_cnn_basics.ipynb`

The notebook contains the convolution demonstration, CNN
architecture, tensor-shape tracing, prediction example, loss
calculation, gradient inspection, and optimizer update demonstration.

## Validation and Observations

The CNN implementation executed successfully.

The tensor-shape tracing confirmed the expected transformation of the
input through the network.

The prediction experiment demonstrated the difference between raw
model outputs, probabilities, and the selected class.

The loss, gradient, and optimizer experiments demonstrated the
basic sequence:

Input → Prediction → Loss → Backpropagation → Gradients → Weight
Update.

The CNN was not trained as part of Day 3. Actual dataset preparation,
CNN training, and classification evaluation are reserved for the
subsequent CNN image-classification stage.

## Problems and Lessons Learned

The main learning focus was understanding what the numerical
parameters in a CNN represent rather than treating the network as a
black box.

It was clarified that values such as `out_channels=4` and
`out_channels=8` are selected as part of the network architecture,
while the numerical weights inside those filters are learned during
training.

The tensor-shape experiment also demonstrated why the fully
connected layer requires 392 input features after the two convolution
and pooling stages.

The gradient and optimizer experiments demonstrated that calculating
a loss alone does not change the model. Backpropagation calculates
gradients, and the optimizer uses those gradients to update the
model parameters.

## Day 3 Status

Learning-based perception introduction completed.

A minimal CNN was implemented and its forward-pass, loss,
backpropagation, and parameter-update mechanisms were studied.

Actual CNN training is deferred to the planned image-classification
stage.