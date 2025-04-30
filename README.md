# Pythons for WMW
A small open-source code for any WMW games. This was many pythons can helping you when you were edit XML levels
## AbsoluteLocationChanger

A simple Python script to shift all `AbsoluteLocation` values in a given XML file.

### Usage

```bash
python AbsoluteLocationChanger.py "{input_xml}" -o "{output_xml}" -value "{x y}"
```

- `input_xml`: path to XML level
- `output_xml`: name of the XML you want to save
- `x y`: number you want to plus or minus (0 to do nothing)

## AbsoluteLocationChanger2

A modified script of `AbsoluteLocationChanger.py`. This script is still shift all `AbsoluteLocation` values in a given XML file, but it's only change `AbsoluteLocation` in `HS` file in `Filename`.

### Usage

```bash
python AbsoluteLocationChanger2.py "{input_xml}" -o "{output_xml}" -value "{x y}" -hs "{hs_name}, {hs_name_2},..."
```

- `input_xml`: path to XML level
- `output_xml`: name of the XML you want to save
- `x y`: number you want to plus or minus (0 to do nothing)
- `hs_name, hs_name_2,...`: name of the HS file in Filename you want to change only (it'll find the path on `value` after `Filename`, you should write correct path of `value` after `Filename`)

## PathPointsExtractor
**PathPointsExtractor** is a Python script that extracts simplified path points from black pixel lines (typically 1-pixel wide) in grayscale images − useful for path-based gameplay, navigation systems, or visual logic tools.
### Features
- Extracts a path from black pixels in an image (e.g., hand-drawn in MS Paint)
- Simplifies the path using angular thresholds and minimum distance
- Outputs points in a compact comma-separated format for use in game engines or visual editors
### Usage
```bash
python PathPointsExtractor.py input_image.png -o output.txt
```
- `input_image.png`: A grayscale image with a black path on a white background
- `output.txt`: The file to save the extracted path points (comma-separated x y pairs)
### Output Format
- The script saves the result as a single line: `x1 y1, x2 y2, x3 y3,...`
- This code you can paste on XML:
```XML
<Property name="PathPoints" value="x1 y1, x2 y2, x3 y3,..."/>
```
### Notes
- Ensure the path is 1-pixel wide, made with pure black (RGB 0,0,0) on a white background.
- The path should not loop back to the start; closed loops may be ignored.
- Endpoints like `0.0 0.0` may appear if the drawing touches image corners − feel free to remove them manually.
- Works best on straight or clearly defined paths. Jagged or overlapping lines might produce noisy results.
### Dependencies
Make sure to install the required Python libraries:
```bash
pip install numpy Pillow scipy scikit-image networkx
```
### Finally
Now you can use `PathPointsExtractor.py` to help you create different metal pipe shapes
