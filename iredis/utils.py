import time
import logging


logger = logging.getLogger(__name__)

_last_timer = time.time()
_timer_counter = 0
logger.debug(f"[timer] start on {_last_timer}")


def timer(title):
    global _last_timer
    global _timer_counter

    now = time.time()
    tick = now - _last_timer
    logger.debug(f"[timer{_timer_counter:2}] {tick:.8f} -> {title}")

    _last_timer = now
    _timer_counter += 1