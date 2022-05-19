class DecorationRepository:

    def __init__(self):
        self.decorations = []

    def add(self, decoration):
        self.decorations.append(decoration)

    def remove(self, decoration):
        if decoration in self.decorations:
            self.decorations.remove(decoration)
            return True
        else:
            return False

    def find_by_type(self, decoration_type: str):
        for deco in self.decorations:
            #Does this work?
            if deco.__class__.__name__ == decoration_type:
                return deco
        return "None"
