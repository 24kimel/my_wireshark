
class BasePacket:
    def __str__(self):
        result = f"##### {self.__class__.__name__} #####\n"
        for k, v in self.__dict__.items():
            result += f"{k}: {v}\n"
        
        return result