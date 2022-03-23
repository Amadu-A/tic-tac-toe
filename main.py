from tkinter import *
from tkinter import Menu
from tkinter import Tk, Canvas, Frame, BOTH


class Example(Frame):
    GRID_SIZE = 3  # Ширина и высота игрового поля
    SQUARE_SIZE = 100  # Размер одной клетки на поле
    root = Tk()  # Основное окно программы

    def __init__(self):
        super().__init__()
        self.menu = Menu(self.root)
        self.new_item = Menu(self.menu)
        self.new_item.add_command(label='Новая игра', command=self.new_game)
        self.menu.add_cascade(label='Файл', menu=self.new_item)
        self.root.config(menu=self.menu)
        self.canvas = Canvas(self.root, width=self.GRID_SIZE * self.SQUARE_SIZE,
                             height=self.GRID_SIZE * self.SQUARE_SIZE)  # Задаем область на которой будем рисовать
        self.root.title("Tic-tac-toe")
        # Следующий код отрисует решетку из клеточек белого цвета на игровом поле
        for i in range(self.GRID_SIZE):
            for j in range(self.GRID_SIZE):
                self.canvas.create_rectangle(i * self.SQUARE_SIZE, j * self.SQUARE_SIZE,
                                             i * self.SQUARE_SIZE + self.SQUARE_SIZE,
                                             j * self.SQUARE_SIZE + self.SQUARE_SIZE, fill='white')
        self.canvas.pack()

    def new_game(self):
        self.root.title("Tic-tac-toe")
        self.clear_canvas()
        self.canvas.bind("<Button-1>", self.click)

    def iks(self, x1, y1, x2, y2):  # рисуем крестик
        self.pack(fill=BOTH, expand=1)
        self.canvas.create_line(x1, y1, x2, y2, fill='blue', width=2)
        self.canvas.create_line(x1, y2, x2, y1, fill='blue', width=2)
        self.canvas.pack(fill=BOTH, expand=1)

    def zero(self, x1, y1, x2, y2):  # рисуем нолик
        self.pack(fill=BOTH, expand=1)
        self.canvas.create_oval(x1, y1, x2, y2, outline='#11ff68', width=2)
        self.canvas.pack(fill=BOTH, expand=1)

    def win_line(self, x1, y1, x2, y2):  # рисуем линию победителя
        self.pack(fill=BOTH, expand=1)
        self.canvas.create_line(x1, y1, x2, y2, fill='#f11', width=2)
        self.canvas.pack(fill=BOTH, expand=1)

    def clear_canvas(self):
        for i_cur in ex.canvas.find_all():
            if i_cur > 9:
                # print(i_cur)
                ex.canvas.delete(i_cur)
        self.clicked = set()  # Создаем сет для клеточек, по которым мы кликнули
        self.clicked_x = set()  # Создаем сет для клеточек c 'x'
        self.clicked_zero = set()  # Создаем сет для клеточек c '0'

    def click(self, event):
        try:
            # print('Игра началась')
            for _ in range(1):
                ids = ex.canvas.find_withtag(CURRENT)[0]  # Определяем по какой клетке кликнули
                # При повторном клике клетки почему-то размножаются, поэтому инициируем бездействие программы на клик,
                # если клеток становится больше, либо, если пришла очередь ставить другой знак
                # print(ids)
                if ids in self.clicked or ex.canvas.find_withtag(CURRENT)[0] > 9 or len(self.clicked) % 2 == 1:
                    continue
                x1, y1, x2, y2 = ex.canvas.coords(ids)
                ex.iks(x1 + 20, y1 + 20, x2 - 20,
                       y2 - 20)  # числовой костыль. При необходимости надо заменить на % соотношение
                self.clicked.add(ids)  # добавляем нажатую клетку в сет нажатых
                self.clicked_x.add(ids)
                ex.canvas.update()
                # открываю цикл с поиском пересекающихся множеств, для определения победителя
                for nums in win_lst:
                    if nums & self.clicked_x == nums:
                        ex.root.title("Tic-tac-toe: Крестики победили!")
                        x1, y1, x2, y2 = ex.canvas.coords(min(nums))
                        x1 = (x1 + x2) / 2
                        y1 = (y1 + y2) / 2
                        x3, y3, x4, y4 = ex.canvas.coords(max(nums))
                        x3 = (x3 + x4) / 2
                        y4 = (y3 + y4) / 2
                        ex.win_line(x1, y1, x3, y4)  # линия победителя
                        self.canvas.bind("<Button-1>", lambda event: None)  # запрет на реакцию мышки

            for _ in range(1):
                ids = ex.canvas.find_withtag(CURRENT)[0]  # Определяем по какой клетке кликнули
                if ids in self.clicked or ex.canvas.find_withtag(CURRENT)[0] > 9:
                    continue
                x1, y1, x2, y2 = ex.canvas.coords(ids)
                ex.zero(x1 + 20, y1 + 20, x2 - 20,
                        y2 - 20)  # числовой костыль. При необходимости надо заменить на % соотношение
                self.clicked.add(ids)  # добавляем нажатую клетку в сет нажатых
                self.clicked_zero.add(ids)
                ex.canvas.update()
                # открываю цикл с поиском пересекающихся множеств, для определения победителя
                for nums in win_lst:
                    if nums & self.clicked_zero == nums:
                        ex.root.title("Tic-tac-toe: Нолики победили!")
                        x1, y1, x2, y2 = ex.canvas.coords(min(nums))
                        x1 = (x1 + x2) / 2
                        y1 = (y1 + y2) / 2
                        x3, y3, x4, y4 = ex.canvas.coords(max(nums))
                        x3 = (x3 + x4) / 2
                        y4 = (y3 + y4) / 2
                        ex.win_line(x1, y1, x3, y4)  # линия победителя
                        self.canvas.bind("<Button-1>", lambda event: None)  # запрет на реакцию мышки

            if len(self.clicked) == 9:
                self.root.title("Tic-tac-toe: Ничья!")

        except IndexError:
            ex.root.title("Новую игру или выход?")


if __name__ == '__main__':
    ex = Example()
    ex.new_game()
    win_lst = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {1, 4, 7}, {2, 5, 8}, {3, 6, 9}, {1, 5, 9}, {3, 5, 7}]
    ex.root.mainloop()  # Запускаем программу
