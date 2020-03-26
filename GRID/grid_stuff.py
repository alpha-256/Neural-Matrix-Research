from typing import Tuple
from enum import Enum
import random
import pygame

X_Y = Tuple[int, int]


class GraphTypes(Enum):
    NONE = 0
    NODE = 1
    LINK = 2


class NodeTypes(Enum):
    NONE = 0
    NODE = 1
    BLACK = 2
    FULL = 4
    CROSS = 8


class NodeCombinations(Enum):
    NOTHING = 0

    BLACK_FULL =   NodeTypes.NODE.value | NodeTypes.BLACK.value | NodeTypes.FULL.value
    BLACK_EMPTY =  NodeTypes.NODE.value
    BLACK_CROSS =  NodeTypes.NODE.value | NodeTypes.BLACK.value | NodeTypes.CROSS.value
    
    BLUE_FULL =    NodeTypes.NODE.value | NodeTypes.FULL.value
    BLUE_EMPTY =   NodeTypes.NODE.value
    BLUE_CROSS =   NodeTypes.NODE.value | NodeTypes.CROSS.value


class GridWorldRenderer(object):

    def __init__(self, grid_dim: X_Y) -> None:
        self.grid_dim: X_Y = grid_dim
        self.grid_size: X_Y = (grid_dim[0] * 3, grid_dim[1] * 3)

        self._grid: List[List[int]] = []
        for yidx in range(0, self.grid_size[0] - 1):
            
            arr: List = []
            for xidx in range(0, self.grid_size[0] - 1):
                if yidx % 2 == 1 and xidx % 2 == 1:
                    arr.append(random.choice(list(NodeCombinations)).value)
                else:
                    arr.append(NodeCombinations.NOTHING.value)
            self._grid.append(arr)
        
        return
    
    def draw_screen(self, screen: pygame.Surface, update_display: bool = True) -> None:
        s_size: Tuple[int, int, int, int] = screen.get_rect()
        
        t_width = s_size[2] // self.grid_size[0]
        t_height = s_size[3] // self.grid_size[1]

        y_idx: int
        y_arr: List[int]
        for y_idx, y_arr in enumerate(self._grid[1:-1], start=1):
            
            x_idx: int
            x_val: int
            for x_idx, x_val in enumerate(y_arr[1:-1], start=1):

                if   x_idx % 2 == 1 and y_idx % 2 == 1:

                    if not (x_val & NodeTypes.NODE.value):
                        continue

                    rect: pygame.Rect = pygame.Rect((x_idx * t_width, y_idx * t_height), (t_width, t_height))
                    rect_width: int = 1
                    rect_color: pygame.Color = pygame.Color("blue")
                    rect_cross: bool = False

                    if x_val & NodeTypes.FULL.value:
                        rect_width = 0
                    
                    if x_val & NodeTypes.CROSS.value:
                        rect_cross = True

                    if x_val & NodeTypes.BLACK.value:
                        rect_color = pygame.Color("black")


                    if rect_cross == True:
                        pos_s: X_Y
                        pos_e: X_Y
                        pos_s = (x_idx * t_width, y_idx * t_height)
                        pos_e = (x_idx * t_width + t_width, y_idx * t_height + t_height)
                        pygame.draw.line(screen, rect_color, pos_s, pos_e)
                        pos_s = (x_idx * t_width, y_idx * t_height + t_height)
                        pos_e = (x_idx * t_width + t_width, y_idx * t_height)
                        pygame.draw.line(screen, rect_color, pos_s, pos_e)

                    pygame.draw.rect(screen, rect_color, rect, rect_width)

                elif (x_idx % 2 != 0 or y_idx % 2 != 0): 
                    
                    pos_s: X_Y
                    pos_e: X_Y

                    up: bool = (self._grid[y_idx - 1][x_idx] & NodeTypes.NODE.value)
                    down: bool = (self._grid[y_idx + 1][x_idx] & NodeTypes.NODE.value)
                    draw_same_color: bool = (self._grid[y_idx + 1][x_idx] & NodeTypes.BLACK.value) == (self._grid[y_idx - 1][x_idx] & NodeTypes.BLACK.value)
                    draw_blue_full: bool = (self._grid[y_idx + 1][x_idx] == NodeCombinations.BLUE_FULL.value) or (self._grid[y_idx - 1][x_idx] == NodeCombinations.BLUE_FULL.value)
                    draw: bool = draw_same_color or draw_blue_full
                    if up and down and draw:
                        pos_s = (x_idx * t_width + t_width / 2, y_idx * t_height)
                        pos_e = (x_idx * t_width + t_width / 2, y_idx * t_height + t_height)
                        pygame.draw.line(screen, pygame.Color("red"), pos_s, pos_e)
                    
                    right: bool = (self._grid[y_idx][x_idx + 1] & NodeTypes.NODE.value)
                    left: bool = (self._grid[y_idx][x_idx - 1] & NodeTypes.NODE.value)
                    draw_same_color: bool = (self._grid[y_idx][x_idx + 1] & NodeTypes.BLACK.value) == (self._grid[y_idx][x_idx - 1] & NodeTypes.BLACK.value)
                    draw_blue_full: bool = (self._grid[y_idx][x_idx + 1] == NodeCombinations.BLUE_FULL.value) or (self._grid[y_idx][x_idx - 1] == NodeCombinations.BLUE_FULL.value)
                    draw: bool = draw_same_color or draw_blue_full
                    if right and left and draw:
                        pos_s = (x_idx * t_width, y_idx * t_height + t_height / 2)
                        pos_e = (x_idx * t_width + t_width, y_idx * t_height + t_height / 2)
                        pygame.draw.line(screen, pygame.Color("red"), pos_s, pos_e)
                    
        if update_display == True:
            pygame.display.update()
        
        return




def main():
    pygame.init()
    
    screen = pygame.display.set_mode((700, 700))
    screen.fill(pygame.Color("white"))
    
    gw = GridWorldRenderer((8, 8))
    gw.draw_screen(screen)

    pygame.display.update()

    while 1:
        for event in pygame.event.get():
            if event.type in (pygame.QUIT, ):
                return
    
    return


if __name__ == "__main__":
    main()