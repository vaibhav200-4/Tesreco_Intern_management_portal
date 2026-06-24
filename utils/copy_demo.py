import copy


def copy_demo():
    original = {"intern": "Asha", "skills": ["Python", "Flask"]}
    shallow_copy = copy.copy(original)
    deep_copy = copy.deepcopy(original)

    original["skills"].append("SQLite")

    return {
        "original": original,
        "shallow_copy": shallow_copy,
        "deep_copy": deep_copy,
    }


if __name__ == "__main__":
    print(copy_demo())
