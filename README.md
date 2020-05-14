# Semantic Segmentation Web and API Project
Web application and REST Api to serve DeepLabV3+ model to perform semantic segmentation on the input image.

### Tech stack
Backend - Django, Django rest framework 3.11
Frontend - HTML, CSS, JavaScript, Bootstrap, Jinja Templating Engine
To test apis - Postman

### Versions Tested with
- Python 3.6.4
- Django 2.2
- DRF 3.11
- django-cors-headers 3.2.1
- OS - Ubuntu 18 LTS 

### Directories
- /frontend --> To test apis 
- /media/images --> Stores Input Images
- /predict-with-deeplabv3 --> contains Deeplabv3 model and scripts
- /prediction --> App with prediction logic
- /sample-images --> Sample images to test
- /semantic-segmentation-api --> Main folder, contains settings 
- setup-env.sh --> Bash script to setup env required for the model
- predict-with-deeplabv3-script.sh --> Bash script to run inference script with environment, used by webapp 

### Steps
1. Make sure you have right dependencies
2. Run setup-env.sh
3. python manage.py migrate
4. python manage.py migrate --run-syncdb
5. python manage.py runserver

### Working
- Web: Run at /predict, Upload Image and it will segment the image and then show both images as comparison.
- API: Upload the image with a POST request to the server at /predict-api with an image as img field and it will respond with a link to the location of output image. 

### Credits
- Special thanks to original the author of DeeplabV3 and its implementation
- Mr Himanshu Mittal for guidance on major project

### Note
- Size of model is large in termas of disk space, making size of project large.
- It would be better to use docker to run the model.