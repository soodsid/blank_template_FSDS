from loguru import logger
import os
from dotenv import find_dotenv
from datetime import datetime

now = datetime.now()
filename= now.strftime("%Y-%m-%d")+'.log'
      
logger.remove()

logger.add(os.path.join(os.path.dirname(find_dotenv()),'logs', filename), backtrace=True, diagnose=True, format="-"*200+"\n{time: YYYY-MM-DD HH:mm:ss} | {level} | {module}.{function}.{line} — {message}", level='INFO', colorize=False)