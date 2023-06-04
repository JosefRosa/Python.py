pip install opencv-python
pip install numpy
import cv2
import numpy as np
def recognize_colors(image_path):
    image = cv2.imread(image_path)
    image = cv2.resize(image, (800, 600))
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    
    colors = {
        'Red': ([0, 100, 100], [10, 255, 255]),
        'Orange': ([10, 100, 100], [20, 255, 255]),
        'Yellow': ([20, 100, 100], [30, 255, 255]),
        'Green': ([40, 100, 100], [70, 255, 255]),
        'Blue': ([100, 100, 100], [140, 255, 255]),
        'Purple': ([140, 50, 50], [170, 255, 255]),
        'Pink': ([170, 100, 100], [180, 255, 255])
    }

    color_counts = {}
    for color_name, (lower, upper) in colors.items():
        lower = np.array(lower, dtype=np.uint8)
        upper = np.array(upper, dtype=np.uint8)
        mask = cv2.inRange(hsv_image, lower, upper)
        color_counts[color_name] = np.sum(mask == 255)

    sorted_colors = sorted(color_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_colors
    if __name__ == '__main__':
    image_path = 'path/to/your/image.jpg'
    results = recognize_colors(image_path)

    for color, count in results:
        print(f'Color: {color}, Count: {count}')
