# Скрипт расчета A/B подготовлен командой EXPF специально для лекций по A/B
# Курс по A/B-тестированиям expf.ru/ab_course
# A/B-платформа по подписке expf.ru/sigma

import pandas as pd

import config as cfg
from metric_builder import _load_yaml_preset
from report import build_experiment_report
import time

logger = cfg.logger
start_time = time.time()

# скачайте отдельно https://drive.google.com/file/d/14Ftj8iSt3ysfNi3889Dg-q78h-E_iaI4/view?usp=sharing
# df = pd.read_parquet(f'data/parquet/df.parquet')

# Мини-версия таблицы с данными по эксперименту, количество строк = 10000
df = pd.read_csv("data/csv/df_sample.csv")
logger.info("Data loaded")

experiment_report = build_experiment_report(
    df=df,
    metric_config=_load_yaml_preset(preset="todo")
)
experiment_report.to_csv(f"experiment_report.csv")

cfg.logger.info(time.time() - start_time)
