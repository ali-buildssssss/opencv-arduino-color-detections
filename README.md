# opencv-arduino-color-detections

# OpenCV + Arduino Color Detection

This is a project I built using Python, OpenCV and Arduino.

The idea was simple: detect different colored objects through a webcam and use Arduino to control LEDs based on the detected color.

I wanted to explore how computer vision can interact with real hardware, so I connected OpenCV with Arduino using Python serial communication.

## How It Works

- A webcam captures live video.
- OpenCV processes the video and detects colors.
- Python communicates with Arduino.
- Arduino controls the connected LEDs according to the detected color.

## Technologies Used

- Python
- OpenCV
- Arduino Uno
- PySerial
- VS Code

## Project Structure

```text
opencv-arduino-color-detection/
│
├── python/
│   └── project_2.py
│
├── arduino/
│   └── multi_lights.ino
│
├── images/
│
└── README.md
```

## What I Learned

While building this project, I got practical experience with:

- Real-time color detection using OpenCV.
- Working with webcam video frames.
- Communicating between Python and Arduino.
- Controlling hardware through serial communication.
- Combining software and electronics in one project.

## Future Improvements

I would like to improve this project by adding more features and exploring additional computer vision applications.

---

**Built as a learning project while exploring Python, computer vision and hardware automation.**
