# Grayscale
Grayscale with Python
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install cv2 and numpy.


```bash
pip install cv2
pip install numpy
```
## Import

```python
import cv2
import numpy as np
```
## Reading image from file

```python
img = cv2.imread("cat.png")
```
## Gray scale

```python
gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
```
## Completion message

```python
print('Image Grayscaled.')
```
## Comparing original vs resized

```python
cv2.imshow('ORIGINAL',img)
cv2.imshow('GRAYSCALE',gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

## Images
<p align="center">
	<img src="/cat.png" alt="Logo", height=200px,width=200px>
	<img src="/cat.png" alt="Logo", height=200px,width=200px>
</p>

### Developed by
 [Ashish ku. Behera](https://github.com/ashish-max "Github Id")
