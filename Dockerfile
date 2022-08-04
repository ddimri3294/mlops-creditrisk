# initiate the base image
FROM python:3.9.12

RUN apt-get update

# define the current working directory
ENV APP_HOME /apps
WORKDIR $APP_HOME

# copy the content into the working dir
COPY . ./

RUN ls -la $APP_HOME

# install the requirements
RUN pip install -r requirements.txt

# run streamlit on container
CMD ["streamlit", "run", "--server.enableCORS", "false", "mlops_prediction.py"]

# gcloud container clusters create mlops-kube --zone "asia-east1-a" --machine-type "n1-standard-1" --num-nodes "1"
