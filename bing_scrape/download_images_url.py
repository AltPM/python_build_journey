from urllib.request import urlopen, HTTPError, URLError


src = "https://images.alltrails.com/eyJidWNrZXQiOiJhc3NldHMuYWxsdHJhaWxzLmNvbSIsImtleSI6InVwbG9hZHMvcGhvdG8vaW1hZ2UvMzc4NjU1MzAvYzM1OWQ2YzliZDZiNGMxMmFiNWM2MzVhYWY0YTBhM2IuanBnIiwiZWRpdHMiOnsidG9Gb3JtYXQiOiJqcGVnIiwicmVzaXplIjp7IndpZHRoIjo1MDAsImhlaWdodCI6NTAwLCJmaXQiOiJpbnNpZGUifSwicm90YXRlIjpudWxsLCJqcGVnIjp7InRyZWxsaXNRdWFudGlzYXRpb24iOnRydWUsIm92ZXJzaG9vdERlcmluZ2luZyI6dHJ1ZSwib3B0aW1pc2VTY2FucyI6dHJ1ZSwicXVhbnRpc2F0aW9uVGFibGUiOjN9fX0="

try:
    img = urlopen(src).read() #fetch image data
    open("target.jpg", "wb").wrtie(img)
    print("Image saved")
except HTTPError:
    print("HTTP Error, Image not available")
except URLError:
    print("URL Error, image can't be downloaded")

    