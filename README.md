# Project Veil
## Setup
### Clone Repository
```
git clone https://github.com/zedaes/Project-Veil.git
cd Project-Veil
```
### Setup Virtual Environment
```
python -m venv .venv
source .venv/bin/activate
```
### Install Libraries
```
pip install -r requirements.txt
```

### Quickstart
```
git clone https://github.com/zedaes/Project-Veil.git
cd Project-Veil
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
## Usage
### Capture and Save Faces
Run the following command to **capture a face** and add it to the database:

`python capture_face.py`

The program will ask you to **enter a name** for the person.

It will **detect** and **display facial landmarks** (lines connecting facial features).

Press **'s' to save** the detected face, or **'q' to quit**.

### Recognize Faces in Real-Time

Once faces are saved, run:

`python recognize_faces.py`

The program will **scan for faces** using your webcam.

**Recognized faces** will be labeled with their **name in green**.

**Unknown faces** will be labeled as "Unknown" in **red**.

Facial landmarks will also be drawn.

Press **'q' to exit**.