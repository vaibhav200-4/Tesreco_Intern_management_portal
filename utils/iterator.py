class TESIdIterator:
    def __init__(self, start=1, stop=3):
        self.current = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.stop:
            raise StopIteration

        intern_id = f"TES{self.current:03d}"
        self.current += 1
        return intern_id


if __name__ == "__main__":
    for generated_id in TESIdIterator():
        print(generated_id)
