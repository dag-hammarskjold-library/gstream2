# Use the official Python image as the base
FROM public.ecr.aws/lambda/python:3.11

# Set the working directory in the container
WORKDIR /app

# Install git
RUN yum install -y git-all

# Copy the requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install git+https://github.com/dag-hammarskjold-library/gdoc-api@948317cd38c91c9a4f0baece13e6eba883beb294

# Copy the rest of the application code
COPY . .

ENV AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID}
ENV AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY}
ENV AWS_DEFAULT_REGION=${AWS_DEFAULT_REGION}
ENV GDOC_ENV=${GDOC_ENV}

# Expose port 8000
EXPOSE 8000

# Start the application
ENTRYPOINT [ "uvicorn" ]
CMD ["api:app", "--host", "0.0.0.0", "--port", "8000"]