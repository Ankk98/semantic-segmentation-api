# Semantic Segmentation Web and API Project
Web application and REST Api to serve DeepLabV3+ model to perform semantic segmentation on the input image.

### Tech stack
- Backend - Django, Django rest framework
- Frontend - HTML, CSS, JavaScript, Bootstrap, Jinja Templating Engine
- To test apis - Postman
- For virtual environment- pyenv

### Tested on
- Python 3.6.8
- Django 3.0.6
- Django rest framework 3.11.0
- django-cors-headers 3.2.1
- OS - Ubuntu 20 LTS 

### Directories
- `/frontend` --> To test apis 
- `/media/images` --> Stores Input Images
- `/predict-with-deeplabv3` --> contains Deeplabv3 model and scripts
- `/prediction` --> App with prediction logic
- `/sample-images` --> Sample images to test
- `/semantic-segmentation-api` --> Main folder, contains settings 
- `setup-env.sh` --> Bash script to setup env required for the model
- `predict-with-deeplabv3-script.sh` --> Bash script to run inference script with environment, used by webapp 

### Steps to run locally (On Linux based distro)
1. Install `pyenv`
2. Run `setup-env.sh`
3. `pyenv local venvSSA`
3. `python manage.py migrate`
4. `python manage.py migrate --run-syncdb`
5. `python manage.py runserver`

### Working
- **Web**: Run at /predict, Upload Image and it will segment the image and then show both images as comparison.
- **API**: Upload the image with a POST request to the server at /predict-api with an image as img field and it will respond with a path to the location of output image. 

### APIs
- `/predict` --> Return webpage with functionality to upload an image and get inferred image.
- `/about` --> Returns about page
- `/predict-api` --> Takes post requests with an image field as 'img' and returns path to inferred image.

### Credits
- Special thanks to original the author of DeeplabV3+ and its implementation
- Mr Himanshu Mittal for guidance on major project

### Note
- Size of model is large in terms of disk space, making size of project large.
- It would be better to use docker to run the model.
- It would be better to use a webserver like nginx to serve inferred images.
- Not for production (It is a simple College Project)

### Screenshots
- Website front page
![GitHub Logo](/screenshots/ss_front_page.png)
- After prediction
![GitHub Logo](/screenshots/ss-output.png)
- API response in postman
![GitHub Logo](/screenshots/Screenshot_postman.png)
- About page
![GitHub Logo](/screenshots/ss-about-page.png)
- Running django server using vscode
![GitHub Logo](/screenshots/Screenshot_code.png)
- Classes it is able to predict
![GitHub Logo](/predict-with-deeplabv3/colour_scheme.png)

### References
- https://github.com/rishizek/tensorflow-deeplab-v3-plus
- https://github.com/DrSleep/tensorflow-deeplab-resnet 
