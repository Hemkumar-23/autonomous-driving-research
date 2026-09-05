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

----------------------------------------------------------------------------------------------

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

``text
git --versionS
git clone
git status
git ls-remote
git config
----------------------------------------------------------------------------------------------

## Day 2 — Classical Lane Detection

## Objective D2

Build and understand a basic classical computer-vision lane-detection
pipeline using recorded road images.

## Concepts Learned D2

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

----------------------------------------------------------------------------------------------

## Day 3 — Learning-Based Perception Introduction

## Objective D3

Understand the basic structure and operation of a convolutional
neural network and establish the foundation for later learning-based
perception experiments.

## Concepts Learned D3

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

## Implementation D3

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

## Problems and Lessons Learned D3

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

----------------------------------------------------------------------------------------------

## Day 4 — CNN Image Classification

### Objective D4

Study and implement the basic image-classification workflow using a
small labelled image dataset and a convolutional neural network.

### Dataset Preparation

The MNIST handwritten-digit dataset was used for the classification
experiment.

The dataset contains:

- 60,000 training images
- 10,000 test images
- Grayscale images with a size of 28 × 28 pixels
- 10 classes representing digits 0–9

The original 60,000-image training dataset was divided into:

- 54,000 training images
- 6,000 validation images

The separate 10,000-image test dataset was kept untouched for final
evaluation.

A fixed random seed was used for the training/validation split to make
the experiment reproducible.

### Data Representation

A single MNIST image was represented as:

[1, 28, 28]

where:

- 1 = grayscale image channel
- 28 = image height
- 28 = image width

A batch size of 64 was used.

Therefore, a training or validation batch was represented as:

[64, 1, 28, 28]

The corresponding label tensor contained 64 class labels.

The images and labels were kept as separate data structures. The labels
were not embedded into or removed from the image data.

### CNN Architecture D4

A simple CNN classifier was implemented using PyTorch.

The architecture consisted of:

- First convolution: 1 input channel → 8 output channels
- ReLU activation
- Max pooling
- Second convolution: 8 input channels → 16 output channels
- ReLU activation
- Max pooling
- Flattening
- Fully connected layer: 784 inputs → 10 outputs

The spatial dimensions changed as follows:

28 × 28
→ 14 × 14
→ 7 × 7

The flattened feature size was therefore:

16 × 7 × 7 = 784

The 8 and 16 convolutional output channels were selected as model
architecture parameters. They were design choices rather than values
calculated from the dataset.

The final 10 outputs corresponded to the ten MNIST classes.

### Training

Cross-entropy loss was used for classification.

The Adam optimizer was used with a learning rate of 0.001.

The basic training sequence was studied and implemented:

Forward pass
→ loss calculation
→ backpropagation
→ gradient calculation
→ optimizer update

One individual training step was first performed to observe the effect
of a parameter update.

The loss changed from approximately 2.3019 before the update to
approximately 2.2846 after the update on the same batch.

The model was then trained for one complete epoch over the 54,000-image
training subset.

### Validation D4

The model was evaluated on the separate 6,000-image validation subset.

During validation:

- The model was switched to evaluation mode.
- Gradient calculation was disabled.
- The model parameters were not updated.

Validation therefore measured the model's performance on images that
were not used to update the model weights.

### Test Evaluation

The trained model was finally evaluated on the separate 10,000-image
MNIST test dataset.

Results after one training epoch:

- Training accuracy: 89.48%
- Validation accuracy: 95.62%
- Test accuracy: 96.30%
- Test correct predictions: 9,630 / 10,000

The test accuracy represents the basic classification performance of
this controlled MNIST experiment. It does not represent autonomous
driving performance.

### Problems and Debugging

During dataset splitting, the labels returned by the MNIST dataset
were Python integers in the inspected samples. Calling `.item()` on
these labels caused an AttributeError.

The issue was resolved by printing the labels directly instead of
calling `.item()`.

### Main Learning Outcomes

The complete CNN image-classification workflow was understood and
implemented:

Dataset
→ training/validation split
→ DataLoader
→ batches
→ CNN
→ forward pass
→ loss
→ backpropagation
→ optimizer update
→ validation
→ test evaluation

The difference between training, validation, and test data was also
understood.

Training data is used to update model parameters. Validation data is
used to evaluate the model during development without updating the
parameters. The test dataset is kept separate for final evaluation.

The experiment provides the foundation for the next stage of CNN
evaluation and improvement.

----------------------------------------------------------------------------------------------

## Day 5 — CNN Evaluation and Improvement

### Objective D5

Analyse CNN classification errors, introduce basic data augmentation,
and compare the resulting model performance with the established
non-augmented baseline.

### Classification Error Analysis

The trained CNN was evaluated on the 10,000-image MNIST test set.

The model produced:

- 9,643 correct predictions
- 357 incorrect predictions
- 96.43% test accuracy

The most common classification errors included confusion between
digits 9 and 4, digits 7 and 2, and digits 8 and 2 or 4.

Per-class evaluation showed that digits 8 and 9 were among the more
difficult classes for the baseline model, with accuracies of 91.99%
and 91.28%, respectively.

### Extended Baseline Training

The baseline CNN was trained for five additional epochs without data
augmentation.

The resulting test accuracy was:

- 98.58%
- 9,858 correct predictions out of 10,000

Training and validation curves were also inspected. Training accuracy
increased throughout the additional epochs, while validation accuracy
also improved and remained close to the training performance.

### Data Augmentation

Basic data augmentation was introduced for the training subset.

The augmentation pipeline consisted of:

- Random rotation of up to ±10 degrees
- Random translation of up to 10% in horizontal and vertical directions
- Random scaling between 90% and 110%

The augmentation was applied only to the 54,000-image training subset.
The 6,000-image validation subset and the 10,000-image test set were
kept unchanged.

The augmented training data were generated on the fly when samples
were retrieved from the dataset.

Visual inspection confirmed that the transformed images retained their
original class labels while exhibiting small changes in orientation,
position, and scale.

### Augmentation Experiment

The augmented model was initialized from the preserved baseline model
state to provide a controlled comparison.

The augmented model was trained for five epochs using the same CNN
architecture, optimizer configuration, batch size, and validation
dataset as the baseline experiment.

The final test results were:

- Baseline without augmentation: 98.58%
- With augmentation: 98.44%
- Overall difference: -0.14 percentage points

Therefore, the applied augmentation configuration did not improve
overall test accuracy in this experiment.

### Per-Class Observation

Although the overall test accuracy was slightly lower, the
per-class results showed substantial changes.

The largest improvements were observed for previously difficult
classes:

- Digit 8: 91.99% → 97.84% (+5.85 percentage points)
- Digit 9: 91.28% → 97.03% (+5.75 percentage points)
- Digit 7: 95.53% → 97.96% (+2.43 percentage points)
- Digit 5: 96.52% → 99.33% (+2.80 percentage points)

Digit 4 decreased from 98.47% to 97.15%.

These results show that augmentation changed the distribution of
classification performance across classes even though the overall
test accuracy remained approximately unchanged.

### Problems and Lessons Learned D5

The augmentation experiment demonstrated that an improvement in
individual classes does not necessarily produce an improvement in
overall accuracy.

The experiment also reinforced the importance of using a controlled
comparison. The augmented model was restored to the same preserved
baseline state before training, while the validation and test datasets
remained unchanged.

The results should therefore be interpreted specifically for the
augmentation configuration tested rather than as a general conclusion
that data augmentation always improves CNN performance.

### Day 5 Status

CNN evaluation and basic improvement experiment completed.

The baseline and augmented models were compared using the same
experimental starting point and unchanged validation/test data.

Overall accuracy did not improve with the selected augmentation
configuration, but substantial class-level improvements were observed
for digits 8 and 9.

----------------------------------------------------------------------------------------------
