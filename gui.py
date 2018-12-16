import style_transfer
import inspect, os, sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import file_io
import shutil

#os.system('python improved_densenet121.py "./images/contents/stata.jpg" "./images/styles/udnie.jpg" "id"')
#os.remove("ChangedFile.csv") #it removes image file
#self.image_size_combo.setEnabled(False)
#‘nearest’, ‘lanczos’, ‘bilinear’, ‘bicubic’ or ‘cubic’ #rescale algo
#python improved_densenet121.py "./images/contents/stata.jpg" "./images/styles/udnie.jpg" "result_prefix" --image_size --content_weight 
#	--style_weight --style_scale --total_variation_weight --num_iter --model --content_loss_type --rescale_image --rescale_method 
#	--maintain_aspect_ratio --content_layer --init_image --pool_type --preserve_color --min_improvement

class App(QMainWindow):

	def __init__(self):
		super().__init__()
		self.title = 'Artify playGround'
		self.left = 10
		self.top = 10
		self.width = 1400
		self.height = 750
		self.initUI()

		#Arguments
		self.base_image_path = ''
		self.syle_image_paths = ''
		self.image_size = 400
		self.content_weight = 0.025
		self.style_weight = 1
		self.style_scale = 1
		self.total_variation_weight = 8.5e-5
		self.num_iter = 10
		self.model = 'VGG16'
		self.content_loss_type = 0
		self.rescale_image = True
		self.rescale_method = 'bilinear'
		self.maintain_aspect_ratio = True
		self.content_layer = 'conv5_2'
		self.init_image = 'content'
		self.pool_type = 'max'
		self.preserve_color = False
		self.min_improvement = 0.0
		self.improved_net = True

		self.artistic_images = []
		self.selected_art_image = ''

	def initUI(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)
		#self.statusBar().showMessage('Message in statusbar.')

		self.browse_button1_label = QLabel(self)
		self.browse_button1_label.move(150, 20)
		self.browse_button1_label.setText("Content Image")		
		self.browse_button1_label.resize(200, 20)

		self.button1 = QPushButton('Browse', self)
		self.button1.setToolTip('Only JPEG/JPG')
		self.button1.move(150,50) 
		self.button1.clicked.connect(self.on_click1)

		self.browse_button2_label = QLabel(self)
		self.browse_button2_label.move(610, 20)
		self.browse_button2_label.setText("Style Image")		
		self.browse_button2_label.resize(200, 20)

		self.button2 = QPushButton('Browse', self)
		self.button2.setToolTip('Only JPEG/JPG')
		self.button2.move(600,50) 
		self.button2.clicked.connect(self.on_click2)
		self.button2.setEnabled(False)

		"""
		self.browse_button3_label = QLabel(self)
		self.browse_button3_label.move(1050, 20)
		self.browse_button3_label.setText("Artistic Image")		
		self.browse_button3_label.resize(200, 20)
		
		button3 = QPushButton('Browse', self)
		button3.setToolTip('Only JPEG/JPG')
		button3.move(1050,50) 
		button3.clicked.connect(self.on_click3)
		"""

		self.label1 = QLabel(self)
		self.label1.move(10, 100)

		self.label2 = QLabel(self)
		self.label2.move(450, 100)
		
		self.label3 = QLabel(self)
		self.label3.move(890, 100)

		self.paint = QPushButton('Paint it!', self)
		self.paint.setToolTip('Only JPEG/JPG')
		self.paint.move(1040,410) 
		self.paint.clicked.connect(self.on_click_paint) #change method
		self.paint.setEnabled(False)

		self.image_initialize_button = QPushButton('Get the painted artistic images', self)
		self.image_initialize_button.setToolTip('Only Image')
		self.image_initialize_button.move(950,5) 
		self.image_initialize_button.resize(300, 30)
		self.image_initialize_button.clicked.connect(self.initialize_images)
		self.image_initialize_button.setEnabled(False)

		self.image_selection_label = QLabel(self)
		self.image_selection_label.move(890, 54)
		self.image_selection_label.setText("Select artistic images")		
		self.image_selection_label.resize(200, 20)
		self.image_selection_label.setEnabled(False)

		self.image_selection_combo = QComboBox(self)
		self.image_selection_combo.move(1050, 50)
		self.image_selection_combo.resize(220,30)
		self.image_selection_combo.setEnabled(False)
		self.image_selection_combo.activated[str].connect(self.showArtImage)

		self.content_weight_label = QLabel(self)
		self.content_weight_label.move(10, 450)
		self.content_weight_label.setText("Content weights")		
		self.content_weight_label.resize(200, 20)

		self.content_weight_textbox = QLineEdit(self)
		self.content_weight_textbox.move(130, 450)
		self.content_weight_textbox.resize(180,20)
		self.content_weight_textbox.setText("0.025")

		self.style_weight_label = QLabel(self)
		self.style_weight_label.move(500, 450)
		self.style_weight_label.setText("Style weights")		
		self.style_weight_label.resize(200, 20)

		self.style_weight_textbox = QLineEdit(self)
		self.style_weight_textbox.move(600, 450)
		self.style_weight_textbox.resize(180,20)
		self.style_weight_textbox.setText("1")

		self.tv_weight_label = QLabel(self)
		self.tv_weight_label.move(900, 450)
		self.tv_weight_label.setText("Total variation weights")		
		self.tv_weight_label.resize(200, 20)

		self.tv_weight_textbox = QLineEdit(self)
		self.tv_weight_textbox.move(1080, 450)
		self.tv_weight_textbox.resize(180,20)
		self.tv_weight_textbox.setText("8.5e-5")

		self.iteration_label = QLabel(self)
		self.iteration_label.move(10, 500)
		self.iteration_label.setText("No. of Iteration")		
		self.iteration_label.resize(200, 20)

		self.iteration_textbox = QLineEdit(self)
		self.iteration_textbox.move(130, 500)
		self.iteration_textbox.resize(180,20)
		self.iteration_textbox.setText("10")

		self.min_improve_label = QLabel(self)
		self.min_improve_label.move(430, 500)
		self.min_improve_label.setText("Minimum Improvement")		
		self.min_improve_label.resize(200, 20)

		self.min_improve_textbox = QLineEdit(self)
		self.min_improve_textbox.move(600, 500)
		self.min_improve_textbox.resize(180,20)
		self.min_improve_textbox.setText("0.0")

		self.style_scale_label = QLabel(self)
		self.style_scale_label.move(900, 500)
		self.style_scale_label.setText("Style scale")		
		self.style_scale_label.resize(200, 20)

		self.style_scale_textbox = QLineEdit(self)
		self.style_scale_textbox.move(1080, 500)
		self.style_scale_textbox.resize(180,20)
		self.style_scale_textbox.setText("1")

		self.model_label = QLabel(self)
		self.model_label.move(10, 550)
		self.model_label.setText("Model name")		
		self.model_label.resize(200, 20)

		self.model_combo = QComboBox(self)
		self.model_combo.addItem("VGG16")
		self.model_combo.addItem("VGG19")
		self.model_combo.move(130, 550)
		self.model_combo.resize(180,20)
		self.model_combo.activated[str].connect(self.onActivated)

		self.image_size_label = QLabel(self)
		self.image_size_label.move(500, 550)
		self.image_size_label.setText("Image size")		
		self.image_size_label.resize(200, 20)

		self.image_size_combo = QComboBox(self)
		self.image_size_combo.addItem("400")
		self.image_size_combo.addItem("500")
		self.image_size_combo.addItem("600")
		self.image_size_combo.move(600, 550)
		self.image_size_combo.resize(180,20)
		self.image_size_combo.activated[str].connect(self.onActivated)

		self.initial_layer_label = QLabel(self)
		self.initial_layer_label.move(900, 550)
		self.initial_layer_label.setText("Initial layer")		
		self.initial_layer_label.resize(200, 20)

		self.initial_layer_combo = QComboBox(self)
		self.initial_layer_combo.addItem("content")
		self.initial_layer_combo.addItem("noise")
		self.initial_layer_combo.addItem("gray")
		self.initial_layer_combo.move(1080, 550)
		self.initial_layer_combo.resize(180,20)
		self.initial_layer_combo.activated[str].connect(self.onActivated)

		self.content_layer_label = QLabel(self)
		self.content_layer_label.move(10, 600)
		self.content_layer_label.setText("Content layer")		
		self.content_layer_label.resize(200, 20)

		self.content_layer_combo = QComboBox(self)
		self.content_layer_combo.addItem("conv5_2")
		self.content_layer_combo.addItem("conv4_2")
		self.content_layer_combo.move(130, 600)
		self.content_layer_combo.resize(180,20)
		self.content_layer_combo.activated[str].connect(self.onActivated)

		self.pooling_type_label = QLabel(self)
		self.pooling_type_label.move(500, 600)
		self.pooling_type_label.setText("Pooling type")		
		self.pooling_type_label.resize(200, 20)

		self.pooling_type_combo = QComboBox(self)
		self.pooling_type_combo.addItem("max")
		self.pooling_type_combo.addItem("avg")
		self.pooling_type_combo.move(600, 600)
		self.pooling_type_combo.resize(180,20)
		self.pooling_type_combo.activated[str].connect(self.onActivated)

		self.content_loss_type_label = QLabel(self)
		self.content_loss_type_label.move(900, 600)
		self.content_loss_type_label.setText("Content loss type")		
		self.content_loss_type_label.resize(200, 20)

		self.content_loss_type_combo = QComboBox(self)
		self.content_loss_type_combo.addItem("0")
		self.content_loss_type_combo.addItem("1")
		self.content_loss_type_combo.addItem("2")
		self.content_loss_type_combo.move(1080, 600)
		self.content_loss_type_combo.resize(180,20)
		self.content_loss_type_combo.activated[str].connect(self.onActivated)

		self.rescale_algo_label = QLabel(self)
		self.rescale_algo_label.move(10, 650)
		self.rescale_algo_label.setText("Rescale algo")		
		self.rescale_algo_label.resize(200, 20)

		self.rescale_algo_combo = QComboBox(self)
		self.rescale_algo_combo.addItem("bilinear")
		self.rescale_algo_combo.addItem("nearest")
		self.rescale_algo_combo.addItem("lanczos")
		self.rescale_algo_combo.addItem("bicubic")
		self.rescale_algo_combo.addItem("cubic")
		self.rescale_algo_combo.move(130, 650)
		self.rescale_algo_combo.resize(180,20)
		self.rescale_algo_combo.activated[str].connect(self.onActivated)

		self.rescale_dim_cb = QCheckBox('Rescale to original dimensions', self)
		self.rescale_dim_cb.move(500, 650)
		self.rescale_dim_cb.toggle()
		self.rescale_dim_cb.resize(300, 20)
		self.rescale_dim_cb.stateChanged.connect(self.changeTitle)

		self.improved_net_cb = QCheckBox('Use Improved Network', self)
		self.improved_net_cb.move(900, 650)
		self.improved_net_cb.toggle()
		self.improved_net_cb.resize(300, 20)
		self.improved_net_cb.stateChanged.connect(self.changeTitle)

		self.preserve_color_cb = QCheckBox('Preserve color', self)
		self.preserve_color_cb.move(10, 700)
		self.preserve_color_cb.toggle()
		self.preserve_color_cb.resize(300, 20)
		self.preserve_color_cb.stateChanged.connect(self.changeTitle)

		self.aspect_ratio_cb = QCheckBox('Maintain aspect ratio', self)
		self.aspect_ratio_cb.move(500, 700)
		self.aspect_ratio_cb.toggle()
		self.aspect_ratio_cb.resize(300, 20)
		self.aspect_ratio_cb.stateChanged.connect(self.changeTitle)

		#pixmap = QPixmap('stata.jpg')
		#label.setPixmap(pixmap)
		#label.resize(400, 300)

		self.show()

	def changeTitle(self, state):
		if state == Qt.Checked:
			print('Checked')
		else:
			print('Unchecked')

	def onActivated(self, text):
		#self.model_label.setText(text)
		#self.model_label.adjustSize()
		print("Activated")
		
	@pyqtSlot()
	def on_click1(self):
		self.openFileNameDialog1()
		self.button2.setEnabled(True)
		print('button click')

	@pyqtSlot()
	def on_click2(self):
		self.openFileNameDialog2()
		self.paint.setEnabled(True)
		print('button click')

	@pyqtSlot()
	def on_click_paint(self):
		#self.openFileNameDialog3()
		self.get_arguments()
		if self.improved_net:
			final_file = './improved_vgg.py'
		else:
			final_file = './vgg.py'

		execute_line = 'python3 ' + str(final_file) + ' "' + str(self.base_image_path) + '" "' + str(self.syle_image_paths) + '" "' + 'painted_img' + '" ' + '--image_size ' + str(self.image_size) + ' --content_weight ' + str(self.content_weight) + ' --style_weight ' + str(self.style_weight) + ' --style_scale ' + str(self.style_scale)	+ ' --total_variation_weight ' + str(self.total_variation_weight) + ' --num_iter ' + str(self.num_iter) + ' --model ' + str(self.model) + ' --content_loss_type ' + str(self.content_loss_type) + ' --rescale_method ' + str(self.rescale_method) + ' --content_layer ' + str(self.content_layer) + ' --init_image ' + str(self.init_image) + ' --pool_type ' + str(self.pool_type) + ' --min_improvement ' + str(self.min_improvement)

		if self.preserve_color:
			execute_line += ' --preserve_color "' + str(self.preserve_color) + '" '

		if self.maintain_aspect_ratio:
			execute_line += '--maintain_aspect_ratio "' + str(self.maintain_aspect_ratio) + '" '

		if self.rescale_image:
			execute_line += ' --rescale_image "' + str(self.rescale_image) + '" '

		self.image_initialize_button.setEnabled(True)
		os.system(execute_line)

	def initialize_images(self):
		print('initialize images')
		if self.improved_net == True:
			self.artistic_images = file_io.list_txt_files('./results/gui/ivgg/', '.png')
		else:
			self.artistic_images = file_io.list_txt_files('./results/gui/vgg/', '.png')
		
		self.image_selection_label.setEnabled(True)
		self.image_selection_combo.setEnabled(True)

		for image in self.artistic_images:
			self.image_selection_combo.addItem(image)

	@pyqtSlot()
	def showArtImage(self):
		self.selected_art_image = self.image_selection_combo.currentText()
		if self.selected_art_image != '':
			file = self.selected_art_image
			
			if self.improved_net == True:
				fileName = './results/gui/ivgg/' + file + '.png'
			else:
				fileName = './results/gui/vgg/' + file + '.png'
				
			if self.check_file(fileName, file):
				shutil.copyfile(fileName, './' + file)

			pixmap = QPixmap(file)
			pixmap = pixmap.scaled(400, 300)
			self.label3.setPixmap(pixmap)
			self.label3.resize(400, 300)
			self.base_image_path = fileName
		os.remove('./' + file)

	def openFileNameDialog1(self):    
		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog
		fileName, _ = QFileDialog.getOpenFileName(self, "Select an Image", "", "All files(*);;Image Files (*.jpeg);;Python Files (*.jpg)", 
			options=options)
		if fileName:
			print(fileName)
			file = fileName.split('/')[-1]
			if self.check_file(fileName, file):
				shutil.copyfile(fileName, './' + file)

			pixmap = QPixmap(file)
			pixmap = pixmap.scaled(400, 300)
			self.label1.setPixmap(pixmap)
			self.label1.resize(400, 300)
			self.base_image_path = fileName
		os.remove('./' + file)

	def openFileNameDialog2(self):    
		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog
		fileName, _ = QFileDialog.getOpenFileName(self, "Select an Image", "", "All files(*);;Image Files (*.jpeg);;Python Files (*.jpg)", 
			options=options)
		if fileName:
			print(fileName)
			file = fileName.split('/')[-1]
			if self.check_file(fileName, file):
				shutil.copyfile(fileName, './' + file)

			pixmap = QPixmap(file)
			pixmap = pixmap.scaled(400, 300)
			self.label2.setPixmap(pixmap)
			self.label2.resize(400, 300)
			self.syle_image_paths = fileName
		os.remove('./' + file)


	def check_file(self, fileName, file):
		currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
		temp = str(currentdir + '/' + file).strip()

		if temp == fileName.strip():
			return False
		return True

	def get_arguments(self):
		self.content_weight = self.content_weight_textbox.text()
		self.style_weight = self.style_weight_textbox.text()
		self.total_variation_weight = self.tv_weight_textbox.text()
		self.style_scale = self.style_scale_textbox.text()
		self.num_iter = self.iteration_textbox.text()
		self.min_improvement = self.min_improve_textbox.text()
		self.image_size = self.image_size_combo.currentText()
		self.model = self.model_combo.currentText()
		self.rescale_method = self.rescale_algo_combo.currentText()
		self.content_layer = self.content_layer_combo.currentText()
		self.pool_type =self.pooling_type_combo.currentText()
		self.init_image = self.initial_layer_combo.currentText()
		self.content_loss_type = self.content_loss_type_combo.currentText()
		self.rescale_image = self.rescale_dim_cb.isChecked()
		self.maintain_aspect_ratio = self.aspect_ratio_cb.isChecked()
		self.preserve_color = self.preserve_color_cb.isChecked()
		self.improved_net = self.improved_net_cb.isChecked()


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec_())