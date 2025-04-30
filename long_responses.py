import random

R_KPOP = "3D by Junkook"
R_POP = "Attention"
R_RAP = "Family ties"
R_SOFT = "Run with me"
R_HINDI = "Mast Malang"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"


def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(4)]
    return response
