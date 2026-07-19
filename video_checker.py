import cv2
import mediapipe as mp


mp_pose = mp.solutions.pose


def analyze_video(path):

    cap = cv2.VideoCapture(path)


    frames = int(
        cap.get(cv2.CAP_PROP_FRAME_COUNT)
    )


    fps = cap.get(
        cv2.CAP_PROP_FPS
    )


    duration = frames / fps


    movement_found = False


    pose = mp_pose.Pose()


    checked_frames = 0


    while True:

        success, frame = cap.read()

        if not success:
            break


        rgb = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )


        results = pose.process(rgb)


        if results.pose_landmarks:
            movement_found = True


        checked_frames += 1


        if checked_frames > 100:
            break



    cap.release()



    score = 0


    if duration >= 10:
        score += 40


    if movement_found:
        score += 60



    verified = score >= 70



    if verified:

        feedback = (
            "Workout verified. "
            "KING XP awarded."
        )

    else:

        feedback = (
            "Verification failed. "
            "Upload a clearer workout video."
        )


    return {

        "verified": verified,

        "score": score,

        "feedback": feedback
    }
