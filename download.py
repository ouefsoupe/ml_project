import kagglehub

# Download latest version
path = kagglehub.dataset_download("saurabhbagchi/deepfake-image-detection", path=".")

print("path = %s" % path)