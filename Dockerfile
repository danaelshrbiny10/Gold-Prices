# Use an official Jupyter Docker image as the base image
FROM jupyter/scipy-notebook:latest

# Copy your Jupyter Notebook file to the working directory in the container
COPY main.ipynb F:\DataScience\code\GoldPrices\src\main.ipynb

# Expose the Jupyter Notebook port
EXPOSE 8888

# Start the Jupyter Notebook server
CMD ["jupyter", "notebook", "--ip=0.0.0.0"]
