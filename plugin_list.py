# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "pedalboard-pluginary>=1.1.0",
#     "pedalboard>=0.9.16",
#     "rich>=13.9.4",
#     "setuptools>=75.6.0",
# ]
# ///

from pedalboard_pluginary import PedalboardPluginary
from rich import print


def main():
    print(PedalboardPluginary().list_plugins())


if __name__ == "__main__":
    main()
