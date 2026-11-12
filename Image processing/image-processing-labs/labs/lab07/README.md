# Lecture 7 — Calibration and planar homographies

Follow the [root setup instructions](../../README.md) once (`uv sync`), then
open a script and use VS Code's top-right **Run Python File** button.

This lab has no starters: every script in `solutions/` is complete. For each
one, first **read the code** with the focus points below. The short comments
in the code explain *why* each step is there. Then **run the demo**, and use it
to test what the code claims rather than just watching it work. Ex01–03 are
the in-class core; ex04 and the investigations are for independent work.

## Before you start

**The card.** The calibration card handed out in class holds a **10 × 7**
checkerboard of **10 mm** squares, which gives **9 × 6 internal corners**
(`PATTERN = (9, 6)`). The odd/even square counts make a 180° rotation
distinguishable. Keep the card flat: calibration assumes a rigid plane, so a
bent card adds an error that no lens model can explain.

**The camera.** Ex01 and ex02 set `CAMERA_ID` and `REQUESTS` at the top of
each file: camera 1, 800 × 600, autofocus **off**, focus **350** in driver
units. Drivers use different focus ranges, so read the requested/actual
values printed in the terminal, and adjust the focus until the card is sharp
at your working distance. The two files must use identical camera requests,
and zoom must not change between capture and application. All settings are
restored when the camera closes, even after an error. Press **Q** to quit.

**The added lens.** The course webcam has almost no lens distortion, so ex01
deliberately adds a known barrel distortion to every frame, like a cheap
wide-angle lens, to give calibration something to find. `ADDED_FOCAL_PX` and
`ADDED_K1_K2` at the top of ex01 define it, and ex02 imports the same
function, so both scripts always see the same "lens". The black corners are
where this lens would look beyond the sensor. Set both coefficients to `0.0`
to calibrate the real camera instead; any change needs a new dataset.

## In class: about 50–60 minutes

### Ex01 — Capture a calibration dataset (about 15 min)

**Read the code** in `solutions/ex01_capture_dataset.py`:

- `REQUESTS`: why autofocus must be off. A calibration describes one lens
  position, and refocusing moves the lens.
- `add_lens_distortion` and `_lens_maps`: `cv2.remap` asks, for each output
  pixel, *where it comes from*, so the lens model has to be used backwards.
  You do not need to follow every line; note that the distortion is purely
  radial around the image centre.
- `detect_corners`: two stages. `findChessboardCorners` finds and orders the
  whole grid or fails; `cornerSubPix` then refines each corner below one pixel,
  because calibration accuracy depends on it.
- `save_view` and `main`: what gets saved is the **full distorted frame**, not
  the crop or the annotated panel. Intrinsics are defined in full-frame pixels.

**Run the demo.** The full frame shows a green central square; the crop and
the detected corners appear beside it. Press **H** to save the current frame
to `outputs/calibration/` (files are numbered automatically, also when you
resume).

1. Find the sharp range first: move the card closer and farther until the
   corners flicker or disappear, then work inside that range.
2. Save only **one or two** views of the card facing the camera, quit, and
   run ex02 once on this tiny dataset (ex02, step 1). Then come back: new
   views are numbered after the existing ones.
3. Capture 15–20 views in total with the whole card inside the green square:
   - near the centre and near each corner of the square, where the added
     distortion is strongest and constrains the lens coefficients;
   - near and far;
   - tilted by roughly 30–45° about both the horizontal and vertical axes.
     Front-facing views alone cannot separate focal length from distance.
4. Before each **H**, check the coloured corner ordering: corner 1 should stay
   on the same physical corner of the card. Push the tilt until detection
   fails, and notice the missing-corner message.

**Self-check:** you saved sharp, varied views, each showing all 54 corners.
Views with missing corners are still saved, but calibration skips them.

### Ex02 — Calibrate once, undistort live (about 20 min)

**Read the code** in `solutions/ex02_calibrate_undistort.py`:

- `template` in `calibrate`: the board *is* the world coordinate system, with
  every corner at Z = 0 and spaced by the square size. The square size only
  sets the units of the board poses; the camera matrix stays in pixels.
- The `calibrateCamera` call: known 3-D points plus observed pixels in, camera
  matrix `K` and distortion coefficients out. Note `CALIB_FIX_K3`, and why
  fewer parameters can transfer better than more.
- The per-view errors: `projectPoints` re-projects the board with the fitted
  model. The overall RMS hides a single bad view; the per-view list exposes it.
- `draw_reprojection`: detected corners as green circles, re-projected corners
  as red crosses, and the residual between them as a yellow line drawn 50
  times longer, because the real residuals are below a pixel.
- `rvecs` and `tvecs`: calibration also estimates the **extrinsics**, the
  board's pose in every view (`X_camera = R X_board + t`, with `R` from
  `cv2.Rodrigues`). `cv2.drawFrameAxes` draws the board's own coordinate
  system at corner 1 using that pose, and `main` writes every `R` and `t` to
  `outputs/reprojection/extrinsics.txt`.
- `process` and `main`: the model is fitted **once**, before the camera opens.
  Live frames only *apply* it with `cv2.undistort`; nothing is refitted. A
  resolution mismatch stops the script, because `K` is measured in pixels of
  one resolution.

**Run the demo.** The terminal shows the reprojection error of every view, the
overall RMS, `K`, and the distortion coefficients, and one image per view is
saved to `outputs/reprojection/` (replaced on every run), together with
`extrinsics.txt`. Read them before looking at the video:

1. **First run, on one or two views** (ex01, step 2). The script warns that
   there are few views, but the errors look excellent, often *lower* than with
   a full dataset, and the crosses sit on the circles. Now read `K`: the focal
   length and `(cx, cy)` are usually off, most clearly with a single view. In
   the live window, move the card to an edge of the frame and check whether it
   really straightens. Write down `K` and the errors, and rename the
   `reprojection` folder to keep these images.
2. **Second run, on the full dataset.** The errors rise a little (typically
   0.2–0.4 px) but `K` settles: `fx` and `fy` close, and `(cx, cy)` near the
   image centre (400, 300). Edges straighten everywhere in the live window.
   Compare the two reprojection folders: a few views can be fitted almost
   exactly, so a small error on the views used for fitting measures the *fit*,
   not whether the model is right. More varied views make the fit harder and
   the model correct.
3. In the full-dataset images, the yellow residuals should be short and point
   in random directions. A view whose error is several times the others
   (flagged in the terminal), or residuals that all point the same way, means
   a bad view: blurred, bent card, or wrong corner ordering. Delete it from
   `outputs/calibration/` and rerun.
4. Look at the board axes: X (red) runs along the first row of corners, Y
   (green) down the columns, and Z (blue) is perpendicular to the card. Pick
   a near and a far view and compare their `t` in `extrinsics.txt`: the
   length of `t` is the camera-to-corner-1 distance, in millimetres because
   the squares are 10 mm. A tilted view has an `R` far from the identity.
5. `k1` comes out negative (barrel) but does not equal the value in ex01. The
   coefficients are relative to the focal length, which the fit estimates.
6. The window shows three panels: the camera frame before the added lens, the
   distorted frame that calibration saw, and the undistorted result. Hold the
   card near the centre, then near an edge. The card's straight edges bend in
   the middle panel and straighten again on the right.
7. Tilt the card strongly: it still looks like a trapezoid after undistortion.
   Perspective comes from geometry, not from the lens, so it stays.

**Self-check:** with the full dataset, every view's error is well below one
pixel with short, randomly oriented residuals, and the undistorted panel
matches the camera frame before the added lens, edges included, while the
printed parameters stay fixed. The two-view run showed that a low error alone
does not prove transfer; the live frames near the edges do.

### Ex03 — Bird's-eye view from four points (about 15 min)

**Read the code** in `solutions/ex03_bird_eye.py`:

- `SOURCE_POINTS` and `DESTINATION_POINTS`: the homography is defined entirely
  by these two visible tables, listed clockwise from top-left.
- `rectify`: four point pairs give exactly the eight unknowns of a homography.
  There is no redundancy, so nothing can warn you about a wrong point.
- The destination rectangle sets the output's aspect ratio (8:5). It has to
  match the real plane's proportions, or the result is stretched.

**Run the demo** on the supplied `assets/planar_perspective.png`, then edit
the tables and rerun:

1. Swap two source points: the plane folds or twists. Restore clockwise order.
2. Move one source point by about 20 px: the result is quietly warped, and no
   error is raised.
3. Change the destination to a 500 × 500 square: the map is stretched.

**Self-check:** with the original tables, the plane fills the 800 × 500 output
as a rectangle with straight grid lines. Compare with ex02: undistortion
removes the lens effect, while a homography removes the perspective of one
plane.

## Optional: Ex04 — Robust stitching

**Read the code** in `solutions/ex04_stitch.py`:

- `LEFT_POINTS` and `RIGHT_POINTS`: eight hand-entered matches, where the last
  one is deliberately wrong. The scene is planar, so one homography relates the
  two views; there is no automatic feature matching.
- `estimate_homographies`: least squares lets every match pull on the
  solution, while RANSAC keeps the model that most matches agree with within
  3 px.
- `warp_pair`: the right view is warped into the left view's frame, and both
  are shifted so negative coordinates fit on the canvas. The overlap is
  averaged, so any misalignment shows as ghosting.

**Run the demo**, then edit and rerun:

1. Raise the RANSAC threshold to 100 px: the false match becomes an inlier
   and the robust stitch degrades like the direct one.
2. Correct the false match (remove its `(+75, -60)` displacement): both
   stitches agree.
3. Corrupt a second match and check whether RANSAC still rejects both.

**Self-check:** the false match is drawn in red, and the RANSAC stitch avoids
the large warp and ghosting of the direct stitch.

## Assumptions

Calibration assumes a rigid planar target, sharp and complete corner
observations, fixed intrinsics, and a lens that the distortion model can
describe. All fitting and application frames must share camera, resolution,
focus, and zoom. Undistortion removes the fitted lens distortion, not
perspective. The homography exercises do not need the focus lock; they assume
the mapped scene is a single plane.
