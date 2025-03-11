from loguru import logger

# Configuration de base du logger
logger.add(
    "projet3.log",  # Nom du fichier de logs
    rotation="1 week",  # Rotation hebdomadaire
    level="INFO"
) # noqa