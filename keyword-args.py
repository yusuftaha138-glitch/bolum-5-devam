def full_name(firstname: str, lastname: str, age: int) -> str:
    return f"Your name is {firstname} {lastname}"

sonuc = full_name("yusuf","dirican")
sonuc = full_name(lastname ="dirican",firstname= "yusuf")
sonuc = full_name()

print(sonuc)