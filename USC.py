from OrderScale import OrderScale

class UniversalCoverter:
    __MinUniversalScaleValue__ = 0
    __MaxUniversalScaleValue__ = 100
    __UniversalSacaleOrder = OrderScale.ASCENDING
    __MinInputScaleValue__ = 0
    __MaxInputScaleValue__ = 100
    __InputSacaleOrder__ = OrderScale.ASCENDING

    def __init__(self, MinInput, MaxInput, InputScale):
        if MaxInput == MinInput:
            raise Exception("O valor do MaxInput e MinInput são iguais")
        if InputScale is OrderScale.ASCENDING:
            if MaxInput < MinInput:
                raise Exception("Escala crescente o input maximo tem que ser maior que imput minimo")
        elif InputScale is OrderScale.DESCENDING:
            if MaxInput > MinInput:
                raise Exception("Escala decrescente o input minimo tem que ser maior que imput maximo")
        else:
            raise TypeError("Tipo de InputScale não suportado")
        self.__MinInputScaleValue__ = MinInput
        self.__MaxInputScaleValue__ = MaxInput
        self.__InputScaleOrder__ = InputScale
    
    def SetUniversalMaxValue(self, value):
        self.__MaxUniversalScaleValue__ = value

    def SetUniversalMinValue(self, value):
        self.__MinUniversalScaleValue__ = value

    def GetValueUniversalScale(self, value):
        if  self.__InputScaleOrder__ is OrderScale.ASCENDING:
            if value < self.__MinInputScaleValue__:
                self.__MinInputScaleValue__ = value
            if value > self.__MaxInputScaleValue__:
                self.__MaxInputScaleValue__ = value

        if  self.__InputScaleOrder__ is OrderScale.DESCENDING:
            if value > self.__MinInputScaleValue__:
                self.__MinInputScaleValue__ = value
            if value < self.__MaxInputScaleValue__:
                self.__MaxInputScaleValue__ = value

        ismin = self.__MinInputScaleValue__

        ismax = self.__MaxInputScaleValue__
        isv = value
        usmax = self.__MaxUniversalScaleValue__
        usmin = self.__MinUniversalScaleValue__

        if self.__InputScaleOrder__ is OrderScale.DESCENDING:
            ismin = self.__MaxInputScaleValue__
            ismax = self.__MinInputScaleValue__
            isv = self.__MinInputScaleValue__ - value

        usv = (usmax - usmin) * ( (isv - ismin)/(ismax - ismin) ) + usmin
        return usv