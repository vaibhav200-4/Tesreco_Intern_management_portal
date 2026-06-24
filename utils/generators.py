def certificate_generator(interns):
    for intern in interns:
        yield f"Certificate generated for {intern}"


if __name__ == "__main__":
    for certificate in certificate_generator(["Asha", "Rahul", "Meera"]):
        print(certificate)
