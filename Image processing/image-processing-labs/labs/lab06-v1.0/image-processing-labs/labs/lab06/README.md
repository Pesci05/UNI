# Lecture 6 — Hough voting and RANSAC

Follow the [root setup instructions](../../README.md) once (`uv sync`), select
the root `.venv` interpreter, and open a script with VS Code's top-right
**Run Python File** or **Debug Python File** button. Starters for every
exercise are in `exercises/`; replace each TODO with code and remove its
matching `NotImplementedError`. Each TODO stops the script with a message until
you implement it, so work through them in order. Camera acquisition, cropping,
segmentation, drawing, and cleanup are supplied. Compare your results with
`solutions/` after the visual self-checks.

## In class: about 50–60 minutes

### Ex01 — Hough lines and circles

Open `exercises/ex01_hough.py`. The script segments the dark ink, blurs the
mask, and computes its Canny boundaries in `edges`. Read the comment above the
blur: `HoughLinesP` votes on thin binary boundaries, not on filled strokes.
`side` is the crop side in pixels; express sizes as fractions of it so they
follow how large the card appears.

1. TODO 1: detect `lines` with `cv2.HoughLinesP` on `edges`. Set `rho` (pixels)
   and `theta` (radians) for the accumulator resolution, then `threshold`
   (votes), `minLineLength` and `maxLineGap` (pixels). On the card, the long
   strokes are about a quarter of the side, each dash about 9%, and the gap
   between dashes about 3%. A reasonable start is a 1-pixel, 1-degree accumulator, a vote
   threshold of 10% of `side`, a minimum length of 15%, and a maximum gap of
   10%. Write the unit of each parameter in a comment.
2. TODO 2: detect `circles` with `cv2.HoughCircles` and
   `method=cv2.HOUGH_GRADIENT` on `blurred_mask`. This method runs Canny
   itself (`param1` is its higher threshold) and lets every edge pixel vote
   for centres along its gradient direction; `param2` is the minimum number of
   votes a centre needs. The circles' radius is about 11% of the side, so a
   radius range of 10–15% is a good start; keep detected centres at least a
   quarter of `side` apart. Start with `dp=1.2`, `param1=127`, and `param2`
   around 5% of `side`.
3. Change one parameter at a time and explain the change using its unit.
   Lower `param2` until false circles appear. Lower `maxLineGap` below the
   dash gap: the dashed stroke disappears, because each dash alone is shorter
   than `minLineLength`.

A global vote can return several models, including segments from the branched
shapes. **Self-check:** three circles, including the open one, and the main
straight strokes appear on a well-framed card.

### Ex02 — Line RANSAC

Open `exercises/ex02_line_ransac.py` and use the same card. Each foreground
pixel of the small crop becomes a point in `points`, as `(x, y)` pairs.
`ordinary_line` fits a line `ax + by + c = 0` to any number of points, and
`distances_to_line` returns each point's perpendicular distance to it in
pixels: the algebraic residual divided by `sqrt(a² + b²)`. The loop, the seeded
random `generator`, the inlier `threshold` (2% of the crop side), the final
refit on the inliers, and the drawings are supplied.

1. At the TODO, write one RANSAC iteration inside the loop: draw two
   different point indices with `generator.choice(..., 2, replace=False)`,
   build the candidate line through them with `ordinary_line`, measure all
   distances with `distances_to_line`, and mark as inliers the points within
   `threshold`. Keep the boolean `inliers_mask` with the most inliers in
   `best_inliers_mask`.
2. Move the upper-right branched line into the small crop. The red ordinary
   fit uses every pixel and is pulled toward the branch; the green robust fit
   should follow the main stroke.
3. Try the disconnected middle line: missing pixels are simply absent votes.
   Then tune `threshold` to the stroke thickness and watch the inlier count.

RANSAC uses the segmented stroke's foreground pixels, including its interior,
as evidence. **Self-check:** in the last panel most main-stroke pixels are
green and most branch pixels are red.

## Optional exercises

### Ex03 — Ellipse RANSAC

Open `exercises/ex03_ellipse_ransac.py` and center the lower-right circle with
an attached tail in the small crop. The RANSAC loop has the same structure as
ex02, with an ellipse as the model. `ordinary_ellipse` fits an ellipse to five
or more points with `cv2.fitEllipse`.

1. TODO 1: in the loop, build the candidate. An ellipse needs five points, so
   draw five different indices with `generator` and fit them with
   `ordinary_ellipse`.
2. TODO 2: complete `distances_to_ellipse` so it returns each point's distance
   in pixels to the candidate's boundary. Draw the boundary with value 0 and
   thickness 1 on a `uint8` image of `image_shape` filled with 255. Then
   `cv2.distanceTransform(image, cv2.DIST_L2, cv2.DIST_MASK_PRECISE)` gives
   every pixel's distance to the nearest 0 pixel. Read that map at each
   point; remember that `points` holds `(x, y)`, which is `(column, row)`.

**Self-check:** the ordinary red fit bends toward the tail; the robust green
ellipse follows the circle, and the tail is mostly red in the last panel.

### Further investigations

- Tilt the physical card and compare the circular models with the new camera
  view. A tilted circle projects as an ellipse, exposing model mismatch in
  `HoughCircles`.
- Pass the filled ink mask directly to `HoughLinesP` in ex01, leaving all
  other parameters fixed. Compare it with Canny boundary voting on the same
  card. The many interior pixels in each thick stroke produce duplicate line
  segments. Raw signed Sobel output is not the binary input used by
  `HoughLinesP`; Canny uses image gradients to produce that boundary map.
- Add the confidence stopping rule derived in the lecture.
