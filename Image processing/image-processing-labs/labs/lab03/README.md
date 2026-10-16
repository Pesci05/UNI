# Lecture 3 — OpenCV acquisition

This optional, ungraded lab has a **50–60 minute core: ex01–ex03**, covering
camera preview and debugging, property requests and frame saving, and image
round trips. Complete the environment setup before the session so the core
time can be used for investigation and discussion. **Ex04–ex05 are optional
video extensions** for independent work after the core; their tasks,
self-checks, and complete solutions are included below.

Follow the [root setup instructions](../../README.md) once (`uv sync`), select
the root `.venv` interpreter, and open a script with VS Code's top-right
**Run Python File** or **Debug Python File** button. No launch configuration
selection is needed. Accept the recommended extensions, including **View Image
for Python Debugging**. Supplied camera scripts default to `CAMERA_ID = 2`.
If your course camera uses another index, set `CAMERA_ID` consistently in
every camera script you run.

Student files for ex01–ex03 are in `exercises/`. Ex01 runs as supplied; ex02 and
ex03 deliberately raise `NotImplementedError` until completed. Replace each
marked unfinished operation with your implementation and remove its matching
`raise`. For ex04 and ex05, create the named files in `exercises/` yourself;
no starter code is supplied. Use the tasks below and the documentation to
build and check each program before comparing it with `solutions/`. Resolve
file paths from the script's `__file__` so VS Code can run it from any working
directory.

The documentation links below open whole reference pages. Explore their
method lists, Python signatures, return values, and notes to find the relevant
operations and constants.

Use your webcam throughout this lab, there is no supplied image or video to download:
ex02 saves the image used by ex03, and ex04 records the video used by ex05.

## Ex01 — Preview, debug, and explain a camera frame

**Objective:** verify the environment and understand the complete acquisition
lifecycle. **Prerequisites:** a connected webcam and the setup above.

Open `exercises/ex01_camera_preview.py`. All executable code is supplied;
there is nothing to implement.

1. Run the file. Identify the printed backend name and check that the preview
   responds to movement. Press **Q** in the image window to quit.
2. Set a breakpoint on the display line, after the successful-read check.
   Choose **Debug Python File**. Execution pauses before that line, with a
   valid `frame` available.
3. Use **View Image for Python Debugging** to open `frame` from the debugger's
   Variables view or image-view action. Inspect the image, `frame.shape`,
   `frame.dtype`, and a pixel's three channel values. For this colour capture,
   explain height/width/channel order, row/column indexing, and BGR order.
   Check the viewer's channel-order setting if red and blue appear swapped.
4. Continue execution, then quit normally. A preview paused at a breakpoint
   cannot update until execution resumes.
5. Add your own comments explaining each stage: opening and checking the
   camera, reporting the backend, reading and checking a frame, displaying it,
   handling keys/window events, and cleanup. Explain why the main guard exists.
   Compare with the commented solution after writing your explanations.

**Self-check:** a live window and backend name appear; debugging exposes an
image array; quitting closes the window and lets you reopen the camera.
This exercise writes no files.

**Troubleshooting:** for an opening/read failure, check the index, USB
connection, OS camera permissions, and whether another application holds the
camera. If debugging cannot import `cv2`, check the selected `.venv`. If the
image viewer is missing, enable the recommended extension and start a debug
session; simply running the file does not expose debugger variables. If **Q**
does nothing, focus the image window and ensure execution is not paused.

**Documentation:** [VideoCapture class reference](https://docs.opencv.org/4.x/d8/dfe/classcv_1_1VideoCapture.html)
and [HighGUI](https://docs.opencv.org/4.x/d7/dfc/group__highgui.html).

## Ex02 — Request camera properties and save a frame

**Objective:** extend the preview with camera configuration and image saving.
**Prerequisite:** ex01 runs with your selected camera index.

Open `exercises/ex02_camera_properties.py`. The preview, request table,
keyboard polling and quit handling, output path, property-result reporting,
camera-open/read checks, and cleanup are supplied. Implement the property
operations and the entire save-key branch, including directory creation,
write validation, and save reporting.

1. Find the documented property identifiers for width, height, and frame rate.
   Replace the three `None` placeholders, retaining requests of 800 pixels,
   600 pixels, and 30 frames per second. This is one of the listed MJPG modes
   for the course camera.
2. Complete `request`: send a property request and read its reported value
   back. Assign the results to the variables named in the TODOs, leaving the
   provided reporting in place.
3. Implement the **S**-key branch: create the output directory if needed and
   write the currently displayed frame to `outputs/camera_frame.png` using
   `OUTPUT`. Check the write result and raise an informative error on failure.
   Report success only after a successful write, printing the saved path,
   frame shape, and dtype. Find the expected filename argument type and return
   value in the documentation.
4. Run the script, inspect each request/result, and save a scene containing
   colour, edges, and fine detail with **S**. Press **Q** to quit.
5. Change one requested value, rerun, and explain what changed. Compare the
   reported dimensions with the saved frame's actual array shape.

**Self-check:** every request prints its requested value, acceptance result,
and reported value. Saving creates a readable PNG and reports its shape and
dtype. A camera may reject or adjust a request: matching the requested value
is not a pass/fail condition. A reported FPS is not an independently measured
capture rate.

**Troubleshooting:** `NotImplementedError` identifies unfinished code. An
unsupported request is a useful observation; try a supported value and inspect
the result. For save failures, check the output path and write permission.
Image writing returns a Boolean, and some invalid operations raise an exception;
do not report success unconditionally. The ex01 camera/key troubleshooting also
applies here.

**Documentation:** [VideoCapture class reference](https://docs.opencv.org/4.x/d8/dfe/classcv_1_1VideoCapture.html),
[Flags for video I/O](https://docs.opencv.org/4.x/d4/d15/group__videoio__flags__base.html),
and [Image file reading and writing](https://docs.opencv.org/4.x/d4/da8/group__imgcodecs.html).

## Ex03 — Save, reload, and compare images

**Objective:** compare lossless and lossy image storage and handle unsigned
pixel arithmetic correctly. **Prerequisite:** save `outputs/camera_frame.png`
in ex02. The camera need not stay open during this exercise.

Open `exercises/ex03_image_io.py`. Imports, paths, the function contract,
montage display, and window cleanup are supplied. Implement the whole body of
`image_round_trip(input_path, output_directory)`; keep its interface unchanged.

1. Read the input as a colour image and validate the result. Inspect its shape,
   dtype, and channel order. A failed load must produce an informative error.
2. Create the output directory if necessary. Save `still_copy.png` and
   `still_quality_35.jpg`, selecting JPEG quality 35 through the documented
   image-writing parameters. Check both write results.
3. Reload both files and validate the reads. Compare the PNG pixels exactly
   with the original; visual similarity alone is insufficient.
4. Compute the absolute JPEG error separately for every pixel and channel.
   Print its mean over all pixels/channels, PNG equality, and the two encoded
   file sizes in bytes. File size is not the array's in-memory size.
5. Build a display image of that error amplified eightfold and clipped to
   0–255. Think about the intermediate dtype before converting to `uint8`.
6. Return a list of four `(label, image)` pairs in this order:

   | Label | Image |
   | --- | --- |
   | `Original BGR` | Loaded input |
   | `PNG reload` | Reloaded PNG |
   | `JPEG reload` | Reloaded JPEG |
   | `JPEG error x8` | Amplified, clipped absolute error |

   Every returned image must have the original shape and `uint8` BGR format.
   Run the script; press any key in the montage window to finish.

**Investigate the uint8 trap:** predict the mathematical results of 10 minus
250 and 40 times 8. Try these operations on small NumPy `uint8` arrays and
explain the discrepancy. Why is taking an absolute value after an already
wrapped subtraction insufficient? Why can clipping after multiplication in
an insufficient dtype be too late? Find an appropriate absolute-difference
operation or safe intermediate representation, without changing the original
image. Use the unamplified error for the reported mean.

**Self-check:** PNG equality is true; its panel matches the original exactly.
The JPEG should depict the same scene, with some changed pixels for a detailed
capture. The error panel makes changes more visible, often around edges and
texture. The mean is in channel-value units, not a percentage. PNG/JPEG file
size ordering depends on image content; smaller size is not guaranteed for
every image. PNG equality concerns pixels, not identical encoded file bytes.

**Troubleshooting:** if the input is absent, return to ex02 and save a frame.
If the error looks implausible, inspect dtype and intermediate values. If it
is nearly black, inspect the numeric error and try a more detailed scene.
Check filename extensions, writer parameters, and read/write results before
assuming the comparison is wrong.

**Documentation:** [Image file reading and writing](https://docs.opencv.org/4.x/d4/da8/group__imgcodecs.html),
[Flags used for image file reading and writing](https://docs.opencv.org/4.x/d8/d6a/group__imgcodecs__flags.html),
and [Operations on arrays](https://docs.opencv.org/4.x/d2/de8/group__core__array.html).

## Ex04 — Record a webcam clip

**Objective:** understand how successive frames become a video file.
**Prerequisite:** a working camera index from ex01. Ex02/ex03 are not required.

Create `exercises/ex04_capture_video.py` from an empty file. Set a `CAMERA_ID`
that opens your course camera and save the clip as `outputs/camera_clip.avi`
relative to this lab directory. Put execution in `main()` behind a main guard;
importing the file must not start a recording.

1. Open the camera with `cv2.VideoCapture`, check that it opened, and read a
   first frame. Reject an unsuccessful read before using the frame. Use its
   shape to get height and width; `VideoWriter` expects `(width, height)`, and
   every frame you write must have that size.
2. Read the camera's reported FPS. If it is nonfinite or nonpositive, use 30
   FPS. Create the output directory, then open an AVI `cv2.VideoWriter` using
   the MJPG four-character codec, that FPS, and the frame size. Check that the
   writer opened before recording. A codec must be supported by the backend.
3. Read and write successive frames until you have written about
   `round(5 * fps)` frames or the user presses **Q**. Check each read, show the
   current frame with `cv2.imshow`, and call `cv2.waitKey` so the window
   responds. Raise an informative error if a read fails unexpectedly.
4. Release the writer and camera and close the window even if recording fails
   or ends early. Run the script while moving an object across the scene.
5. Reopen `outputs/camera_clip.avi` in a video player or with a video reader.
   Check its dimensions, motion, and nominal duration. The target is about five
   seconds of playback unless you stopped early; writer FPS does not control
   acquisition speed. Explain why both the writer and camera need releasing.

**Self-check:** the output reopens, contains the scene and motion you recorded,
and has the capture dimensions. Nominal duration is about five seconds unless
you stopped early. This recording contains no audio.

After your recording passes the self-check, compare your code and observations
with `solutions/ex04_capture_video.py`.

**Troubleshooting:** apply ex01's camera checks. If the writer cannot open,
check output permissions and MJPG/AVI support. If the file cannot be reopened,
ensure the script completed cleanup before reading it. Unexpected playback
speed can reflect a difference between the reported FPS and the delivered
capture rate.

**Documentation:** [VideoCapture class reference](https://docs.opencv.org/4.x/d8/dfe/classcv_1_1VideoCapture.html),
[Flags for video I/O](https://docs.opencv.org/4.x/d4/d15/group__videoio__flags__base.html),
and [VideoWriter class reference](https://docs.opencv.org/4.x/dd/d9e/classcv_1_1VideoWriter.html).

## Ex05 — Mirror and replay your recording

**Objective:** distinguish file processing from timed playback.
**Prerequisite:** finish ex04 so `outputs/camera_clip.avi` exists and is closed.
No live camera is needed here.

Create `exercises/ex05_video_io.py` from an empty file. Read
`outputs/camera_clip.avi` from ex04 and write `outputs/motion_mirrored.avi` in
this lab directory. Put execution behind a `main()` guard.

1. Check that the input exists and opens with `cv2.VideoCapture`. Read its FPS,
   width, and height; reject nonfinite or nonpositive values and invalid frame
   dimensions before using them for a writer or timing calculation.
2. Create the output directory and open an MJPG/AVI `cv2.VideoWriter` with the
   input FPS and `(width, height)`. Check that the writer opened. Process frames
   until a read fails at the end of the file. Check each frame's dimensions,
   flip it horizontally with the documented `cv2.flip` argument, write it, and
   count it. Do not delay file processing to simulate playback.
3. Release both files even if conversion fails. Reject a recording with no
   readable frames. Print the processed frame count, FPS, and nominal duration
   in seconds (`count / fps`).
4. Reopen the completed output and display its frames with `cv2.imshow`.
   Use `cv2.waitKey` with a delay based on FPS, at least one millisecond. Stop
   at end of file or when **Q** is pressed, then release the reader and close
   the window. **Q** ends replay after conversion; it does not undo the file.
5. Run your script and compare both clips' frame counts, dimensions, FPS, and
   nominal durations. Use text or an asymmetric object to verify the mirror
   direction. Explain why replay needs a delay and window-event handling, and
   why its timing is approximate.

**Self-check:** horizontal positions reverse and text appears mirrored. The
output retains the input frame count, dimensions, and nominal timing. Pixel
values need not match an exact mirrored array after lossy MJPG re-encoding.
For a healthy local recording, a failed next-frame read marks the end; read
failure can also indicate a damaged file, so an unexpectedly short output
should be investigated.

After your output passes the self-check, compare your code and observations
with `solutions/ex05_video_io.py`.

**Troubleshooting:** for a missing input, record it with ex04. For unreadable
frames or invalid metadata, finish/repeat the recording. If replay fails,
check that conversion completed and the output file opens. If **Q** is ignored,
focus the replay window. Large playback timing differences may originate in
the recording rather than the mirror operation.

**Documentation:** [VideoCapture class reference](https://docs.opencv.org/4.x/d8/dfe/classcv_1_1VideoCapture.html),
[VideoWriter class reference](https://docs.opencv.org/4.x/dd/d9e/classcv_1_1VideoWriter.html),
[Flags for video I/O](https://docs.opencv.org/4.x/d4/d15/group__videoio__flags__base.html),
[Operations on arrays](https://docs.opencv.org/4.x/d2/de8/group__core__array.html),
and [HighGUI](https://docs.opencv.org/4.x/d7/dfc/group__highgui.html).

Camera settings are requests, not commands. Unsupported values are useful
observations, not lab failures. Do not record classmates without permission.
