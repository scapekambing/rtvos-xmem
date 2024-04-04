# Real-time Video Object Segmentaiton with XMem

This is a fork of [XMem](https://github.com/hkchengrex/XMem). To our current knowledge, this is the first demonstration of XMem running real-time detection.

This has been tested on Windows 11.

## Requirements

* Python 3.8+
* PyTorch 1.11+ (See [PyTorch](https://pytorch.org/) for installation instructions)
* torchvision (follow the *pip* instructions in https://pytorch.org/get-started/locally/)
* OpenCV (try pip install opencv-python)
* Others: pip install -r requirements.txt
* Others: pip install -r requirements_demo.txt
* Pretrained models: Download fbrs.pth, s2m.pth and XMem.pth into a new directory from root called saves.

## Getting Started

First, ensure you are in the correct enviornment and then run 

python ./main.py
`
Then, you'll be prompted to take a photo of the first frame. Ensure there is minimal change to the scene after the photo has been taken. Press "enter" to take the photo.

Next, you'll be given the option to select a single object mask with the left mouse button. If you make a mistake, simply hit the reset frame. Do not select more than 1 as the feature for more than 1 object has not been implemented. Close the window when complete.

After first frame selection, we demonstrate boundary detection with a rectangular boundary. You will be prompted to select the top, then bottom, then left, then right borders. Once complete, the window will close and launch the demo!
