# Image Resizer Offline

Image Resizer Offline is a simple and efficient tool for resizing images to predefined or custom dimensions(thumbnail,medium,large). It works entirely offline, ensuring your privacy and security.

## Features
- Resize images from any format JPEG, PNG or WEBP
- Batch processing support for resizing multiple images at once.
- Reduce file size without loosing image quality.
- Works entirely offline, ensuring privacy and security.

## Installation

### Windows:
1. Have python installed in your system
2. Make a virtual enviornment
3. Install all dependencies


## Usage
1. Run make_key.py
2. Right click on your current directory -> Resize -> Choose from files
3. Enter width dimensions and suffix. Click resize.
4. To remove the key binding, Run remove_key.py

## Build
1. Install pyinstaller library
2. Run ```pyinstaller --onefile --noconsole --name=resizer resizer.py```
3. Run ```pyinstaller --onefile --name=makekey makekey.py```
4. Run ```pyinstaller --onefile --name=remove_key remove_key.py```

## Requirements
- Windows 10 or later / macOS 10.14 or later / Linux (Ubuntu, Fedora, Arch, etc.)
- Minimum 2GB RAM (4GB recommended)
- At least 100MB of free disk space

## Support
For issues and feature requests, please open an issue on the [GitHub repository](#) or contact support via email at `official.himanshudubey@gmail.com`.

## License
This project is licensed under the [MIT License](LICENSE).

