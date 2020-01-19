import cv2

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') #classifier (if face is present or not)
cap = cv2.VideoCapture(0)

while True:

	ret, frame = cap.read()

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


	faces = faceCascade.detectMultiScale(
		frame, 
		scaleFactor=1.1,
		minSize=(30,30))

	for (x,y,w,h) in faces:
		print("cd")
		cv2.rectangle(frame, 
			(x,y), 
			(x+w, y+h), 
			(0,255,0),2
			)

	cv2.imshow('camera', frame)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
