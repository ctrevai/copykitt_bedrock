FROM public.ecr.aws/lambda/python:3.12

COPY requirements.txt ${LAMBDA_TASK_ROOT} 

RUN pip3 install -r requirements.txt

COPY src/* ${LAMBDA_TASK_ROOT}
# resolving permission denied in lambda
RUN chmod 644 ${LAMBDA_TASK_ROOT}/*

CMD [ "copykitt_api.handler" ]