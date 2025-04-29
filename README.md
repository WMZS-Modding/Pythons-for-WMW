# Pythons for WMW
A very small open-source code for any WMW games
## AbsoluteLocationChanger

A simple Python script to shift all AbsoluteLocation values in a given XML file.

### Usage

```bash
python AbsoluteLocationChanger.py "{input_xml}" -o "{output_xml}" -value "{x y}"

- `input_xml`: path to XML level
- `output_xml`: name of the XML you want to save
- `x y`: number you want to plus or minus (0 to do nothing)

## AbsoluteLocationChanger2

A modified script of AbsoluteLocationChanger.py. This script is still shift all AbsoluteLocation values in a given XML file, but it's only change AbsoluteLocation in HS file in Filename.

### Usage

```bash
python AbsoluteLocationChanger2.py "{input_xml}" -o "{output_xml}" -value "{x y}" -hs "{hs_name}, {hs_name_2},..."

- `input_xml`: path to XML level
- `output_xml`: name of the XML you want to save
- `x y`: number you want to plus or minus (0 to do nothing)
- `hs_name, hs_name_2,...`: name of the HS file in Filename you want to change only (it'll find the path on `value` after `Filename`, you should write correct path of `value` after `Filename`)
