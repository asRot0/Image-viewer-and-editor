# Image Viewer and Editor

![Project Logo](./assets/image.png) <!-- Optional: Add an image logo -->

Welcome to the **Image Viewer and Editor**! This application is designed to provide users with a powerful yet user-friendly interface for viewing and editing images. Built using Python's `customtkinter`, it offers a variety of functionalities, including rotating images, adjusting colors, applying effects, and exporting in multiple formats.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Code Structure](#code-structure)
- [Components Overview](#components-overview)
- [Detailed Functionality](#detailed-functionality)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **Intuitive User Interface**: Designed for ease of use, even for beginners.
- **Image Manipulation**: Rotate, zoom, flip, and apply various color adjustments and effects.
- **Multiple Export Formats**: Save your edited images in JPG or PNG formats.
- **Real-Time Preview**: See changes as you make them with real-time updates.
- **Customization**: Adjust sliders and switches to fine-tune your images.
- **About Section**: View information about the application, its version, and the developer.

## Installation

To set up the Image Viewer and Editor on your local machine, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/asRot0/Image-viewer-and-editor.git
2. **Navigate to the Project Directory:**
    ```bash
   cd Image-viewer-and-editor
3. **Install Dependencies: Make sure you have Python installed. Then install the required libraries using pip**
    ```bash
   pip install -r requirements.txt
4. **Run the Application: Start the application using the command**
    ```bash
   python run.py

## Usage

### Launching the Application
After running `run.py`, the main interface will appear.

### Opening an Image
Use the **File Path Panel** to select an image from your file system. Click the button to open the file explorer and choose your desired image.

### Editing the Image
- **Position Tab**: Adjust the rotation and zoom level using sliders. You can also flip the image vertically or horizontally.
- **Color Tab**: Modify properties like brightness, contrast, and vibrance. You can also convert the image to grayscale or invert its colors.
- **Effects Tab**: Apply various effects to the image, including blur and contour.

### Exporting the Edited Image
- Use the `Export` section to specify a name and choose the format (JPG or PNG). Click the save button to export your edited image.

## Code Structure
The project is organized as follows:

```lua
Image-viewer-and-editor/
|-- assets/                 # Contains assets like images and icons
|-- files/                  # Main application files
|   |-- __init__.py
|   |-- frame.py            # Frame structure and layout
|   |-- frame_widgets.py    # Widgets for frames
|   |-- image_widgets.py    # Image handling widgets
|   |-- menu.py             # Main menu and tabs
|   |-- panels.py           # UI panels and components
|   |-- photo_editor.py     # Main application logic
|   |-- settings.py         # Configuration settings
|-- run.py                  # Entry point for the application
```

## Key Files and Their Responsibilities

- **run.py**: The main entry point of the application, responsible for launching the application.

- **settings.py**: Contains configuration settings, constants, and paths for assets used in the application.

- **menu.py**: Implements the main menu layout and manages the navigation between different editing tabs.

- **panels.py**: Contains various UI panels that house the editing controls and options for users.

- **photo_editor.py**: This file contains the core logic for the image editing functionalities.

## Components Overview

### Main Components

- **Menu**: The application is organized into tabs:
  - **Position**: Adjust image rotation and zoom.
  - **Color**: Modify brightness, contrast, and color settings.
  - **Effects**: Apply effects like blur or contour.
  - **Export**: Specify the file name and format for saving the image.

- **Panels**: Each tab contains specific panels that group related controls, making it easy for users to navigate the functionalities.

- **Settings**: Centralized settings for asset paths and default values used throughout the application.

## Detailed Functionality

### Position Frame
- **Rotation**: Control the rotation of the image from 0 to 360 degrees using a slider.
- **Zoom**: Adjust the zoom level from 0% to 200% using a slider.
- **Invert**: Use a segmented button to flip the image in different orientations (None, X, Y, Both).

### Color Frame
- **Brightness**: Adjust the brightness of the image with a slider (0 to 5).
- **Grayscale**: Convert the image to black and white using a switch.
- **Invert Colors**: Toggle color inversion using a switch.
- **Vibrance**: Adjust the vibrance of the image with a slider (0 to 5).

### Effects Frame
- **DropDown Menu**: Select from various effects (None, Emboss, Find edges, etc.).
- **Blur**: Apply a blur effect adjustable from 0 to 10.
- **Contrast**: Adjust the contrast of the image from 0 to 10.

### Export Frame
- **File Name**: Input the desired file name for the exported image.
- **File Format**: Choose between JPG and PNG formats using checkboxes.
- **File Path**: Select the destination folder for saving the edited image.
- **Save Button**: Click to export the edited image with the specified parameters.

## Screenshots

#### Main Interface

#### Position Controls

#### Color Adjustments

#### Effects Panel

#### Export Options

## Contributing
Contributions are welcome! If you have suggestions for improvements or new features, please create an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For any questions or inquiries, feel free to contact.
- *Name*: Asif Ahmed (asRot0)
- *LinkedIn*: [in/asifahm9090](https://www.linkedin.com/in/asifahm9090/)