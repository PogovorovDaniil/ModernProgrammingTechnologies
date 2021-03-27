maze = [
    "####B######################",
    "# #       #   #      #    #",
    "# # # ###### #### ####### #",
    "# # # #       #   #       #",
    "#   # # ######### # ##### #",
    "# # # #   #       #     # #",
    "### ### ### ############# #",
    "# #   #     # #           #",
    "# # #   ####### ###########",
    "# # # #       # #         C",
    "# # ##### ### # # ####### #",
    "# # #     ### # #       # #",
    "#   ##### ### # ######### #",
    "######### ### #           #",
    "# ####### ### #############",
    "A           #   ###   #   #",
    "# ############# ### # # # #",
    "# ###       # # ### # # # #",
    "# ######### # # ### # # # F",
    "#       ### # #     # # # #",
    "# ######### # ##### # # # #",
    "# #######   #       #   # #",
    "# ####### ######### #######",
    "#         #########       #",
    "#######E############D######"
]

def Search(pos: (int, int), maze: list):
    lab = []
    for string in maze:
        lab.append(list(string))

    def get(pos: (int, int), lab: list):
       return lab[pos[1]][pos[0]]
    def set(pos: (int, int), lab: list, value):
       lab[pos[1]][pos[0]] = value

    if pos[0] < 0 or pos[0] >= len(lab) or pos[1] < 0 or pos[1] >= len(lab[0]):
        print('Не верные координаты')
        return

    if get(pos, lab) == '#':
        print('Не верные координаты')
        return

    exits = []
    def SearchReq(pos: (int, int), lab: list):
        cell = get(pos, lab)
        if cell == '#':
            return
        if cell == ' ':
            newLab = lab.copy()
            set(pos, newLab, '#')
            SearchReq((pos[0] + 1, pos[1]), newLab)
            SearchReq((pos[0] - 1, pos[1]), newLab)
            SearchReq((pos[0], pos[1] + 1), newLab)
            SearchReq((pos[0], pos[1] - 1), newLab)
            return
        exits.append(cell)
    SearchReq(pos, lab)

    if len(exits) > 0:
        for i in exits:
            print(i, end=' ')
        print()
    else:
        print('Выхода нет')

inp = input().split(' ')
Search((int(inp[0]), int(inp[1])), maze)