from flask import Flask, render_template, Response
import cv2

app = Flask(__name__)


def gen_frames():
    cap1 = cv2.VideoCapture(0)
    cap2 = cv2.VideoCapture(1)

    while True:
        success1, img1 = cap1.read()
        success2, img2 = cap2.read()

        if not success1 or not success2:
            break

        else:
            img1 = cv2.resize(img1, (0, 0), fx=1, fy=1)
            img2 = cv2.resize(img2, (0, 0), fx=1, fy=1)

            frame = cv2.hconcat([img1, img2])
            ret, buffer = cv2.imencode('.jpg', frame)
            frpiame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    cap1.release()
    cap2.release()


@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/')
def index():
    return '''<html>Hello</html>'''


if __name__ == '__main__':
    app.run(debug=True)
