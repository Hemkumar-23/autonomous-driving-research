# Learning Log

This document records the concepts, implementations, experiments,
tests, problems, and lessons learned throughout the autonomous-driving
research project.

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

## Day 2 Status

Classical lane-detection baseline implemented and tested.

The basic perception pipeline is working, with known limitations
identified for further development.
