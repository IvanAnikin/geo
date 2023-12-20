import rasterio

def get_four_corners_coordinates(tif_file):
    with rasterio.open(tif_file) as src:
        # Get the transformation matrix
        transform = src.transform

        # Get the image dimensions
        width = src.width
        height = src.height

        # Get the coordinates of the four corners
        top_left = transform * (0, 0)
        top_right = transform * (width, 0)
        bottom_left = transform * (0, height)
        bottom_right = transform * (width, height)

    return top_left, top_right, bottom_left, bottom_right

# Replace 'your_file.tif' with the actual path to your GeoTIFF file
tif_file_path = 'mytif.tif'
corners = get_four_corners_coordinates(tif_file_path)

print("Top Left Corner:", corners[0])
print("Top Right Corner:", corners[1])
print("Bottom Left Corner:", corners[2])
print("Bottom Right Corner:", corners[3])