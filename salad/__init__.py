# -*- coding: utf-8 -*-
from logging import INFO, getLogger, StreamHandler

logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(INFO)
logger.setLevel(INFO)
logger.addHandler(handler)
logger.propagate = False
