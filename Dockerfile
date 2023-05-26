FROM python:3.10.8
ADD a.py
RUN pip install -r requirements.txt
CMD [ "python", "./a.py" ]
