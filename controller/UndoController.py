class UndoController:
    def __init__(self):
        self._history = []
        self._index = 0
        self._duringUndo = False

    def recordOperation(self, operation):
        if self._duringUndo == True:
            return
        self._history.append(operation)
        self._index += 1
        print(self._index)

    def Undo(self):
        print(self._index)
        if self._index == 0:
            raise Exception("No more undos!")
        self._duringUndo = True
        self._index -= 1
        self._history[self._index].undo()
        self._duringUndo = False

    def Redo(self):
        if self._index == len(self._history):
            raise Exception("No more redos!")

        self._duringUndo = True
        self._history[self._index].redo()
        self._index += 1
        self._duringUndo = False


class FunctionCall:
    def __init__(self, function, *params):
        self._function = function
        self._params = params

    def call(self):
        self._function(*self._params)


class Operation:
    def __init__(self, undo, redo):
        self._undo = undo
        self._redo = redo  # redo function

    def undo(self):
        self._undo.call()

    def redo(self):
        self._redo.call()

class CascadedOperation:
    def __init__(self,  operations):
        self._operations = operations

    def undo(self):
        for op in self._operations:
            op.undo()
    def redo(self):
        for op in self._operations:
            op.redo()
