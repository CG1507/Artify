<h1 align="center">
  :art: style-transfer :framed_picture:
  <h3 align="center">
  :video_game: PlayGround
  </h3>
  <br />
  <img src="https://github.com/CG1507/style-transfer/blob/master/images/demo.gif" width="900" height="500" />
</h1>

## Requirements:
* PyQt5
* Keras
* numpy
* scipy
* h5py
* scikit-image

## Run:

Following code-snippet opens window to select content and style images. It gives you flexibility to change the hyperparameter of the learning process.
```
python3 gui.py
```

After generation of style transfered images, if you want to preserve the original color of the content image then:
```
python3 color_transform.py <path-to-content-image> <path-to-generated image>
```

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Author

[<img src="https://avatars3.githubusercontent.com/u/24426731?s=460&v=4" width="70" height="70" alt="Ghanshyam_Chodavadiya">](https://github.com/CG1507)

## Acknowledgement

:green_heart: [ozamanan](https://github.com/ozamanan/Neural-Style-Transfer)
