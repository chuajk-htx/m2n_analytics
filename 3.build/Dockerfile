# Start with an official Python base image, somehow this is the only version that I tested so I just gonna use this
FROM python:3.12.4

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Install Jupyter and I dunno if there are anything else better to run this
RUN pip install --no-cache-dir notebook
RUN pip install pandas
RUN pip install sqlalchemy
RUN pip install matplotlib
RUN pip install mysqlclient
# RUN pip install -r requirements.txt, somehow this does not work as intended, then I just let it run the pip install above
# Expose Jupyter's default port, have not tried changing this value and I do not want to break anything
EXPOSE 8888

# Set the working directory in the container
WORKDIR /workspace

# Start Jupyter Notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]

# To build and run: (you can ignore the sudo as well)
# sudo docker build -t python-analytics .
# sudo docker run -p 8888:8888 python-analytics
# To access the notebook:
# http://localhost:8888

# To cleanup excess docker images:
# sudo docker rm $(sudo docker ps -a -q -f status=exited)
# sudo docker images -f dangling=true
# sudo docker rmi $(sudo docker images -q -f dangling=true)

# For windows
# docker build -t analytics-platform .
# docker run -p 8888:8888 analytics-platform
# http://localhost:8888

# To save the image, run
# docker save -o analytics-platform-image.tar analytics-platform
# 