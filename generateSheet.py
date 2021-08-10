OB = "{"
CB = "}"

def generateInstrument(name, shortName, clef, music):
    return f"""
    \\new Staff \\with {OB}
        instrumentName = #"{name}"
        shortInstrumentName = #"{shortName}"
    {CB}
    {OB}
        \\clef {clef}
        {music}
    {CB}
    """

def generateScore(time, staffs):
    return f"""
\\score {OB}
    <<

        \\time {time}
        {staffs}
    >>
{CB}
    """
