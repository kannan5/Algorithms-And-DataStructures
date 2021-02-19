RED = 0
BLUE = 1
GREEN = 2


def color(c):
    if c == RED:
        return "RED"
    elif c == BLUE:
        return "BLUE"
    else:
        return "GREEN"


class Dp:
    def find_house_rec(self, costs, i, color):
        if len(costs) == i:
            return 0
        if color == RED:
            color_blue = self.find_house_rec(costs, i + 1, BLUE)
            color_green = self.find_house_rec(costs, i + 1, GREEN)
            return costs[i][RED] + min(color_blue, color_green)
        elif color == BLUE:
            color_red = self.find_house_rec(costs, i + 1, RED)
            color_green = self.find_house_rec(costs, i + 1, GREEN)
            return costs[i][BLUE] + min(color_red, color_green)
        elif color == GREEN:
            color_blue = self.find_house_rec(costs, i + 1, BLUE)
            color_red = self.find_house_rec(costs, i + 1, RED)
            return costs[i][GREEN] + min(color_red, color_blue)

    def find_house(self, costs):
        cost_red = self.find_house_rec(costs, 0, RED)
        cost_blue = self.find_house_rec(costs, 0, BLUE)
        cost_green = self.find_house_rec(costs, 0, GREEN)
        return min(cost_red, min(cost_blue, cost_green))

    def find_house_top(self, costs):
        n = len(costs)
        no_house = 0
        if costs[0] is not None:
            no_house = len(costs[0])
        dp_sol = [[0 for _ in range(0, no_house)] for _ in range(0, n + 1)]
        for i in range(1, n + 1):
            dp_sol[i][RED] = costs[i - 1][RED] + min(dp_sol[i - 1][GREEN], dp_sol[i - 1][BLUE])
            dp_sol[i][BLUE] = costs[i - 1][BLUE] + min(dp_sol[i - 1][RED], dp_sol[i - 1][GREEN])
            dp_sol[i][GREEN] = costs[i - 1][GREEN] + min(dp_sol[i - 1][RED], dp_sol[i - 1][BLUE])
        return min(dp_sol[n][RED], min(dp_sol[n][BLUE], dp_sol[n][GREEN]))

    def find_house_top(self, costs):
        n = len(costs)
        no_house = 0
        if costs[0] is not None:
            no_house = len(costs[0])
        dp_finalVal = 0
        dp_sol = [[0 for _ in range(0, no_house)] for _ in range(0, n + 1)]
        dp_dec = [["x" for _ in range(0, no_house)] for _ in range(0, n + 1)]
        for i in range(1, n + 1):
            if dp_sol[i - 1][BLUE] > dp_sol[i - 1][GREEN]:
                dp_dec[i][RED] = GREEN
                dp_sol[i][RED] = costs[i - 1][RED] + dp_sol[i - 1][GREEN]
            else:
                dp_dec[i][RED] = BLUE
                dp_sol[i][RED] = costs[i - 1][RED] + dp_sol[i - 1][BLUE]

            if dp_sol[i - 1][RED] > dp_sol[i - 1][GREEN]:
                dp_dec[i][BLUE] = GREEN
                dp_sol[i][BLUE] = costs[i - 1][BLUE] + dp_sol[i - 1][GREEN]
            else:
                dp_dec[i][BLUE] = RED
                dp_sol[i][BLUE] = costs[i - 1][BLUE] + dp_sol[i - 1][RED]

            if dp_sol[i - 1][RED] > dp_sol[i - 1][BLUE]:
                dp_dec[i][GREEN] = BLUE
                dp_sol[i][GREEN] = costs[i - 1][GREEN] + dp_sol[i - 1][BLUE]
            else:
                dp_dec[i][GREEN] = RED
                dp_sol[i][GREEN] = costs[i - 1][GREEN] + dp_sol[i - 1][RED]

        result = min(dp_sol[n][RED], min(dp_sol[n][BLUE], dp_sol[n][GREEN]))
        i = n
        if result == dp_sol[n][RED]:
            c = RED
        elif result == dp_sol[n][BLUE]:
            c = BLUE
        else:
            c = GREEN

        while i > 0:
            print("House {} is painted with color {} ".format(i, color(c)))
            c = dp_dec[i][c]
            i -= 1
        return result


if __name__ == '__main__':
    costs = [[17, 2, 17], [16, 16, 5], [14, 3, 9]]
    a = Dp()
    print(a.find_house(costs))
    print(a.find_house_top(costs))
