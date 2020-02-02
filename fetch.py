import os
import urllib.request

VERSIONS = [
	'4.2.0',
	'4.1.2',
	'4.1.1',
	'4.1.0',
	'3.4.9',
	'3.4.8',
	'3.4.7',
	'3.4.6',
]

def downlown_opencvjs_file (version, filename):
	url = "https://docs.opencv.org/%s/opencv.js" % version

	with urllib.request.urlopen(url) as response, open(filename, 'wb') as out_file:
		data = response.read() # a `bytes` object
		out_file.write(data)

def main():
	for v in VERSIONS:
		print("Checking version %s" % v)

		dst_dir_path = os.path.join(os.path.dirname(__file__), "v%s" % (v))
		dst_file_path = os.path.join(dst_dir_path, "opencv.js")
		if os.path.isfile(dst_file_path):
			print("The file already exist. Skip this version.")
		else:
			print('Dowloadinag v%s' % v)
			os.makedirs(dst_dir_path)
			downlown_opencvjs_file(v, dst_file_path)

if __name__ == '__main__':
	main()
