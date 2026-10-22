# Lecture 5 — Components, shapes, templates, and color

Follow the [root setup instructions](../../README.md) once (`uv sync`), select
the root `.venv` interpreter, and open a script with VS Code's top-right
**Run Python File** or **Debug Python File** button. Starters for every
exercise are in `exercises/`; replace each TODO with code and remove its
matching `NotImplementedError`. Each TODO stops the script with a message until
you implement it, so work through them in order. Camera acquisition, cropping,
display, and cleanup are supplied. Compare your results with `solutions/` after
the visual self-checks. These scripts use your webcam and the printed cards;
your live image will vary with focus, angle, lighting, and printer colors.

Ex03 and Ex05 deliberately spoil the camera's colors so there is something to
correct: their `REQUESTS` disable automatic white balance, then set the white
balance to 6500 K and the hue to 40. Edit `REQUESTS` at the top of either script
to try a different distortion. `camera_frames` restores every requested
setting before releasing the camera, including when the script stops with an
error.

## In class: about 50–60 minutes

### Ex01 — Connected components

Open `exercises/ex01_components.py` and use the shape card. The card has a
plain white background, so a fixed dark-ink threshold is supplied and applied
directly to the crop. Keep the paper filling the crop; dark surroundings and
strong shadows can become foreground too.

1. At the TODO, label the white regions of `ink` with
   `connectedComponentsWithStats` and 8-connectivity. It returns the number of
   labels, the label image, and the `stats` and `centroids` tables; label 0 is
   the background.
2. Build `accepted` from the foreground labels whose area, read from `stats`,
   is at least `minimum_area`.
3. Print `stats[label]` and `centroids[label]` for one accepted label and match
   them to its box in the last panel.
4. Draw a small dark speck on the paper: it appears in the binary mask but is
   rejected by the area filter.

**Self-check:** the last panel shows six boxed and
numbered objects. The numbers follow label order, which comes from the raster
scan and not from a left-to-right reading of the card. If the count changes,
first inspect the binary mask for merged or missing ink.

**Documentation:** [structural analysis and shape descriptors](https://docs.opencv.org/4.x/d3/dc0/group__imgproc__shape.html).

### Ex02 — Fit and enclose shapes

Open `exercises/ex02_simple_shapes.py` with the same card. Labeling is
supplied, and the script sorts the six components into two rows because each
position has a known shape prior. The upright rectangle is a worked example.
Enclosing methods use **all foreground pixels** of a component, given in
`points`. Fitting and approximation use **boundary points** instead: the ellipse
uses the supplied Canny edges of its component mask, and the polygon uses the
ordered contour from `findContours`.

1. TODOs 1, 2, and 4: enclose the rotated rectangle, the circle, and the
   triangle with the matching method from the lecture's shape-prior table.
   Follow the worked example's use of `points`.
2. TODO 3: fit the ellipse to `ellipse_points`.
3. TODO 5: compute the convex hull of the concave final object.
4. TODO 6: approximate the same object's contour with a closed polygon. Choose
   epsilon as a fraction of the contour perimeter; start from 1%.

**Self-check:** the hull bridges the notch; the polygonal approximation follows
it with about eight corners. Change the epsilon fraction to 0 and then to 0.1 to
see every pixel step kept and the notch cut away. A fitted or approximated
boundary need not enclose the original shape.

**Documentation:** [structural analysis and shape descriptors](https://docs.opencv.org/4.x/d3/dc0/group__imgproc__shape.html)
and [contour features](https://docs.opencv.org/4.x/dd/d49/tutorial_py_contour_features.html).

### Ex03 — Eight-pair empirical color normalization

Open `exercises/ex03_color_matrix.py` and use the color chart under steady,
even light. The circles show the eight sampled camera patches: six from row 1
and two neutrals from row 4. The source RGB pairs are visible in the script,
and sampling them into the 8 × 3 `measured` array is supplied.

1. TODO 1: compute the 3 × 3 `matrix` that minimizes
   `|measured @ matrix - REFERENCE_RGB|²`. Write the closed-form solution from
   the lecture first, then compare it with `np.linalg.lstsq`.
2. TODO 2: apply `matrix` to every pixel of the float `rgb` crop and clip the
   result to [0, 1].
3. Why does the fit need the two neutral patches as well as six saturated
   colors?

**Self-check:** all eight circles lie inside their patches, and in the
swatch panel the corrected row is closer to the reference row than the measured
row is. The matrix is recomputed on
every frame from the fixed sample positions; move the card to see how misaligned
sampling affects the result. Ex05 adds capture of one matrix for use on later
frames. Printer, illumination, clipping, and webcam processing make this
empirical normalization under fixed conditions, not metrological color
calibration.

**Documentation:** [`numpy.linalg.lstsq`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.lstsq.html)
and [camera capture](https://docs.opencv.org/4.x/d8/dfe/classcv_1_1VideoCapture.html).

## Optional exercises

### Ex04 — Template matching

Open `exercises/ex04_template_matching.py` and use the template scene. The
supplied 57 × 57 pixel template is already sized for a card filling a
600 × 600 camera crop. The decision rule that turns the score map into
detections, a threshold plus local peaks, is supplied together with the
heatmap and the boxes.

1. At the TODO, compute the `scores` map with `matchTemplate` and
   mean-subtracted normalized correlation of `template` over `gray`.
2. Compare the heatmap with the scene: bright peaks mark positions where the
   window looks like the template.
3. Move or tilt the card and watch the peak values drop.

**Self-check:** three upright symbols are boxed; the rotated and smaller
symbols are missed. A fixed raster template assumes the same scale and
rotation, so a different camera resolution also changes the symbol's pixel
size relative to this template.

**Extension:** switch to normalized squared differences. It scores a distance
rather than a similarity, so use `1 - scores` for the decision rule and the
heatmap. The supplied 0.75 threshold no longer separates the symbols: compare
the peak values of the matches and the rotated symbol under both methods, then
choose a new threshold.

**Documentation:** [template matching](https://docs.opencv.org/4.x/d4/dc6/tutorial_py_template_matching.html).

### Ex05 — Complete color chart

Open `exercises/ex05_full_color_chart.py` and use the color chart. Its title,
rules, frame, and numbered badge are ordinary printed graphics that also become
foreground components. Thresholding, labeling, row ordering, patch sampling,
the matrix fit from Ex03, and capture are supplied.

1. Inspect the raw threshold panel and identify which components are patches
   and which are printed graphics.
2. At the TODO, use `stats` and `centroids` to keep plausible patches by area
   relative to the crop, centroid position, aspect ratio, and fill ratio (area
   over bounding-box area). Measure a few components to choose the limits; a
   reasonable start is 0.4–5% of the crop area, aspect 0.65–1.7, fill at least
   0.75, and the centroid within the middle 60% of the crop's height.
3. The supplied labeling uses 4-connectivity; switch to 8 and confirm that the
   count does not change, since connectivity only matters where regions touch
   diagonally.
4. Once all 24 patches are labelled, press **C** to keep that matrix in memory.
   The last panel then applies it to each new camera crop, even when you point
   the camera elsewhere; restart the script to capture a new one.

**Self-check:** the accepted panel labels exactly 24 squares left to right, row
by row, with sampling rectangles inside each patch. After capture, the display
shows the full frame, original crop, and corrected crop; chart detection and
fitting stop. If chart detection fails, fewer diagnostic panels appear and C
captures no matrix. Under uneven light, improve lighting and framing before
changing code.

**Documentation:** [structural analysis and shape descriptors](https://docs.opencv.org/4.x/d3/dc0/group__imgproc__shape.html)
and [`numpy.linalg.lstsq`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.lstsq.html).
