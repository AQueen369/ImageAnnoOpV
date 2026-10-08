import cv2
import matplotlib.pyplot as plt

#step 1: loadd the image
image_path = 'example.jpg'  #user-provided image path
image = cv2.imread(image_path)

# convert BGR to RGB for correct colour display with matplotlib
image_rgb = cv2.cvt.Color(image, cv2.COLOR_BGR2RGB)

# get image dimensions
height, width, _ = image_rgb.shape

# step  2: Draww two rectangles around the interesting regions
#rectangle 1: top left corner
rect1_width, rect1_height = 150, 150
top_left1 = (20, 20)  # fixed 20 pixels padding from top-left
bottom_right1 = (top_left1[0] + rect1_width, top_left1[1] + rect1_height)
cv2.rectangle(image_rgb, top_left1, bottom_right1, (0, 255, 255), 3)  #yellow rectangle

# rectangle 2: bottomm right corner
rect2_width, rect2_height = 200, 150
top_left2 = (width - 20, height - rect2_height - 20) # 20 pixels padding
bottom_right2 = (top_left2[0] + rect2_width, top_left2[1] + rect2_height)
cv2.rectangle(image_rgb, top_left2, bottom_right2, (255, 0, 255), 3) # magenta

# step 3: draww circles at the centers of both rectangles
center1_x = top_left1[0] + rect1_width // 2
center1_y = top_left1[1] + rect1_height // 2
center2_x = top_left2[0] + rect2_width // 2
center2_y = top_left1[1] + rect2_height // 2
cv2.circle(image_rgb, (center1_x, center1_y), 15 (0, 255, 0), -1) # Filled Green Circle
cv2.circle(image_rgb, (center2_x, center2_y), 15 (0, 255, 0), -1) # Filled Red Circle

# Step 4: Draww Connecting lines between centers of rectangles
cv2.line(image_rgb, (center1_x, center1_y), (center2_x, center2_y), (0, 255, 0), 3)

# Step 5: Add text labels for regions and centers
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image_rgb, 'Region 1', (top_left1[0], top_left1[1] - 10), font, 0.7, (255, 255, 255), 2, cv2.Line.AA)
cv2.putText(image_rgb, 'Region 2', (top_left2[0], top_left2[1] - 10), font, 0.7, (255, 255, 255), 2, cv2.Line.AA)
cv2.putText(image_rgb, 'Center 1', (center1_x - 40, center1_y + 40), font, 0.6, (0, 255, 0), 2, cv2.Line_AA)
cv2.putText(image_rgb, 'Center 2', (center2_x - 40, center2_y + 40), font, 0.6, (0, 255, 0), 2, cv2.Line_AA)

# Step 6: add Bi-directional arrow representing height
arrow_start = (width - 50, 20)  # start near the top right
arrow_end = (width - 50, height - 20)  # End near the bottom-right

# draw arrow in both directions
cv2.arrowedLine(image_rgb, arrow_start, arrow_end, (255, 255, 0), 3, tipLength=0.05)
#Downward Arrow
cv2.arrowedLine(image_rgb, arrow_end, arrow_start, (255, 255, 0), 3, tipLength=0.05)
#Upward Arrow
