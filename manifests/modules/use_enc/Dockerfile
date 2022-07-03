FROM daynauth/jaseci-kit:latest
ENV DEBIAN_FRONTEND=noninteractive

#COPY /home/ypkang/jaseci/jaseci_kit ./jaseci_kit
#RUN cd jaseci_kit && source install.sh
COPY load_model.py .
RUN python3 load_model.py

# RUN sed -i '13d' /jaseci/jaseci_kit/jaseci_kit/modules/text_segmenter/text_segmenter.py
