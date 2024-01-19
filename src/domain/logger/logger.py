from typing import Dict, Optional

import logging
import logging.config


import src.domain.logger.formatter as fmtr


_loggers: Dict[str, logging.Logger] = {}


def new_colored_logger(
    name: str,
    level: Optional[int] = logging.INFO,
) -> logging.Logger:
    """Register new colored logger object."""
    # Create logging object with given name
    logger = logging.getLogger(name)

    # Add print format for stdout
    ch = logging.StreamHandler()
    ch.setLevel(level)
    ch.setFormatter(fmtr.ColoredFormatter())
    
    # Set format and set logging level
    logger.addHandler(ch)
    logger.setLevel(level)
    
    # Register logger
    _loggers[name] = logger
    
    return logger


def get_logger(name: str) -> logging.Logger:
    """Fetch logger object with given name."""
    if name not in _loggers:
        raise KeyError(f'cannot find logger with given name: {name}.')
    
    return _loggers[name]
