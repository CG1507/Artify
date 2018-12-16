<h1 align="center">
  <img src="https://github.com/CG1507/style-transfer/blob/master/images/logo.png"/>
</h1>

Artify is Neural Style Transfer playground for creating art, coloring the sketches, and transfering the styles to content image. It is implemented to faster experimentation with different images and settings.

## Requirements
* PyQt5
* Keras
* numpy
* scipy
* h5py
* scikit-image

## Run

Following code-snippet opens window to select content and style images. It gives you flexibility to change the hyperparameter of the learning process.
```
python3 gui.py
```

<h1 align="center">
  <img src="https://github.com/CG1507/style-transfer/blob/master/images/demo.gif" width="900" height="500" />
</h1>

After generation of style transfered images, if you want to preserve the original color of the content image then:
```
python3 color_transform.py <path-to-content-image> <path-to-generated image>
```

## Results

Images

## Todo

- [ ] Colab support
- [ ] custom model support for finding better settings
- [ ] preserve color in GUI

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Author

[<img src="https://avatars3.githubusercontent.com/u/24426731?s=460&v=4" width="70" height="70" alt="Ghanshyam_Chodavadiya">](https://github.com/CG1507)

## Acknowledgement

:green_heart: [ozamanan](https://github.com/ozamanan/Neural-Style-Transfer)
