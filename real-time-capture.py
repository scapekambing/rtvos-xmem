import cv2
import time

def draw_rectangle(event, x, y, flags, param):
    global start_x, start_y, end_x, end_y, drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        start_x, start_y = x, y
        drawing = True

    elif event == cv2.EVENT_LBUTTONUP:
        end_x, end_y = x, y
        drawing = False

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            end_x, end_y = x, y

def init_rect():
    global start_x, start_y, end_x, end_y, drawing

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Cannot open camera")
        exit()

    desired_fps = 15
    cap.set(cv2.CAP_PROP_FPS, desired_fps)

    # Init coordinates
    start_x, start_y = -1, -1
    end_x, end_y = -1, -1
    drawing = False

    cv2.namedWindow('frame')
    cv2.setMouseCallback('frame', draw_rectangle)

    print('first loop')
    while True:
        ret, frame = cap.read()

        if not ret:
            print("uh stream end? Exiting ...")
            break
        
        cv2.putText(frame, 'draw a rectangle then press "q" when done', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.rectangle(frame, (start_x, start_y), (end_x, end_y), (0, 0, 255), 2)
        cv2.imshow('frame', frame)    
        if cv2.waitKey(1) == ord('q'):
            break

        time.sleep(1/desired_fps)
        
    cap.release()
    cv2.destroyAllWindows()


def detect_boundary():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Cannot open camera")
        exit()

    desired_fps = 15
    cap.set(cv2.CAP_PROP_FPS, desired_fps)


    cv2.namedWindow('frame')

    print('second loop')
    while True:
        ret, frame = cap.read()

        if not ret:
            print("uh stream end? Exiting ...")
            break

        cv2.rectangle(frame, (start_x, start_y), (end_x, end_y), (0, 0, 255), 2)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) == ord('q'):
            break

        time.sleep(1/desired_fps)

    cap.release()
    cv2.destroyAllWindows()

def main():
    init_rect()
    detect_boundary()

if __name__ == '__main__':
    main()
