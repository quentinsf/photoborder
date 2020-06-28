# Add a border to an image

This very simple script adds a border to an image, and then saves the result as a copy in the same location as the original but with a '-wb' suffix on its name.

The 'wb' stood for 'white border', but now you can specify the colour, so I guess it stands for 'with border'!
(My original use for this was when incorporating photos in slides or videos that had a black background.)

You can run it with a '-h' option to see the syntax.

By default, the border will be white, and its width will be half a percent of the longest dimension. 
So the output image will be 1% bigger than the original in that dimension.

This requires Python 3 and the Pillow imaging library.  It should therefore support [the same file formats as Pillow](https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#fully-supported-formats), and you can specify colours using [the colour names supported by Pillow](https://pillow.readthedocs.io/en/stable/reference/ImageColor.html).  Remember that characters like '#' and '%' may mean something to your shell, so you should probably put strings like '#ffc0e0' in quotes.

Quentin Stafford-Fraser
https://quentinsf.com
June 2021
