import cv2

video_path = "./co-tracker/ShawnAssets/MouseRun_UnifyBG_16_9cut_8sec.mp4"
cap = cv2.VideoCapture(video_path)
print("Video opened:", cap.isOpened())

frame_idx = 0  # 想找第 0 幀
cap.set(cv2.CAP_PROP_POS_FRAMES, frame_idx)

ret, frame = cap.read()

if ret:
    # 顯示畫面並用滑鼠選點
    def click_event(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            print(f"Clicked coordinates: ({x}, {y})")

    cv2.imshow("Frame", frame)
    cv2.setMouseCallback("Frame", click_event)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
