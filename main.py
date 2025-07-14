import cv2

# Load a sample image (replace with your frame path)
img = cv2.imread('sample_frame.jpg')

# Show image window
cv2.imshow('Annotation Frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# In a real-world task, you'd annotate, label, and log accuracy/KPI
