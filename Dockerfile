FROM python:3.6-slim

# Create user and change cwd
ARG USERNAME=dockerman
RUN useradd -ms /bin/bash $USERNAME
WORKDIR /home/$USERNAME

# Install python-bitshares prerequisites
RUN apt-get update && apt-get install -y libssl-dev g++ libffi-dev

# Used for debugging only
RUN apt-get install -y net-tools curl wget procps nano

# Setup app + gunicorn
COPY requirements.txt ./
RUN python -m venv venv
RUN venv/bin/pip install --upgrade pip
RUN venv/bin/pip install -r requirements.txt

# Bug fix. Forcing the use of node.testnet.bitshares.eu
RUN grep -Rli 'wss://node.testnet.bitshares.eu' * | xargs -i@ sed -i 's/wss:\/\/node.bitshares.eu/wss:\/\/node.testnet.bitshares.eu/g' @

# Patching transaction builder
RUN wget -O venv/lib/python3.6/site-packages/bitshares/transactionbuilder.py https://raw.githubusercontent.com/bitshares/python-bitshares/27701d4f9d92ee2eecdc8001633083f856546820/bitshares/transactionbuilder.py

COPY run.py ./

ENTRYPOINT ["/home/dockerman/venv/bin/python", "run.py"]
