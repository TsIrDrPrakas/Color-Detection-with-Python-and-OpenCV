# Color-Detection-with-Python-and-OpenCV

## Color Detection with Python and OpenCV

This repository showcases a Python script utilizing OpenCV to detect specific colors in real-time video capture. 

**Key Features:**

* **Flexible Color Selection:** Supports detecting any color you choose by adjusting the script's color definitions.
* **Real-time Detection:** Analyzes each frame of your webcam input to highlight the chosen color in real-time.
* **Bounding Box Visualization:** Draws a bounding box around the detected color region for clear identification.

**Prerequisites:**

* **Python 3:** Ensure you have Python 3 installed on your system.
* **OpenCV:** Install OpenCV library through `pip install opencv-python`.
* **Alternative installation methods:** Install OpenCV and other library:  `pip install -r requirements.txt`.
* **util.py:** This repository includes a separate `util.py` file containing the `get_limits` function responsible for calculating HSV limits of the chosen color.

**Getting Started:**

1. Clone the repository or download the zip file.
2. Install OpenCV if not already done.
3. Run the script `main02.py`.
4. Observe the webcam feed with a highlighted bounding box around the detected color.
5. Modify the `yellow` variable in `main01.py` to any desired BGR color tuple (e.g., (255, 0, 0) for red) to track different colors.

**Customization:**

* Adjust the `lowerlimit` and `upperlimit` values in the `get_limits` function for finer control over the detected color range.
* Explore using different color spaces like Lab or grayscale for specific scenarios where HSV might not be ideal.
* Implement additional functionalities like counting instances of the detected color or triggering actions based on its presence.

**Contributing:**

* Feel free to fork and improve the code! Pull requests with bug fixes, enhancements, or new features are welcome.
* Share your experiences and challenges to further develop the project's capabilities.

**Note:** This script and its color detection accuracy might be affected by lighting conditions, object textures, and camera quality. Experiment and adjust settings for optimal results in your specific environment.

I hope this README file provides a clear overview of the project and encourages you to explore and contribute to color detection with Python and OpenCV!
