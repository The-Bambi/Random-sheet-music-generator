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
def makeBase(variables, voices, title, subtitle, composer, time, key):
    """
    variables - list of names of variables in the codes for each voice line
    voices - instruments, like ['Violin 1', 'Violin 2', 'blah']
    title - self-expl.
    subtitle - kappa
    composer - kappa
    time kappa
    key kappa
    """
    voices_str = ""
    staffs_str = ""
    scores_str = ""


    header = f"""
\\header {OB}
    title = \\title
    subtitle = \\subtitle
    composer = \\composer
    arranger = "Krystian Figiel"
{CB}
    """

    for voice, variable in zip(voices, variables):
        voice_str = f"""
{variable} = \\relative c {OB}

{CB}
        """
        voices_str += voice_str

        staff_str = f"""
                    \\new Staff \\with {OB}
                        instrumentName = #"{voice}"
                    {CB}
                    {OB}
                        \\global
                        \\{variable}
                    {CB}
        """
        staffs_str += staff_str

        score_str = f"""
\\score {OB}
        <<
            {staff_str}
        >>
        {header}
        {CB}
\\pageBreak
        """
        scores_str += score_str

    return f"""
title = #"{title}
subtitle = #"{subtitle}"
composer = #"{composer}"

{voices_str}

global = {OB}
        \\time {time}
        \\key {key}
{CB}


\\book {OB}
        \\paper {OB}
                print-all-headers = ##t
                print-page-number = ##f
        {CB}
        \\score {OB}
                <<
                    {staffs_str}
                >>
        {header}
        {CB}
        \\pageBreak

    {scores_str}
{CB}
\\version "2.18.2"
    """
