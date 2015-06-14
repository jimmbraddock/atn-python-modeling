# -*- coding: koi8-r -*-

class GeneratorId:
    current_id = 0

    @staticmethod
    def get_id():
        GeneratorId.current_id += 1
        return GeneratorId.current_id
