class DragonBallException(Exception):
    """Clase base para las excepciones personalizadas de Dragon Ball."""
    pass
class ListadoVacioException(DragonBallException):
    """Excepción lanzada cuando un listado está vacío."""
    pass
class ListadoNoEsListaException(DragonBallException):
    """Excepción lanzada cuando el argumento no es una lista."""
    pass