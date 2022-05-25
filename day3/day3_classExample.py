from astropy.stats import sigma_clipped_stats
from photutils import datasets
from photutils import DAOStarFinder
import numpy as np
import matplotlib.pyplot as plt
from astropy.visualization import SqrtStretch
from astropy.visualization.mpl_normalize import ImageNormalize
from photutils import CircularAperture


# load a star image using photutils datasets
hdu = datasets.load_star_image()

# This line of code get the data and then cuts any pixel past row and column 401. The cut makes the image smaller and
# easier to work with
data = hdu.data[0:401, 0:401]

# get the standard deviation from pixel to pixel of things that are not stars. This will help us distinguish between
# pixels which are random noise and which are actually stars
mean, median, std = sigma_clipped_stats(data, sigma=5.0)

# load the DAOStarFinder function. The fwhm tell it how to determine the radius of a star
# the threshold helps determine when to ignore something and consider it not a star.

# Give a high threshold, only brighter stars will be selected, a low threshold will circule nearly everything
threshold = 28. * std

# this tells which size of PSF (size of star on image) that you want to circle. Give a high fwhm to circle larger PSF's
# or in other words, larger stars. Give a small fwhm to circle smaller PSF's or 'smaller' stars.
fwhm = 8.0
daofind = DAOStarFinder(fwhm=fwhm, threshold=threshold, ratio=.5)

# subtract the background from the imgage so the software doesn't get background light confused with stars
background_subracted_data = data - median

# call the loaded DAOStarFinder function and pass into the funtion the background subtracted data
sources_nomask = daofind(background_subracted_data)

# You will then get a bunch of information about the stars you find which you can print out
for col in sources_nomask.colnames:
    sources_nomask[col].info.format = '%.8g'  # for consistent table output
sources_nomask.pprint(max_lines=-1, max_width=-1)

# we will do a visulization of what daofind found by drawing circles around the discovered targets
circle_size = 6
# So this just transposes the positions matrix so the data is in the right format for photutil
positions_nomask = np.transpose((sources_nomask['xcentroid'], sources_nomask['ycentroid']))
# This is a photutil function which draws circles around targets
apertures_nomask = CircularAperture(positions_nomask, r=circle_size)
# normalized the image by the sqrt so more details can be seen
norm = ImageNormalize(stretch=SqrtStretch())

# next thing we can do is tell daoStarFinder to ignore certain parts of the image if you only want to look at one star
# we do this by creating what is called a mask and passing this mask into the function

# first create an empty true/false array (bool array) and make every value in the array False
# data.shape tells numpy to make this array the same size as our data array
mask = np.zeros(data.shape, dtype=bool)

# This basically draws a box of True values in our mask array. Any True values in the mask array will be ignored.
# Now, this sets the pixels in row 50 to 151, column 50 to 351 to True
mask[50:151, 50:351] = True

# We can draw a second box. THe location of this second box will be row 250 to 351, columns 150 to 351
right_side = 351
left_side = 150
top_side = 250
bottom_side = 351
mask[top_side:bottom_side, left_side:right_side] = True

# now lets find all the sources, but pass in the mask so that sources that are located in our two boxes are ignored
sources = daofind(background_subracted_data, mask=mask)

# again we have to transpose the array so that it is in the correct formate for photutils
positions = np.transpose((sources['xcentroid'], sources['ycentroid']))
# call the circle drawing function for the new positions
apertures = CircularAperture(positions, r=circle_size)
norm = ImageNormalize(stretch=SqrtStretch())

# finally lets plot everything out and vizualize what  we have found

# this sets the plot size to 12 by 12
plt.figure(figsize=(12, 12))

# plot the data using imshow, use a colormap that is gray
plt.imshow(data, cmap='Greys', origin='lower', norm=norm,
           interpolation='nearest')

# make the circles we draw red with the no mask sources
apertures_nomask.plot(color='red', lw=1.5, alpha=0.5)

# the sources outside the mask we color blue
apertures.plot(color='blue', lw=1.5, alpha=0.5)
plt.show()

