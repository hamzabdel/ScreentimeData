import json
import math
from pathlib import Path

import numpy as np
import onnx
import pandas as pd
import pytorch_lightning as pl
import tensorflow as tf
import torch
import torch.nn as nn
import torch.nn.functional as F
import torchmetrics
import wandb
from kaggle_secrets import UserSecretsClient
from onnx_tf.backend import prepare
from pytorch_lightning.callbacks import EarlyStopping
from pytorch_lightning.callbacks import LearningRateMonitor
from pytorch_lightning.loggers import WandbLogger
from sklearn.model_selection import StratifiedGroupKFold
from timm.optim import create_optimizer_v2
from torchmetrics import MetricCollection