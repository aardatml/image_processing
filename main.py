import cv2
import numpy as np
import matplotlib.pyplot as plt

def detect_traffic_sign(image_path):
    img = cv2.imread(image_path)
    if img is None:
        print("Görüntü okunamadı")
        return

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    hsv = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2HSV)

    img_area = img.shape[0] * img.shape[1]


    lower_red1 = np.array([0, 100, 100])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([160, 100, 100])
    upper_red2 = np.array([180, 255, 255])

    lower_blue = np.array([90, 100, 100])
    upper_blue = np.array([130, 255, 255])

    red_mask = cv2.inRange(hsv, lower_red1, upper_red1) + \
               cv2.inRange(hsv, lower_red2, upper_red2)
    blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)

    combined_mask = red_mask + blue_mask


    edges = cv2.Canny(combined_mask, 100, 200)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    sign_type = "Levha bulunamadı"
    distance_info = ""

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area < 1500:
            continue

        peri = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, 0.04 * peri, True)

        x, y, w, h = cv2.boundingRect(approx)
        cv2.rectangle(img_rgb, (x, y), (x+w, y+h), (0, 255, 0), 2)


        ratio = area / img_area
        if ratio > 0.08:
            distance_info = "Yakın"
        elif ratio > 0.03:
            distance_info = "Orta Mesafe"
        else:
            distance_info = "Uzak"


        if len(approx) == 3:
            sign_type = "Uyarı Levhası"


        elif len(approx) > 6:
            mean_color = np.mean(hsv[y:y+h, x:x+w, 0])
            if mean_color < 10 or mean_color > 160:
                sign_type = "Yasak Levhası"
            else:
                sign_type = "Zorunlu Levha"

        break


    title = f"Tespit: {sign_type}"
    if distance_info:
        title += f" | Mesafe: {distance_info}"

    plt.figure(figsize=(8, 6))
    plt.imshow(img_rgb)
    plt.title(title)
    plt.axis("off")
    plt.show()



detect_traffic_sign("levha1.jpg")
