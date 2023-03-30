class Structure:
    def __init__(self, N):
        self.N: int = N
        self.ids: [int] = [-1]*N
        self.cursor: int = 0

    def record_id(self, order_id: int):
        self.ids[self.cursor] = order_id
        self.cursor = (self.cursor + 1) % self.N

    def get_last(self, i):
        return self.ids[(self.cursor - i + self.N) % self.N]


struct = Structure(5)

struct.record_id(1)
struct.record_id(25)
struct.record_id(235)
struct.record_id(2)
struct.record_id(34)
struct.record_id(4)
struct.record_id(42)
struct.record_id(52)
struct.record_id(6)


print(struct.get_last(1))
print(struct.get_last(2))
print(struct.get_last(3))
print(struct.get_last(4))
print(struct.get_last(5))
