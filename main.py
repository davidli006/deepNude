import cv2

from run import process


def main():

	for name in [1, 11, 111]:
		# name = "666"
		img = cv2.resize(cv2.imread(f"images/{name}.png"), (512, 512))

		#Process
		watermark = process(img)

		# Write output image
		cv2.imwrite(f"images/output_{name}.png", watermark)


if __name__ == '__main__':
	main()