""" Предлагает, как можно развить ноду """

class NodeExtender():
    """ TODO: должен ли это быть единый класс по типу фабрики,
    или каждый способ должен быть самостоятельной функцией?
    """

    def __init__(self):
        # TODO: разделить стратегии на несколько списков по смыслу (?)
        self._strategies = [

            # изменения высоты
            "transposeAll",
            "transposeSingle",
            "mirrorHorizontal",
            "mirrorVertical",

            # изменения темпа
            "speedUp",
            "slowDown"
            "randomizeTempo"

            # TODO: изменения динамики
        ]
