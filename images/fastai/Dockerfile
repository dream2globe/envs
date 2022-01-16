FROM pytorch/pytorch:latest

RUN conda install -c fastchan fastai -y && \
    conda install -c conda-forge jupyterlab_widgets ipywidgets jupyterlab -y

RUN mkdir -p /root/.fastai && \
    mkdir -p /root/.cache

ENTRYPOINT ["/bin/bash", "-c", "jupyter lab --ip=0.0.0.0 --allow-root --no-browser"]
