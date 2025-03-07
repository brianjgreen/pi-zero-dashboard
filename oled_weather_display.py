#
# Read weather reports from JSON files and display forecast on a tony OLED
# Tested on a Raspberry Pi Zero W
# 0.96 Inch OLED I2C Display Module 12864 128x64 Pixel SSD1306
# Reusing code from https://github.com/rm-hull/luma.examples
# Demo Video: https://youtu.be/gYM97AqxEqI
#

import json
import sys
import time
from pathlib import Path

from luma.core import cmdline, error
from luma.core.render import canvas
from PIL import ImageFont

font_name = "DejaVuSansMono.ttf"
font_size = 17
font_size2 = 19

font_default = ImageFont.truetype(
    str(Path(__file__).resolve().parent.joinpath("fonts", font_name)), font_size
)
font_larger = ImageFont.truetype(
    str(Path(__file__).resolve().parent.joinpath("fonts", font_name)), font_size2
)
margin_y_line = [0, 20, 40, 45, 60]
margin_x = 0


def get_device(actual_args=None):
    """
    Create device from command-line arguments and return it.
    """
    if actual_args is None:
        actual_args = sys.argv[1:]
    parser = cmdline.create_parser(description="luma.examples arguments")
    args = parser.parse_args(actual_args)

    if args.config:
        # load config from file
        config = cmdline.load_config(args.config)
        args = parser.parse_args(config + actual_args)

    # create device
    try:
        device = cmdline.create_device(args)
        return device

    except error.Error as e:
        parser.error(e)
        return None


device = get_device()


def main():
    #
    # For locations.json, dictionary of key name and value zipcode
    # {
    #     "Boston": "02110",
    #     "NewYorkCity": "10010"
    # }
    #
    with open("locations.json", "r") as file:
        locations = json.load(file)

    for loc, addr in locations.items():
        with open(f"{loc}.json", "r") as file:
            report = json.load(file)

        for f in report["forecast"]:
            with canvas(device) as draw:
                draw.text(
                    (margin_x, margin_y_line[0]),
                    report["location"],
                    font=font_default,
                    fill="white",
                )
                draw.text(
                    (margin_x, margin_y_line[1]),
                    f["day_temp"],
                    font=font_larger,
                    fill="white",
                )
                draw.text(
                    (margin_x, margin_y_line[2]),
                    f["conditions"],
                    font=font_larger,
                    fill="white",
                )

            time.sleep(5)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
